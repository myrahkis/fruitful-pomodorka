from ninja import Router
from .models import Todo
from .schema import TodoSchema


router = Router(tags=["todos"])


@router.get("/", operation_id="getTodos")
def list_todos(request):
    """List todos"""
    todos = Todo.objects.to_list()
    return todos


@router.get("/{todo_id}", operation_id="getTodo")
def todo_details(request, todo_id: int):
    """Retrive todo"""
    todo = Todo.objects.get(id=todo_id)
    return todo.to_json()


@router.delete("/{todo_id}", operation_id="deleteTodo")
def delete_todo(request, todo_id: int):
    """Delete todo"""
    obj = Todo.objects.filter(id=todo_id).first()
    if obj is not None:
        obj.delete()
        return {"message": f"deleted to with id {todo_id}"}

    return router.create_response(
        request,
        {"message": "Delete failed obj not found"},
        status=404,
    )


@router.post("/", operation_id="addTodo")
def post_todo(request, payload: TodoSchema):
    """Add todo"""
    obj = Todo.objects.create(detail=payload.detail, status=payload.status)
    obj.save()
    return obj.to_json()



# @api.post("/todo", tags=['Todo'])
# def add_todo(request, payload: AddTodo):
#     todo = Todo.objects.create(**payload.dict())
#     return {"id": todo.id}
#
#
# @api.get("/todo/{todo_id}", tags=['Todo'], response=DeleteTodo)
# def get_todo(request, todo_id: int):
#     todo = get_object_or_404(Todo, id=todo_id)
#     return todo
#
#
# @api.patch("/todo/{todo_id}", tags=['Todo'])
# def update_todo(request, todo_id: int, payload: UpdateTodo):
#     todo = get_object_or_404(Todo, id=todo_id)
#     for atr, value in payload.dict().items():
#         setattr(todo, atr, value)
#     todo.save()
#     return {"Success": True}
#
#
# @api.delete("/todo/{todo_id}", tags=['Todo'])
# def delete_todo(request, todo_id: int):
#     todo = get_object_or_404(Todo, id=todo_id)
#     todo.delete()
#     return {"Success": True}
#
#
# @api.get("/todo", tags=['Todo'], response=List[DeleteTodo])
# def list_todo(request):
#     todo = Todo.objects.all()
#     return todo


