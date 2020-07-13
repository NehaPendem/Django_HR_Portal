from django.db import models
from custom_auth.models import User
from resume.models import Resume
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from .validators import validate_number, validate_skills
from django.db.models import CharField, Model
from django_mysql.models import ListCharField


interview_status_list = (
    ('1', 'Round 1 done'),
    ('2', 'Round 2 done'),
    ('3', 'HR Round done'),
    ('4', 'All of the above done'),
    ('5', 'None done')
)

mode = (
    ('1', 'Online'),
    ('2', 'Offline')
)


class employee(models.Model):
    req_id = models.AutoField(primary_key=True)
    hr_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    resume = models.FileField(upload_to='files/', null=True, verbose_name="")
    date_posted = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=30)

    mobile_no = models.CharField(max_length=10, validators=[validate_number])
    email = models.EmailField()
    skills = ListCharField(
        base_field=CharField(max_length=10),
        size=10,
        max_length=(10 * 11),  # 6 * 10 character nominals, plus commas
        validators=[validate_skills],
    )

    total_exp = models.IntegerField(blank=True, null=True)
    rel_exp = models.IntegerField(blank=True, null=True)
    cctc = models.IntegerField(blank=True, null=True)
    ectc = models.IntegerField(blank=True, null=True)
    notice_period = models.IntegerField(blank=True, null=True)
    reason_for_shifting = models.TextField(blank=True, null=True)
    current_location = models.CharField(max_length=30, blank=True, null=True)
    current_company = models.CharField(max_length=30, blank=True, null=True)
    hr_comments = models.TextField(blank=True, null=True)
    interview_status = models.CharField(choices=interview_status_list, default='1', max_length=30, blank=True, null=True)
    round1_schedule = models.DateTimeField(blank=True, null=True)
    round1_feedback = models.TextField(blank=True, null=True)
    round2_schedule = models.DateTimeField(blank=True, null=True)
    round2_feedback = models.TextField(blank=True, null=True)
    mode_of_interview = models.CharField(choices=mode, default='1', max_length=30)
    sourced_from = models.CharField(max_length=30, blank=True, null=True)
    placement_location = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employee:profile', kwargs={'pk': self.pk})
