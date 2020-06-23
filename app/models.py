from django.db import models

class User(models.Model):
    name  = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Project(models.Model):
    pjid = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

class TestSuite(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, related_name='testsuites', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class TestCase(models.Model):
    RESULT_NULL = "NULL"
    RESULT_OK = "OK"
    RESULT_NG = "NG"
    RESULT_FIXED = "NG→OK"
    RESULT_SET = (
        (RESULT_NULL, "NULL"),
        (RESULT_OK, "OK"),
        (RESULT_NG, "NG"),
        (RESULT_FIXED, "FIXED"),
    )
    title = models.CharField(max_length=128)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    result = models.CharField(choices=RESULT_SET, default=RESULT_NULL, max_length=8, blank=True)
    author = models.ForeignKey(User, related_name='testcases', on_delete=models.CASCADE, null=True)
    testsuite = models.ForeignKey(TestSuite, related_name='testsuites', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Issue(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
        (STATUS_DRAFT, "下書き"),
        (STATUS_PUBLIC, "公開中"),
    )
    title = models.CharField(max_length=128)
    body = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8, null=True)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, related_name='project', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
