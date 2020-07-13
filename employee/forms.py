from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from employee.models import employee
from custom_auth.models import User


class register_employee(forms.ModelForm):

    widgets = {
        'hr_id': forms.Select(attrs={'class': 'form-control'}),
        'reason_for_shifting': forms.Textarea(attrs={'placeholder': 'State Reason for Shifting'})



    }



    date_posted = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),

    )

    round1_schedule = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),
        required=False,
    )

    round2_schedule = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),
        required=False,
    )

    class Meta:
        model = employee

        fields = ['req_id', 'hr_id', 'date_posted', 'resume', 'name', 'mobile_no', 'email', 'skills', 'total_exp', 'rel_exp', 'cctc', 'ectc', 'notice_period', 'reason_for_shifting', 'current_location', 'current_company', 'hr_comments', 'interview_status', 'round1_schedule', 'round1_feedback', 'round2_schedule', 'round2_feedback', 'mode_of_interview', 'sourced_from', 'placement_location']


class edit_employee_form(forms.ModelForm):
    date_posted = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),

    )

    round1_schedule = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),
        required=False,
    )

    round2_schedule = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),
        required=False,
    )

    class Meta:
        model = employee

        fields = ['req_id', 'hr_id', 'date_posted', 'name', 'mobile_no', 'email', 'skills', 'total_exp', 'rel_exp', 'cctc', 'ectc', 'notice_period', 'reason_for_shifting', 'current_location', 'current_company', 'hr_comments', 'interview_status', 'round1_schedule', 'round1_feedback', 'round2_schedule', 'round2_feedback', 'mode_of_interview', 'sourced_from', 'placement_location', 'resume']
