from django.shortcuts import render


def tag_home(request):
    print(request.session.get('tag_id'))

    return render(request, "carts/home.html", {})
