from django.shortcuts import render
from django.template import Template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from VoidPortal.PostForm import Post
import psycopg2


# Create your views here.
def primary(request):
    if request.method == "POST":
        form = Post(request.POST)
        if form.is_valid():
            connection = psycopg2.connect("dbname=postgres user=postgres password=Password")
            cursor = connection.cursor()
            message = request.POST["message"]
            cursor.execute("""INSERT INTO public.posts(messages) VALUES(%s)""", (message,))
            connection.commit()
            cursor.close()
            connection.close()
            return HttpResponseRedirect('/Thanks/')
    context = {'Listeners': '0'}
    return render(request, 'index.html', context)


def Secondary(request):

    context = {'Listeners': '0'}
    return render(request, 'Thanks.html', context)

