from django.shortcuts import render
from django.http import  Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat no meat for the month",
    "february": "Code for 300 hours",
    "march": "Fight",
    "april": "Eat no meat for the month 1",
    "may": "Code for 300 hours 1",
    "june": "Fight 1",
    "july": "Eat no meat for the month 2",
    "august": "Code for 300 hours 2",
    "september": "Fight 2",
    "october": "Eat no meat for the month 3",
    "november": "Code for 300 hours 3",
    "december": None,
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {
            "challengeMonth": month,
            "text": challenge_text
        })        
    except:
        raise Http404()
