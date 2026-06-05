from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from todoapp.models import TODOAPP


@login_required
def add_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')

        TODOAPP.objects.create(
            user=request.user,
            task_name=task
        )

    return redirect('home')


@login_required
def home(request):
    comp_task = TODOAPP.objects.filter(
        user=request.user,
        is_completed=False
    )

    finish_task = TODOAPP.objects.filter(
        user=request.user,
        is_completed=True
    )

    context = {
        'comp_task': comp_task,
        'finish_task': finish_task,
    }

    return render(request, 'home.html', context)


def all(request):
    data = TODOAPP.objects.all().values(
        'task_name',
        'is_completed',
        'created',
        'updated'
    )

    return JsonResponse(list(data), safe=False)