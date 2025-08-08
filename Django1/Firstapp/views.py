from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponse
import requests

def hellofunction(request):
    name= "anathony"
    age = 20
    return HttpResponse(f"<h1>Hello, World!</h1> My Name Is {name} and I am {age} years old.")
   # return HttpResponse("<h1>Hello, World!</h1> My Name Is anathony and I am a software engineer.")

def mydictionary(request):
    context = "My Dictionary <br>"
    items = {
        'name': 'anathony',
        'age': 20,
        'location': 'New York'
    }
    for item, description in items.items():
        context += f"<li>{item} : {description}</li>"
    return HttpResponse(context)

def listfunction(request):
    items = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    html = "<h2>Fruit List</h2>"
    for item in items:
        html += f"<li>{item}</li>"
    return HttpResponse(html)

def showname(request,name):
    return HttpResponse(f"<h1>Hello, {name}!</h1>")


def sum(request, a, b):
    result = int(a) + int(b)
    return HttpResponse(f"<h1>Sum of {a} and {b} is {result}</h1>")

def getval(request):
    name = request.GET.get('name1')
    return HttpResponse(f"<h1>The name is , {name}!</h1>")
# http://127.0.0.1:8000/getval/?name1=Kundan

def add(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    try:
        a = float(a)
        b = float(b)
        return HttpResponse(f"<h1>Sum of {a} and {b} is {int(a) + int(b)}</h1>")
    except (ValueError, TypeError):
        return HttpResponse("<h1>Invalid input. Please provide valid numbers.</h1>")
    

def calculator(request):
    op = request.GET.get('op')
    a = request.GET.get('a')
    b = request.GET.get('b')
    try:
        a = float(a)
        b = float(b)
        if op == 'add':
            result = a + b
            operation = '+'
        elif op == 'sub':
            result = a - b
            operation = '-'
        elif op == 'mul':
            result = a * b
            operation = '*'
        elif op == 'div':
            if b == 0:
                return HttpResponse("<h1>Error: Division by zero!</h1>")
            result = a / b
            operation = '/'
        else:
            return HttpResponse("<h1>Invalid operation. Use op=add, sub, mul, or div.</h1>")
        return HttpResponse(f"<h1>{op} is {a} {operation} {b} = {result}</h1>")
    except (ValueError, TypeError):
        return HttpResponse("<h1>Invalid input. Please provide valid numbers for a and b.</h1>")
    

def json(request):
    data = {
        'name': 'anathony',
        'age': 20,
        'location': 'New York'
    }
    return JsonResponse(data)

def apidata(request):
    response = requests.get("https://api.cricapi.com/v1/cricScore?apikey=%APIKEY%")
    data = response.json()
    return JsonResponse(data,safe=False)
