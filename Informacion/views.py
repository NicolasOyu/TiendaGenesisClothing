from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Post, Categoria

def informacion(request):

    return render(request, "informacion/informacion.html")

class PostListView(ListView):
    template_name = 'informacion/lista.html'
    context_object_name = 'posts'
    paginate_by = 9
    def get_queryset(self):
        return Post.objects.filter(publicado=True).select_related('autor').prefetch_related('categorias')
    def get_context_data(self, **kw):
        ctx = super().get_context_data(**kw); ctx['categorias']=Categoria.objects.all(); ctx['categoria_activa']=None; return ctx

class PostByCategoryView(PostListView):
    def get_queryset(self):
        self.categoria = get_object_or_404(Categoria, slug=self.kwargs['slug'])
        return Post.objects.filter(publicado=True, categorias=self.categoria).select_related('autor').prefetch_related('categorias')
    def get_context_data(self, **kw):
        ctx = super().get_context_data(**kw); ctx['categoria_activa']=self.categoria; return ctx

class PostDetailView(DetailView):
    model = Post; template_name = 'informacion/detalle.html'
    context_object_name = 'post'; slug_field='slug'; slug_url_kwarg='slug'
    def get_queryset(self):
        return Post.objects.filter(publicado=True).select_related('autor').prefetch_related('categorias')


