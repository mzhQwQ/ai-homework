from openai import OpenAI
from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()

# 初始化客户端
# DeepSeek 官方接口兼容 OpenAI 格式， base_url 固定为 https://api.deepseek.com/v1
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)

def chat_with_deepseek(user_input, history=None):
    """
    调用 DeepSeek 模型进行对话
    """
    messages = []
    # 系统提示词：可以定义机器人角色
    messages.append({"role": "system", "content": "你是一个专业的 AI 助手，请用简洁、准确的语言回答问题。"})
    
    # 添加历史对话（支持多轮对话）
    if history:
        messages.extend(history)
    
    # 添加当前用户输入
    messages.append({"role": "user", "content": user_input})

    try:
        # 调用模型
        response = client.chat.completions.create(
            model="deepseek-chat", # 固定模型名
            messages=messages,
            temperature=0.7,       # 随机性，越低越稳定
            stream=False           # 同步模式，等待完整回复
        )
        # 提取回复内容
        reply = response.choices[0].message.content
        # 更新历史对话
        history = messages + [{"role": "assistant", "content": reply}]
        return reply, history
    except Exception as e:
        return f"❌ 调用失败：{str(e)}", history

# 主程序入口
if __name__ == "__main__":
    print("===== DeepSeek Chatbot (输入 exit 退出) =====")
    conv_history = None
    while True:
        user_msg = input("\n你: ")
        if user_msg.lower() == "exit":
            print("👋 再见！")
            break
        if not user_msg:
            continue
        
        print("🤖 机器人正在思考中...")
        reply, conv_history = chat_with_deepseek(user_msg, conv_history)
        print(f"🤖 机器人: {reply}")