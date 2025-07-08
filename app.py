import gradio as gr
from src.task3_rag_pipeline import rag_pipeline

def chatbot_fn(question):
    try:
        answer, sources, meta = rag_pipeline(question)
        sources_text = "\n\n".join(sources)
        response = f"{answer}\n\n---\n\n🔍 **Sources:**\n{sources_text}"
        return response
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

demo = gr.Interface(
    fn=chatbot_fn,
    inputs=gr.Textbox(lines=2, placeholder="Ask about customer complaints..."),
    outputs=gr.Textbox(label="AI Response"),
    title="CrediTrust Complaint Insights Chatbot",
    description="Ask questions about financial complaints using AI-powered insights."
)

if __name__ == "__main__":
    demo.launch()
