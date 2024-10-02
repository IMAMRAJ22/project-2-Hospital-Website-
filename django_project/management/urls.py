from django.urls import path # type: ignore
from management import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login_page,name='login'),
    path('signup/',views.signup_page,name='signup'),
    path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('patients/',views.patients,name='patients'),
    path('doctorlogin/',views.doctorlogin,name='doctorlogin'),
    path('delete/<int:id>/',views.delete_data,name='deletedata'),
    # path('delete/',views.delete,name='delete'),

]