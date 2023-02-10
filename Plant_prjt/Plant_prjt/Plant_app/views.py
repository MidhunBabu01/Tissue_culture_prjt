from django.shortcuts import render
from django.http.response import HttpResponse
from.models import Products,ProductsCategory
from django.shortcuts import redirect
# MAIL SENDING SECTION
from django.core.mail import  EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        emaill = request.POST.get('email')
        # print('EMAIL',email)
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        template = render_to_string('email.html',{'name':name,'phone':mobile,'subject':subject,'message':message,'emaill':emaill})
        email = EmailMessage(
            'Enquiry', #subject
            template, #body
            emaill, #sender mail id
            ['midhunkb57@gmail.com'] #recever mail id
        )
        email.fail_silently = False
        email.send()
        messages.success(request,'Email send succesfully')
        # print('Email Send')
        return redirect('Plant_app:index')


    new_arrivals = Products.objects.all()[:4]
    return render(request,'index.html',{'new_arrivals':new_arrivals})



def about(request):
    return render(request,'about.html')


def products(request):
    products = Products.objects.all().order_by("-id")
    context = {
        'products' : products

    }
    return render(request,'products.html',context)


def products_details(request,slug):
    details = Products.objects.filter(slug=slug)
    return render(request,'products-details.html',{'details':details})



def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        emaill = request.POST.get('email')
        # print('EMAIL',email)
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        template = render_to_string('email.html',{'name':name,'phone':mobile,'subject':subject,'message':message,'emaill':emaill})
        email = EmailMessage(
            'Enquiry', #subject
            template, #body
            emaill, #sender mail id
            ['midhunkb57@gmail.com'] #recever mail id
        )
        email.fail_silently = False
        email.send()
        messages.success(request,'Email send succesfully')
#         print('Email Send')
        return redirect('Plant_app:contact_us')
    return render(request,'contact.html')
