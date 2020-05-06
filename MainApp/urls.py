from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home_view'),
    path('imageDetails/<int:pk>', views.ImageDetailsView.as_view(), name='image_details'),
    path('ImageUpload', views.ImageUploadView.as_view(), name='image_upload'),
    path('image_likes', views.Image_likes, name='image_like'),
    path('imageComment', views.Image_comment, name='image_comment'),
    path('image_delete', views.Image_delete, name='image_delete'),
]
