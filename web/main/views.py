from django.shortcuts import render


def news_page(request):
    return render(request, 'main/news_page.html')

def home_page(request):
    return render(request, 'main/home_page.html')

def about_page(request):
    return render(request, 'main/about_page.html')

def contact_page(request, test):
    context = {'test': test}
    return render(request, 'main/contact_page.html', context=context)

