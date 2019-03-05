from django.shortcuts import render
from catelog.models import BookInstance, Book, Genre, Author


# Create your views here.

def index(request):
    """View Function for home page site."""
    # Generate counts of som of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available Books ( status='a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The all() is implified by default
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instance': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors
    }

    # Rendering template with context
    return render(request, 'index.html', context=context)
