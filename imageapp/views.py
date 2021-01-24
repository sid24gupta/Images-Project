from django.shortcuts import render,redirect
from .forms import BookForm
from django.contrib import messages
from .models import Book
# Create your views here.
def index(request):

    if request.method == 'POST':

        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('/')
    else:
        form = BookForm()
    form = BookForm()
    img = Book.objects.all().order_by('book_name')
    return render(request, "index.html", {"img": img, "form": form})


def search(request):

    name1 = request.POST['name1']
    if Book.objects.filter(book_name=name1).exists():
        print("yes")
        messages.info(request,'Book exist in database')
        return render(request, 'search.html',{'obj':name1})
    else:
        print("no")
        messages.info(request,'Book does not exist in database')
        return render(request, 'search.html')

def delete(request):
    name1 = request.POST['value1']
    print(name1)
    Book.objects.filter(book_name=name1).delete()
    return render(request,'delete.html')




