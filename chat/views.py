from genericpath import samestat
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chat.models import Message , chatusers, MessageChat
from chat.forms import SignUpForm
from chat.serializers import CreateSerializer, MessageSerializer, UserSerializer
from ChatApp.settings import ChatMode
from .functions.function import handle_uploaded_file

from .chat import responce, train

f = open('C:/Users/mishr/Desktop/project/Dataset.csv', 'r', encoding='utf-8')
print(f)

traindata=train(f)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def home(request):
    context={}
    try:
        getchatuser=chatusers.objects.filter(ip=str(get_client_ip(request)))
        if  not getchatuser.exists():
            print('jdsflkdslkfjsdjfldskfjlsd')
            getchatuser=chatusers.objects.create(ip=str(get_client_ip(request)))
        context={'ip':get_client_ip(request),'sender':getchatuser[0].id,"ChatMode":ChatMode}
    except:
        return redirect('home')
    # print(type(context['ip']))
    return render(request, 'chat/userchat.html', context)


@csrf_exempt
def response(request):
    global traindata
    if request.method=="POST":
        data = JSONParser().parse(request)
        print('this is data', end='->')
        # print(request.POST)
        print(data['message'])
        k=chatusers.objects.filter(ip=data['sender'])[0].id
        data['sender']=k
        # print(data)
        serializer = CreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("this is chatbot status-->" , end="")
            print(ChatMode)
            if ChatMode:
                print("flkdjfls")
                r=responce(traindata,data['message'])
                print(r)
                print("this is msg form bot:"+str(r))
                serializer1 = CreateSerializer(data={'message':str(r),"receiver":k,"sender":22})
                if serializer1.is_valid():
                    print("this is gotta be true")
                    serializer1.save()
            else:
                pass
            return JsonResponse(serializer.data, status=201)
       
        return JsonResponse({'answer':"hwllo"} , safe=False)


def createHistory(request):
    data = request.POST["messageText"]
    print("sdjfj")
    serializer = MessageSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)



def chat_viewMY(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, 'chat/chat1.html',
                      {'users': chatusers.objects.all()})



def AdLogin(request):
    context={}
    if request.user.is_authenticated:

        return render(request, 'chat/adminDashboard.html', context)

    if request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            context['msg']="wrong credintial"
        
    return render(request, 'chat/login.html', context)


def index(request):
    context={}
    if not request.user.is_authenticated:
        return redirect("adminlogin")

    global ChatMode

    if request.method=="POST":
        bmode=request.POST
        print(bmode)
        for i in bmode:
            if i=='manual':
                ChatMode=False
            if i=='bot':
                ChatMode=True
    context={"mode":ChatMode}
    print(context)
    print(ChatMode)

        
    return render(request, 'chat/adminDashboard.html', context)





@csrf_exempt
def message_list1(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    # print("your got hear")
    if request.method == 'GET':
        messages = MessageChat.objects.filter(sender=sender, receiver=receiver, is_read=False)
        serializer = CreateSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        # serializer = MessageSerializer(data=data)
        serializer = CreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else: print("data is not valid")
            # return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)
        print("this is post requests")
        return JsonResponse({'answer':"hwllo"} , safe=False)
        


def register_view(request):
    """
    Render registration template
    """
    if request.method == 'POST':
        print("working1")
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('chats')
    else:
        print("working2")
        form = SignUpForm()
    template = 'chat/register.html'
    context = {'form':form}
    return render(request, template, context)




def message_view1(request, reciver):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, "chat/messages1.html",
                      {'users': chatusers.objects.all(),
                       'receiver': chatusers.objects.get(id=reciver),
                       'messages': MessageChat.objects.filter(sender=22, receiver=reciver) |
                                   MessageChat.objects.filter(sender=reciver, receiver=22)})


def trianBot(request):
    global traindata
    

    context={}
    if request.method=="POST":
        print("fsjfjsl")
        print(request.FILES)
        k=request.FILES['docfile']
        print(k)
        handle_uploaded_file(k)
        try:
            f = open('upload/'+ k.name, 'r', encoding='utf-8')
            traindata=train(f)
        except:
            context['err']="Something Went Wrong/maybe file is not csv or formate is wrong"
        print(traindata)
        context['file']="File Successfully Uploaded"
        print("request is post")
        print(context)
    return render(request, 'chat/trainbot.html',context)


def testPrint():
    print(testVAr)

def test(a):
    global testVAr
    testVAr=a
    print("this test is runnig")