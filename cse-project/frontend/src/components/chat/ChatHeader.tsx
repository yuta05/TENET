// src/components/chat/ChatHeader.tsx
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"

export function ChatHeader() {
  return (
    <div className="flex items-center space-x-4 p-4 border-b">
      <Avatar>
        <AvatarImage src="/bot-avatar.png" alt="AI Assistant" />
        <AvatarFallback>AI</AvatarFallback>
      </Avatar>
      <div>
        <h2 className="font-semibold">AI Assistant</h2>
        <p className="text-sm text-muted-foreground">Always here to help</p>
      </div>
    </div>
  )
}