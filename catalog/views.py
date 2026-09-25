from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Отображаем сообщение об успешной отправке данных
        return HttpResponse(f"Спасибо, {name}! Ваши данные успешно отправлены.")
    return render(request, 'contacts.html')


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

