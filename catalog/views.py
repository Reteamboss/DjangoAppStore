from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponse


from .forms import ReviewForm
from .models import Product, Category



class ProductListView(generic.ListView):
    model = Product
    template_name = 'product_list.html'

    # def get_queryset(self):
    #     self.category = get_object_or_404(
    #         Category,
    #         slug=self.kwargs['category_slug']
    #     )
    #     return Product.objects.filter(
    #         category__slug=self.category.slug
    #     ).select_related('category')
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['category'] = self.category
    #     return context


class ShowDetail(generic.DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'





    # slug_field = 'slug'
    # slug_url_kwarg = 'product_slug'
    # context_object_name = 'product'

    # def get_context_data(self, **kwargs):
    #     context = super(ProductDetail, self).get_context_data()
    #     context['form'] = ReviewForm
    #     return context
    #
    # def post(self, request, *args, **kwargs):
    #     form = ReviewForm(request.POST, request.FILES)
    #     self.object = super(ProductDetail, self).get_object()
    #     context = super(ProductDetail, self).get_context_data()
    #     context['form'] = ReviewForm
    #     if form.is_valid():
    #         new_review = form.save(commit=False)
    #         new_review.product = self.object
    #         new_review.save()
    #
    #     else:
    #         context['form'] = form
    #
    #     return self.render_to_response(context=context)


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'index.html'
    allow_empty = False

    def get_queryset(self):
        return Category.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Категория - ' + str(context['posts'][0].cat)
    #     context['menu'] = menu
    #     context['cat_selected'] = context['posts'][0].cat_id
    #     return context


def index(request):
    return render(request, 'home.html')

