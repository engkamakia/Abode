from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [
    
    
    path('register/', views.registrationPage, name = "register"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    path('', views.index, name = "home"),
    path('about/', views.about_us, name = "about"),
    path('userProfile/', views.userPage, name = "userProfile"),
    path('blogs/', views.blog, name = "blogs"),
    path('blog/', views.blogSingle, name = "blog"),
    path('properties/', views.property, name = "properties"),
    path('property/<str:pk>/', views.propertySingle, name = "property"),
    path('contact/', views.contact, name = "contact"),
    path('agent/', views.agentSingle, name = "agent"),
    path('agents/', views.agent, name = "agents"),
    path('list_property/', views.createListing, name = "list_property"),
    path('update_property/<str:pk>/', views.updateListing, name = "update_property"),
    path('delete_property/<str:pk>/', views.deleteProperty, name = "delete_property"),
    path('darajaa/', views.mpesa, name='mpesa'),
   # path('search/', views.search, name = "search"),
   
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "realestate/password_reset.html"),name = "reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "realestate/password_reset_sent.html"),name = "password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "realestate/password_reset_form.html"),name = "password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "realestate/password_reset_done.html"),name = "password_reset_complete"),
   
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)