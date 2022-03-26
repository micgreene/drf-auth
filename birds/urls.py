from django.urls import path
from .views import BirdList, BirdDetail

urlpatterns =[
    path('', BirdList.as_view(), name='bird_list'),
    path('<int:pk>/', BirdDetail.as_view(), name='bird_detail'),
]