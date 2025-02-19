from django.shortcuts import render, redirect


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_key = request.GET.get('sort')
    all_phones = Phone.objects.all()
    if sort_key == 'name':
        all_phones = all_phones.order_by('name')
    elif sort_key == 'min_price':
        all_phones = all_phones.order_by('price')
    else:
        all_phones = all_phones.order_by('-price')

    context = {'phones': all_phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug)
    context = {'phone': phone[0]}
    return render(request, template, context)
