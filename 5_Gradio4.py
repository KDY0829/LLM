import gradio as gr

def handle_fruits(fruit):
    return f'선택한 과일: {fruit}'


with gr.Blocks() as demo:
    fruit_dropdown = gr.Dropdown(label='과일', choices = ['사과', '오렌지', '바나나', '멜론'])
    output_fruit = gr.Textbox(label='구입한 과일')
    fruit_dropdown.change(handle_fruits, inputs=fruit_dropdown, outputs=output_fruit)

    
demo.launch()