from openai import OpenAI

class ChatClient:
    """
    a CahtClient to simple the way to talk to llm-based service

    demo:
    ```python
    from chat_client import ChatClient
    client = ChatClient(api_key='NULL', base_url='http://127.0.0.1:7777/v1',
                        model='Qwen1.5-14B-Chat-GPTQ-Int4')
    client.chat("你好")
    ```

    start with gui by gradio
    ```
    import gradio as gr

    gr.ChatInterface(client.predict, chatbot=gr.Chatbot(height=700))\
    .launch(server_name='0.0.0.0', server_port=9999)
    ```
    """
    def __init__(self, api_key:str, base_url:str, model: str = None, system_prompt: str = None):
        """
        初始化ChatClient

        parameters:
        - api_key: the api-key given access to the llm-based server or 'NULL' if not needed
        - base_url: the base_url for the llm-based server, like 'http://127.0.0.1:7777/v1'
        - model: model's name, like 'Qwen1.5-14B-Chat-GPTQ-Int4'
        - system_prompt: a system prompt like
          你是 Qwen1.5, Qwen1.5 is the beta version of Qwen2, a transformer-based decoder-only language model pretrained
          on a large amount of data. 你擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。
        """
        self.api_key = api_key
        self.base_url = base_url
        self.client = OpenAI(
            api_key=self.api_key or 'NULL',
            base_url=self.base_url
        )

        self.model = model or 'anonymous'

        self.system_prompt = system_prompt or """
        你是一个基于大语言模型的智能助手，在训练的过程中，你掌握了多个领域的丰富的知识。你擅长中文和英文的对话、编码、人工智能技术，在人工智能方面，
        你擅长机器学习、深度学习、强化学习、知识图谱等内容，包括理论知识和相关工具、库的使用。你会为用户提供安全，有帮助，准确的回答。
        """
        self.history = []


    def predict(self, message, history):
        """
        这个方法实施了gradio的history数据结构，以及向openao风格的消息转换
        """
        history_openai_format = [
            {"role": "system", "content": self.system_prompt}
        ]
        for human, assistant in history:
            history_openai_format.append({"role": "user", "content": human })
            history_openai_format.append({"role": "assistant", "content":assistant})
        history_openai_format.append({"role": "user", "content": message})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=history_openai_format,
            temperature=0.3)

        return response.choices[0].message.content

    def chat(self, message):
        """
        主要使用这个方法来发送消息，同时保存历史记录
        """
        response = self.predict(message, self.history)
        item = message, response
        self.history.append(item)
        return response
