
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     
    # path('sinup',views.login,name='signup'),
    # path('login',views.login,name='login'),
     path('login/',views.LoginPage,name='login'),
      path('logout/',views.LogoutPage,name='logout'),
    path('home',views.home,name='home'),
    # path('fixed',views.fixednav,name='fixednav'),

    path('',views.SignupPage,name='signup'),
    path('insert',views.Insertvendor,name='index'),

    # path('',views.page2,name='page2'),
    path('insert1',views.FormDetails,name='page2'),
    path('gstin/',views.Search_gstin,name="gstin"),

    
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)