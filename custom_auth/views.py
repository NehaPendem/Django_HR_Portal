from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from custom_auth.models import User
from employee.models import employee
from django.contrib.auth.decorators import login_required


class SignupView(FormView):
    """sign up user view"""
    form_class = forms.SignupForm
    template_name = 'custom_auth/signup.html'
    success_url = reverse_lazy('custom_auth:login')

    def form_valid(self, form):
        """ process user signup"""
        user = form.save(commit=False)
        user.save()

        login(self.request, user)
        if user is not None:

            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)


def Dashboard(request):

    id1 = request.user.id
    print(str(id1), 'hiiiii')

    user = User.objects.filter(id=request.user.id).first()

    if(user != None):
        user = authenticate(username=id1,
                            password=user.password)

        #employees = employee.objects.filter(hr_id=id1)

        employees = employee.objects.filter(hr_id=str(id1)).order_by('-date_posted')

        context = {
            'user': user,
            'employees': employees

        }

        return render(request, 'custom_auth/dashboard.html', context)

    """ make dashboard view """


def Homepage(request):
    return render(request, 'custom_auth/homepage.html')


def Logout(request):
    """logout logged in user"""
    logout(request)
    return HttpResponseRedirect(reverse_lazy('custom_auth:login'))


class LoginView(FormView):
    """login view"""

    form_class = forms.LoginForm
    success_url = reverse_lazy('custom_auth:dashboard')
    template_name = 'custom_auth/login.html'

    def form_valid(self, form):
        """ process user login"""
        credentials = form.cleaned_data

        # print(credentials['email'])

        user = authenticate(username=credentials['id'],
                            password=credentials['password'])
        #print(credentials['id'], credentials['password'], 'hi')

        if user is not None:
            login(self.request, user)
            u = User.objects.filter(id=credentials['id'], password=credentials['password']).first()

            #e = employee.objects.filter(hr_id=u.id)
            e = employee.objects.filter(hr_id=u.id).order_by('-date_posted')

            if(u != None):
                context = {
                    'user': u,
                    'employees': e

                }
            # if(not e):
                #print(e, 'hiiiiiii')
            return render(self.request, 'custom_auth/dashboard.html', context)

        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                 please try again')
            return HttpResponseRedirect(reverse_lazy('custom_auth:login'))

        # user = authenticate(username=credentials['email'],
        # password=credentials['password'])

        # if user is not None:
        # login(self.request, user)
        # return HttpResponseRedirect(self.success_url)

        # else:
        # messages.add_message(self.request, messages.INFO, 'Wrong credentials\
        #                         please try again')
        #     return HttpResponseRedirect(reverse_lazy('custom_auth:login'))
