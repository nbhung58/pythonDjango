from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm


# Create your views here.
class IndexClass(View):
    def get(self, request):
        return HttpResponse("<h1>Xin chao</h1>")


class LoginClass(View):
    def get(self, request):
        return render(request, template_name='Login/login.html')

    def post(self, request):
        username = request.POST.get("tendangnhap")
        password = request.POST.get("password")
        my_user = authenticate(username= username, password= password)
        if my_user is None:
            return HttpResponse(f"Dang nhap that bai User {username} khong ton tai")

        login(request, my_user)
        return render(request, 'Login/success.html')

class ViewUser(LoginRequiredMixin, View):
    login_url= '/login/'
    def get(self, request):
        return HttpResponse("<h1>Day la view user </h1>")
    
    def post(self, request):
        pass

@decorators.login_required(login_url='/login/')
def view_product(request):
    return HttpResponse('Xem san pham')


class AddPost(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        f = PostForm()
        context = {'fm': f}
        return render(request, 'Login/add_post.html', context)

    def post(self, request):
        f = PostForm(request.POST)
        if not f.is_valid():
            return HttpResponse('Ban nhap sai du lieu')
        #check user permission
        print(request.user.get_all_permissions())
        if request.user.has_perm('Login.add_post'):
            f.save()
        else: 
            return HttpResponse('Ban chua duoc cap quyen')
        return HttpResponse("Oke")