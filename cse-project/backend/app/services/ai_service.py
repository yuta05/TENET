import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from app.models.chat import Message  # Messageクラスをインポート

# .envファイルから環境変数を読み込む
load_dotenv()
class AIService:
    def __init__(self):
        # 環境変数からOpenAIのAPIキーを取得
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OpenAI API key is not set in the environment variables")
        
        # OpenAIのインスタンスを初期化
        self.llm = OpenAI(api_key=api_key)

        # プロンプトテンプレートの設定
        self.prompt_template = PromptTemplate(
            input_variables=["message"],
            template="You are a helpful assistant. Respond to the following message: {message}"
        )

    async def generate_response(self, message: Message) -> str:
        # プロンプトを生成し、OpenAIを使用して応答を生成
        prompt = self.prompt_template.format(message=message.content)
        response = self.llm(prompt)
        return response