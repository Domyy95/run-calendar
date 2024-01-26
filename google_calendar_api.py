from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

calendar_id = "93e71d5c988c73f8798318e195a9df94cd68247c2449b8f0048dd725320429f1@group.calendar.google.com"

# Lavender: 1, Sage: 2, Grape: 3, Flamingo: 4, Banana: 5, Tangerine: 6, Peacock: 7, Graphite: 8, Blueberry: 9, Basil: 10, Tomato: 11
event_color = 2

# Set the scope for Google Calendar API
SCOPES = ["https://www.googleapis.com/auth/calendar.events"]


def authenticate():
    """Authenticates with Google Calendar API using a service account."""
    credentials = Credentials.from_service_account_file(
        "service-account.json", scopes=SCOPES
    )
    return credentials


def create_event(title: str, description: str, date: str, location: str):
    """Creates a new event on the user's Google Calendar."""
    service = build("calendar", "v3", credentials=creds)

    event = {
        "summary": title,
        "description": description,
        "start": {
            "date": date,
            "timeZone": "Europe/Rome",
        },
        "end": {
            "date": date,
            "timeZone": "Europe/Rome",
        },
        "colorId": event_color,
        "location": location,
    }

    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    print("Event created: %s" % (event.get("htmlLink")))


creds = authenticate()
