# from random import randint
# # from random import randintfrom
# from random import randint
# from random import randint
# from random import randintfrom

from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from Designing_Cyber_Insurance_Policies.settings import DEFAULT_FROM_EMAIL
from user.forms import RegisterForms
from user.models import RegisterModel, UploadModel, RequestModel, FeedbackModel


# def index(request):
#     usid=''
#     if request.method=="POST":
#         usid=request.POST.get('username')
#         pswd = request.POST.get('password')
#         try:
#             check = RegisterModel.objects.get(userid=usid,password=pswd)
#             request.session['userid']=check.id
#             return redirect('user_page')
#         except:
#             pass
#     return render(request,'user/index.html',{'fh':usid})

# def register(request):
#     if request.method=="POST":
#         forms=RegisterForms(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('index')
#     else:
#         forms=RegisterForms()
#     return render(request,'user/register.html',{'form':forms})

# def user_page(request):
#     uid = request.session['userid']
#     request_obj = RegisterModel.objects.get(id=uid)
#     myfile=''
#     a=''
#     b=''
#     c=''
#     d=''
#     if request.method=="POST"and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         a=request.POST.get('name')
#         b=request.POST.get('category')
#         c=request.POST.get('area')
#         UploadModel.objects.create(file_name=a,category=b,upload_user=request_obj,upload_file=myfile,area=c)
#     return render(request,'user/user_page.html')

# def upload_fileview(request):
#     uid=''
#     sts = 'pending'
#     sent = 'sent'
#     uid = request.session['userid']
#     request_obj = RegisterModel.objects.get(id=uid)
#     obj=UploadModel.objects.filter(upload_user=request_obj)
#     if request.method=="POST":
#         uid=request.session['userid']
#         request_obj=RegisterModel.objects.get(id=uid)
#         subject = "OTP"
#         text_content = ""
#         otp = randint(1000, 9999)
#         request.session['otp']=otp
#         html_content = "<br/><p>OTP :<strong>" + str(otp) + "</strong>/p>"
#         from_mail = DEFAULT_FROM_EMAIL
#         to_mail = [request_obj.email]
#     # if send_mail(subject,message,from_mail,to_mail):
#         msg = EmailMultiAlternatives(subject, text_content, from_mail, to_mail)
#         msg.attach_alternative(html_content, "text/html")
#         if msg.send():
#             sts='sent'
#             #return redirect('otppage',lawer=userObj.id)
#     return render(request,'user/upload_fileview.html',{'obj':obj,'sts':sts,'sent':sent,})

# def otppage(request,pk):
#     password = request.session['otp']
#     sts = "c"
#     pas = type(password)
#     ss=''
#     count=0
#     aaa=''
#     vott,vott1=0,0
#     pkid=UploadModel.objects.get(id=pk)
#     aaa=pkid.id
#     request.session['jhf']=aaa
#     if request.method == "POST":

#         objs = UploadModel.objects.get(id=pk)
#         unid = objs.id
#         vot_count = UploadModel.objects.all().filter(id=unid)
#         for t in vot_count:
#             vott = t.add_count
#         vott1 = vott + 1
#         obj = get_object_or_404(UploadModel, id=unid)
#         obj.add_count = vott1
#         obj.save(update_fields=["add_count"])



#         onetime = request.POST.get('otp', '')
#         ss = onetime
#         if int(password) == int(onetime):

#             return redirect('download_page')
#         else:
#             sts = "Please Enter Correct OTP"

#     return render(request, 'user/otppage.html',{'password':pas,'sts':sts,'count':aaa})

# def download_page(request):
#     count=0
#     aaaa= request.session['jhf']
#     obj=UploadModel.objects.filter(id=aaaa)
#     if request.method == "POST":
#         obj = get_object_or_404(UploadModel, id=obj)
#         obj.add_count = count
#         obj.save(update_fields=["add_count"])
#         return redirect('upload_fileview')
#     return render(request,'user/download_page.html',{'a':aaaa,'obj':obj})
# def request(request,pk):
#     a=''
#     userid = request.session['userid']
#     uobj = RegisterModel.objects.get(id=userid)
#     obj = UploadModel.objects.get(id=pk)
#     a=obj.category
#     RequestModel.objects.create(accessone=uobj,accesstwo=obj,cate=a)
#     return redirect('download_page')


# def view_file(request):
#     uid = request.session['userid']
#     request_obj = RegisterModel.objects.get(id=uid)
#     obj = UploadModel.objects.filter(upload_user=request_obj)
#     return render(request,'user/view_file.html',{'obj':obj})

# def send_feedback(request):
#     uid = request.session['userid']
#     objec = RegisterModel.objects.get(id=uid)
#     if request.method == "POST":
#         feed = request.POST.get('feedback')
#         FeedbackModel.objects.create(username=objec, feedback=feed)
#     return render(request,'user/send_feedback.html')

# def mydetails(request):
#     usid = request.session['userid']
#     us_id = RegisterModel.objects.get(id=usid)
#     return render(request,'user/mydetails.html',{'obje':us_id})

from random import randint
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect, get_object_or_404
from Designing_Cyber_Insurance_Policies.settings import DEFAULT_FROM_EMAIL
from user.forms import RegisterForms
from user.models import RegisterModel, UploadModel, RequestModel, FeedbackModel
from django.shortcuts import render
from django.http import HttpResponse
# from .models import UserProfile

def index(request):
    usid = ''
    if request.method == "POST":
        usid = request.POST.get('username')
        pswd = request.POST.get('password')
        try:
            check = RegisterModel.objects.get(userid=usid, password=pswd)
            request.session['userid'] = check.id
            return redirect('user_page')
        except RegisterModel.DoesNotExist:
            pass
    return render(request, 'user/index.html', {'fh': usid})


def register(request):
    if request.method == "POST":
        forms = RegisterForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    else:
        forms = RegisterForms()
    return render(request, 'user/register.html', {'form': forms})


def user_page(request):
    uid = request.session.get('userid')
    if not uid:
        return redirect('index')  # Redirect if no session is present

    request_obj = RegisterModel.objects.get(id=uid)
    if request.method == "POST" and request.FILES.get('myfile'):
        myfile = request.FILES['myfile']
        name = request.POST.get('name')
        category = request.POST.get('category')
        area = request.POST.get('area')
        UploadModel.objects.create(
            file_name=name, category=category, upload_user=request_obj, upload_file=myfile, area=area
        )
    return render(request, 'user/user_page.html')


def upload_fileview(request):
    uid = request.session.get('userid')
    if not uid:
        return redirect('index')  # Redirect if no session is present

    request_obj = RegisterModel.objects.get(id=uid)
    obj = UploadModel.objects.filter(upload_user=request_obj)
    sts = 'pending'
    
    if request.method == "POST":
        subject = "OTP"
        otp = randint(1000, 9999)
        request.session['otp'] = otp

        html_content = f"<br/><p>OTP : <strong>{otp}</strong></p>"
        text_content = f"Your OTP is {otp}"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [request_obj.email]

        msg = EmailMultiAlternatives(subject, text_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")

        try:
            if msg.send():
                sts = 'sent'
        except Exception as e:
            print(f"Error sending email: {e}")
            sts = 'error'
    
    return render(request, 'user/upload_fileview.html', {'obj': obj, 'sts': sts})


def otppage(request, pk):
    stored_otp = request.session.get('otp')
    if not stored_otp:
        return redirect('upload_fileview')  # Redirect if no OTP in session

    pkid = get_object_or_404(UploadModel, id=pk)
    request.session['file_id'] = pkid.id
    status_message = ""

    if request.method == "POST":
        entered_otp = request.POST.get('otp', '')
        if entered_otp and str(stored_otp) == entered_otp:
            return redirect('download_page')
        else:
            status_message = "Please Enter Correct OTP"

    return render(request, 'user/otppage.html', {'sts': status_message, 'file_id': pkid.id})


# def download_page(request):
#     aaaa = request.session['jhf']
#     try:
#         obj = UploadModel.objects.get(id=aaaa)  # Use get() for a single object
#     except UploadModel.DoesNotExist:
#         obj = None

#     if request.method == "POST":
#         if obj:
#             obj.add_count = 0  # Set count to 0 or desired value
#             obj.save(update_fields=["add_count"])
#         return redirect('upload_fileview')

#     return render(request, 'user/download_page.html', {'obj': obj})

def download_page(request):
    count=0
    aaaa= request.session['jhf']
    obj=UploadModel.objects.filter(id=aaaa)
    if request.method == "POST":
        obj = get_object_or_404(UploadModel, id=obj)
        obj.add_count = count
        obj.save(update_fields=["add_count"])
        return redirect('upload_fileview')
    return render(request,'user/download_page.html',{'a':aaaa,'obj':obj})

def request_access(request, pk):
    user_id = request.session.get('userid')
    if not user_id:
        return redirect('index')  # Redirect if no session

    user = RegisterModel.objects.get(id=user_id)
    file_obj = get_object_or_404(UploadModel, id=pk)
    RequestModel.objects.create(accessone=user, accesstwo=file_obj, cate=file_obj.category)
    return redirect('download_page')


def view_file(request):
    user_id = request.session.get('userid')
    if not user_id:
        return redirect('index')  # Redirect if no session

    user = RegisterModel.objects.get(id=user_id)
    obj = UploadModel.objects.filter(upload_user=user)
    return render(request, 'user/view_file.html', {'obj': obj})


def send_feedback(request):
    user_id = request.session.get('userid')
    if not user_id:
        return redirect('index')  # Redirect if no session

    user = RegisterModel.objects.get(id=user_id)
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        FeedbackModel.objects.create(username=user, feedback=feedback)

    return render(request, 'user/send_feedback.html')


# def mydetails(request):
#     user_id = request.session.get('userid')
#     if not user_id:
#         return redirect('index')  # Redirect if no session

#     user = get_object_or_404(RegisterModel, id=user_id)
#     return render
# def mydetails(request):
#     # Example logic to fetch user details
#     try:
#         user_details = UserProfile.objects.get(user=request.user)
#     except UserProfile.DoesNotExist:
#         user_details = None  # Handle case where user details don't exist

#     context = {
#         'user_details': user_details,
#     }
#     return render(request, 'mydetails.html', context) 
def mydetails(request):
    usid = request.session['userid']
    us_id = RegisterModel.objects.get(id=usid)
    return render(request,'user/mydetails.html',{'obje':us_id})