from django.views import generic
from articles.models import Article, Series, Section, Tag
class ArticleDetail(generic.DetailView):
    model = Article
    template_name = 'articles/article.htm'
class ArticleList(generic.ListView):
    model = Article
    template_name = 'articles/article_list.htm'
