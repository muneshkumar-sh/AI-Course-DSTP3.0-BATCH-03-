from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.memory import ConversationBufferMemory
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)

memory = ConversationBufferMemory(return_messages=True)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a chatbot. Remember the user's preferences."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])


def load_history(_):
    return memory.load_memory_variables({})["history"]


chain = (
    {
        "history": load_history,
        "input": RunnablePassthrough()
    }
    | prompt
    | llm
)

# -----------------------------
# Chat
# -----------------------------

msg1 = "My name is Munesh and I am student at SIBA."

res1 = chain.invoke(msg1)

memory.save_context(
    {"input": msg1},
    {"output": res1.content}
)

print(res1.content)

msg2 = "What do you know about me?"

res2 = chain.invoke(msg2)

memory.save_context(
    {"input": msg2},
    {"output": res2.content}
)

print(res2.content)