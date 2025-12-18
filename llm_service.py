from groq import Groq
import os
import os
GROQ_API_KEY ="Grok_Key"
client = Groq(api_key=GROQ_API_KEY)

def validate_meeting(details: dict) -> bool:
    prompt = f"""
    You are validating meeting details.
    Check if the date and time look reasonable.
    Return only VALID or INVALID.

    Details:
    {details}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    result = response.choices[0].message.content.strip()
    return result == "VALID"
