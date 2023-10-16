from django.shortcuts import render

def index_view(request):

    age = 5 
    year = 2020

    context = {
        'age':age,
        'year':year,
    }

    return render(request,'index.html',context)


