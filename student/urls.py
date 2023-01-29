from django.urls import path

from student import views

urlpatterns = [
    path('create_student/', views.StudentCreateView.as_view(), name='create-student'),
    path('list_of_students/', views.StudentListView.as_view(), name='list-of-students'),
    path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name='update-student'),
    path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name='delete-student'),
    path('details_of_student/<int:pk>/', views.StudentDetailView.as_view(), name='details-of-student'),
    path('inactive_student/<int:pk>/', views.inactivate_student, name='inactive-student'),
]