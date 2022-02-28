from django.urls import path
from . import views

app_name = 'appshop'
urlpatterns = [
  path('',views.home,name='home'),
  path('create_view',views.create_view,name='create_view'),
]