# 运行：nohup python ./gradio_app.py > ./logs/gradio_app.log 2>&1 &

from ..llm_chat_service.chat_client import ChatClient
import gradio as gr


def chat_interface(api_key, base_url, model):
    client = ChatClient(api_key=api_key,
                        base_url=base_url,
                        model=model)
    gr.ChatInterface(client.predict).launch(server_name='0.0.0.0', server_port=9999)


if __name__ == "__main__":
    chat_interface(api_key="NULL", base_url="http://10.3.219.61:52073/v1", model="Qwen2-7B-Instruct")