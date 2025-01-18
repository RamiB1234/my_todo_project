from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json

# Create your views here.

def get_all_tasks(request):
    tasks = Task.objects.all().values()  # Query all tasks from the database
    return JsonResponse(list(tasks), safe=False)  # Convert queryset to JSON response


# Add a new task
@csrf_exempt  # Disable CSRF for simplicity (not recommended for production)
def add_task(request):
    if request.method == 'POST':
        try:
            # Decode the bytes and load as JSON
            data = json.loads(request.body.decode('utf-8'))
            # Create a new Task
            task = Task.objects.create(description=data['description'], completed=False)
            # Return the created task as a JSON response
            return JsonResponse({'id': task.id, 'description': task.description, 'completed': task.completed})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

# Toggle completed
@csrf_exempt # Disable CSRF for simplicity (not recommended for production)
def set_completed(request):
    if request.method == "PUT":
        try:
            # Parse the JSON body to get the task ID and new completed status
            data = json.loads(request.body.decode('utf-8'))
            task_id = data.get('id')
            completed_status = data.get('completed')

            # Validate the required fields
            if task_id is None or completed_status is None:
                return JsonResponse({'error': 'Both "id" and "completed" fields are required'}, status=400)

            # Retrieve the task from the database
            task = Task.objects.get(id=task_id)

            # Update the 'completed' field
            task.completed = completed_status
            task.save()

            # Return the updated task as a JSON response
            return JsonResponse({
                'id': task.id,
                'description': task.description,
                'completed': task.completed
            })
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
