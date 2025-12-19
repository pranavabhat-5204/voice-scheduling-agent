# voice-scheduling-agent
A real-time voice assistant that schedules meetings by collecting user details via voice, confirming them, and creating a real calendar event using Google Calendar. The assistant is deployed and accessible via a hosted URL and integrates with a backend API deployed on Render.
Deployed Application
Backend API: voice-scheduling-agent.onrender.com
You will get {"status": "running"}.
Scheduling endpoint: POST /schedule
How to Test the Voice Agent
The voice assistant is tested using Vapi.ai.
Steps:
1.	Open the Vapi dashboard and navigate to the configured assistant.
2.	Click “Talk to Assistant”.
3.	Allow microphone access.
4.	Follow the voice prompts:
o	Provide your name
o	Provide meeting date
o	Provide meeting time
o	Optionally provide a meeting title
5.	When asked for confirmation, say “Yes”.
6.	The assistant calls the backend API and schedules the meeting.
You can test if your backend is running smoothly by running:
curl -X POST https://voice-scheduling-agent.onrender.com/schedule \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Raghavan",
    "date": "2025-12-20",
    "time": "16:00",
    "title": "Voice Agent Test Meeting"
  }'



Voice assistant testing
 

Calendar updated
 

