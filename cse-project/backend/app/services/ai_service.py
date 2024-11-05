from langchain.llms import OpenAI

class AIService:
    def __init__(self):
        # OpenAIのインスタンスを初期化
        # 必要に応じてAPIキーやモデル名を設定
        self.llm = OpenAI(api_key='YOUR_API_KEY')

    def generate_response(self, message: str) -> str:
        # OpenAIを使用してメッセージに対する応答を生成
        response = self.llm(message)
        return response