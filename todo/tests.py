import pytest


from .models import Todo, Category, Comment  # E302 fixed: Added blank line


@pytest.fixture
def todo():  # E302 fixed: Added blank line
    return Todo.objects.create(
        title="Test Todo",
        description="Test Description",
        completed=False
    )


@pytest.fixture
def category():  # E302 fixed: Added blank line
    return Category.objects.create(
        name="Test Category",
        description="Test Category Description"
    )


@pytest.fixture
def comment(todo):  # E302 fixed: Added blank line
    return Comment.objects.create(
        todo=todo,
        text="Test Comment"
    )


# Todo Tests
@pytest.mark.django_db
def test_todo_creation(todo):  # E302 fixed: Added blank line
    assert todo.title == "Test Todo"
    assert todo.description == "Test Description"
    assert todo.completed is False  # E712 fixed: Changed comparison to `is False`
    assert todo.created_at is not None
    assert todo.updated_at is not None


@pytest.mark.django_db
def test_todo_str_method(todo):  # E302 fixed: Added blank line
    assert str(todo) == "Test Todo"


@pytest.mark.django_db
def test_todo_update(todo):  # E302 fixed: Added blank line
    old_updated_at = todo.updated_at
    todo.title = "Updated Todo"
    todo.save()
    assert todo.title == "Updated Todo"
    assert todo.updated_at != old_updated_at


# Category Tests
@pytest.mark.django_db
def test_category_creation(category):  # E302 fixed: Added blank line
    assert category.name == "Test Category"
    assert category.description == "Test Category Description"


@pytest.mark.django_db
def test_category_str_method(category):  # E302 fixed: Added blank line
    assert str(category) == "Test Category"


@pytest.mark.django_db
def test_category_unique_name(category):  # E302 fixed: Added blank line
    with pytest.raises(Exception):
        Category.objects.create(name="Test Category")


# Comment Tests
@pytest.mark.django_db
def test_comment_creation(comment, todo):  # E302 fixed: Added blank line
    assert comment.todo == todo
    assert comment.text == "Test Comment"
    assert comment.created_at is not None


@pytest.mark.django_db
def test_comment_str_method(comment, todo):  # E302 fixed: Added blank line
    assert str(comment) == f"Comment on {todo.title} by {comment.id}"


@pytest.mark.django_db
def test_comment_related_name(comment, todo):  # E302 fixed: Added blank line
    assert todo.comments.count() == 1
    assert todo.comments.first() == comment


@pytest.mark.django_db
def test_comment_cascade_delete(comment, todo):  # E302 fixed: Added blank line
    comment_id = comment.id
    todo.delete()
    assert Comment.objects.filter(id=comment_id).count() == 0
