from django.shortcuts import render,redirect
from .models import library
from .forms import bookform
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'html.html')




def booklist(request):
    shelf = library.objects.all()
    return render(request, 'booklist.html', {'shelf': shelf})

def adminpanel(request):
    return render(request,'admin.html')

def upload(request):
    uploads = bookform()

    if request.method == "POST":
        uploads = bookform( request.POST,request.FILES)
        if uploads.is_valid():
            uploads.save()
            return redirect('upload')
        else:
            return HttpResponse("something went wrong please reload the webpage by clicking")
    else:
        return render(request,'upload.html',{"upload_form":uploads})

def update_book(request,book_id):
    book_id = int(book_id)
    try:
        book_shelf = library.objects.get(id=book_id)
    except library.DoesNotExist:
        return redirect('booklist')
    book_form = bookform(request.POST or None,instance=book_shelf)
    if book_form.is_valid():
        book_form.save()
        return redirect('booklist')
    return render(request,'upload.html',{'upload_form':book_form})
def delete(request,book_id):
    book_id = int(book_id)
    try:
        book_shelf = library.objects.get(id=book_id)
    except library.DoesNotExist:
        return redirect('booklist')
    book_shelf.delete()
    return redirect('booklist')
