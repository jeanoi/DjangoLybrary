from django.urls import path, include
from library import views

app_name='library'

urlpatterns=[
    path('', views.HomePage.as_view(), name='index'),
    path('bookList/', views.BookList.as_view(), name='list'),
    path('bookList/<pk>/', views.BookDetail.as_view(), name='details'),
    path('authorList/', views.AuthorList.as_view(), name='authors'),
    path('authorList/<pk>', views.AuthorDetail.as_view(), name='detail_author'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('borrowed/', views.LoanedBooksByUser.as_view(), name='borrowed')
]