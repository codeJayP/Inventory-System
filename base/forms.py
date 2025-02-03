from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import UserProfile, Equipment

class RegForm(UserCreationForm):
    OFFICE_CHOICES = [
        ('hr', 'Human Resources'),
        ('it', 'Information Technology'),
        ('sales', 'Sales'),
        ('finance', 'Finance'),
    ]

    office = forms.ChoiceField(choices=OFFICE_CHOICES, required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'office', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        registered_offices = UserProfile.objects.values_list('office', flat=True)
        available_offices = [choice for choice in self.OFFICE_CHOICES if choice[0] not in registered_offices]
        self.fields['office'].choices = available_offices

        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Username'})
        self.fields['first_name'].widget.attrs.update({'class':'form-control', 'placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control', 'placeholder':'Last Name'})
        self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Re-type Password'})
        self.fields['office'].widget.attrs.update({'class':'form-select'})

    def clean_office(self):
        office_name = self.cleaned_data.get('office')
        if UserProfile.objects.filter(office=office_name).exists():
            raise forms.ValidationError('This office already exist')
        return office_name
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        office_name = self.cleaned_data.get('office')
        UserProfile.objects.create(user=user, office=office_name)
        employee_group, created = Group.objects.get_or_create(name='Employee')
        user.groups.add(employee_group)

        return user
    
class ItemForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['property_num', 'article_item', 'description', 'person_accountable', 'cost', 'remarks']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['property_num'].widget.attrs.update({'class':'form-control', 'placeholder': 'Property NUmber'})
        self.fields['article_item'].widget.attrs.update({'class':'form-control', 'placeholder': 'Article Item'})
        self.fields['description'].widget.attrs.update({'class':'form-control', 'placeholder': 'Description'})
        self.fields['person_accountable'].widget.attrs.update({'class':'form-control', 'placeholder': 'Person Accountable'})
        self.fields['cost'].widget.attrs.update({'class':'form-control', 'placeholder': 'Cost'})
        self.fields['remarks'].widget.attrs.update({'class':'form-control', 'placeholder': 'Remarks'})