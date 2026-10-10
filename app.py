import gradio as gr
from skills.triage_skill import execute_triage_skill, SKILL_DESCRIPTOR

def predict(message, history):
    # Execute through the standard agent skill wrapper
    result = execute_triage_skill(user_query=message)
    
    if result["status"] == "success":
        return result["data"]["response"]
    else:
        return f"⚠️ **Skill Execution Failure:** {result['error_message']}"

with gr.Blocks() as demo:
    gr.Markdown("# 🏥 LocalGuard AI (India Edition)")
    gr.Markdown(f"### Open Standard Agent Skill: `{SKILL_DESCRIPTOR['name']}` v{SKILL_DESCRIPTOR['version']}")
    gr.Markdown("Complies with the **Agent Skill Open Standard** • Powered locally by **Llama 3.2 3B**")
    
    gr.ChatInterface(
        fn=predict,
        examples=[
            "My uncle is experiencing sudden severe chest pain and sweating.",
            "I accidentally stepped on a rusty nail outside.",
            "What is the first aid procedure for a heat stroke during Indian summer?"
        ]
    )

if __name__ == "__main__":
    demo.queue().launch(theme=gr.themes.Soft(primary_hue="red", secondary_hue="slate"))
