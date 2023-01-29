from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.filters import StudentFilter
from student.forms import StudentForm, StudentUpdateForm
from student.models import Student


class StudentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('homepage')


class StudentListView(LoginRequiredMixin,ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'

    def get_queryset(self):
        return Student.objects.filter( active=True)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # all_trainers = Trainer.objects.all()
        # data['trainers'] = all_trainers

        students = Student.objects.filter(active=True)
        filters = StudentFilter(self.request.GET, queryset=students)
        students = filters.qs

        data['all_students'] = students
        data['my_filters'] = filters

        return data
class StudentUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('list-of-students')


class StudentDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-of-students')


class StudentDetailView(LoginRequiredMixin,DetailView):
    template_name = 'student/details_of_student.html'
    model = Student



def inactivate_student(request, pk):
    Student.objects.filter(id=pk).update(active=False)
    return redirect('list-of-students')

