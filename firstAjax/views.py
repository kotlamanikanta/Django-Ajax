from django.http import JsonResponse
from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):
    form = StudentForm()
    stu = Student.objects.all()
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
            print("mani kanta")
            return JsonResponse({"status": "Data not saved"})
