from pydantic import BaseModel

class MeetingRequest(BaseModel):
    name: str
    date: str
    time: str
    title: str | None = "Scheduled Meeting"