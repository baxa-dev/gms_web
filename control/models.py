from django.db import models


# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    category = models.CharField(verbose_name="Категория", max_length=64, unique=True)
    slug = models.SlugField(verbose_name="Английское название", unique=True)

    def get_absolute_url(self):
        return f"/categories/{self.slug}/"

    # def save(self, *args, **kwargs):
    #     if not self.id and not self.slug:
    #         self.slug = slugify(self.category) + ".html"
    #     else:
    #         if not self.id:
    #             self.slug = slugify(self.slug) + ".html"
    #         else:
    #             self.slug = slugify(self.slug.rstrip('.html')) + ".html"
    #     super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.category} = {self.slug}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(models.Model):
    # category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    category_slug = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE,
                                      related_name='category_slug')
    sub_category = models.CharField(verbose_name="Подкатегория", max_length=64, unique=True)
    slug = models.SlugField(verbose_name="Английское название", unique=True)

    def get_absolute_url(self):
        return f"/subcategories/{self.slug}/"

    # def save(self, *args, **kwargs):
    #     if not self.id and not self.slug:
    #         self.slug = slugify(self.sub_category) + ".html"
    #     else:
    #         if not self.id:
    #             self.slug = slugify(self.slug) + ".html"
    #         else:
    #             self.slug = slugify(self.slug.rstrip('.html')) + ".html"
    #     super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.sub_category} -> {self.category_slug.category}"

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Product(models.Model):
    # category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    category_slug = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE,
                                      related_name='category_slug_product')
    # sub_category = models.ForeignKey(SubCategory, verbose_name="Подкатегория", on_delete=models.CASCADE, null=True,
    #                                  blank=True)
    subcategory_slug = models.ForeignKey(SubCategory, verbose_name="Подкатегория",
                                         on_delete=models.CASCADE, null=True, blank=True,
                                         related_name='subcategory_slug_product')
    photo = models.ImageField(verbose_name="Фото")
    name = models.CharField(verbose_name="Название", max_length=200)
    slug = models.SlugField(verbose_name="Английское название", unique=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    price = models.CharField(verbose_name="Цена", max_length=100, null=True, blank=True)
    on_main = models.BooleanField(verbose_name="Показать на главной странице", default=False)

    def get_absolute_url(self):
        return f"/products/{self.slug}/"

    def __str__(self):
        return f"{self.name} = {self.slug}"

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Service(models.Model):
    photo = models.ImageField(verbose_name="Фото", null=True, blank=True)
    name = models.CharField(verbose_name="Название", max_length=200)
    slug = models.SlugField(verbose_name="Английское название", unique=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    on_main = models.BooleanField(verbose_name="Показать на главной странице", default=False)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class News(models.Model):
    date = models.DateField(verbose_name="Дата")
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    text = models.TextField(verbose_name="Текст", null=True, blank=True)
    on_main = models.BooleanField(verbose_name="Показать на главной странице", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Apply(models.Model):
    applier_name = models.CharField(verbose_name="Имя", max_length=64)
    applier_phone = models.CharField(verbose_name="Номер телефона", max_length=13)
    # product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.SET_NULL, null=True)
    message = models.TextField(verbose_name="Сообщение", null=True, blank=True)
    date_applied = models.DateTimeField(verbose_name="Время заявки", auto_now_add=True)

    def __str__(self):
        return self.applier_name

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
