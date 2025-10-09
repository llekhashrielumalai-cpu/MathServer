# Ex.05 Design a Website for Server Side Processing
## Date:09/10/2025

## AIM:
  To design a Website to calculate the body Mass Index in the server side.

## FORMULA:
BMI = W/H<sup>2</sup>
<br> BMI --> Body Mass Index
<br> W --> Weight
<br> H --> Height

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
ex5.html
<html> 
    <head> 
        <title>BMI Calculation</title> 
        <style>
            .box{
                margin-left: 40%;
                margin-top: 10%;
                background-color: rgb(180, 239, 175);
                width:fit-content;
                border: 3px solid rgb(13, 13, 13);
                padding:10px;
                text-decoration: underline;
            }
             .body{
                    background-color: rgb(35, 67, 33);
            }

        </style>
        <link rel="stylesheet" href="style.css">
    </head> 
    <body class="body">
            <div class="box"> 
                <h1>BMI CALCULATION</h1>
                <form method="POST">
                        {%csrf_token %}
                    <div> 
                            Height<input type="text" name="height" value="{{h}}">(in cm)
                    </div><br>
                    <div> 
                            Weight:<input type="text" name="weight" value="{{w}}">(in kg)
                    </div><br>
                        <div> 
                            <input type="submit" value="Calculate" class="button"><br> 
                       </div><br>
                      <div> 
                         BMI:<input type="text" name="bmi" value="{{bmi}}">
                      </div><br>
                </form>
               </div>
   </body>
</html>

views.py
from django.shortcuts import render 
def bmi(request): 
    context={} 
    context['bmi'] = "0" 
    context['h'] = "0" 
    context['w'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        h = request.POST.get('height','0')
        w = request.POST.get('weight','0')
        bmi=0
        print('request=',request) 
        print('height=',h) 
        print('weight=',w) 
        bmi = int(w)/((int(h)/100)**2)
        context['bmi'] = bmi
        context['h'] = h
        context['w'] = w
        print('bmi=',bmi) 
    return render(request,'myapp/ex5.html',context)

urls.py
from django.shortcuts import render
from django.contrib import admin 
from django.urls import path 
from myapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('bmicalculation/',views.bmi,name="bmicalculation"),
    path('',views.bmi,name="bmicalculationroot")
]
```
## SERVER SIDE PROCESSING:
![alt text](<bmi terminal.png>)

## HOMEPAGE:
![alt text](<bmi output.png>)

## RESULT:
The program for performing server side processing is completed successfully.
