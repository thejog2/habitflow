from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Habit
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import HabitForm
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created and you are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
        
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


class HabitListView(LoginRequiredMixin, ListView):
    model = Habit
    template_name = "habit_list.html"
    context_object_name = "habits"

    def get_queryset(self):
        # Only show habits belonging to the logged-in user
        return Habit.objects.filter(user=self.request.user, is_active=True)
    

class HabitCreateView(LoginRequiredMixin, CreateView):
    model = Habit
    form_class = HabitForm
    template_name = "habit_form.html"
    success_url = reverse_lazy("habit_list")

    def form_valid(self, form):
        # Assign the habit to the logged-in user
        habit = form.save(commit=False)
        habit.user = self.request.user
        habit.save()
        messages.success(self.request, "Habit created successfully!")
        return redirect(self.success_url)
    

class HabitDetailView(LoginRequiredMixin, DetailView):
    model = Habit
    template_name = "habit_detail.html"
    context_object_name = "habit"

    def get_queryset(self):
        # Prevent users from accessing habits that aren't theirs
        return Habit.objects.filter(user=self.request.user)
    

class HabitUpdateView(LoginRequiredMixin, UpdateView):
    model = Habit
    form_class = HabitForm
    template_name = "habit_form.html"
    success_url = reverse_lazy("habit_list")

    def get_queryset(self):
        # Only allow editing of the user's own habits
        return Habit.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Habit updated successfully!")
        return super().form_valid(form)
    

class HabitDeleteView(LoginRequiredMixin, DeleteView):
    model = Habit
    template_name = "habit_confirm_delete.html"
    success_url = reverse_lazy("habit_list")

    def get_queryset(self):
        # Only allow deleting the user's own habits
        return Habit.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Habit deleted successfully!")
        return super().delete(request, *args, **kwargs)
    

class CreateLogEntryView(LoginRequiredMixin, CreateView):
    model = LogEntry
    form_class = LogEntryForm
    template_name = "tracker/logentry_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.habit = get_object_or_404(Habit, pk=kwargs["habit_pk"], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.habit = self.habit
        messages.success(self.request, "Log entry created successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("habit_detail", kwargs={"pk": self.habit.pk})


class UpdateLogEntryView(LoginRequiredMixin, UpdateView):
    model = LogEntry
    form_class = LogEntryForm
    template_name = "tracker/logentry_form.html"

    def get_queryset(self):
        return LogEntry.objects.filter(habit__user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Log entry updated successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("habit_detail", kwargs={"pk": self.object.habit.pk})


class DeleteLogEntryView(LoginRequiredMixin, DeleteView):
    model = LogEntry
    template_name = "tracker/logentry_confirm_delete.html"

    def get_queryset(self):
        return LogEntry.objects.filter(habit__user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Log entry deleted successfully.")
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("habit_detail", kwargs={"pk": self.object.habit.pk})
