from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)
# Create your views here.


def index(request):
    logger.info(f'Посетили главную страницу')
    return render(request, 'index.html')


def about(request):
    logger.info(f'Посетили страницу About')
    return render(request, 'about.html')
