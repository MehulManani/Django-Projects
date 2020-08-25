from django.shortcuts import render
from home.models import Topic, AccessRecords,WebPage
from . import forms

from home.models import Users
# Create your views here.
def index(request):
    index_context = {'index':'Welcome to the index page!'}
    return render(request,'index.html',context=index_context)

def home(request):
    home_context = {'home': "Welcome to the home page!"}
    return render(request,'home/home.html', context=home_context)
def aboutus(request):
    aboutus_context = {'aboutus': "Welcome to the about us page!"}
    return render(request,'home/aboutus.html',context=aboutus_context)
def contactus(request):
    contactus_context = {'contactus': "Welcome to the contact us page!"}
    return render(request,'home/contactus.html',context=contactus_context)
def articles(request):
    articles_context = {'articles': "Welcome to the articles page!"}
    return render(request,'home/articles.html',context=articles_context)

def displayrecords(request):
    webpages_list = AccessRecords.objects.order_by('date')
    date_dict = {'access_records' : webpages_list}
    return render(request,'home/displayrecords.html',context=date_dict)

def formdisplay(request):
    form = forms.FormName() # Create the form instance of django forms and the name of the form is
                            # taken from the views.py Here it is 'FormName'
    # This code essentially check for the POST request
    # and the validation of the data
    if request.method == 'POST':
        form = forms.FormName(request.POST) # Here this statement pass the post as a method

        if form.is_valid():
            print("Validation Success!")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])


    return render(request, 'home/formdisplay.html',{'form':form})

def register(request):
    form = forms.UserData()

    if request.method == 'POST':
        form = forms.UserData(request.POST)

        if form.is_valid():
            form.save(commit=True) # This will save the form data and commit it.
            return home(request)
        else :
            print("Error! Form Invalid!")
    return render(request,'home/registration.html',{'form':form})
