from django.db import models
import uuid


class Author(models.Model):
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=100)
    picture = models.URLField("Picture")

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField("Category", max_length=100)
    title = models.CharField("Title", max_length=250)
    summary = models.TextField("Summary", max_length=500)
    first_paragraph = models.TextField("First paragraph")
    body = models.TextField("Body")
