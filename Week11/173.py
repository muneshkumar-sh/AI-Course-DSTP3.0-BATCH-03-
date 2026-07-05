from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2
)

outline_prompt = ChatPromptTemplate.from_template(
    "Create a short outline for a lecture on: {topic}"
)

lecture_prompt = ChatPromptTemplate.from_template(
    "Write a detailed lecture using this outline:\n{outline}"
)

outline_chain = outline_prompt | llm
lecture_chain = lecture_prompt | llm

topic = "LangChain Chains"

outline = outline_chain.invoke({"topic": topic}).content

lecture = lecture_chain.invoke({"outline": outline}).content

print("OUTLINE:\n", outline)
print("\nLECTURE:\n", lecture)