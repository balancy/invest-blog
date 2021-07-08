from django import forms

from education.models import Category, Course, Mentor


class FormPrettifyFieldsMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, obj in self.fields.items():
            obj.widget.attrs['class'] = f'form-control mt-3 form-{name}'


class CourseForm(FormPrettifyFieldsMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = [
            (
                category.id,
                category.title,
            ) for category in Category.objects.all()
        ]
        self.fields['responsible'].choices = [
            (
                mentor.id, mentor.user.username,
            ) for mentor in Mentor.objects.select_related('user')
        ]

    class Meta:
        model = Course
        fields = '__all__'


class ContactForm(FormPrettifyFieldsMixin, forms.Form):
    name = forms.CharField(required=True, label='ФИО')
    email = forms.EmailField(required=True, label='Электронная почта')
    subject = forms.CharField(required=True, label='Тема письма')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')

