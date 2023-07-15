from django.contrib import admin
from django.urls import path
from crud.views import *

urlpatterns = [
    path('view',article_list),
    path('list/<int:pk>',detail_list)
]
