# 运行：nohup python ./gradio_app.py > ./logs/gradio_app.log 2>&1 &

from .chat_client import predict
import gradio as gr


gr.ChatInterface(predict, chatbot=gr.Chatbot(height=700)).launch(server_name='0.0.0.0', server_port=9999)
