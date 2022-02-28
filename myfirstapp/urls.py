from django.urls import path
from . import views

app_name = 'myfirstapp'
urlpatterns = [
    path('',views.list_view, name='index'),
    path('create_view',views.create_view,name='create_view'),
    path('update/<id>',views.update_view,name='update_view'),
    path('<id>/delete',views.delete_view,name='delete_view'),
    path('<id>', views.detail_view,name='detail_view'),
    
    
]