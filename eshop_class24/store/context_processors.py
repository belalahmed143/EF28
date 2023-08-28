from .models import Category

def categories(request):
    categories = Category.objects.filter(main_category=None)

    context ={
        'categories':categories
    }
    return context