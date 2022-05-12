from django.urls import path
from inventory import views

app_name = 'store'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('api/', views.api, name='api'),

]