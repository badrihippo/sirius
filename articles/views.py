from django.views import generic
from articles.models import Article, Series, Section, Tag
class ArticleDetail(generic.DetailView):
    model = Article
    template_name = 'articles/article.htm'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['page_icon'] = self.object.section.icon_left
        context['page_section'] = self.object.section.name
        return context
class ArticleList(generic.ListView):
    model = Article
    template_name = 'articles/article_list.htm'
