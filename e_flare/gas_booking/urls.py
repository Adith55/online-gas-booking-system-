from django.urls import path
from. import views
# from .views import booking_histroy,booking_histroy

urlpatterns = [
    path('',views.main, name="home"),
    path('signup/',views.signup,name='signup'),
    path('login/', views.login, name="login"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name="logout"),
    path('new_connection/',views.new_connection,name="new_connection"),
    path('book_cylinder/',views.book_cylinder,name="book_cylinder"),
    path('booking_histroy/',views.booking_histroy,name="booking_histroy"),
    path('create_admin/', views.create_admin),
    path('admin_login/', views.admin_login,name="admin_login"),
    path('admin_base/', views.admin_base,name="admin_base"),
    path('admin_users/', views.admin_users,name="admin_users"),
    path('delete/<id>',views.delete,name="delete"),
    path('admin_adduser/',views.admin_adduser,name="admin_adduser"),
    path('employee_add/',views.employee_form,name="employee_add"),
    path('employee_list/',views.employee_list,name="employee_list"),
    path('employee_delete/<empCode>',views.employee_delete,name="employee_delete"),
    path('bookings/',views.bookings,name="bookings"),
    path('approve/<number>',views.approve,name="approve"),
    path('reject/<number>',views.reject,name="reject"),
    path('profile/', views.profile,name="profile"),



]