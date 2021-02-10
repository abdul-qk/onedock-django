from django.shortcuts import render, redirect, get_object_or_404
from employee.forms import EmployeeForm, CategoryForm
from employee.models import Employee, Category, Dash_Cateogry
import datetime

# Create your views here.


# def emp(request):
#     if request.method == "POST":
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/show')
#             except:
#                 pass
#     else:
#         form = EmployeeForm()
#     return render(request, 'index.html', {'form': form})


# def show(request):
#     employees = Employee.objects.all()
#     return render(request, "show.html", {'employees': employees})


# def edit(request, id):
#     employee = Employee.objects.get(id=id)
#     return render(request, 'edit.html', {'employee': employee})


# def update(request, id):
#     employee = Employee.objects.get(id=id)
#     form = EmployeeForm(request.POST, instance=employee)
#     if form.is_valid():
#         form.save()
#         return redirect("/show")
#     return render(request, 'edit.html', {'employee': employee})


# def destroy(request, id):
#     employee = Employee.objects.get(id=id)
#     employee.delete()
#     return redirect("/show")


# Category Function
def emp(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = CategoryForm()
    print(form)
    return render(request, 'index.html', {'form': form})


def show(request):
    cats_1 = Dash_Cateogry.objects.filter(
        category_level=0,
        business_profile_id=1
    )
    cats_2 = Dash_Cateogry.objects.filter(
        category_level=1,
        business_profile_id=1
    )
    cats_3 = Dash_Cateogry.objects.filter(
        category_level=2,
        business_profile_id=1
    )
    form = CategoryForm()
    return render(request, "show.html", {
        'cats_1': cats_1,
        'cats_2': cats_2,
        'cats_3': cats_3,
        'form': form
    })

def dash(request):
    
    from_date = datetime.datetime.now() - datetime.timedelta(days=30)
    to_date = datetime.datetime.now()
    return render(request, "overview.html", {
        'from_date': from_date,
        'to_date': to_date
    })


def edit(request, id):
    cats = Dash_Cateogry.objects.get(category_id=id)
    return render(request, 'edit.html', {'cats': cats})


def update(request, id):
    cats = Dash_Cateogry.objects.get(category_id=id)
    form = CategoryForm(request.POST, instance=cats)
    print (form)
    if form.is_valid():
        form.save()
        return redirect("/show")
    print(form.errors)
    return render(request, 'edit.html', {'cats': cats})


# def update(request, id):
#     cats = get_object_or_404(cats, category_id=id)
#     if request.POST:
#         form = CategoryForm(instance=cats, data=request.POST)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect('/show')
#     else:
#         form = CategoryForm(instance=cats)
#     print(form.errors)
#     return render_to_response('edit.html', {'cats': cats})


def destroy(request, id):
    cats = Dash_Cateogry.objects.get(category_id=id)
    cats.delete()
    return redirect("/show")
