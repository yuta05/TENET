// src/components/chat/ChatMessages.tsx
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { cn } from "@/lib/utils"
import { useChatStore } from "@/stores/chat-store"
import { Message } from "@/types/chat"
import { format } from "date-fns"

export function ChatMessages() {
  const messages = useChatStore((state) => state.messages)

  return (
    <div className="space-y-4">
      {messages.map((message) => (
        <ChatMessage key={message.id} message={message} />
      ))}
    </div>
  )
}

function ChatMessage({ message }: { message: Message }) {
  const isUser = message.role === "user"

  return (
    <div
      className={cn(
        "flex items-start gap-3 text-sm",
        isUser ? "justify-end" : "justify-start"
      )}
    >
      {!isUser && (
        <Avatar className="w-8 h-8">
          <AvatarImage src="/bot-avatar.png" alt="AI" />
          <AvatarFallback>AI</AvatarFallback>
        </Avatar>
      )}

      <div
        className={cn(
          "rounded-lg px-3 py-2 max-w-[80%]",
          isUser
            ? "bg-primary text-primary-foreground"
            : "bg-muted"
        )}
      >
        <p className="whitespace-pre-wrap">{message.content}</p>
        <span className="text-xs opacity-50 mt-1 block">
          {format(message.timestamp, "HH:mm")}
        </span>
      </div>

      {isUser && (
        <Avatar className="w-8 h-8">
          <AvatarImage src="/user-avatar.png" alt="User" />
          <AvatarFallback>Me</AvatarFallback>
        </Avatar>
      )}
    </div>
  )
}