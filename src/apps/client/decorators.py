from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse


def login_required(f):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous():
            return HttpResponseRedirect(reverse('client:index'))
        else:
            return f(request, *args, **kwargs)
    return wrapper


def profile_reverse(f):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_anonymous():
            return HttpResponseRedirect(reverse('client:profile'))
        else:
            return f(request, *args, **kwargs)
    return wrapper
