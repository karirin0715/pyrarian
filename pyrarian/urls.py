from django.urls import path
from . import views


urlpatterns = [
    path('', views.front_page),
    path('table', views.list_table),
    path('table/<slug:slug>', views.table_def, name='table_name'),
]
