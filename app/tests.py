import requests
import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import Project

class TestProject(TestCase):
    def test_projects001(self):
        url = "http://localhost:8000/api/projects"
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        print(json.dumps(data, ensure_ascii=False, indent=4))
