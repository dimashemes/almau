from django.db import models


class Applicant(models.Model):
    full_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    school = models.CharField(max_length=100)
    verification_code = models.CharField(max_length=6)


class Document(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, null=False, default='unknown')
