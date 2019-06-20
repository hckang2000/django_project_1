from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.board_list),
    path('write/', views.board_write),
    path('detail/<int:pk>/', views.board_detail),
]
