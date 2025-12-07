from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from .models import Book, Publisher, Book9, Student, Address, Student2, ImageModel
from django.db.models import Q, F, Count, Sum, Avg, Max, Min
from .forms import BookForm, StudentForm, StudentForm2, ImageForm
# Lab 12 Modification: Import login_required 
from django.contrib.auth.decorators import login_required

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
    mybooks=Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books':mybooks}) 


def complex_query(request): 
    mybooks=books=Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10] 
    if len(mybooks) >= 1: 
        return render(request, 'bookmodule/bookList.html', {'books':mybooks}) 
    else: 
        return render(request, 'bookmodule/index.html') 
    

# -------------------- LAB 8 --------------------

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

# -------------------- LAB 9 --------------------
def lab9_task1(request):
    total_q = Book9.objects.aggregate(total=Sum('quantity'))['total'] or 1
    books = Book9.objects.all()

    for b in books:
        b.availability = (b.quantity * 100.0) / total_q

    return render(request, 'bookmodule/lab9_task1.html', {'books': books})


def lab9_task2(request):
    publishers = Publisher.objects.annotate(
        total_stock = Sum('book9__quantity')
    )
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})


def lab9_task3(request):
    publishers = Publisher.objects.annotate(
        oldest_book_date=Min('book9__pubdate')
    )
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})

def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price = Avg('book9__price'),
        min_price = Min('book9__price'),
        max_price = Max('book9__price')
    )
    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})


def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_count = Count('book9', filter=Q(book9__rating__gte=4))
    )
    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})


def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        filtered_books = Count(
            'book9',
            filter=(
                Q(book9__price__gt=50) &
                Q(book9__quantity__lt=5) &
                Q(book9__quantity__gte=1)
            )
        )
    )
    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})



# -------------------- LAB 10 - Part 1 (CRUD WITHOUT Django Forms) --------------------

def lab10_part1_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_part1_listbooks.html', {'books': books})

# --- Lab 12: Added login_required ---
@login_required(login_url='login_user')
def lab10_part1_addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')

        if title and author:
            Book.objects.create(
                title=title,
                author=author,
                price=float(price) if price else 0.0,
                edition=int(edition) if edition else 1,
            )
            return redirect('lab10_part1_listbooks')

    return render(request, 'bookmodule/lab10_part1_addbook.html')

# --- Lab 12: Added login_required ---
@login_required(login_url='login_user')
def lab10_part1_editbook(request, id):
    book = get_object_or_404(Book, pk=id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')

        book.price = float(price) if price else 0.0
        book.edition = int(edition) if edition else 1
        book.save()
        return redirect('lab10_part1_listbooks')

    return render(request, 'bookmodule/lab10_part1_editbook.html', {'book': book})

# --- Lab 12: Added login_required ---
@login_required(login_url='login_user')
def lab10_part1_deletebook(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    return redirect('lab10_part1_listbooks')

# -------------------- LAB 10 - Part 2 (CRUD With Django Forms) --------------------

def lab10_part2_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_part2_listbooks.html', {'books': books})

# --- Lab 12: Added login_required ---
@login_required(login_url='login_user')
def lab10_part2_addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab10_part2_listbooks')
    else:
        form = BookForm()

    return render(request, 'bookmodule/lab10_part2_addbook.html', {'form': form})

# --- Lab 12: Added login_required ---
@login_required(login_url='login_user')
def lab10_part2_editbook(request, id):
    book = get_object_or_404(Book, pk=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('lab10_part2_listbooks')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookmodule/lab10_part2_editbook.html', {'form': form, 'book': book})

# --- Lab 12: Added login_required ---
@login_required(login_url='login_user')
def lab10_part2_deletebook(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    return redirect('lab10_part2_listbooks')

# -------------------- LAB 11 --------------------

# --- Lab 12: Added login_required ---
@login_required(login_url='login_user')
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    
    else:
        form = StudentForm()
    
    return render(request, 'bookmodule/add_student.html', {'form': form})

def list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/list_students.html', {'students': students})

# --- Lab 12: Added login_required ---
@login_required(login_url='login_user')
def add_student_2(request):
    if request.method == 'POST':
        form = StudentForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students_2')
    else:
        form = StudentForm2()
    return render(request, 'bookmodule/add_student_2.html', {'form': form})

def list_students_2(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/list_students_2.html', {'students': students})


# --- Lab 12: Added login_required ---
@login_required(login_url='login_user')
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
    else:
        form = ImageForm()
    
    images = ImageModel.objects.all()
    return render(request, 'bookmodule/upload_image.html', {'form': form, 'images': images})