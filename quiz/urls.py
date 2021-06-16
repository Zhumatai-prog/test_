from django.urls import path, include
from django.contrib.auth.views import LoginView

from .views import *

urlpatterns = [
    path('', home_view, name='home_view'),
    path('test-list/', student_exam_view, name='topic_list'),
    path('test/take/<int:pk>/', take_exam_view, name='test_take'),
    path('test/start/<int:pk>/', start_exam_view,name='test_start'),
    path('user/list/', user_view, name='user_list'),

    path('login/', ProjectLoginView.as_view(),name='login'),

    path('signup/', RegisterUserView.as_view(), name='signup'),
    path('logout/', MyProjectLogout.as_view(), name='logout'),


]
