from django.shortcuts import render
from .models import Advertisement
from .forms import AdvertisementForm
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.

def example(request):
    advertisements = Advertisement.objects.all()
    context = {"advertisements": advertisements}
    return render(request, "index.html", context)

def top_sellers(request):
    return render(request, "top-sellers.html")

def advertisement_post(request):
    # если пришел запрос на добавление
    if request.method == "POST":
        # заполняем форму введенной ифнормацией
        form = AdvertisementForm(request.POST, request.FILES)
        # делаем проверку на правильность заполнения
        if form.is_valid():
            # создаем новый объект для добавления в БД
            advertisement = Advertisement(**form.cleaned_data)
            # т.к. пользователя не вводили в форме, то получим его из запроса
            advertisement.user = request.user
            # отсюда вывод - формы смогут заполнять только залогиненные пользователи
            # пока логина нету - может заполнять админ (входим под админкой)
            advertisement.save()
            url = reverse("main-page")
            return redirect(url)
    else:
        # при загрузке страницы создаем новую пустую форму
        form = AdvertisementForm()
        # передаем ее через контекст
    context = {'form': form}
    return render(request, "advertisement-post.html", context)