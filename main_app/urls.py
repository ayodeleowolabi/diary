from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name='home'),
    path("accounts/signup/", views.signup, name='signup'),
    path('diary/', views.diary_index, name='diary-index')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)