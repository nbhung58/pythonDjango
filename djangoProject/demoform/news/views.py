from django.shortcuts import render
from django.http import HttpResponse
from requests import request
from .forms import PostForm, SendEmail
from django.views import View

# Create your views here.
class IndexClass(View):
    def get(self, request):
        ketqua = "1233232345"
        return HttpResponse(ketqua)

# class PostClass(View):
#     def get(self, request):
#         a = PostForm()
#         return render(request, 'news/add_news.html', {'f': a})

class ClassSaveNews(View):
    def get(self, request):
        a = PostForm()
        return render(request, 'news/add_news.html', {'f': a})

    def post(self, request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('Luu oke')
        else:
            return HttpResponse('Khong duoc validate')
    
    def put(self):
        pass

def email_view(request):
    b = SendEmail
    return render(request, 'news/email.html', {'f': b})

def prosess(request):
    if request.method == "POST":
        m = SendEmail(request.POST)
        if m.is_valid():
            # tieude = m.cleaned_data['title']
            # cc = m.cleaned_data['cc']
            # noidung = m.cleaned_data['content']
            # email = m.cleaned_data['email']
            # context = { 'td':tieude, 'c': cc, 'b': noidung, 'd': email}
            context2 = {'email_data': m}
            return render(request, 'news/print_email.html', context2)
        else:
            return HttpResponse('Form not validate')
    else:
        return HttpResponse('Không phải POST method')
            