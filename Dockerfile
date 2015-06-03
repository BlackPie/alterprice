FROM createdigitalspb/py3:1.1

WORKDIR /project

# logs
RUN mkdir -p /var/log/app

# django.log / uwsgi.log
RUN chown www-data:www-data /var/log/app

# Django service

# this should go to base py3
ADD docker/images/web/start_django.sh /bin/start_django.sh
ADD docker/images/web/start_celery.sh /bin/start_celery.sh

# this should remain here
ADD docker/images/web/run_main_service.sh  /etc/service/main/run
RUN chmod 755 /bin/start_django.sh
RUN chmod 755 /bin/start_celery.sh
RUN chmod 755 /etc/service/main/run

ADD docker/images/web/requirements.txt /tmp/requirements_local.txt
RUN cd /tmp && pip3 install -r /tmp/requirements_local.txt

RUN cd /project/ && buildout init
ADD docker/images/web/buildout.cfg /project/buildout.cfg
RUN cd /project/ && buildout

ADD src /project/src

# TODO: test if 'from PIL import _imaging as core' works without this
#RUN ln -s /usr/lib/x86_64-linux-gnu/libtiff.so.5 /usr/lib/x86_64-linux-gnu/libtiff.so.4

# also https://github.com/tdMulga/Nod/blob/master/Samples/Dockerfile

ENV DJANGO_CONFIGURATION Production
ENV PATH=/project/bin:$PATH
EXPOSE 8000 44000
VOLUME ["/project/src"]
