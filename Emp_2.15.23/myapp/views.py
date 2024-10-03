from django .http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    isActive = True
    if request.method == 'POST':
        check = request.POST.get("check")
        print(check)
        if check is not None: isActive=False
        else: isActive=True
        
    date = datetime.datetime.now()
    name = "Devang Parmar"
    list_of_programs = [
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime number from 1 to 100'
    ]
    
    student={
        'student_name':"Rahul",
        'student_college':"Jg University" ,
        'student_city' : "Botad",
    }
    
    # print("Test Function is called from view")
    # return HttpResponse("<h1>Hello This is index page</h1>" + str(date))
    
    data = {
        'date' : date,
        'isActive' : isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    return render(request,'home.html',data)

def about(request):
    # return HttpResponse("<h1>This is About Page</h1>")
    return render(request,'about.html',{})

def services(request):
    # return HttpResponse("<h1>This is Services Page</h1>")
    return render(request,'services.html',{})