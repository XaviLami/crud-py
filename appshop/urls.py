from django.urls import path
from . import views

app_name = 'appshop'
urlpatterns = [
  path('',views.home,name='home'),
  path('create_product',views.create_view,name='create_view'),
  path('update/<id>',views.update_view,name='update_view'),
  path('<id>/delete',views.delete_view,name='delete_view'),
  path('<id>',views.detail_view,name='detail_view')
]