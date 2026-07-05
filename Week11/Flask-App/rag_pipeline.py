# ==========================================================
# rag_pipeline.py
# LangChain + FAISS + Qwen RAG Pipeline
# ==========================================================


# ==========================================================
# Import Required Libraries
# ==========================================================

import torch

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline
)

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFacePipeline

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableLambda,
    RunnablePassthrough
)


# ==========================================================
# Create Sample Document
# ==========================================================

content = """
LangChain is a framework for developing applications powered by language models.

It enables applications that are context-aware and reason across problems.

Key components of LangChain include Models, Prompts, Chains, and Memory.

Chains allow you to combine multiple components together.

Retrieval-Augmented Generation (RAG) is a popular technique used in LangChain.

FAISS is commonly used as a vector database for semantic search.

Embeddings convert text into numerical vectors for similarity search.

Large Language Models (LLMs) use retrieved context to generate accurate responses.
"""


with open("langchain_intro.txt", "w", encoding="utf-8") as f:
    f.write(content)


print("✅ Sample document created.")


# ==========================================================
# Load the Document
# ==========================================================

loader = TextLoader(
    "langchain_intro.txt",
    encoding="utf-8"
)

documents = loader.load()

print(f"Loaded {len(documents)} document(s).")


# ==========================================================
# Split the Document
# ==========================================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    separators=[
        "\n\n",
        "\n",
        " ",
        ""
    ]
)

splits = text_splitter.split_documents(documents)

print(f"Created {len(splits)} chunks.")


for i, chunk in enumerate(splits):

    print("=" * 50)
    print(f"Chunk {i + 1}")
    print(chunk.page_content)


# ==========================================================
# Create Embeddings
# ==========================================================

print("\nLoading embedding model...")

embedding_function = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("✅ Embedding model loaded.")


# ==========================================================
# Create FAISS Vector Database
# ==========================================================

print("Creating FAISS Vector Store...")

db = FAISS.from_documents(
    documents=splits,
    embedding=embedding_function
)

print("✅ FAISS Vector Database Created")
print(f"Stored {len(splits)} document vectors.")



# ==========================================================
# Load Qwen Model
# ==========================================================

model_id = "Qwen/Qwen2-0.5B-Instruct"

print(f"\nLoading model: {model_id}")

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto"
)

print("✅ Qwen model loaded successfully.")


# ==========================================================
# Create Hugging Face Pipeline
# ==========================================================

pipe = pipeline(
    task="text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=128,
    temperature=0.1,
    do_sample=True
)

print("✅ Hugging Face pipeline created.")


# ==========================================================
# Convert Pipeline into LangChain LLM
# ==========================================================

raw_llm = HuggingFacePipeline(
    pipeline=pipe
)


# ==========================================================
# Prompt Formatter
# ==========================================================

def format_for_qwen(input_dict):
    """
    Formats retrieved context and question
    into Qwen chat template.
    """

    messages = [
        {
            "role": "system",
            "content": """
You are a helpful AI assistant.

Answer ONLY from the provided context.

If the answer is not available, reply:

I don't know based on the provided context.
"""
        },
        {
            "role": "user",
            "content": f"""
Context:
{input_dict['context']}

Question:
{input_dict['question']}
"""
        }
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    return prompt


# ==========================================================
# Generate Response
# ==========================================================

def generate_with_qwen(prompt):

    response = raw_llm.invoke(prompt)

    if response.startswith(prompt):
        response = response[len(prompt):]

    return response.strip()


# ==========================================================
# Create LangChain LLM
# ==========================================================

llm = (
    RunnableLambda(format_for_qwen)
    | RunnableLambda(generate_with_qwen)
    | StrOutputParser()
)

print("✅ LangChain LLM Ready")


# ==========================================================
# Create Retriever
# ==========================================================

retriever = db.as_retriever(
    search_kwargs={
        "k": 2
    }
)

print("✅ Retriever Created")


# ==========================================================
# Build RAG Pipeline
# ==========================================================

rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | RunnablePassthrough.assign(
        answer=lambda x: llm.invoke(
            {
                "context": "\n\n".join(
                    [
                        doc.page_content
                        for doc in x["context"]
                    ]
                ),
                "question": x["question"]
            }
        )
    )
)

print("✅ RAG Pipeline Ready")


# ==========================================================
# Test the Pipeline
# ==========================================================

if __name__ == "__main__":

    question = "What is LangChain?"

    result = rag_chain.invoke(question)

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print(result["answer"])