#模板全局变量


# # from blog.models import Category
from arch_blog.models import Category as Arch_Category  # 导入需要的全局变量
from code_blog.models import Category as Code_Category
#
#
def global_params(request):
    arch_categorys= Arch_Category.objects.all()
    code_categorys= Code_Category.objects.all()
    # categorys = Category.objects.all()

    return {
        # 'nav_categorys': categorys,
        'nav_arch_categorys': arch_categorys,  # 生成全局变量的字典
        'nav_code_categorys': code_categorys,
    }