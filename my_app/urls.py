from django.urls import path
from my_app.views import index_view,detail_index

urlpatterns = [
    
path('',index_view, name ='index'),
path('detail/<int:id>',detail_index, name ='detail'),


]