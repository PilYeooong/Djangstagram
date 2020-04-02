from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.conf import settings
from django.template.loader import render_to_string
from django.core.validators import RegexValidator


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'Male', '남성'  # DB 저장이 앞, 보여지는부분 뒤
        FEMALE = 'Female', '여성'

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13,
                                    validators=[RegexValidator(r'^010-?[1-9]\d{3}-?\d{4}$')], blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, blank=True)
    avatar = models.ImageField(blank=True, upload_to='accounts/avatar/%Y/%m/%d',
                               help_text='48px * 48px의 크기의 png/jpg 파일을 업로드 해주세요')

    # def send_welcome_email(self):
    #     subject = render_to_string('accounts/welcome_email_subject.txt', {
    #         'user': self,
    #     })
    #     content = render_to_string('accounts/welcome_email_content.txt', {
    #         'user': self,
    #     })
    #     sender_email = settings.WELCOME_EMAIL_SENDER
    #     send_mail(subject, content, sender_email, [self.email], fail_silently=False)
