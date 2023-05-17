from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Movie, Actor
from .utils import search_movies, paginate_movies, selection_data_genres, selection_data_year
from .forms import ReviewForm
from django.core.paginator import EmptyPage


def home(request):
    movies, search_query = search_movies(request)
    last_added = Movie.objects.order_by('-pk')[:5]
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено'})
    context = {
        'movies': movies,
        'last_added': last_added,
        'search_query': search_query,
        # 'paginator': paginator,
        'custom_range': custom_range
    }
    return render(request, 'home/index.html', context)


def get_movie(request, slug):
    movie_single = Movie.objects.get(url=slug)
    last_added = Movie.objects.order_by('-pk')[:5]
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.movie = movie_single
        review.owner = request.user
        review.save()

        movie_single.get_vote_count()

        messages.success(request, 'Ваш отзыв успешно отправлен!')
        return redirect(movie_single.get_absolute_url())

    context = {
        'movie_single': movie_single,
        'last_added': last_added,
        'form': form
    }
    return render(request, 'home/moviesingle.html', context)


def category_movies(request):
    movies = Movie.objects.filter(category=1)
    last_added = Movie.objects.filter(category=1).order_by('-pk')[:5]
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено'})
    context = {'movies': movies,
               'last_added': last_added,
               'custom_range': custom_range
               }
    return render(request, 'home/index.html', context)


def category_series(request):
    series = Movie.objects.filter(category=2)
    last_added = Movie.objects.filter(category=2).order_by('-pk')[:5]
    try:
        custom_range, series = paginate_movies(request, series, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено'})
    context = {'movies': series,
               'last_added': last_added,
               'custom_range': custom_range
               }
    return render(request, 'home/index.html', context)


def category_cartoon(request):
    cartoon = Movie.objects.filter(category=3)
    last_added = Movie.objects.filter(category=3).order_by('-pk')[:5]
    try:
        custom_range, cartoon = paginate_movies(request, cartoon, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено'})
    context = {'movies': cartoon,
               'last_added': last_added,
               'custom_range': custom_range
               }
    return render(request, 'home/index.html', context)


def rating_movies_red(request):
    movie_obj = Movie.objects.all()
    movies = list()
    last_added = Movie.objects.order_by('-pk')[:5]
    for i in movie_obj:
        if i.vote_ratio < 5:
            movies.append(i)
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено'})
    context = {'movies': movies,
               'last_added': last_added,
               'custom_range': custom_range
               }
    return render(request, 'home/index.html', context)


def rating_movies_grey(request):
    movie_obj = Movie.objects.all()
    movies = list()
    last_added = Movie.objects.order_by('-pk')[:5]
    for i in movie_obj:
        if 4.9 < i.vote_ratio < 7:
            movies.append(i)
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено'})
    context = {'movies': movies,
               'last_added': last_added,
               'custom_range': custom_range
               }
    return render(request, 'home/index.html', context)


def rating_movies_green(request):
    movie_obj = Movie.objects.all()
    movies = list()
    last_added = Movie.objects.order_by('-pk')[:5]
    for i in movie_obj:
        if 6.9 < i.vote_ratio <= 10:
            movies.append(i)
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено'})
    context = {'movies': movies,
               'last_added': last_added,
               'custom_range': custom_range
               }
    return render(request, 'home/index.html', context)


def checkbox_search_genre(request):
    movies = selection_data_genres(request)
    last_added = Movie.objects.order_by('-pk')[:5]
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено'})
    context = {'movies': movies,
               'last_added': last_added,
               'custom_range': custom_range
               }
    return render(request, 'home/index.html', context)


def checkbox_search_year(request):
    movies = selection_data_year(request)
    last_added = Movie.objects.order_by('-pk')[:5]
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено', 'last_added': last_added})
    context = {'movies': movies,
               'last_added': last_added,
               'custom_range': custom_range
               }
    return render(request, 'home/index.html', context)


def actor_detail(request, slug):
    actor = Actor.objects.get(name=slug)
    last_added = Movie.objects.order_by('-pk')[:5]
    context = {
        'actor': actor,
        'last_added': last_added,
    }
    return render(request, 'home/actor.html', context)

