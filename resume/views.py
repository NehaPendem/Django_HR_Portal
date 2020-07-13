from django.shortcuts import render
from . import forms
from .models import Resume
from .forms import FileForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect, HttpResponse


class showform(FormView):
    """sign up user view"""
    form_class = forms.FileForm
    template_name = 'resume/files.html'
    success_url = reverse_lazy('resume:test')

    def form_valid(self, form):
        """ process user signup"""
        file = form.save(commit=False)
        file.save()

        if file is not None:
            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)


def success(request):
    return render(request, 'resume/test.html')


def showfile(request):
    #lastfile = File.objects.last()

    #filepath = request.filepath

    #filename = request.name

    form = FileForm(request.POST or None, request.FILES or None)

    if form.is_valid():

        form.save()
    else:

        return render(request, 'resume/test.html')

    filepath = form.cleaned_data['filepath']
    filename = form.cleaned_data['filename']

    context = {'filepath': filepath,
               'form': form,
               'filename': filename
               }

    return render(request, 'resume/files.html', context)
