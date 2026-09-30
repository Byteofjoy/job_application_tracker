from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):

    STATUS_CHOICES = [
        ("Saved", "Saved"),
        ("Applied", "Applied"),
        ("Interview", "Interview"),
        ("Assessment", "Assessment"),
        ("Rejected", "Rejected"),
        ("Offer", "Offer"),
    ]

    JOB_TYPE_CHOICES = [
        ("Full-time", "Full-time"),
        ("Part-time", "Part-time"),
        ("Internship", "Internship"),
        ("Contract", "Contract"),
        ("Freelance", "Freelance"),
        ("Remote", "Remote"),
        ("Hybrid", "Hybrid"),
    ]

    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="applications"
)
    
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    application_date = models.DateField(null=True, blank=True)

    job_type = models.CharField(
        max_length=50,
        choices=JOB_TYPE_CHOICES,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Saved"
    )

    salary = models.CharField(max_length=100, blank=True)
    job_url = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    priority = models.CharField(
    max_length=20,
    choices=[
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ],
    default="Medium"
    )

    interview_date = models.DateField(
    null=True,
    blank=True
    )

    follow_up_date = models.DateField(
    null=True,
    blank=True
    )

    contact_person = models.CharField(
    max_length=100,
    blank=True
    )

    interview_notes = models.TextField(
    blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job_title} at {self.company}"