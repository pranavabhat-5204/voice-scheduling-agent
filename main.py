from fastapi import FastAPI, HTTPException
from schemas import MeetingRequest
from llm_service import validate_meeting
from calendar_service import create_calendar_event
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Voice Scheduling Agent")

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/schedule")
async def schedule_meeting(data: MeetingRequest):
    if not validate_meeting(data.dict()):
        raise HTTPException(status_code=400, detail="Invalid meeting details")

    event_link = create_calendar_event(
        name=data.name,
        date=data.date,
        time=data.time,
        title=data.title
    )

    return {
        "status": "success",
        "message": "Meeting scheduled successfully",
        "calendar_link": event_link
    }

