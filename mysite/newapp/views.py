from django.contrib.auth import login # 追加
from django.contrib.auth.forms import UserCreationForm # 追加
from django.shortcuts import render, redirect # redirectをインポート
from django.contrib.auth.decorators import login_required # 追加


def index(request):
    return render(request, "newapp/index.html")

@login_required
def home(request):
    return render(request, "newapp/home.html")


# ここから追加
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("newapp:home")
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'newapp/signup.html', context)
# ここまで追加