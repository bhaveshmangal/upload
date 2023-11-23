from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('files/', views.myFiles, name="files"),
    path('sharedFiles/', views.sharedFiles, name="shared_files"),
    path('upload-file/', views.uploadFile, name="upload_file"),
    path('share-file/', views.share, name="share_form"),
]
