from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render , redirect

# Create your views here.
from .models import Register


def registerpage(request):
    return render(request, 'reg.html')
def registrationpage(request):
    r = Register()
    r.name = request.POST.get("name")
    r.dob = request.POST.get("dob")
    r.phone = request.POST.get("phone")
    photo = request.FILES['image']
    img = FileSystemStorage()
    filename = img.save(photo.name, photo)
    upload_file_url = img.url(filename)
    r.image = upload_file_url
    r.username = request.POST.get("username")
    r.password = request.POST.get("password")
    r.type = "student"
    r.save()
    return render(request, 'reg.html')
def loginpage(request):
    lg = Register()
    lg.username = request.POST.get("username")
    lg.password = request.POST.get("password")
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        data = Register.objects.all()
        username = request.POST.get("username")
        password = request.POST.get("password")
        flag = 0
        for i in data:
            if username == i.username and password == i.password:
                flag = 1
                type = i.type
                request.session['uid'] = username
                if type == "student":
                    return render(request, 'students.html')
                if type == "admin":
                    return render(request, 'admin.html')


        if flag == 0:
            return HttpResponse("user does not exist")
def ViewStudents(request):
    st = Register.objects.all()
    return render(request, 'index.html', {'st': st})
def AdminEdit(request, id):
    ap = Register.objects.get(id=id)
    return render(request, 'AdminEdit.html', {'uv':ap})

def update(request, id):
    up = Register.objects.get(id=id)
    up.name = request.POST.get("name")
    up.dob = request.POST.get("dob")
    up.phone = request.POST.get("phone")
    photo = request.FILES['image']
    img = FileSystemStorage()
    filename = img.save(photo.name, photo)
    upload_file_url = img.url(filename)
    up.image = upload_file_url
    up.save()
    return redirect('/index.html')