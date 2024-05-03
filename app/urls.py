from django.urls import path
from . import views
from .views import export_data_as_excel

urlpatterns = [
    path('', views.login, name='login'),
    path('verify/', views.verify_email, name='verify_email'),
    path('upload/files/', views.upload_files, name='upload_files'),
    path('applicant/submitions/', views.submissions, name='export_users'),
    path('applicant/submitions/export-excel/', export_data_as_excel, name='export_excel'),
    path('upload/certificate/', views.upload_certificate, name='upload_certificate'),
    path('upload/photo/', views.upload_photo, name='upload_photo'),
    path('upload/ent/', views.upload_ent, name='upload_ent'),
    path('upload/grant/', views.upload_grant, name='upload_grant'),
    path('upload/military/', views.upload_military, name='upload_military'),
    path('upload/medical/', views.upload_medical, name='upload_medical'),
    path('upload/birth/', views.upload_birth, name='upload_birth'),

]
