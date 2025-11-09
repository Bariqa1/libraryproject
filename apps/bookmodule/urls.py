# apps/bookmodule/urls.py

from django.urls import path
from . import views 

urlpatterns = [ 
    path('', views.index, name="books.index"), 
    
    path('list_books/', views.list_books, name="books.list_books"), 
    
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"), 
    
    path('aboutus/', views.aboutus, name="books.aboutus"), 
    
    path('html5/links', views.links_page_view, name='html5_links'),

    path('html5/text/formatting', views.text_formatting_view, name='text_formatting'),

    path('html5/listing', views.listing_view, name='html5_listing'),

    path('html5/tables', views.tables_view, name='html5_tables'),
    
    path('search', views.book_search_view, name='book_search'),

    path('simple/query', views.simple_query, name='simple_book_query'),
    
    path('complex/query', views.complex_query, name='complex_book_query'),

    path('lab8/task1', views.task1, name='task1'),

    path('lab8/task2', views.task2, name='task2'),

    path('lab8/task3', views.task3, name='task3'),

    path('lab8/task4', views.task4, name='task4'),

    path('lab8/task5', views.task5, name='task5'),

    path('lab8/task6', views.task6, name='task6'),
    
    path('lab8/task7', views.task7, name='task7'),

]


