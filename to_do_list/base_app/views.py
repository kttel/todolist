from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import TaskForm
from .models import Task
from .utils import DataMixin


class UserRegisterView(DataMixin, FormView):
    template_name = 'base_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_data = self.get_user_context(title='Register')
        return dict(list(context.items()) + list(new_data.items()))

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(UserRegisterView, self).get(*args, **kwargs)


class UserLoginView(DataMixin, LoginView):
    template_name = 'base_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_data = self.get_user_context(title='Login')
        return dict(list(context.items()) + list(new_data.items()))

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(DataMixin, LoginRequiredMixin, ListView):
    model = Task
    template_name = 'base_app/task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        new_data = self.get_user_context(title='To Do List', count=context['tasks'].filter(done=False).count())
        search_data = self.request.GET.get('search-field') or ''
        if search_data:
            context['tasks'] = context['tasks'].filter(title__icontains=search_data)
        context['search_data'] = search_data
        return dict(list(context.items()) + list(new_data.items()))


class TaskDetail(DataMixin, LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'base_app/task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_data = self.get_user_context(title=context['task'])
        return dict(list(context.items()) + list(new_data.items()))


class TaskCreate(DataMixin, LoginRequiredMixin, CreateView):
    form_class = TaskForm
    template_name = 'base_app/task_form.html'
    success_url = reverse_lazy('tasks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_data = self.get_user_context(title='Create task')
        return dict(list(context.items()) + list(new_data.items()))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(DataMixin, LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'base_app/task_form.html'
    success_url = reverse_lazy('tasks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_data = self.get_user_context(title="Task editing")
        return dict(list(context.items()) + list(new_data.items()))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskUpdate, self).form_valid(form)


class TaskDelete(DataMixin, LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'base_app/task_delete.html'
    success_url = reverse_lazy('tasks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_data = self.get_user_context(title="Task delete")
        return dict(list(context.items()) + list(new_data.items()))