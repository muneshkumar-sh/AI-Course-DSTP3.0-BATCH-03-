from langchain_groq import ChatGroq
from langchain_classic.memory import ConversationSummaryMemory
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2
)

summary_memory = ConversationSummaryMemory(llm=llm)


def chat(user_text):
    history = summary_memory.load_memory_variables({}).get("history", "")

    prompt = f"""
You are a helpful assistant.
Conversation summary so far:
{history}

User: {user_text}
Assistant:
"""

    response = llm.invoke(prompt).content

    summary_memory.save_context(
        {"input": user_text},
        {"output": response}
    )

    return response


print(chat("My name is Munesh Kumar. I am student at sukkur IBA University, currently in 3rd year."))
print(chat("I also learn ML & DL from Digiskills."))
print(chat("What should you remember about me?"))