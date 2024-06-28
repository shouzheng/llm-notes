# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from openai import OpenAI

app = Flask(__name__)

# 假设这是从环境变量或配置文件中获取的 OpenAI API 密钥
API_KEY = "NULL"
base_url = "http://10.3.219.72:38554/v1"
model = "Qwen2-7B-Instruct"

client = OpenAI(
    api_key=API_KEY,
    base_url=base_url
)

# 定义翻译的路由
@app.route('/translator', methods=['GET'])
def translator():
    # 从查询参数中获取数据
    text_to_translate = request.args.get('q', '')

    if not text_to_translate:
        return render_template('error.html', message='No text provided')

    # 调用翻译服务
    translation = translate_text(text_to_translate)

    # 返回翻译结果
    return render_template('interprete_result.html',
                           original_text=text_to_translate,
                           translated_text=translation)

def translate_text(text):
    # 这里我们假设有一个符合 OpenAI API 规范的翻译服务
    # 构建请求数据
    prompt = """
    请将下面的内容翻译成中文，并只返回译文内容：
    """ + text
    message = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
        model=model,
        messages=message,
        temperature=0.3)
    return response.choices[0].message.content

if __name__ == '__main__':
    app.run()