from ninja import Router, ModelSchema
from .models import Todo


class AddTodo(ModelSchema):
    class Config:
        model = Todo
        model_fields = ['title']


class UpdateTodo(ModelSchema):
    class Config:
        model = Todo
        model_fields = ['id', 'completed']


class DeleteTodo(ModelSchema):
    class Config:
        model = Todo
        model_fields = ['id', 'title', 'completed']




# router = Router(tags=["todos"])
#
# def list_todos(request):
#     """List todos"""
#     todos = Todo.objects.to_list()
#     return todos
#
#
# @router.get("/{todo_id}", operation_id="getTodo")
# def todo_details(request, todo_id: int):
#     """Retrive todo"""
#     todo = Todo.objects.get(id=todo_id)
#     return todo.to_json()
#
#
# @router.delete("/{todo_id}", operation_id="deleteTodo")
# def delete_todo(request, todo_id: int):
#     """Delete todo"""
#     obj = Todo.objects.filter(id=todo_id).first()
#     if obj is not None:
#         obj.delete()
#         return {"message": f"deleted to with id {todo_id}"}
#
#     return router.create_response(
#         request,
#         {"message": "Delete failed obj not found"},
#         status=404,
#     )
#
#
# @router.post("/", operation_id="addTodo")
# def post_todo(request, payload: TodoSchema):
#     """Add todo"""
#     obj = Todo.objects.create(detail=payload.detail, status=payload.status)
#     obj.save()
#     return obj.to_json()