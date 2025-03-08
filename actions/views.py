import json
from django.http import JsonResponse
from .models import SustainabilityAction

def get_actions(request):
    actions = SustainabilityAction.objects.all()
    action_list = [{'id': action.id, 'action': action.action, 'date': action.date, 'points': action.points} for action in actions]
    return JsonResponse(action_list, safe=False)

def add_action(request):
    if request.method == 'POST':
        action_data = json.loads(request.body)
        action = SustainabilityAction.objects.create(
            action=action_data['action'],
            date=action_data['date'],
            points=action_data['points']
        )
        return JsonResponse({'id': action.id, 'action': action.action, 'date': action.date, 'points': action.points}, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def update_action(request, action_id):
    try:
        action = SustainabilityAction.objects.get(pk=action_id)
    except SustainabilityAction.DoesNotExist:
        return JsonResponse({'error': 'Action not found'}, status=404)

    if request.method == 'PUT':
        action_data = json.loads(request.body)
        action.action = action_data.get('action', action.action)
        action.date = action_data.get('date', action.date)
        action.points = action_data.get('points', action.points)
        action.save()
        return JsonResponse({'id': action.id, 'action': action.action, 'date': action.date, 'points': action.points})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def delete_action(request, action_id):
    try:
        action = SustainabilityAction.objects.get(pk=action_id)
    except SustainabilityAction.DoesNotExist:
        return JsonResponse({'error': 'Action not found'}, status=404)

    if request.method == 'DELETE':
        action.delete()
        return JsonResponse({'message': 'Action deleted successfully'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)