from django.urls import path
from base import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_patient',views.add_patient,name='add_patient'),
    path('list',views.list,name='list'),
    path('remove<int:pk>/',views.remove,name='remove')
    
]
