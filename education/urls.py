from django.urls import path

from education import views

urlpatterns = [
    path('', views.CategoriesList.as_view(), name='categories_list'),
    path('mentors/', views.MentorsList.as_view(),
         name='mentors_list'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('courses/<int:course_id>/', views.CourseDetailView.as_view(),
         name='course_detail'),
    path('lessons/<int:lesson_id>/', views.LessonDetailView.as_view(),
         name='lesson_detail'),
    path('mentors/<int:mentor_id>/', views.MentorDetailView.as_view(),
         name='mentor_detail'),
    path('courses/add/', views.CourseAddView.as_view(), name='course_add'),
    path('courses/update/<int:pk>/', views.CourseUpdateView.as_view(),
         name='course_update'),
    path('courses/delete/<int:pk>/', views.CourseDeleteView.as_view(),
         name='course_delete'),
]
