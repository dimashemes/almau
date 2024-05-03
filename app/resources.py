from import_export import resources
from .models import User, UploadId, UploadCertificate


class UserResource(resources.ModelResource):
    class Meta:
        model = User


class UploadIdResource(resources.ModelResource):
    class Meta:
        model = UploadId


class UploadCertificateResource(resources.ModelResource):
    class Meta:
        model = UploadCertificate
