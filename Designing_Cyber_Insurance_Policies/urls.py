# """Designing_Cyber_Insurance_Policies URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/1.11/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import re_path, include
#     2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
# """
# from django.urls import re_path
# from django.conf.urls.static import static
# from django.contrib import admin

# from Designing_Cyber_Insurance_Policies import settings
# from user import views as user_views
# from admins import views as admin_views

# urlpatterns = [
#     re_path('admin/', admin.site.urls),

#     re_path('^$',user_views.index,name="index"),
#     re_path('user/register', user_views.register, name="register"),
#     re_path('user_page', user_views.user_page, name="user_page"),
#     re_path('upload_fileview', user_views.upload_fileview, name="upload_fileview"),
#     re_path('view_file', user_views.view_file, name="view_file"),
#     re_path(r'^user/otppage/(?P<pk>\d+)/$', user_views.otppage, name="otppage"),
#     re_path('download_page',user_views.download_page,name="download_page"),
#     re_path('send_feedback',user_views.send_feedback,name="send_feedback"),
#     re_path('mydetails',user_views.mydetails,name="mydetails"),
#     re_path(r'^user/request/(?P<pk>\d+)/$',user_views.request_access, name="request_access"),



#     re_path('login',admin_views.login,name="login"),
#     re_path('admin_page',admin_views.admin_page,name="admin_page"),
#     re_path('view_userdetails',admin_views.view_userdetails,name="view_userdetails"),
#     re_path('view_uploadfile',admin_views.view_uploadfile,name="view_uploadfile"),
#     re_path('view_user_request',admin_views.view_user_request,name="view_user_request"),
#     re_path(r'^admin_update/(?P<pk>\d+)/$', admin_views.admin_update, name="admin_update"),
#     re_path('admin_graphicalanalysis', admin_views.admin_graphicalanalysis, name="admin_graphicalanalysis"),
#     re_path('view_userquery', admin_views.view_userquery, name="view_userquery"),
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path  # Import path for simpler URL patterns
from django.conf.urls.static import static
from django.contrib import admin

from Designing_Cyber_Insurance_Policies import settings
from user import views as user_views
from admins import views as admin_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', user_views.index, name="index"),
    path('user/register/', user_views.register, name="register"),
    path('user_page/', user_views.user_page, name="user_page"),
    path('upload_fileview/', user_views.upload_fileview, name="upload_fileview"),
    path('view_file/', user_views.view_file, name="view_file"),
    path('user/otppage/<int:pk>/', user_views.otppage, name="otppage"),
    path('download_page/', user_views.download_page, name="download_page"),
    path('send_feedback/', user_views.send_feedback, name="send_feedback"),
    path('mydetails/', user_views.mydetails, name="mydetails"),  # Ensure trailing slash
    path('user/request/<int:pk>/', user_views.request_access, name="request_access"),

    path('login/', admin_views.login, name="login"),
    path('admin_page/', admin_views.admin_page, name="admin_page"),
    path('view_userdetails/', admin_views.view_userdetails, name="view_userdetails"),
    path('view_uploadfile/', admin_views.view_uploadfile, name="view_uploadfile"),
    path('view_user_request/', admin_views.view_user_request, name="view_user_request"),
    path('admin_update/<int:pk>/', admin_views.admin_update, name="admin_update"),
    path('admin_graphicalanalysis/', admin_views.admin_graphicalanalysis, name="admin_graphicalanalysis"),
    path('view_userquery/', admin_views.view_userquery, name="view_userquery"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
