import ollama
from typing import Dict, Any

# Meta-descriptor complying with Agent Skill Open Standard definitions
SKILL_DESCRIPTOR = {
    "name": "indian_medical_triage_assistant",
    "description": "An offline triage tool for identifying urgency levels and primary first aid steps tailored for Indian emergency contexts.",
    "parameters": {
        "type": "object",
        "properties": {
            "user_query": {
                "type": "string",
                "description": "The symptom statement, injury description, or first aid inquiry provided by the user."
            }
        },
        "required": ["user_query"]
    },
    "version": "1.0.0",
    "license": "MIT"
}

SYSTEM_PROMPT = """
You are LocalGuard AI, an offline first-aid and triage assistant operating under the Agent Skill Open Standard.

CRITICAL SAFETY & REGIONAL RULES:
1. Present general information only. Never give personalized medical advice or definitive diagnoses.
2. If the user describes a life-threatening scenario (e.g., severe bleeding, unconsciousness, chest pain), start your response with a highly visible warning instructing them to contact emergency services immediately (National Emergency Number: 112).
3. List at least THREE distinct possibilities/considerations for what the symptom might resemble using hedging language ("resembles", "is consistent with").
4. If recommending home remedies or basic actions, suggest at least THREE distinct treatment options or steps.
5. Reject personalized medication dosage calculations and remind users to double-check the physical product label. Do not provide dosage instructions for infants.
"""

def execute_triage_skill(user_query: str) -> Dict[str, Any]:
    """
    Executes the core agent skill task.
    Returns a standardized dictionary envelope containing execution metadata and response content.
    """
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]
    
    try:
        response = ollama.chat(model='llama3.2', messages=messages, stream=False)
        content = response['message']['content']
        
        # Standardized return payload format
        return {
            "status": "success",
            "skill_name": SKILL_DESCRIPTOR["name"],
            "version": SKILL_DESCRIPTOR["version"],
            "data": {
                "response": content
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "skill_name": SKILL_DESCRIPTOR["name"],
            "version": SKILL_DESCRIPTOR["version"],
            "error_message": str(e)
        }
