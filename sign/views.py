from django.shortcuts import render

from sign.forms import SignatureForm


def sign(request):
    if request.method == "GET":
        return render(request, "sign.html")
    elif request.method == "POST":
        form = SignatureForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, "message.html",
                          {"message": "There was a critical error executing your request. The form was not valid."})
