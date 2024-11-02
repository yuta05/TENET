// src/components/chat/ChatInput.tsx
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { useChatStore } from "@/stores/chat-store"
import { useState } from "react"
import { SendHorizontal } from "lucide-react"

export function ChatInput() {
  const [input, setInput] = useState("")
  const addMessage = useChatStore((state) => state.addMessage)

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim()) return

    addMessage({
      id: Date.now().toString(),
      content: input,
      role: "user",
      timestamp: new Date(),
    })

    setInput("")
  }

  return (
    <form onSubmit={handleSubmit} className="p-4 border-t">
      <div className="flex gap-2">
        <Input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          className="flex-1"
        />
        <Button type="submit" size="icon">
          <SendHorizontal className="h-4 w-4" />
        </Button>
      </div>
    </form>
  )
}