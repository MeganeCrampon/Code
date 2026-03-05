import gradio as gr

def saluer(nom):
    return f"Bonjour {nom} !"

# Interface
demo = gr.Interface(fn=saluer, inputs="text", outputs="text")
demo.launch()