from datetime import datetime

def serialize_model(model):
    return {column.name: getattr(model, column.name) for column in model.__table__.columns}

def serialize_goal(goal):
    return {
        'goal_id': goal.goal_id,
        'title': goal.title,
        'description': goal.description,
        'start_date': goal.start_date.strftime('%Y-%m-%d'),
        'end_date': goal.end_date.strftime('%Y-%m-%d'),
        'reminder_time': goal.reminder_time.strftime('%H:%M:%S') if goal.reminder_time else None
    }

def validate_goal_data(data):
    required_fields = ['title', 'description', 'start_date', 'end_date', 'reminder_time']
    for field in required_fields:
        if field not in data:
            return f'{field} is required.'
    try:
        datetime.strptime(data['start_date'], '%Y-%m-%d')
        datetime.strptime(data['end_date'], '%Y-%m-%d')
        if 'reminder_time' in data:
            datetime.strptime(data['reminder_time'], '%H:%M:%S')
    except ValueError:
        return 'Invalid date or time format.'
    return None