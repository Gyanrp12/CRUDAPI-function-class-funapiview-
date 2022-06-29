from django.urls import path
from  . import views

urlpatterns = [

#  path('',views.user,name='user'),
 path('rest_api/',views.UserAPI.as_view()),


]

