// src/components/chat/ChatContainer.tsx
import React, { useState, useEffect } from 'react';
import { Card } from "@/components/ui/card";
import { ScrollArea } from "@/components/ui/scroll-area";
import { ChatInput } from "./ChatInput";
import { ChatMessages } from "./ChatMessages";
import { ChatHeader } from "./ChatHeader";
import { useChatStore } from "@/stores/chat-store";

export function ChatContainer() {
  const [socket, setSocket] = useState<WebSocket | null>(null);
  const addMessage = useChatStore((state) => state.addMessage);

  useEffect(() => {
    // WebSocket接続を初期化
    const ws = new WebSocket('ws://localhost:8000/ws/chat');
    setSocket(ws);

    // 接続が確立されたときの処理
    ws.onopen = () => {
      console.log("WebSocket connection established");
    };

    // エラー発生時の処理
    ws.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    // メッセージ受信時の処理
    ws.onmessage = (event) => {
      addMessage({
        id: Date.now().toString(),
        content: event.data,
        role: "bot",
        timestamp: new Date(),
      });
    };

    // クリーンアップ
    return () => {
      ws.close();
    };
  }, [addMessage]);

  return (
    <Card className="w-full max-w-2xl mx-auto h-[600px] flex flex-col">
      <ChatHeader />
      <ScrollArea className="flex-1 p-4">
        <ChatMessages />
      </ScrollArea>
      <ChatInput socket={socket} />
    </Card>
  );
}