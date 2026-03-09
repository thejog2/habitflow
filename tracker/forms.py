from django import forms
from .models import Habit, LogEntry
from django.utils import timezone

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

    def __init__(self, *args, **kwargs):
        # We pass the habit into the form from the view
        self.habit = kwargs.pop("habit", None)
        super().__init__(*args, **kwargs)

    def clean_date(self):
        date = self.cleaned_data["date"]

        # Rule 1: No future dates
        if date > timezone.now().date():
            raise forms.ValidationError("You cannot log a future date.")

        # Rule 2: No duplicate logs for the same habit/date
        if LogEntry.objects.filter(habit=self.habit, date=date).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("A log entry for this date already exists.")

        return date
