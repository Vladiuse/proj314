from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('all_data/', views.all_data, name='all_data'),
]
