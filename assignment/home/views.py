from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from home.form import UserRegisterationForm,MessagingForm
from django.http import HttpResponseRedirect
from .models import User,Message
from django.contrib import messages

# Create your views here.
def base(request):
    return render(request,'base.html')

def home(request):
    userRegForm=UserRegisterationForm()
    context={
        'form':userRegForm
    }
    return render(request,'home.html',context)

def message(request):
    messageForm=MessagingForm()
    data=User.objects.all()
    context={
        'form':messageForm,
        'data':data
    }
    return render(request,'message.html',context)

def saveUser(request):
    if request.method=='POST':
        form=UserRegisterationForm(request.POST)
        if form.is_valid:
            print("pass")
            form.save()
            messages.add_message(request, messages.SUCCESS,"User added successfully",fail_silently=True,)
    return HttpResponseRedirect("/")


def saveMessage(request):
    if request.method=='POST':
        form=MessagingForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.receiverName = request.POST.get('receiverName')
            message.save()
            messages.add_message(request, messages.SUCCESS,"Mesage added successfully",fail_silently=True,) 
    else:
        print("sssaa")
    return HttpResponseRedirect("message")

def get_receivers(request):
    age_bracket = request.GET.get('ageBracket')
    receiver_names = []
    if age_bracket:
        users = User.objects.filter(ageBracket=age_bracket)
        receiver_names = [{'id': user.id, 'username': user.userName} for user in users]

    return JsonResponse({'receivers': receiver_names})

def chart(request):
    Messages=Message.objects.all()
    textByMe=Messages.filter(senderName="Usama Anwer").count()
    textToMe=Messages.filter(receiverName="Usama Anwer").count()
    zeroToTen=Messages.filter(ageBracket="age1").count()
    elevenToTwenty=Messages.filter(ageBracket="age2").count()
    twentyOneToThirty=Messages.filter(ageBracket="age3").count()
    thirtyOneToForty=Messages.filter(ageBracket="age4").count()
    context={
        'textByMe':textByMe,
        'textToMe':textToMe,
        'zeroToTen':zeroToTen,
        'elevenToTwenty':elevenToTwenty,
        'twentyOneToThirty':twentyOneToThirty,
        'thirtyOneToForty':thirtyOneToForty,
    }
    print(context)
    return render(request,'chart.html',context)