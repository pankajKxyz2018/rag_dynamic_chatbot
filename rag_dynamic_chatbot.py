# ==========================================
# COMPLETE RAG APPLICATION: BUILDING DYNAMIC CHATBOAT
# ==========================================
print("Starting Program")
# ==========================================
# STEP 1 Importing of libraries
# ==========================================
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)
from langchain_chroma import Chroma

import os

GOOGLE_API_KEY = os. getenv("GOOGLE_API_KEY")

# ==========================================
# STEP 2 LOAD PDF
# ==========================================

loader = PyPDFLoader("sample.pdf")
documents = loader.load()

print("PDF Loaded")
print("Pages: ", len(documents))

# ==========================================
# STEP 2 : CLEAN REPEATED HEADER
# ==========================================

for doc in documents:
    doc.page_content = doc.page_content.replace(
        "AI Basics\n", ""
    )
    
    doc.page_content = doc.page_content.replace(
        "RAG stands for Retrieval Augmented Generation.\n", ""
    )

    doc.page_content = doc.page_content.replace(
        "Embeddings convert text into vectors.\n", ""
    )

    doc.page_content = doc.page_content.replace(
        "Chroma is a vector database.\n", ""
    )

print("PDF Cleaned")
print(documents[:3])

# ==========================================
# STEP 4 : CHUNKING
# ==========================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 100
)

chunks = splitter.split_documents(documents)

print("Chunks Created: ", len(chunks))

# ==========================================
# STEP 5 : EMBEDDINGS
# ==========================================

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key="GOOGLE_API_KEY"
)

print("Embeddings Object Created")

# ==========================================
# STEP 6 : VECTOR DATABASE
# ==========================================

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings
)

print("Vector Store Created")

# ==========================================
# STEP 7 : USER QUESTION
# ==========================================

question = input("Enter your query: ")

# ==========================================
# STEP 8 : RETRIEVAL
# ==========================================

results = vectorstore.similarity_search(
    question,
    k=3
)

print("\nTop Retrieved Chunks:\n")

for i, doc in enumerate(results):
    print(f"\n----- RESULT {i+1} -----")
    print(doc.page_content)

# ==========================================
# STEP 9 : CREATE CONTEXT
# ==========================================

context = ""

for doc in results:
    context += doc.page_content + "\n\n"

# ==========================================
# STEP 10 : GEMINI LLM
# ==========================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key="GOOGLE_API_KEY"
)

print("\nLLM Created")

# ==========================================
# STEP 11 : BUILD PROMPT
# ==========================================

prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

Answer:
"""

# ==========================================
# STEP 12 : GENERATION
# ==========================================

response = llm.invoke(prompt)

print("\n========================")
print("FINAL ANSWER")
print("========================\n")

print(response.content)