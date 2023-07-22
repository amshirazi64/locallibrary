from django.shortcuts import render
from django.views import generic
from . import models


class Index(generic.TemplateView):

    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_books'] = models.Book.objects.all().count()
        context['num_instances'] = models.BookInstance.objects.all().count()
        context['num_instances_available'] = models.BookInstance.objects.filter(status__exact='a').count()
        context['num_authors'] = models.Author.objects.count() 
        return context
    
class BookListView(generic.ListView):
    model = models.Book
    template_name = 'catalog/book_list.html'


class BookDetailView(generic.DetailView):
    model = models.Book
    template_name = 'catalog/book_detail.html'

class AuthorListView(generic.ListView):
    model = models.Author
    template_name = 'catalog/author_list.html'

