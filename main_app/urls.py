from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("accounts/signup/", views.signup, name='signup'),
    path('diary/', views.diary_index, name='diary-index'),
    path('diary/<int:diary_id>/', views.diary_detail, name='diary-detail'),
    path('diary/<int:diary_id>/add-physical/', views.add_physical, name='add-physical'),
    path('diary/<int:pk>/update/', views.PhysicalUpdate.as_view(), name='physical-update'),
    path('diary/<int:pk>/delete/', views.PhysicalDelete.as_view(), name='physical-delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)