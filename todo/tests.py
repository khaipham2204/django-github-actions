import pytest
from django.utils import timezone
from .models import Todo, Category, Comment

@pytest.fixture
def todo():
    return Todo.objects.create(
        title="Test Todo",
        description="Test Description",
        completed=False
    )

@pytest.fixture
def category():
    return Category.objects.create(
        name="Test Category",
        description="Test Category Description"
    )

@pytest.fixture
def comment(todo):
    return Comment.objects.create(
        todo=todo,
        text="Test Comment"
    )

# Todo Tests
@pytest.mark.django_db
def test_todo_creation(todo):
    assert todo.title == "Test Todo"
    assert todo.description == "Test Description"
    assert todo.completed == False
    assert todo.created_at is not None
    assert todo.updated_at is not None

@pytest.mark.django_db
def test_todo_str_method(todo):
    assert str(todo) == "Test Todo"

@pytest.mark.django_db
def test_todo_update(todo):
    old_updated_at = todo.updated_at
    todo.title = "Updated Todo"
    todo.save()
    assert todo.title == "Updated Todo"
    assert todo.updated_at != old_updated_at

# Category Tests
@pytest.mark.django_db
def test_category_creation(category):
    assert category.name == "Test Category"
    assert category.description == "Test Category Description"

@pytest.mark.django_db
def test_category_str_method(category):
    assert str(category) == "Test Category"

@pytest.mark.django_db
def test_category_unique_name(category):
    with pytest.raises(Exception):
        Category.objects.create(name="Test Category")

# Comment Tests
@pytest.mark.django_db
def test_comment_creation(comment, todo):
    assert comment.todo == todo
    assert comment.text == "Test Comment"
    assert comment.created_at is not None

@pytest.mark.django_db
def test_comment_str_method(comment, todo):
    assert str(comment) == f"Comment on {todo.title} by {comment.id}"

@pytest.mark.django_db
def test_comment_related_name(comment, todo):
    assert todo.comments.count() == 1
    assert todo.comments.first() == comment

@pytest.mark.django_db
def test_comment_cascade_delete(comment, todo):
    comment_id = comment.id
    todo.delete()
    assert Comment.objects.filter(id=comment_id).count() == 0
