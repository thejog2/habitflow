from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Habit, LogEntry
from .forms import HabitForm, LogEntryForm
from .utils import has_logged_today, get_today_log, calculate_streak


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

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        habit = self.object

        # Get the date filter from the query string
        filter_date = self.request.GET.get("date")

        if filter_date:
            logs = habit.logs.filter(date=filter_date)
        else:
            logs = habit.logs.all()

        context["logs"] = logs
        context["filter_date"] = filter_date

        return context

    
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
    template_name = "logentry_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.habit = get_object_or_404(Habit, pk=kwargs["habit_pk"], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["habit"] = self.habit
        return kwargs

    def form_valid(self, form):
        form.instance.habit = self.habit
        messages.success(self.request, "Log entry created successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("habit_detail", kwargs={"pk": self.habit.pk})



class UpdateLogEntryView(LoginRequiredMixin, UpdateView):
    model = LogEntry
    form_class = LogEntryForm
    template_name = "logentry_form.html"

    def get_queryset(self):
        return LogEntry.objects.filter(habit__user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["habit"] = self.object.habit
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, "Log entry updated successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("habit_detail", kwargs={"pk": self.object.habit.pk})



class DeleteLogEntryView(LoginRequiredMixin, DeleteView):
    model = LogEntry
    template_name = "logentry_confirm_delete.html"

    def get_queryset(self):
        return LogEntry.objects.filter(habit__user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Log entry deleted successfully.")
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("habit_detail", kwargs={"pk": self.object.habit.pk})


@login_required
def dashboard(request):
    today = timezone.now().date()

    habits = Habit.objects.filter(user=request.user, is_active=True)

    habits_today = []
    streaks = {}

    for habit in habits:
        habits_today.append({
            "habit": habit,
            "logged_today": has_logged_today(habit),
        })

        streaks[habit] = calculate_streak(habit)

    context = {
        "today": today,
        "habits_today": habits_today,
        "streaks": streaks,
    }

    return render(request, "dashboard.html", context)
