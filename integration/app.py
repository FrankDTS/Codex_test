import os
from datetime import datetime
from flask import Flask, jsonify, render_template

# Example usage of Google Calendar and Asana APIs.
# Replace placeholders with your own credentials and API calls.

# TODO: Add OAuth setup and authentication.

def fetch_google_events():
    """Fetch events from Google Calendar."""
    # This function should use Google Calendar API to retrieve events
    # For simplicity, return a static example
    return [
        {
            "id": "event-1",
            "summary": "Meeting",
            "start": datetime.utcnow().isoformat() + "Z",
            "end": datetime.utcnow().isoformat() + "Z",
        }
    ]


def fetch_asana_tasks():
    """Fetch tasks from Asana."""
    # This function should use Asana API to retrieve tasks
    # For simplicity, return a static example
    return [
        {
            "id": "task-1",
            "name": "Design wireframes",
            "status": "In Progress",
            "due": datetime.utcnow().isoformat(),
        }
    ]


def merge_tasks_and_events(events, tasks):
    """Merge tasks and calendar events by day."""
    merged = {}
    for event in events:
        day = event["start"].split("T")[0]
        merged.setdefault(day, {"events": [], "tasks": []})
        merged[day]["events"].append(event)
    for task in tasks:
        day = task["due"].split("T")[0]
        merged.setdefault(day, {"events": [], "tasks": []})
        merged[day]["tasks"].append(task)
    return merged


app = Flask(__name__)


@app.route("/")
def dashboard():
    events = fetch_google_events()
    tasks = fetch_asana_tasks()
    merged = merge_tasks_and_events(events, tasks)
    return jsonify(merged)


if __name__ == "__main__":
    app.run(debug=True)
