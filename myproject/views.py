from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserForm
from service.models import service 
from news.models import News
from django.core.paginator import Paginator


def homepage(request):
#    serviceData=service.objects.all().order_by('first_name')
#    newsData=News.objects.all()
#    data = {'serviceData':serviceData, 'newsData':newsData}
   data = {
       "title": "Hamra website",
       "Name" : "Rashmi",
       "Clist" : ['DSA', 'Prob',"AI"],
       "numbers" : [10,78,95],
       "Details" : [{'name' : 'Shivam' , 'city' :'Patna'},
                  {'name' : 'Rashmi' , 'city' :'Nawada'}]

   }
   return render(request, "index.html", data)

def aboutus(request):
    return HttpResponse("<b> Hii Django <b>")

def coursedetails(request, courseid):
    return HttpResponse(courseid)

def submitform(request):
    return HttpResponse(request)

def calculator(request):
        c = ''
        try:
            if request.method=="POST":
                First_No = eval(request.POST.get('num1'))
                Second_no = eval(request.POST.get('num2'))
                opr = request.POST.get('opr')
                if opr == "+":
                    c = First_No+ Second_no
                elif opr == "-":
                    c = First_No- Second_no
                elif opr == "*":
                    c = First_No*Second_no
                elif opr == "/":
                    c = First_No / Second_no
            

        except:
                c = "Invalid opr..."
        print(c)
        return render(request, "calculator.html",{'c': c})
    
def SaveEvenODD(request):
    c = ""
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render(request, "Even_Odd.html",{'error':True})
        Input_No = eval(request.POST.get('num1'))
        if Input_No % 2 == 0:
            c = "Even_Number"
        else:
            c = "ODD_NUmber"
                     
    return render(request, "Even_Odd.html",{"c":c})

def marksheet(request):
    if request.method=="POST":
        s1 = eval(request.POST.get('mark1'))
        s2 = eval(request.POST.get('mark2'))
        s3 = eval(request.POST.get('mark3'))
        s4 = eval(request.POST.get('mark4'))
        s5 = eval(request.POST.get('mark5'))
        t = s1 + s2 + s3 + s4 +s5
        p = t*100/(500)
        if p>=60:
            d = "First Div"
        elif p>=48:
            d = "Second Div"
        if p>=35:
            d = "Third Div"
        else:
            d = "Fail"
        data = {
             'total': t, 'per' : p, 'div': d}
        return render(request, "marksheet.html", data)
    return render(request, "marksheet.html") 
     

def userForm(request):
    finalans = 0
    fn = UserForm()
    data = {}
    # data = {'form': fn}
    
    try:
        if request.method=="POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1+n2
            data = {'n1':n1, 'n2':n2, 'output':finalans}
            # data = {'form':fn, 'output':finalans}
            url = "/about-us/?output={}".format(finalans)
        return HttpResponseRedirect(url)
        # return redirect(url)
    except:
        pass
    return render(request, "userform.html",data)


def newsDetails(request, newsid):
    return render(request, "newsDetails.html")


    