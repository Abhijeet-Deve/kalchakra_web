from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')



def personality_view(request):
    return render(request, 'personality.html')