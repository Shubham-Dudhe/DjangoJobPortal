
from django.urls import path
from .views import post_data,sidebar

urlpatterns = [
    path('post_data/',post_data,name='post_data'),
    path('sidebar/',sidebar,name='sidebar')
]