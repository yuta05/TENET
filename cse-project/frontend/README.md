以下は、視覚的に改善されたREADME.mdの例です。

```markdown
# Customer Service Engine (CSE) Frontend

Frontend implementation for the Customer Service Engine using React, TypeScript, and shadcn/ui.

## Table of Contents
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Development](#development)
- [Components](#components)
- [State Management](#state-management)
- [Styling](#styling)
- [Git Workflow](#git-workflow)
- [Build and Deploy](#build-and-deploy)
- [Future Enhancements](#future-enhancements)
- [Troubleshooting](#troubleshooting)

## Project Structure

```
frontend/
├── public/
│   └── assets/
│       ├── bot-avatar.png
│       └── user-avatar.png
├── src/
│   ├── components/
│   │   ├── chat/
│   │   │   ├── ChatContainer.tsx
│   │   │   ├── ChatHeader.tsx
│   │   │   ├── ChatInput.tsx
│   │   │   ├── ChatMessages.tsx
│   │   │   ├── ChatLoading.tsx
│   │   │   └── ChatError.tsx
│   │   └── ui/
│   │       ├── alert.tsx
│   │       ├── avatar.tsx
│   │       ├── button.tsx
│   │       ├── card.tsx
│   │       ├── input.tsx
│   │       └── scroll-area.tsx
│   ├── lib/
│   │   └── utils.ts
│   ├── stores/
│   │   └── chat-store.ts
│   ├── types/
│   │   └── chat.ts
│   ├── App.tsx
│   ├── main.tsx
│   └── index.css
```

## Tech Stack

- **React 18**
- **TypeScript**
- **Vite**
- **Tailwind CSS**
- **shadcn/ui**
- **Zustand**
- **Radix UI**

## Setup

### Prerequisites

- Node.js 18.x or higher
- npm 9.x or higher

### Installation

```sh
# Clone the repository
git clone [repository-url]
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### Environment Variables

Create a `.env` file in the root directory:

```env
VITE_API_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000/ws
```

## Development

### Available Scripts

```sh
# Start development server
npm run dev

# Build for production
npm run build

# Run linter
npm run lint

# Preview production build
npm run preview
```

## Coding Guidelines

- Use TypeScript for type safety
- Follow component-based architecture
- Implement responsive design
- Write clean and documented code
- Follow shadcn/ui design system

## Components

### Chat Components

| Component      | Description            |
| -------------- | ---------------------- |
| ChatContainer  | Main chat container    |
| ChatHeader     | Chat header section    |
| ChatMessages   | Message display area   |
| ChatInput      | Message input section  |
| ChatLoading    | Loading indicator      |
| ChatError      | Error display          |

### UI Components

| Component      | Description            |
| -------------- | ---------------------- |
| Alert          | Notifications and errors |
| Avatar         | User and bot avatars   |
| Button         | Button elements        |
| Card           | Card container         |
| Input          | Input fields           |
| ScrollArea     | Scrollable areas       |

## State Management

Using Zustand for state management:

```ts
interface Message {
  id: string
  content: string
  role: "user" | "assistant"
  timestamp: Date
}

interface ChatStore {
  messages: Message[]
  addMessage: (message: Message) => void
  clearMessages: () => void
}
```

### Usage Example

```ts
import { useChatStore } from '@/stores/chat-store'

const Component = () => {
  const messages = useChatStore((state) => state.messages)
  const addMessage = useChatStore((state) => state.addMessage)
  
  // Use the store
}
```

## Styling

- Using Tailwind CSS for styling
- Custom styles in `index.css`
- Following shadcn/ui design system
- Responsive design patterns

## Git Workflow

### Commit Messages

Use the following prefixes:

- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation updates
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test updates
- `chore`: Maintenance

### Branch Strategy

- `main`: Production branch
- `develop`: Development branch
- `feature/*`: Feature branches
- `fix/*`: Bug fix branches

## Build and Deploy

```sh
# Production build
npm run build

# Preview build
npm run preview
```

## Future Enhancements

- Message read status
- Typing indicators
- File attachments
- Emoji picker
- Message search
- Dark mode support

## Troubleshooting

### Common issues and solutions:

#### Build Errors

- Clear npm cache: `npm cache clean --force`
- Remove `node_modules`: `rm -rf node_modules`
- Reinstall dependencies: `npm install`

#### Development Server Issues

- Check port availability
- Verify environment variables
- Check for conflicting processes
```