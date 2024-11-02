// src/components/chat/ChatContainer.tsx
import { Card } from "@/components/ui/card"
import { ScrollArea } from "@/components/ui/scroll-area"
import { ChatInput } from "./ChatInput"
import { ChatMessages } from "./ChatMessages"
import { ChatHeader } from "./ChatHeader"

export function ChatContainer() {
  return (
    <Card className="w-full max-w-2xl mx-auto h-[600px] flex flex-col">
      <ChatHeader />
      <ScrollArea className="flex-1 p-4">
        <ChatMessages />
      </ScrollArea>
      <ChatInput />
    </Card>
  )
}