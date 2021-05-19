from django.contrib.auth import get_user_model
from django.db import models
from tinymce.models import HTMLField


class Author(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.PROTECT,
        null=False,
        verbose_name="Пользователь",
    )

    status = models.CharField(
        max_length=200,
        null=False,
        default="",
        blank=True,
        verbose_name="Статус",
    )

    bio = models.TextField(
        null=False,
        default="",
        blank=True,
        verbose_name="Биография",
    )

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return f"{self.__class__.__name__} <{self.user}>"


class Category(models.Model):
    title = models.CharField(
        max_length=150,
        null=False,
        default="",
        blank=False,
        verbose_name="Название",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_articles(self):
        return Article.objects.filter(category=self)

    def __str__(self):
        return f"{self.__class__.__name__} <{self.title}>"


class Article(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        verbose_name="Автор",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория",
        related_name="articles",
    )
    tags = models.ManyToManyField(
        "Tag",
        verbose_name="Тэг",
        related_name="articles",
    )

    title = models.CharField(
        max_length=150,
        null=False,
        default="",
        blank=False,
        verbose_name="Заголовок",
    )
    text = HTMLField(
        null=False,
        default="",
        blank=True,
        verbose_name="Текст статьи",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    published_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата публикации",
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return f"{self.__class__.__name__} <{self.title}> by {self.author}"


class TagQuerySet(models.QuerySet):
    def popular(self):
        return self.annotate(
            articles_count=models.Count('articles')
        ).order_by('-articles_count')


class Tag(models.Model):
    title = models.CharField(
        max_length=150,
        null=False,
        default="",
        blank=False,
        verbose_name="Название",
    )

    objects = TagQuerySet.as_manager()

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return f"{self.__class__.__name__} <{self.title}>"