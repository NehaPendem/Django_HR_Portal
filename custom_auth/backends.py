from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from custom_auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

class UserBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        success_url = reverse_lazy('custom_auth:dashboard')
        print(kwargs)
        username = kwargs['username']
        password = kwargs['password']
        try:
            user = User.objects.get(id=username)
            print(user.id, username, user.password, password)
            if(user.password == password):
                return user
        except User.DoesNotExist:
            pass
