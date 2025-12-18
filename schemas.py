from pydantic import BaseModel
from typing import Optional

class MeetingRequest(BaseModel):
    name: str
    date: str        # YYYY-MM-DD
    time: str        # HH:MM
    title: Optional[str] = "Meeting"
