import os
from dotenv import load_dotenv
import dashscope
from dashscope import Generation

# 1. 加载环境变量（读取你的 API Key）
load_dotenv()
dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")

print("🤖 你的专属 AI 聊天机器人已启动！(输入 'quit' 退出)")

while True:
    # 2. 获取你的输入
    user_input = input("\n你: ")
    if user_input.lower() == 'quit':
        print("👋 下次再见！")
        break

    # 3. 调用大模型接口
    messages = [
        {'role': 'system', 'content': '你是一个热心、专业的 AI 助手。'},
        {'role': 'user', 'content': user_input}
    ]
    response = Generation.call(
        model='qwen-plus',  # 使用通义千问的 qwen-plus 模型
        messages=messages,
        result_format='message'
    )

    # 4. 打印 AI 的回答
    if response.status_code == 200:
        print(f"AI: {response.output.choices[0].message.content}")
    else:
        print(f"出错了: {response.code} - {response.message}")