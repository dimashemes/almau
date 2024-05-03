import random
import smtplib
from email.mime.text import MIMEText

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from openpyxl.workbook import Workbook

from . import forms
from . import models
from .models import Applicant, Document
import os


def send_verification_email(email, verification_code):
    sender = settings.EMAIL_HOST_USER
    subject = "Email Verification"
    message = f'Open the link to verify your email: http://127.0.0.1:8000/verify/?code={verification_code}?exp=15 /// https://drive.google.com/file/d/1MJR3Dtkzn7_oh-kiClj8jK4lrmMOuhHO/view?usp=sharing.'

    pdf_file_path = os.path.join(settings.BASE_DIR, 'static', 'Инструкция по пользованию нашим сервисом.pdf')

    msg = MIMEText(message, _charset='utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = email

    try:
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT) as smtp_server:
            smtp_server.login(sender, settings.EMAIL_HOST_PASSWORD)
            smtp_server.sendmail(sender, email, msg.as_string())
        return "Message sent successfully!"
    except smtplib.SMTPException as e:
        raise e


def login(request):
    request.session['verified_email'] = ''
    if request.method == 'POST':
        user_form = forms.ApplicantForm(request.POST.copy())
        if user_form.is_valid():
            verification_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            user = user_form.save(commit=False)
            user.verification_code = verification_code
            send_verification_email(user.email, verification_code,
                                    )
            user.save()
        else:
            print(user_form.errors)
    else:
        user_form = forms.ApplicantForm()
    return render(request, 'app/index.html', {'user_form': user_form})


def verify_email(request):
    if request.method == 'GET':
        verification_code = request.GET.get('code')
        if verification_code:
            user = models.Applicant.objects.filter(verification_code=verification_code).first()
            if user:
                user.verified = True
                user.save()
                request.session['verified_email'] = user.email
                return redirect('upload_files')
    return JsonResponse({'message': 'Verification code sent successfully!'})


def upload_files(request):
    if request.method == 'POST':
        verified_email = request.session.get('verified_email')
        user = models.Applicant.objects.filter(email=verified_email).last()
        mutable_post_data = request.POST.copy()
        mutable_post_data['user'] = user
        form = forms.DocumentForm(mutable_post_data, request.FILES)
        if form.is_valid():
            uploaded_files = request.FILES.getlist('file')

            for uploaded_file in uploaded_files:
                models.Document.objects.create(file=uploaded_file, applicant=user, type='Id')
            return redirect('upload_photo')
        else:
            print(form.errors)
    else:
        form = forms.DocumentForm()
    return render(request, 'app/upload_id.html', {'form': form})


def upload_ent(request):
    if request.method == 'POST':
        verified_email = request.session.get('verified_email')
        user = models.Applicant.objects.filter(email=verified_email).last()
        mutable_post_data = request.POST.copy()
        mutable_post_data['user'] = user
        form = forms.DocumentForm(mutable_post_data, request.FILES)
        if form.is_valid():
            print(5)
            uploaded_files = request.FILES.getlist('file')
            for uploaded_file in uploaded_files:
                models.Document.objects.create(file=uploaded_file, applicant=user, type='Ent')
            return redirect('upload_ent')
    else:
        form = forms.DocumentForm()

    return render(request, 'app/upload_ent.html', {'form': form})


def upload_grant(request):
    if request.method == 'POST':
        verified_email = request.session.get('verified_email')
        user = models.Applicant.objects.filter(email=verified_email).last()
        mutable_post_data = request.POST.copy()
        mutable_post_data['user'] = user
        form = forms.DocumentForm(mutable_post_data, request.FILES)
        if form.is_valid():
            print(5)
            uploaded_files = request.FILES.getlist('file')
            for uploaded_file in uploaded_files:
                models.Document.objects.create(file=uploaded_file, applicant=user, type='Grant')
            return redirect('upload_grant')
    else:
        form = forms.DocumentForm()

    return render(request, 'app/upload_grant.html', {'form': form})


def upload_military(request):
    if request.method == 'POST':
        verified_email = request.session.get('verified_email')
        user = models.Applicant.objects.filter(email=verified_email).last()
        mutable_post_data = request.POST.copy()
        mutable_post_data['user'] = user
        form = forms.DocumentForm(mutable_post_data, request.FILES)
        if form.is_valid():
            print(5)
            uploaded_files = request.FILES.getlist('file')
            for uploaded_file in uploaded_files:
                models.Document.objects.create(file=uploaded_file, applicant=user, type='Military')
            return redirect('upload_military')
    else:
        form = forms.DocumentForm()

    return render(request, 'app/upload_military.html', {'form': form})


def upload_medical(request):
    if request.method == 'POST':
        verified_email = request.session.get('verified_email')
        user = models.Applicant.objects.filter(email=verified_email).last()
        mutable_post_data = request.POST.copy()
        mutable_post_data['user'] = user
        form = forms.DocumentForm(mutable_post_data, request.FILES)
        if form.is_valid():
            print(5)
            uploaded_files = request.FILES.getlist('file')
            for uploaded_file in uploaded_files:
                models.Document.objects.create(file=uploaded_file, applicant=user, type='Medical')
            return redirect('upload_medical')
    else:
        form = forms.DocumentForm()

    return render(request, 'app/upload_medical.html', {'form': form})


def upload_birth(request):
    if request.method == 'POST':
        verified_email = request.session.get('verified_email')
        user = models.Applicant.objects.filter(email=verified_email).last()
        mutable_post_data = request.POST.copy()
        mutable_post_data['user'] = user
        form = forms.DocumentForm(mutable_post_data, request.FILES)
        if form.is_valid():
            print(5)
            uploaded_files = request.FILES.getlist('file')
            for uploaded_file in uploaded_files:
                models.Document.objects.create(file=uploaded_file, applicant=user, type='Birth')
            return redirect('upload_birth')
    else:
        form = forms.DocumentForm()

    return render(request, 'app/upload_birth.html', {'form': form})


def upload_certificate(request):
    if request.method == 'POST':
        verified_email = request.session.get('verified_email')
        user = models.Applicant.objects.filter(email=verified_email).last()
        mutable_post_data = request.POST.copy()
        mutable_post_data['user'] = user
        form = forms.DocumentForm(mutable_post_data, request.FILES)
        if form.is_valid():
            print(5)
            uploaded_files = request.FILES.getlist('file')
            for uploaded_file in uploaded_files:
                models.Document.objects.create(file=uploaded_file, applicant=user, type='certificate')
            return redirect('upload_certificate')
    else:
        form = forms.DocumentForm()

    return render(request, 'app/upload_certificate.html', {'form': form})


def upload_photo(request):
    if request.method == 'POST':
        verified_email = request.session.get('verified_email')
        user = models.Applicant.objects.filter(email=verified_email).last()
        mutable_post_data = request.POST.copy()
        mutable_post_data['user'] = user
        form = forms.DocumentForm(mutable_post_data, request.FILES)
        if form.is_valid():
            uploaded_files = request.FILES.getlist('file')
            for uploaded_file in uploaded_files:
                models.Document.objects.create(file=uploaded_file, applicant=user, type='photo')
    else:
        form = forms.DocumentForm()

    return render(request, 'app/upload_photo.html', {'form': form})


def submissions(request):
    applicants = Applicant.objects.all()
    data = {'applicants': []}
    for applicant in applicants:
        documents = Document.objects.filter(applicant=applicant)
        data['applicants'].append({'applicant': applicant, 'documents': documents})
    return render(request, 'app/table.html', data)


def export_data_as_excel(request):
    applicants = Applicant.objects.all()
    documents = Document.objects.all()
    wb = Workbook()
    applicant_sheet = wb.active
    applicant_sheet.title = "Applicants"
    document_sheet = wb.create_sheet(title="Documents")
    applicant_sheet.append(["Full Name", "Gender", "Birth Date", "Email", "Verified", "School", "Verification Code"])
    document_sheet.append(["Applicant ID", "File Name", "Uploaded At"])
    for applicant in applicants:
        applicant_sheet.append(
            [applicant.full_name, applicant.gender, applicant.birth_date, applicant.email, applicant.verified,
             applicant.school, applicant.verification_code])
    for document in documents:
        uploaded_at_without_tz = document.uploaded_at.replace(tzinfo=None)
        document_sheet.append([document.applicant_id, document.file.name, uploaded_at_without_tz])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=applicants_and_documents.xlsx'
    wb.save(response)
    return response
