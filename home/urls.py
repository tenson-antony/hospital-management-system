from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name="index"),
    path('about/',views.about, name="about" ),
    path('doctors/',views.doctors, name="doctors"),
    path('contact/',views.contact, name="contact"),
    path('department/',views.department, name="department"),
    path('booking/',views.booking, name="booking"),
    path('contact/',views.contact, name="contact"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',views.signup, name="signup"),    
    path('recommendation/', views.smart_recommendation, name='recommendation'),
]
