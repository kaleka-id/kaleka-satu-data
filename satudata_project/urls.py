from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import views as authViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', authViews.LoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(), name='logout'),
    path('password-change/', authViews.PasswordChangeView.as_view(), name='password-change'),
    path('password-change/done/', authViews.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', authViews.PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/done/', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', include('operation.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
