# -*- coding: utf-8 -*-
from openai import OpenAI
import gradio as gr

api_key = "NULL"  # Replace with your key
base_url = "http://10.3.219.51:44788/v1"
model = "Qwen2-7B-Instruct"
client = OpenAI(api_key=api_key, base_url=base_url)


def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = client.chat.completions.create(model=model,
                                              messages=history_openai_format,
                                              temperature=1.0,
                                              stream=True)

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            partial_message = partial_message + chunk.choices[0].delta.content
            yield partial_message


gr.ChatInterface(predict).launch()
