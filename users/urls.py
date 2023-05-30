from django.urls import path
from .views import home, profile, RegisterView, dashboard, tasks, ders, faq, elaqe, success, kitabxana, chatbot, riyaz, purchase

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('dashboard/',dashboard, name='dashboard'),
    path('tasks/', tasks, name='tasks'),
    path('ders/', ders, name='ders'),
    path('faq/', faq, name='faq'),
    path('elaqe/', elaqe, name='elaqe'),
    path('success/', success, name='success'),
    path('kitabxana/', kitabxana, name='kitabxana'),
    path('chatbot/', chatbot, name='chatbot'),
    path('purchase/', purchase, name='purchase'),
    path('riyaz/', riyaz, name='riyaz'),
]
