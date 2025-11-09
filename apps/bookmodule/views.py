from django.shortcuts import render
from django.http import HttpResponse 
from .models import Book
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Student

BOOKS_DATA = {
    1: {'id': 1, 'title': 'Internet & World Wide Web How to Program', 'author': 'author name', 'description': 'Description for Book 1.', 'image_file': 'book1.jpg'},
    2: {'id': 2, 'title': 'C++ How to Program, Late Objects Version', 'author': 'author name', 'description': 'Description for Book 2.', 'image_file': 'book2.jpg'},
    3: {'id': 3, 'title': 'Images in Another Folder', 'author': 'author name', 'description': 'Description for Book 3.', 'image_file': 'book3.jpg'}
}
BOOK_123 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley', 'description': 'CD description.', 'image_file': 'book1.jpg'}
BOOK_456 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam', 'description': 'SRE description.', 'image_file': 'book2.jpg'}

BOOKS_DATA[BOOK_123['id']] = BOOK_123
BOOKS_DATA[BOOK_456['id']] = BOOK_456


def index(request): 
    return render(request, "bookmodule/index.html") 

def list_books(request): 
    return render(request, 'bookmodule/list_books.html') 

def viewbook(request, bookId): 
    targetBook = BOOKS_DATA.get(bookId)

    if targetBook is None:
        targetBook = {'title': 'Book Not Found', 'author': 'N/A', 'description': 'N/A', 'image_file': 'default.jpg'}
        
    context = {'book': targetBook, 'book_id': bookId}
    return render(request, 'bookmodule/one_book.html', context) 

def aboutus(request): 
    return render(request, 'bookmodule/aboutus.html')

def links_page_view(request):
    return render(request, 'bookmodule/links_page.html')

def text_formatting_view(request):
    return render(request, 'bookmodule/formatting_page.html')

def listing_view(request):
    return render(request, 'bookmodule/listing_page.html')

def tables_view(request):
    return render(request, 'bookmodule/tables_page.html')


def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def book_search_view(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')  
        isAuthor = request.POST.get('option2') 

        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            
            if isTitle and string in item['title'].lower(): 
                contained = True
 
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
                
            if contained: 
                newBooks.append(item)
        
        return render(request, 'bookmodule/bookList.html', {'books': newBooks, 'keyword': string})
   
    return render(request, 'bookmodule/bookSearchForm.html')


def simple_query(request): 
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects 
    return render(request, 'bookmodule/bookList.html', {'books':mybooks}) 


def complex_query(request): 
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10] 
    if len(mybooks)>=1: 
       return render(request, 'bookmodule/bookList.html', {'books':mybooks}) 
    else: 
      return render(request, 'bookmodule/index.html') 
    
def task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': books})


def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) &
        (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})


def task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) &
        ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})


def task4(request):
    books = Book.objects.all().order_by('title') 
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})


def task5(request):
    stats = Book.objects.aggregate(
        count=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})

def task6(request):
    students = Student.objects.select_related('address').all()
    return render(request, 'bookmodule/lab8_task6.html', {'students': students})

def task7(request):
    data = Student.objects.values('address__city').annotate(count=Count('id'))
    return render(request, 'bookmodule/lab8_task7.html', {'data': data})

