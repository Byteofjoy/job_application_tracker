from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Application
from .forms import ApplicationForm


@login_required
def application_list(request):

    applications = Application.objects.filter(
        user=request.user
    )

    search = request.GET.get("search", "")
    status = request.GET.get("status", "")
    sort = request.GET.get("sort", "-application_date")

    if search:
        applications = applications.filter(
            company__icontains=search
        ) | applications.filter(
            job_title__icontains=search
        )

    if status:
        applications = applications.filter(
            status=status
        )

    allowed_sorts = [
        "application_date",
        "-application_date",
        "company",
        "-company",
        "job_title",
        "-job_title",
    ]

    if sort in allowed_sorts:
        applications = applications.order_by(sort)

    paginator = Paginator(applications, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Statistics for the logged-in user only
    user_applications = Application.objects.filter(
        user=request.user
    )

    total = user_applications.count()
    saved = user_applications.filter(status="Saved").count()
    applied = user_applications.filter(status="Applied").count()
    interview = user_applications.filter(status="Interview").count()
    assessment = user_applications.filter(status="Assessment").count()
    rejected = user_applications.filter(status="Rejected").count()
    offer = user_applications.filter(status="Offer").count()

    status_choices = Application.STATUS_CHOICES

    context = {
        "applications": page_obj,
        "page_obj": page_obj,

        "total": total,
        "saved": saved,
        "applied": applied,
        "interview": interview,
        "assessment": assessment,
        "rejected": rejected,
        "offer": offer,

        "search": search,
        "selected_status": status,
        "sort": sort,
        "status_choices": status_choices,
    }

    return render(
        request,
        "applications/application_list.html",
        context
    )


@login_required
def application_create(request):

    if request.method == "POST":
        form = ApplicationForm(request.POST)

        if form.is_valid():

            application = form.save(commit=False)

            # Automatically assign the logged-in user
            application.user = request.user

            application.save()

            return redirect("application_list")

    else:
        form = ApplicationForm()

    return render(
        request,
        "applications/application_form.html",
        {
            "form": form,
            "title": "Add Application",
        }
    )


@login_required
def application_edit(request, pk):

    application = get_object_or_404(
        Application,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        form = ApplicationForm(
            request.POST,
            instance=application
        )

        if form.is_valid():
            form.save()
            return redirect("application_list")

    else:
        form = ApplicationForm(
            instance=application
        )

    return render(
        request,
        "applications/application_form.html",
        {
            "form": form,
            "title": "Edit Application",
        }
    )


@login_required
def application_delete(request, pk):

    application = get_object_or_404(
        Application,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        application.delete()
        return redirect("application_list")

    return render(
        request,
        "applications/application_confirm_delete.html",
        {
            "application": application
        }
    )


@login_required
def application_detail(request, pk):

    application = get_object_or_404(
        Application,
        pk=pk,
        user=request.user
    )

    return render(
        request,
        "applications/application_detail.html",
        {
            "application": application
        }
    )