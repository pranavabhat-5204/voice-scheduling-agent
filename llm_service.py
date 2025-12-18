import os
from groq import Groq

def get_groq_client():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not set")
    return Groq(api_key=api_key)

def validate_meeting(details: dict) -> bool:
    client = get_groq_client()

    prompt = f"""
    Validate the following meeting details.
    Return only VALID or INVALID.

    Details:
    {details}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip() == "VALID"
