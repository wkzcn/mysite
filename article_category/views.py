from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from article.models import Article
from article_category.models import ArticleCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

from article_category.forms import CategoryForm
per_page = getattr(settings, 'PER_PAGE')


@login_required
def manage_category(request):
    category_form = CategoryForm()
    return render(request, 'category/category_backend.html',
                  {'form': category_form})


def get_all_articles_by_category(request, category_id):
    """Get all articles by category
    :param
        @request: receive request from client
        @category_id: receive captured string from url
    :return: a response object with categorized articles
    """
    category = ArticleCategory.objects.get(pk=category_id)
    articles_list = Article.objects.order_by('-created_time').filter(
        category_id=category_id)
    paginator = Paginator(articles_list, per_page=per_page)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request,
                  'category/article_categorized.html',
                  {"category": category, "articles": articles})


def get_all_category(request):
    category_lists = ArticleCategory.objects.all()
    return render(request, 'category/all_categories.html',
                  {'category_lists': category_lists})


@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # print(form.is_valid(), request.POST.get('name', 'blank'))
        if request.user.is_superuser and form.is_valid():
            name = request.POST.get('name')
            try:
                category = ArticleCategory(name=name)
                category.save()
            except Exception:
                error_message = "Can not add %s category" % repr(name)
                category_form = CategoryForm()
                return render(request, 'category/category_backend.html',
                              {'form': category_form,
                               'error_msg': error_message})
            finally:
                return HttpResponseRedirect(reverse('category:manage'))
        else:
            return render(request, 'category/category_backend.html',
                          {'form': form})


@login_required
def delete_category(request, category_id):
    if request.method == 'POST':
        if request.user.is_superuser:
            ArticleCategory.objects.get(pk=category_id).delete()
        return HttpResponseRedirect(reverse('category:manage'))
    message = 'Can not be deleted.'
    category = ArticleCategory.objects.get(pk=category_id)
    return render(request, 'category/delete_confirm.html',
                  {'category': category, 'message': message})
