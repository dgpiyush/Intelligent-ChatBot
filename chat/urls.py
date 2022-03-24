from django.contrib.auth.views import logout
from django.urls import path
from . import views





urlpatterns = [
    path('', views.home, name='home'),
    
    path('ask', views.response, name='response'),

    path('administration', views.index, name='index'),
    path('administration/login', views.AdLogin, name='adminlogin'),
  
    path('chat_viewMY/', views.chat_viewMY, name='chat_viewMY'),

    path('trianbot/', views.trianBot, name='trianBot'),

 
    path('chat1/<int:reciver>/', views.message_view1, name='chat1'),


    
    path('api/messages1/<int:sender>/<int:receiver>', views.message_list1, name='message-detail1'),
    path('api/messages1/', views.message_list1, name='message-list1'),
    
    path('logout/', logout, {'next_page': 'index'}, name='logout'),
    path('register/', views.register_view, name='register'),
]
