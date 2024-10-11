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
    path('diary/<int:diary_id>/add-mental/', views.add_mental, name='add-mental'),
    path('diary/<int:diary_id>/add-emotional/', views.add_emotional, name='add-emotional'),
    path('diary/mental/<int:pk>/update/', views.MentalUpdate.as_view(), name='mental-update'),
    path('diary/physical/<int:pk>/update/', views.PhysicalUpdate.as_view(), name='physical-update'),
    path('diary/<int:pk>/update/', views.EmotionalUpdate.as_view(), name='emotional-update'),
    path('diary/physical/<int:pk>/delete/', views.PhysicalDelete.as_view(), name='physical-delete'),
    path('diary/mental/<int:pk>/delete/', views.MentalDelete.as_view(), name='mental-delete'),
    path('diary/<int:pk>/delete/', views.EmotionalDelete.as_view(), name='emotional-delete'),
    path('diary/<int:diary_id>/add_photo', views.add_photo, name="add-photo")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)