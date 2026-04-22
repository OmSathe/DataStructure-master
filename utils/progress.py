import json
import os
from datetime import date, datetime

FILE_PATH = "progress.json"


def load_progress():
    if not os.path.exists(FILE_PATH):
        return {
            "completed": {},
            "streak": 0,
            "last_completed_date": None
        }

    with open(FILE_PATH, "r") as f:
        return json.load(f)


def save_progress(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)


def mark_completed(problem_title):
    progress = load_progress()
    today = str(date.today())

    if "completed" not in progress:
        progress["completed"] = {}

    progress["completed"][problem_title] = today

    last_completed_date = progress.get("last_completed_date")
    current_streak = progress.get("streak", 0)

    if last_completed_date is None:
        progress["streak"] = 1
    else:
        last_date_obj = datetime.strptime(last_completed_date, "%Y-%m-%d").date()
        today_obj = date.today()
        difference = (today_obj - last_date_obj).days

        if difference == 0:
            progress["streak"] = current_streak
        elif difference == 1:
            progress["streak"] = current_streak + 1
        else:
            progress["streak"] = 1

    progress["last_completed_date"] = today
    save_progress(progress)


def is_completed_today(problem_title):
    progress = load_progress()
    today = str(date.today())
    completed = progress.get("completed", {})
    return completed.get(problem_title) == today


def get_streak():
    progress = load_progress()
    return progress.get("streak", 0)