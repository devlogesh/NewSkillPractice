from django.urls import path,include
from .views import *


urlpatterns = [
    path('signup/',Singup.as_view(),name='signup'),
    path('login/',UserLoginAPIView.as_view(),name='login'),
    path('user_list/',ListUserProfile.as_view(),name='user_list'),
    path('user_lis2t/',ListUserProfile2.as_view(),name='user_list2')
]
