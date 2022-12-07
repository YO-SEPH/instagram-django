from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed
from rest_framework.response import Response
import os
from .settings import MEDIA_ROOT
from uuid import uuid4


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')
        return render(request, 'instargram/main.html', context=dict(feed_list=feed_list))