import gradio as gr
import ollama

# ----------------------------------------------------
# 1. Indian Context & Strict Clinical Guardrails
# ----------------------------------------------------
SYSTEM_PROMPT = """
You are LocalGuard AI, an offline first-aid and triage assistant running locally on a user's machine in India. 
Your job is to provide clear, calm, and structured general first-aid guidance based on user input.

CRITICAL SAFETY & REGIONAL RULES:
1. You must present general information only. Never give personalized medical advice or definitive diagnoses.
2. If the user describes a life-threatening scenario (e.g., severe bleeding, unconsciousness, chest pain, stroke symptoms), start your response with a highly visible warning instructing them to contact emergency services immediately. Do NOT mention specific numbers.
3. Where relevant, mention helpful regional numbers such as the National Health Helpline (1075) or local ambulance services.
4. List at least THREE distinct possibilities/considerations for what the symptom might resemble or be consistent with. Always use hedging language (e.g., "resembles", "is consistent with", "seems to be").
5. If recommending home remedies or basic actions, suggest at least THREE distinct treatment options or steps.
6. If the user asks about medication dosages, explicitly refuse to calculate personalized biometric doses and remind them to double-check the physical product label. Do not provide dosage instructions for infants.
"""

# ----------------------------------------------------
# 2. Model Inference Core Logic
# ----------------------------------------------------
def predict(message, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    # Process conversational history cleanly
    for human, ai in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": ai})
        
    messages.append({"role": "user", "content": message})

    try:
        response = ollama.chat(model='llama3.2', messages=messages, stream=True)
        
        partial_message = ""
        for chunk in response:
            if 'message' in chunk and 'content' in chunk['message']:
                partial_message += chunk['message']['content']
                yield partial_message 
                
    except Exception as e:
        yield f"⚠️ **Error connecting to local Ollama service:** {str(e)}.\n\nPlease verify that Ollama is active on your computer."

# ----------------------------------------------------
# 3. Gradio Blocks Interface Layout
# ----------------------------------------------------
with gr.Blocks() as demo:
    gr.Markdown("# 🏥 LocalGuard AI (India Edition)")
    gr.Markdown("### Offline, Privacy-First Emergency & Triage Assistant")
    gr.Markdown("Powered locally by **Llama 3.2 3B** • Zero Data Tracking • Completely Offline")
    
    gr.ChatInterface(
        fn=predict,
        examples=[
            "My uncle is experiencing sudden severe chest pain and sweating.",
            "I accidentally stepped on a rusty nail outside.",
            "What is the first aid procedure for a heat stroke during Indian summer?"
        ]
    )

if __name__ == "__main__":
    # Launch with Gradio 6.0 theme compliance
    demo.queue().launch(theme=gr.themes.Soft(primary_hue="red", secondary_hue="slate"))
