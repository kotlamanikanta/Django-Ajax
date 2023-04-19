from django.http import JsonResponse
from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import json
import re

# Create your views here.


@csrf_exempt
def home(request):
    form = StudentForm()
    stu = Student.objects.all()
    # html_string = loader.render_to_string("usersdata.html", {"stu": stu})
    # print(html_string)
    context = {"form": form, "stu": stu}
    return render(request, "home.html", context)


@csrf_exempt
def data(request):
    if request.method == "POST":
        # print(request.body, "mani")
        form = StudentForm(request.POST)
        # print("kanta")
        # print(request.POST["name"])
        # print(request.POST["email"])
        # print(request.POST["course"])
        # print(form.is_valid())
        if form.is_valid():
            # print("kanta")
            # print(request.POST["name"])
            # print(request.POST["email"])
            # print(request.POST["course"])
            name = request.POST["name"]
            email = request.POST["email"]
            course = request.POST["course"]

            s = Student(name=name, email=email, course=course)
            s.save()

            stu = Student.objects.values()
            student_data = list(stu)

            return JsonResponse({"status": "Data Saved", "student_data": student_data})
        else:
            return JsonResponse({"status": "Data not saved"})


def get_ajax(request):
    # form = StudentForm()
    stu = Student.objects.all()
    # print(stu)
    # context = {"form": form, "stu": stu}
    get_data = list(stu)
    # print(get_data)
    html_string = loader.render_to_string("usersdata.html", {"get_data": get_data})
    # print(html_string)
    return JsonResponse({"html_string": html_string})


def fun_change(request):
    print("fun")
    if request.method == "POST":
        print("mani")
        name = request.POST["name"]
        email = request.POST["email"]
        mail = email
        special_chars = re.findall("[^a-zA-Z0-9_]+", mail)
        print(special_chars)
        # string = email
        # c1 = 0
        # c2 = 0
        # for i in string:
        #     if i.isdigit():
        #         c1 = c2 + 1
        #     print(c1)
        #     print(c2)

        course = request.POST["course"]

        if name or email or course:
            print("kotla")
            # sdata = {"name": name, "email": email, "course": course}
            namedata = {
                "name": name,
                "firstletter": name[0],
                "lastletter": name[-1],
                "alph": len(name),
                "email": email,
                "emaillen": len(email),
                "special": (special_chars),
                "course": course,
            }

            # context = {"sdata": sdata, "first_char": first_char, "last": last, "al": al}
            # return render(request, "home.html", context)
            # li = str(json.dumps(sdata))
            # print(type(li))
            # return JsonResponse({"li": li})
            return JsonResponse(namedata)

        else:
            print("error")
            return JsonResponse({"error": "no data"})
    else:
        print("lst error")
        return JsonResponse({"error": "Invalid"})
