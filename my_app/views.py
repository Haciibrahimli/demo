from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from my_app.models import MyModel



def index_view(request):

 my_datas = MyModel.objects.all()


 paginator = Paginator(my_datas, 2)
 page = request.GET.get('page', 1)
 p = paginator.get_page(page)
 try:
  p = paginator.page(page)
 except PageNotAnInteger:
  p = paginator.page(1)
 except EmptyPage:
  p = paginator.page(paginator.num_pages)
 context = {
    'my_datas':my_datas,
    'p':p,

    }

 return render(request,'index.html',context)

def detail_index(request, id):
 
 my_obj = MyModel.objects.get(id=id)
 
 context = {
  
  'my_obj':my_obj

 }
 
 

 return render(request,'detail.html',context)

