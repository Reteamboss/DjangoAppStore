from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
from django.views import generic
from catalog.models import Product




class ESearchView(generic.ListView):
    template_name = 'search_result.html'

    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('q')
        if question is not None:
            search_titles = Product.objects.filter( title__contains =  question)

            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            context['last_question'] = '?q=%s' % question

            current_page = Paginator(search_titles, 7)

            page = request.GET.get('page')
            try:
                context['search_list'] = current_page.page(page)
            except PageNotAnInteger:
                context['search_list'] = current_page.page(1)
            except EmptyPage:
                context['search_list'] = current_page.page(current_page.num_pages)
            context['question']=question

        return render(request,template_name = self.template_name, context = context)
