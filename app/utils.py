from django.http import HttpResponse
from tablib import Dataset

from app import models


def export_table():
    users = models.User.objects.all()
    data = []
    for user in users:
        upload_id_files = models.UploadId.objects.filter(user=user).values_list('upload_id', flat=True)
        upload_certificate_files = models.UploadCertificate.objects.filter(user=user).values_list(
            'upload_certificate',
            flat=True)
        upload_id_file = ", ".join(upload_id_files)
        upload_certificate_file = ", ".join(upload_certificate_files)
        data.append(
            [user.name, user.email, user.phone_number, user.verified, user.verification_code, upload_id_file,
             upload_certificate_file])

    headers = ['Name', 'Email', 'Phone Number', 'Verified', 'Verification Code', 'Upload ID File',
               'Upload Certificate File']
    dataset = Dataset()
    dataset.headers = headers
    for row in data:
        dataset.append(row)

    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="user_data.xls"'
    return response
