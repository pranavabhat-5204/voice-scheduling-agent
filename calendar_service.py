import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta

def get_google_creds():
    required_vars = [
        "GOOGLE_CLIENT_ID",
        "GOOGLE_CLIENT_SECRET",
        "GOOGLE_REFRESH_TOKEN"
    ]

    for var in required_vars:
        if not os.environ.get(var):
            raise RuntimeError(f"{var} not set")

    return Credentials(
        None,
        refresh_token=os.environ["GOOGLE_REFRESH_TOKEN"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.environ["GOOGLE_CLIENT_ID"],
        client_secret=os.environ["GOOGLE_CLIENT_SECRET"],
        scopes=["https://www.googleapis.com/auth/calendar"]
    )

def create_calendar_event(name, date, time, title):
    creds = get_google_creds()
    service = build("calendar", "v3", credentials=creds)

    start = datetime.fromisoformat(f"{date}T{time}")
    end = start + timedelta(hours=1)

    event = {
        "summary": title,
        "description": f"Meeting scheduled for {name}",
        "start": {"dateTime": start.isoformat(), "timeZone": "Asia/Kolkata"},
        "end": {"dateTime": end.isoformat(), "timeZone": "Asia/Kolkata"},
    }

    created_event = service.events().insert(
        calendarId="primary", body=event
    ).execute()

    return created_event.get("htmlLink")
