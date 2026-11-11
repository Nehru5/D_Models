from userapp.models import Student
from django.shortcuts import redirect, render

def saveStudent(request):
  if request.method == "POST":
    a = request.POST.get("a")
    b = request.POST.get("b")
    c = request.POST.get("c")
    d = request.POST.get("d")
    e = request.POST.get("e")
    
    Student.objects.create(name =a,email = b, phone = c, department = d,addrress = e)
    return redirect("student_link")
  else:
    return render(request,"index.html")
  
  
def fetchStudents(request):
  a = Student.objects.all()
  return render(request,"students.html",{"a":a})
  
  