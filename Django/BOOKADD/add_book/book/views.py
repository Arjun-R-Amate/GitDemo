from django.shortcuts import render, HttpResponse
from . models import book_add

# Create your views here.
def homepage(request):
    if request.method == "POST":
        book_author = request.POST['author']
        book_title = request.POST['title']
        book_description = request.POST['desc']

        new_book = book_add(author= book_author, title= book_title, description = book_description)
        new_book.save()

        return HttpResponse("Book saved successfully into database.")

    return render(request, 'index.html', {})
    