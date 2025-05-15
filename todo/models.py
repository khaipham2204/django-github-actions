from django.db import models


class Todo(models.Model):  # E302 fixed: Added blank line
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):  # E302 fixed: Added blank line
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):  # E302 fixed: Added blank line
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.todo.title} by {self.id}"
# W292 fixed: Added a newline at the end of the file
