from django import forms
from employee.models import Employee, Category, Dash_Cateogry
from .widgets import BootstrapDateTimePickerInput


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Dash_Cateogry
        fields = ['category_name', 'category_id', 'category_level']


class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=BootstrapDateTimePickerInput()
    )
