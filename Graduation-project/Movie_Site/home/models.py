from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User


class Movie(models.Model):
    """Фильм"""
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="movies/%Y/%m/%d/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    country = models.CharField("Страна", max_length=30)
    directors = models.ManyToManyField('Actor', verbose_name="режиссер", related_name="film_director")
    actors = models.ManyToManyField('Actor', verbose_name="актеры", related_name="film_actor")
    genres = models.ManyToManyField('Genre', verbose_name="жанры")
    world_premiere = models.DateField("Премьера в мире", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0,
                                         help_text="указывать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField(
        "Сборы в США", default=0, help_text="указывать сумму в долларах"
    )
    fess_in_world = models.PositiveIntegerField(
        "Сборы в мире", default=0, help_text="указывать сумму в долларах"
    )
    category = models.ForeignKey(
        'Category', verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    vote_total = models.IntegerField('Общее количество оценок', default=0)
    vote_ratio = models.FloatField('Соотношение оценок', default=0)
    url_trailer = models.CharField(max_length=1000, default='')
    created = models.DateTimeField('Добавлен', auto_now_add=True)
    adding_movie = models.ManyToManyField(User, default=None, blank=True,
                                          verbose_name='Какие пользователи добавили фильм')
    kinopoisk_url = models.URLField('Кинопоиск', default='')
    kinopoisk_rating = models.FloatField('Рэйтинг Кинопоиска', default=0)
    imdb_url = models.URLField('IMDb', default='')
    imdb_rating = models.FloatField('Рэйтинг IMDb', default=0)
    eng_title = models.CharField("Название на английском", max_length=100, default='')
    age_rating_movie = (
        (0, '0+'),
        (6, '6+'),
        (12, '12+'),
        (16, '16+'),
        (18, '18+'),
    )
    age_rating = models.IntegerField('Возрастной рейтинг', default=0, choices=age_rating_movie)
    movie_duration = models.IntegerField('Продолжительность фильма', default=0, help_text='Указывать в минутах')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get-movie', kwargs={'slug': self.url})

    def get_absolute_url_added(self):
        return reverse('add-movie', kwargs={'slug': self.url})

    def get_absolute_url_deleting_added(self):
        return reverse('deleting-added', kwargs={'slug': self.url})

    def get_absolute_url_deleting_review(self):
        return reverse('review-delete', kwargs={'slug': self.url})

    def written_by(self):
        return [str(p) for p in self.adding_movie.all()]

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ['-created']

    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

    def get_vote_count(self):
        reviews = self.review_set.all()
        up_votes = reviews.filter(value='up').count()
        total_votes = reviews.count()

        ratio = round(((up_votes / total_votes) * 100) / 10, 1)
        self.vote_total = total_votes
        self.vote_ratio = ratio

        self.save()


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    """Актеры и режиссеры"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/%Y/%m/%d/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class MovieShots(models.Model):
    """Кадры из фильма"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots/%Y/%m/%d/")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)
    cms_css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS класс')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Положительная оценка'),
        ('down', 'Отрицательная оценка')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')
    body = models.TextField(null=True, blank=True, verbose_name='Отзыв')
    value = models.CharField(max_length=200, choices=VOTE_TYPE, verbose_name='Оценка')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return self.value

    class Meta:
        unique_together = [['owner', 'movie']]
        ordering = ["-created"]
        verbose_name = "Отзыв и оценка"
        verbose_name_plural = "Отзыв и оценка"


class FactsMovie(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Факты о фильме"
        verbose_name_plural = "Факты о фильме"
