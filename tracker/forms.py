from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description', 'habit_type', 'is_active']

class LogEntryForm(forms.ModelForm):
    class Meta:
        model = LogEntry
        fields = ["date", "notes"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
