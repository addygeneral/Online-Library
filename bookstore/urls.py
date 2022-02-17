from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [

# Shared URL's
 path('', views.login_form, name='home'),
 path('login/', views.loginView, name='login'),
 path('logout/', views.logoutView, name='logout'),
 path('regform/', views.register_form, name='regform'),
 path('register/', views.registerView, name='register'),



 # Lecturers URL's

path('lecturer/', views.lecturer, name='lecturer'),
path('labook_form/', views.labook_form, name='labook_form'),
path('labook/', views.labook, name='labook'),
path('llbook/', views.LBookListView.as_view(), name='llbook'),
path('lsearch/', views.lsearch, name='lsearch'),
path('ldbook/<int:pk>', views.LDeleteBook.as_view(), name='ldbook'),
path('lmbook/', views.LManageBook.as_view(), name='lmbook'),
path('ldbookk/<int:pk>', views.LDeleteView.as_view(), name='ldbookk'),
path('lvbook/<int:pk>', views.LViewBook.as_view(), name='lvbook'),
path('lebook/<int:pk>', views.LEditView.as_view(), name='lebook'),
path('lcchat/', views.LCreateChat.as_view(), name='lcchat'),
path('llchat/', views.LListChat.as_view(), name='llchat'),
path('ldrequest/<int:pk>'  , views.LDeleteRequest.as_view(), name='ldrequest'),
path('lmrequest/', views.LMakeRequest.as_view(), name='lmrequest'),





 # Student URL's
 path('student/', views.UBookListView.as_view(), name='student'),
 path('uabook_form/', views.uabook_form, name='uabook_form'),
 path('uabook/', views.uabook, name='uabook'),
 path('ucchat/', views.UCreateChat.as_view(), name='ucchat'),
 path('ulchat/', views.UListChat.as_view(), name='ulchat'),
 path('mkreq_form/', views.mkreq_form, name='mkreq_form'),
 path('make_request/', views.make_request, name='make_request'),
 path('about/', views.about, name='about'),
 path('usearch/', views.usearch, name='usearch'),
 path('delete_request/', views.AMakeRequest.as_view(), name='delete_request'),
 path('amrequest/', views.AMakeRequest.as_view(), name='amrequest'),





 # Admin URL's
 path('dashboard/', views.dashboard, name='dashboard'),
 path('acchat/', views.ACreateChat.as_view(), name='acchat'),
 path('alchat/', views.AListChat.as_view(), name='alchat'),
 path('aabook_form/', views.aabook_form, name='aabook_form'),
 path('aabook/', views.aabook, name='aabook'),
 path('albook/', views.ABookListView.as_view(), name='albook'),
 path('ambook/', views.AManageBook.as_view(), name='ambook'),
 path('adbook/<int:pk>', views.ADeleteBook.as_view(), name='adbook'),
 path('avbook/<int:pk>', views.AViewBook.as_view(), name='avbook'),
 path('aebook/<int:pk>', views.AEditView.as_view(), name='aebook'),
 path('amrequest/', views.AMakeRequest.as_view(), name='amrequest'),
 path('afeedback/', views.AFeedback.as_view(), name='afeedback'),
 path('asearch/', views.asearch, name='asearch'),
 path('adbookk/<int:pk>', views.ADeleteBookk.as_view(), name='adbookk'),
 path('create_user_form/', views.create_user_form, name='create_user_form'),
 path('aluser/', views.ListUserView.as_view(), name='aluser'),
 path('create_use/', views.create_user, name='create_user'),
 path('alvuser/<int:pk>', views.ALViewUser.as_view(), name='alvuser'),
 path('aeuser/<int:pk>', views.AEditUser.as_view(), name='aeuser'),
 path('aduser/<int:pk>', views.ADeleteUser.as_view(), name='aduser'),

 path('adrequest/<int:pk>'  , views.ADeleteRequest.as_view(), name='adrequest'),





















]
