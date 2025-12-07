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
    
    path('lab9/task1', views.lab9_task1, name='lab9_task1'),
    path('lab9/task2', views.lab9_task2, name='lab9_task2'),
    path('lab9/task3', views.lab9_task3, name='lab9_task3'),
    path('lab9/task4', views.lab9_task4, name='lab9_task4'),
    path('lab9/task5', views.lab9_task5, name='lab9_task5'),
    path('lab9/task6', views.lab9_task6, name='lab9_task6'),

    # ---------- Lab 10 - Part 1 ----------
    path('lab10_part1/listbooks',  views.lab10_part1_listbooks,  name='lab10_part1_listbooks'),
    path('lab10_part1/addbook',    views.lab10_part1_addbook,    name='lab10_part1_addbook'),
    path('lab10_part1/editbook/<int:id>',   views.lab10_part1_editbook,   name='lab10_part1_editbook'),
    path('lab10_part1/deletebook/<int:id>', views.lab10_part1_deletebook, name='lab10_part1_deletebook'),

    # ---------- Lab 10 - Part 2  ----------
    path('lab10_part2/listbooks',  views.lab10_part2_listbooks,  name='lab10_part2_listbooks'),
    path('lab10_part2/addbook',    views.lab10_part2_addbook,    name='lab10_part2_addbook'),
    path('lab10_part2/editbook/<int:id>',   views.lab10_part2_editbook,   name='lab10_part2_editbook'),
    path('lab10_part2/deletebook/<int:id>', views.lab10_part2_deletebook, name='lab10_part2_deletebook'),

# ---------- lab 11 ----------
    path('add_student/', views.add_student, name='add_student'),
    path('list_students/', views.list_students, name='list_students'),

    path('add_student_2/', views.add_student_2, name='add_student_2'),
    path('list_students_2/', views.list_students_2, name='list_students_2'),

    
    path('upload_image/', views.upload_image, name='upload_image'),
]


