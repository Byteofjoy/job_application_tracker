from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application

        fields = [
            "company",
            "job_title",
            "location",
            "job_type",
            "application_date",
            "status",
            "priority",
            "salary",
            "job_url",
            "contact_person",
            "follow_up_date",
            "interview_date",
            "notes",
            "interview_notes",
        ]

        widgets = {

            "company": forms.TextInput(attrs={
                "placeholder": "e.g. Safaricom",
                "class": "form-control",
            }),

            "job_title": forms.TextInput(attrs={
                "placeholder": "e.g. Software Developer",
                "class": "form-control",
            }),

            "location": forms.TextInput(attrs={
                "placeholder": "e.g. Nairobi, Kenya",
                "class": "form-control",
            }),

            "job_type": forms.Select(
                choices=Application.JOB_TYPE_CHOICES,
                attrs={
                    "class": "form-control",
                }
            ),

            "application_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),

            "priority": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),

            "salary": forms.TextInput(attrs={
                "placeholder": "e.g. KSh 60,000 - 80,000",
                "class": "form-control",
            }),

            "job_url": forms.URLInput(attrs={
                "placeholder": "https://example.com/job",
                "class": "form-control",
            }),

            "contact_person": forms.TextInput(attrs={
                "placeholder": "e.g. Jane Doe",
                "class": "form-control",
            }),

            "follow_up_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),

            "interview_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),

            "notes": forms.Textarea(attrs={
                "placeholder": "Add notes about the application...",
                "class": "form-control",
                "rows": 5,
            }),

            "interview_notes": forms.Textarea(attrs={
                "placeholder": "Add notes about the interview...",
                "class": "form-control",
                "rows": 5,
            }),
        }