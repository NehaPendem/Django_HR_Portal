from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, UpdateView, DeleteView
from . import forms
from .models import employee

from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import edit_employee_form
from custom_auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader


class add_employee(FormView):
    """sign up user view"""
    model = employee
    form_class = forms.register_employee
    template_name = 'employee/register.html'
    success_url = reverse_lazy('custom_auth:dashboard')

    def form_valid(self, form):
        """ process user signup"""

        emp = employee.objects.filter(hr_id=self.request.POST.get('hr_id'))
        e = form.save(commit=False)
        e.save()
        login(self.request, e)
        user = User.objects.filter(id=self.request.POST.get('hr_id')).first()
        # print(user.name)
        employees = employee.objects.filter(hr_id=e.hr_id)

        context = {
            'employee': e,
            'user': user,
            'employees': employees
        }

        # return HttpResponseRedirect(reverse('employee:dashboard'))
        # return HttpResponseRedirect(reverse_lazy('custom_auth:dashboard'))
        # return render(self.request, e.get_absolute_url())
        return render(self.request, 'custom_auth/dashboard.html', context)


class edit_employee(UpdateView):
    model = employee

    form_class = forms.edit_employee_form
    template_name = 'employee/edit.html'

    def form_valid(self, form):

        e = form.save(commit=False)
        e.save()
        login(self.request, e)
        # print(e)

        user = User.objects.filter(id=str(e.hr_id)).first()

        employees = employee.objects.filter(hr_id=e.hr_id)

        context = {
            'employees': employees,
            'user': user
        }

        return render(self.request, 'custom_auth/dashboard.html', context)

        # template = loader.get_template('custom_auth/dashboard.html')

        # return HttpResponseRedirect(reverse('custom_auth:dashboard', args=[context]))

        # return HttpResponse(template.render(context, self.request))

        # return redirect('/custom_auth', kwargs={'user': user})

        # return render(self.request, '/custom_auth/', context)

        # return super().form_valid(form)


class delete_employee(DeleteView):
    model = employee

    success_url = reverse_lazy('custom_auth:dashboard')


def Dashboard(request):
    """ make dashboard view """
    return render(request, 'employee/dashboard.html')


def profile(request, pk=None):
    # print(pk)
    print(request.user, '1wgdi2ygdi3ug')
    user = User.objects.filter(id=str(request.user))
    emp = employee.objects.filter(pk=pk).first()

    context = {
        'employee': emp,
        'user': user,
    }
    return render(request, 'employee/profile.html', context)


def filter_employees(request):

    skills = employee.objects.values_list('skills')
    # print(skills)
    l = []

    for i in skills:
        for j in i:
            for k in j:
                if(k not in l):
                    l.append(k)

    # print(l)

    context = {
        'skills': l
    }

    return render(request, 'employee/filter.html', context)


def show_filtered_emp(request):

    mode = request.POST.get('mode')
    # print(mode)

    s = request.POST.getlist('s')
    # print(s)

    exp = request.POST.get('exp')
    loc = request.POST.get('loc')

    if(exp == '1'):
        emp = employee.objects.filter(skills=s, mode_of_interview=mode, total_exp__lte=1, placement_location=loc)
    elif(exp == '2'):
        emp = employee.objects.filter(skills=s, mode_of_interview=mode, total_exp__gte=1, total_exp__lte=2, placement_location=loc)
    else:
        emp = employee.objects.filter(skills=s, mode_of_interview=mode, total_exp__gte=2, placement_location=loc)

    # print(emp)

    context = {
        'employees': emp
    }
    return render(request, 'employee/show_filtered_emp.html', context)


def view_pdf(request, pk=None):
    emp = employee.objects.filter(pk=pk).first()
    print(request, 'hiiiii')

    with open('/Users/nehapendem/Desktop/Neha/custom_login/media/' + str(emp.resume), 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=' + '/Users/nehapendem/Desktop/Neha/custom_login/media/' + str(emp.resume)
        return response
    pdf.closed
