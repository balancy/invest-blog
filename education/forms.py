from django import forms

from education.models import Course


class FormPrettifyFieldsMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, obj in self.fields.items():
            obj.widget.attrs['class'] = f'form-control mt-3 form-{name}'


class CourseForm(FormPrettifyFieldsMixin, forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class ContactForm(FormPrettifyFieldsMixin, forms.Form):
    name = forms.CharField(required=True, label='ФИО')
    email = forms.EmailField(required=True, label='Электронная почта')
    subject = forms.CharField(required=True, label='Тема письма')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')

