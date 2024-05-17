from openai import OpenAI
client = OpenAI(
    api_key="Qwen1.5-14B-Chat-GPTQ-Int4", # 不能不设置，也不能为空
    base_url="http://127.0.0.1:7777/v1" # 注意，这里是base_url，不是具体chat接口的地址
)

system_prompt = "你是 Qwen1.5, Qwen1.5 is the beta version of Qwen2, a transformer-based decoder-only language model pretrained on a large amount of data. 你擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。"

def predict(message, history):
    """
    这个方法实施了gradio的history数据结构，以及向openao风格的消息转换
    """
    history_openai_format = [
        {"role": "system", "content": system_prompt}
    ]
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})
  
    response = client.chat.completions.create(
        model="Qwen1.5-14B-Chat-GPTQ-Int4",
        messages=history_openai_format,
        temperature=0.3)

    return response.choices[0].message.content

history = []
def chat(message):
    """
    主要使用这个方法来发送消息，同时保存历史记录
    """
    response = predict(message, history)
    item = message, response
    history.append(item)
    return response