from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import BACKEND_SESSION_KEY
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache

from social_auth.models import UserSocialAuth
from social_auth.views import complete as social_complete
from social_auth.backends.facebook import FacebookBackend

import pdb


def home(request):

    return render_to_response('home.html')

def is_complete_authentication(request):
    return request.user.is_authenticated() and \
           FacebookBackend.__name__ in request.session.get(
                BACKEND_SESSION_KEY, ''
            )

def get_access_token(user):
    key = str(user.id)
    access_token = cache.get(key)

    # If cache is empty read the database
    if access_token is None:
        try:
            social_user = user.social_user if hasattr(user, 'social_user') \
                          else UserSocialAuth.objects.get(
                                  user=user.id, provider=FacebookBackend.name
                               )
        except UserSocialAuth.DoesNotExist:
            return None

        if social_user.extra_data:
            access_token = social_user.extra_data.get('access_token')
            expires = social_user.extra_data.get('expires')

            cache.set(key, access_token, int(expires) if expires is not None
                                                       else 0)
    return access_token


@login_required
@csrf_exempt
def done(request, *args, **kwargs):
    # If there is a ready response just return it. Not recommended though.
    auth_response = kwargs.get('auth_response')
    at = get_access_token(request.user)
    if auth_response:
        return auth_response
    return render_to_response('done.html', {
        'fb_app_id': getattr(settings, 'FACEBOOK_APP_ID', None),
         'warning': request.method == 'GET'
    }, RequestContext(request))
