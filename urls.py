# #Задание 1
# from django.contrib import admin
# from django.urls import path
#
# from blog.views import contact
#
# urlpatterns = [
#     path("admin/", admin.site.urls),
#
#     path("contact/", contact, name="contact"),
# ]

# #Задание 2
# from django.urls import path
# from . import views
#
# app_name = 'blog'
#
# urlpatterns = [
#
#     path('', views.feedback_view, name='feedback_url'),
#
#     path('success/', views.success_view, name='success_url'),
# ]

# # Задание 3
#
# from django.urls import path
# from . import views
#
# app_name = 'blog'
#
# urlpatterns = [
#
#     path('', views.my_view, name='my_view'),
# ]