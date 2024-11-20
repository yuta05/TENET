from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from app.models.chat import Message  # Messageクラスをインポート
from app.core.config import settings  # settingsをインポート
from app.services.graph import part_3_graph  # Import part_3_graph from graph.py
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import uuid

# .envファイルから環境変数を読み込む
load_dotenv()

def convert_message_to_supported_type(message: Message):
    if message.role == "user":
        return HumanMessage(content=message.content, id=str(uuid.uuid4()))
    elif message.role == "assistant":
        return AIMessage(content=message.content, id=str(uuid.uuid4()))
    elif message.role == "system":
        return SystemMessage(content=message.content, id=str(uuid.uuid4()))
    else:
        raise NotImplementedError(f"Unsupported message role: {message.role}")

def convert_messages_to_supported_types(messages: list[Message]):
    return [convert_message_to_supported_type(msg) for msg in messages]

class AIService:
    def __init__(self):
        # 環境変数からOpenAIのAPIキーを取得
        api_key = settings.OPENAI_API_KEY
        if not api_key:
            raise ValueError("OpenAI API key is not set in the environment variables")
        
        # OpenAIのスタンスを初期化
        self.llm = OpenAI(api_key=api_key)

        # プロンプトテンプレートの設定
        self.prompt_template = PromptTemplate(
            input_variables=["message"],
            template="You are a helpful assistant. Respond to the following message: {message}"
        )

    async def generate_response(self, state: dict, config: dict, _printed: set) -> str:
            # Convert messages to supported types
            state["messages"] = convert_messages_to_supported_types(state["messages"])
            
                    # デバッグ用の出力を追加
            print("Converted messages:")
            for i, msg in enumerate(state["messages"], start=1):
                print(f"{i}: {msg} (type: {type(msg).__name__})")

            # part_3_graphを使用して応答を生成
            events = part_3_graph.stream(
                state, config, stream_mode="values"
            )
            responses = []
            seen_messages = set()
            for event in events:
                event["messages"][-1].pretty_print()
                for msg in event.get("messages", []):
                    if isinstance(msg, AIMessage) and hasattr(msg, "content"):
                        if msg.content not in seen_messages and msg.content not in _printed:
                            seen_messages.add(msg.content)
                            responses.append(msg.content)
                            _printed.add(msg.content)
            return "\n".join(responses)
