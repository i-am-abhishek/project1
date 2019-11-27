from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list')

]
