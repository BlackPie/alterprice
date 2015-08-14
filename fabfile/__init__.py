# -*- coding: utf-8 -*-
import os
from datetime import datetime
from fabric.api import run, env, put, cd, lcd, local, require, settings, hide, execute
from fabric.colors import red, green, yellow, magenta


def commons():

    env.docker_username = os.environ.get('docker_username', None)
    env.docker_password = os.environ.get('docker_password', None)
    env.docker_email = os.environ.get('docker_email', None)
    env.app_container_name = 'createdigitalspb/alterprice'


def staging():
    execute(commons)
    env.settings = 'staging'
    env.hosts = ['144.76.79.14']
    env.user = 'vagrant'
    env.port = '19022'
    env.django_exec = '/project/bin/django'
    env.fig_file = 'docker-compose-staging.yml'
    message_highlight("Configuration set", "Staging")


def production():
    execute(commons)
    env.settings = 'production'
    env.hosts = ['95.213.189.186']
    env.user = 'alterprice'
    env.django_exec = '/project/bin/django'
    env.fig_file = 'docker-compose-production.yml'
    message_highlight("Configuration set", "Production")


def development():

    os.environ['ENV_FILE'] = 'docker/private/base/docker.env'

    from envious import load_env

    load_env()

    execute(commons)

    env.settings = 'development'
    env.login_required = False


def message_highlight(msg, variable):
    print yellow(msg), ":", magenta(variable)


def circleci():
    execute(commons)
    env.settings = 'circleci'


def docker(cmd, loc=False):
    """
    Run Docker cmd
    """
    if loc:
        return local("docker {}".format(cmd))
    else:
        return run("docker {}".format(cmd))


def docker_login(loc=False):

    return docker(
        'login -u {} -p {} -e {}'.format(
            env.docker_username,
            env.docker_password,
            env.docker_email), loc=loc)


def fig(cmd, yes=False):
    """
    Run Fig cmd
    """
    if yes:
        return run('yes | docker-compose {}'.format(cmd))
    return run('docker-compose {}'.format(cmd))


def django_cmd(cmd):
    """
    Runs django command inside container
    """
    return fig('run web {env[django_exec]} {cmd}'.format(cmd=cmd, env=env))


def migrate(params='', do_backup=False):
    """
    Runs migrate management command. Database backup is performed
    before migrations if ``do_backup=False`` is not passed.
    """
    # if do_backup:
    #     dump_db()
    return django_cmd('migrate --noinput {}'.format(params))


def docker_local(cmd):
    return docker(cmd, loc=True)


def deploy_media():
    """
    Collects static media using 'collect; command
    """
    django_cmd("collectstatic --noinput")
    print(magenta("Media deployed"))


def make_container(tag=None):
    if not tag:
        tag = env.app_container_name
    return docker_local('build --tag {} .'.format(tag))


def push_container(tag=None):
    if not tag:
        tag = env.app_container_name
    return docker_local('push {}'.format(tag))


def build_client():
    local('npm install')
    local('./bin/gulp build')


def build_container(login="True"):
    if bool(eval(login)):
        docker_login(loc=True)
    print 'before make: ', datetime.now().strftime('%H.%M.%S')
    make_container()
    print 'after make: ', datetime.now().strftime('%H.%M.%S')


def publish_container(login="True"):
    if bool(eval(login)):
        docker_login(loc=True)
    print 'before push: ', datetime.now().strftime('%H.%M.%S')
    push_container()
    print 'after push: ', datetime.now().strftime('%H.%M.%S')


def deploy():
    if not env.docker_username:
        print(magenta("Environment variables not set"))
        return

    require('settings', provided_by=[staging])

    docker_login()

    print(yellow('Deploying...'))
    run('mkdir -p ~/alterprice')
    put(env.fig_file, '~/alterprice/docker-compose.yml')
    with cd('~/alterprice'):
        fig('pull')
        print('pull finished, upping')
        fig('stop')  # needed because of a bug with compose
        fig('rm web', yes=True)  # needed because of a bug with compose
        fig('rm worker', yes=True)  # needed because of a bug with compose
        fig('up -d')

        migrate()
        deploy_media()
        # django_cmd('startup')
