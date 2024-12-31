from flask import jsonify, request, Blueprint
from .model import TaskManager, WorkTask, StudyTask, RoutineTask

from . import home
manager = TaskManager()

@home.route('/api/tasks/add', methods=['POST'])
def add_task():
    try:
        data = request.get_json()
        title = data['title']
        note = data['note']
        deadline = data['deadline']
        priority = data['priority']
        category = data['category'].lower()

        if category == "work":
            task = WorkTask(None, title, note, deadline, priority)
        elif category == "study":
            task = StudyTask(None, title, note, deadline, priority)
        elif category == "routine":
            task = RoutineTask(None, title, note, deadline, priority)
        else:
            return jsonify({"status": "failed", "message": "Invalid category!"}), 400

        manager.add_task(task)
        return jsonify({"status": "success", "message": "Task added successfully!"}), 201

    except Exception as err:
        return jsonify({"status": "failed", "message": str(err)}), 500

@home.route('/api/tasks/remove', methods=['DELETE'])
def remove_task():
    try:
        data = request.get_json()
        id = data['id']

        if manager.remove_task(id):
            return jsonify({"status": "success", "message": "Task removed successfully!"}), 200
        else:
            return jsonify({"status": "failed", "message": "Task not found!"}), 404

    except Exception as err:
        return jsonify({"status": "failed", "message": str(err)}), 500

@home.route('/api/tasks/all', methods=['GET'])
def get_all_tasks():
    try:
        tasks = manager.get_all_tasks()
        return jsonify({"status": "success", "tasks": tasks}), 200
    except Exception as err:
        return jsonify({"status": "failed", "message": str(err)}), 500

@home.route('/api/tasks/upcoming', methods=['GET'])
def get_upcoming_tasks():
    try:
        tasks = manager.upcoming_tasks()
        return jsonify({"status": "success", "tasks": tasks}), 200
    except Exception as err:
        return jsonify({"status": "failed", "message": str(err)}), 500
    
@home.route('/api/tasks/priority', methods=['GET'])
def get_priority_tasks():
    try:
        # Mengambil parameter 'priority' dari query string
        priority = request.args.get('priority', 'all')  # Default ke 'all' jika tidak ada parameter
        tasks = manager.priority_tasks(priority)
        return jsonify({"status": "success", "tasks": tasks}), 200
    except Exception as err:
        return jsonify({"status": "failed", "message": str(err)}), 500