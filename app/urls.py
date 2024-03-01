from django.urls import path
from . import views
urlpatterns = [path('', views.home,name="home"),
               path('upload',views.upload,name="upload"),
                path('booklist',views.booklist,name="booklist"),
               path('adminpanel',views.adminpanel ,name="adminpanel"),
               path('update/<int:book_id>',views.update_book,name="update"),
               path('delete/<int:book_id>',views.delete,name="delete"),
               ]