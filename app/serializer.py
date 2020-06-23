from rest_framework import serializers

from .models import User, Project, TestSuite, TestCase, Issue

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'desc')

class TestSuiteSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    class Meta:
        model = TestSuite
        fields = ('title', 'body', 'created_at', 'project')

class TestCaseSerializer(serializers.ModelSerializer):
    testsuite = TestSuiteSerializer()
    class Meta:
        model = TestCase
        fields = ('title', 'body', 'created_at', 'result', 'testsuite')

class IssueSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    project = ProjectSerializer()

    class Meta:
        model = Issue
        fields = ('title', 'body', 'created_at', 'status', 'author', 'project')