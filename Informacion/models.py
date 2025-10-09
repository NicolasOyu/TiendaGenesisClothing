from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()

class Categoria(models.Model):
    titulo = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=100, unique=True, help_text="Usado en la URL")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['titulo']


    def __str__(self):
        return self.titulo


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)




class Post(models.Model):
    titulo = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, help_text="Usado en la URL")
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='informacion', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    categorias = models.ManyToManyField('Categoria', blank=True, related_name='posts')
    publicado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'publicación'
        verbose_name_plural = 'publicaciones'
        ordering = ['-created']


    def __str__(self):
        return self.titulo


    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.titulo)
            slug = base
            i = 1
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f"{base}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)
