#模板全局变量


from blog.models import Category
from arch_blog.models import Category as Arch_Category


def global_params(request):
    arch_categorys= Arch_Category.objects.all()
    categorys = Category.objects.all()

    return {
        'categorys': categorys,
        'arch_categorys': arch_categorys,
    }