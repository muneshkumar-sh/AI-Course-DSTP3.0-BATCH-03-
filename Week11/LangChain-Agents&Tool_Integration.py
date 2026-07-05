import requests
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent

load_dotenv()


@tool
def get_random_joke(query: str) -> str:
    """Fetches a random programming joke from an API."""

    url = "https://official-joke-api.appspot.com/jokes/programming/random"
    data = requests.get(url, timeout=20).json()

    joke = data[0]

    return f"{joke['setup']} --- {joke['punchline']}"


model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)

tools = [get_random_joke]

agent = create_agent(
    model=model,
    tools=tools
)

result = agent.invoke(
    {
        "messages": [
            HumanMessage(
                content="Tell me a programming joke using the tool."
            )
        ]
    }
)

print(result["messages"][-1].content)