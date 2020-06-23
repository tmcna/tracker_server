from django.contrib import admin

from .models import User, Project, TestSuite, TestCase, Issue

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class Project(admin.ModelAdmin):
    pass

@admin.register(TestSuite)
class TestSuite(admin.ModelAdmin):
    pass

@admin.register(TestCase)
class TestCase(admin.ModelAdmin):
    pass

@admin.register(Issue)
class Issue(admin.ModelAdmin):
    pass