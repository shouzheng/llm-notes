# 运行：nohup python ./gradio_app.py > ./logs/gradio_app.log 2>&1 &

from chat_client import ChatClient
import gradio as gr


client = ChatClient(api_key='NULL', base_url='http://127.0.0.1:7777/v1',
                    model='Qwen1.5-14B-Chat-GPTQ-Int4')

gr.ChatInterface(client.predict, chatbot=gr.Chatbot(height=700)).launch(server_name='0.0.0.0', server_port=9999)
