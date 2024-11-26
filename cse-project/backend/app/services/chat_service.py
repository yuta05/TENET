from app.services.ai_service import AIService
from datetime import datetime
from app.services.cs_agents.agent import part_4_graph
from langchain_core.messages import ToolMessage, SystemMessage, HumanMessage, AIMessage
from app.models.chat import Message
import asyncio
import uuid
from fastapi import WebSocket

class ChatService:
    def __init__(self, connection_manager):
        self.ai_service = AIService()
        self.connection_manager = connection_manager
        self.messages = []
        self.thread_id = str(uuid.uuid4())
        self.config = {
            "configurable": {
                "passenger_id": "3442 587242",
                "thread_id": self.thread_id,
            }
        }
        self._printed = set()

    async def process_message(self, message_content: str, websocket: WebSocket):
        # Initialize a new state for each session
        state = {
            "messages": [],
            "user_info": None,
        }
        message = Message(id=str(uuid.uuid4()), content=message_content, role="user", timestamp=datetime.now())
        state["messages"].append(message)
        
        # Handle interrupts
        response = await self._generate_response_with_interrupts(state, websocket)
        return response
    
    async def _generate_response_with_interrupts(self, state, websocket: WebSocket):
        response = await self.ai_service.generate_response(state, self.config, self._printed)
        
        # Handle interrupts
        response = await self.check_for_interrupts_and_handle_approvals(state, response, websocket)
        
        return response if response else None

    async def check_for_interrupts_and_handle_approvals(self, state, response, websocket: WebSocket):
        snapshot = part_4_graph.get_state(self.config)
        while snapshot.next:
            # Send a message to the user asking for approval
            approval_message = Message(id=str(uuid.uuid4()), content="Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changes.", role="system", timestamp=datetime.now())
            state["messages"].append(approval_message)
            
            # Output the approval message to the chat
            await self.output_message(approval_message, websocket)
            
            # Wait for the user's response
            user_input = await self._wait_for_user_input(websocket)
            
            if user_input.strip().lower() == 'y':
                # Just continue
                result = part_4_graph.invoke(None, self.config)
            else:
                # Satisfy the tool invocation by providing instructions on the requested changes / change of mind
                last_message = snapshot.values['messages'][-1]
                tool_call_id = last_message.tool_calls[0]["id"] if last_message.tool_calls else None
                result = part_4_graph.invoke(
                    {
                        "messages": [
                            ToolMessage(
                                tool_call_id=tool_call_id,
                                content=f"API call denied by user. Reasoning: '{user_input}'. Continue assisting, accounting for the user's input.",
                            )
                        ]
                    },
                    self.config,
                )
            # 出力メッセージを生成
            output_message = self.format_result_message(result)
            print('output_message', output_message)
            if output_message:  # 空のメッセージを送信しないようにする
                await self.output_message(Message(id=str(uuid.uuid4()), content=output_message, role="system", timestamp=datetime.now()), websocket)
            snapshot = part_4_graph.get_state(self.config)
        
            break
        
        print('response', response)
        return response if response else None

    async def _wait_for_user_input(self, websocket: WebSocket):
        # This method waits for the user's response via the chat service
        while True:
            try:
                message = await websocket.receive_text()
                return message
            except asyncio.CancelledError:
                # Handle the cancellation of the task
                print("Task was cancelled")
                return None
            except:
                await asyncio.sleep(1)

    async def output_message(self, message, websocket: WebSocket):
        # This method outputs a message to the chat via WebSocket
        await self.connection_manager.send_personal_message(message.content, websocket)

    def format_result_message(self, result):
        # 結果メッセージをフォーマット
        ai_message = result['messages'][-1]
        return ai_message.content if ai_message.content else None

def handle_tool_error(state) -> dict:
    error = state.get("error")
    tool_calls = state["messages"][-1].tool_calls
    return {
        "messages": [
            ToolMessage(
                content=f"Error: {repr(error)}\n please fix your mistakes.",
                tool_call_id=tc["id"],
            )
            for tc in tool_calls
        ]
    }