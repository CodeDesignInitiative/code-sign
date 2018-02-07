from django.http import JsonResponse
from django.shortcuts import render

from sign.forms import SignatureForm


def sign(request):
    if request.method == "GET":
        return render(request, "sign.html")
    elif request.method == "POST":
        form = SignatureForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Your signature was successfully saved. Thank you!"})
        else:
            return JsonResponse({
                "message": "There was a critical error executing your request. The form was not valid.",
                "error": form.errors})
