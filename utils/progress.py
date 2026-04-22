from pathlib import Path
import json
from datetime import date, datetime

BASE_DIR = Path(__file__).resolve().parent.parent
FILE_PATH = BASE_DIR / "progress.json"


def load_progress():
    if not FILE_PATH.exists():
        return {
            "completed": {},
            "streak": 0,
            "last_completed_date": None
        }

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {
            "completed": {},
            "streak": 0,
            "last_completed_date": None
        }

    if "completed" not in data:
        data["completed"] = {}
    if "streak" not in data:
        data["streak"] = 0
    if "last_completed_date" not in data:
        data["last_completed_date"] = None

    return data


def save_progress(data):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def mark_completed(problem_title):
    progress = load_progress()
    today = str(date.today())

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
    return progress["completed"].get(problem_title) == today


def get_streak():
    progress = load_progress()
    return progress.get("streak", 0)