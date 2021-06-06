from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    ListView,
    UpdateView,
)

from education.forms import CourseForm, ContactForm
from education.models import Category, Course
from education.tasks import send_mail_task

class CategoriesList(ListView):
    model = Category
    title = 'Список курсов'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class CourseDetailView(DetailView):
    model = Course
    pk_url_kwarg = 'course_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = kwargs['object'].title
        return context


class CourseTitleMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


@method_decorator(staff_member_required, name='dispatch')
class CourseAddView(CourseTitleMixin, CreateView):
    model = Course
    form_class = CourseForm
    title = 'Добавить курс'
    success_url = reverse_lazy('categories_list')


@method_decorator(staff_member_required, name='dispatch')
class CourseUpdateView(CourseTitleMixin, UpdateView):
    model = Course
    form_class = CourseForm
    title = 'Обновить курс'
    success_url = reverse_lazy('categories_list')


@method_decorator(staff_member_required, name='dispatch')
class CourseDeleteView(CourseTitleMixin, DeleteView):
    model = Course
    title = 'Удалить курс'
    success_url = reverse_lazy('categories_list')
    template_name_suffix = '_delete'


class ContactFormView(CourseTitleMixin, FormView):
    form_class = ContactForm
    template_name = "education/contact.html"
    success_url = reverse_lazy('categories_list')
    title = 'Отправить'

    def form_valid(self, form):
        support_mail = settings.EMAIL_HOST_USER
        subject = (form.cleaned_data.get('name').strip()
                   + ' / ' + form.cleaned_data.get('subject').strip())
        sender_mail = form.cleaned_data.get('email').strip()

        send_mail_task.delay(
            subject=subject,
            message=form.cleaned_data.get('message'),
            from_mail=sender_mail,
            to_mail=support_mail,
        )
        send_mail_task.delay(
            subject="Ваше сообщение было отправлено в службу поддержки сервиса"
                    " 'Invest_blog'",
            message="Ваше сообщение было отправлено в службу поддержки сервиса"
                    " 'Invest_blog' и вскоре будет рассмотрено нашими "
                    "специалистами",
            from_mail=support_mail,
            to_mail=sender_mail,
        )
        return super(ContactFormView, self).form_valid(form)
