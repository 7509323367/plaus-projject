from django.urls import path
from .import views 
from plus.views import UploadView
from .views import JobCreate
urlpatterns=[   
    
     path('job',views.job,name='job'),
     path('candidate',views.candidate,name='candidate'),
     path('registration',views.registration,name='registration'),
     path('login',views.login,name='login'),
     path('logout',views.logout,name='logout'),
     path('Home',views.Home,name='Home'),
     path('scookie',views.scookie,name='scookie'),
     path('gcookie',views.gcookie,name='gcookie'),
     path('fileuplod',views.fileuplod,name='fileuplod'),
     path('port',views.port,name='port'),
     path('portpho1',UploadView.as_view()),
     path('jobcreate',JobCreate.as_view())
    
     ]