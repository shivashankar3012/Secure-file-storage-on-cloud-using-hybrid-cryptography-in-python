from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from user.models import RegisterModel, UploadModel, RequestModel, FeedbackModel


def login(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                return redirect('admin_page')
    return render(request,'admins/login.html')

def admin_page(request):
    return render(request,'admins/admin_page.html')

def view_userdetails(request):
    obj = RegisterModel.objects.all()
    return render(request,'admins/view_userdetails.html',{'objects':obj})

def view_uploadfile(request):
    obj = UploadModel.objects.all()
    return render(request,'admins/view_uploadfile.html',{'object':obj})

def view_user_request(request):
    obj=RequestModel.objects.all()
    return render(request,'admins/view_user_request.html',{'obj':obj})

def admin_update(request,pk):
    obj = RequestModel.objects.get(id=pk)
    a=obj.accesstwo.id
    jki=UploadModel.objects.filter(id=a)

    if request.method == "POST":
        add_count = request.POST.get('add_count', '')


        obj = get_object_or_404(UploadModel, id=a)
        obj.add_count = add_count


        obj.save(update_fields=["add_count",])
        return redirect('view_user_request')

    return render(request,'admins/admin_update.html',{'a':jki})


def admin_graphicalanalysis(request):
    chart = RequestModel.objects.values('cate').annotate(dcount=Count('cate'))
    return render(request,'admins/admin_graphicalanalysis.html',{'objects':chart})

def view_userquery(request):
    obj = FeedbackModel.objects.all()
    return render(request,'admins/view_userquery.html',{'object':obj})