# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View

class HomePageView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "active": {
                "home": "active",
                "team": "",
                "about": "",
                "search": "",
                "classifier": ""
            }
        }
        return render(request, 'app/index.html', context)


class TeamPageView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "active": {
                "home": "",
                "team": "active",
                "about": "",
                "search": "",
                "classifier": ""
            }
        }
        return render(request, 'app/team.html', context)
