# RAG Dynamic Chatbot

## Project Overview

This project demonstrates an end-to-end Retrieval-Augmented Generation (RAG) chatbot built using Python, LangChain, Gemini Embeddings, Gemini 2.5 Flash, and Chroma Vector Database.

The chatbot loads PDF documents, cleans and preprocesses the content, creates text chunks, generates embeddings, stores vectors in Chroma, retrieves relevant information using semantic search, and generates context-aware answers using Gemini.

This project was developed as part of my GenAI learning journey to understand the complete RAG architecture and workflow.

---

## Features

* PDF Document Loading
* Document Cleaning and Preprocessing
* Text Chunking using RecursiveCharacterTextSplitter
* Embedding Generation using Gemini Embeddings
* Chroma Vector Database Integration
* Semantic Similarity Search
* Context Retrieval
* Prompt Augmentation
* Answer Generation using Gemini 2.5 Flash
* Dynamic User Query Support

---

## Technologies Used

### Programming Language

* Python

### Libraries & Frameworks

* LangChain
* LangChain Community
* LangChain Chroma
* LangChain Google GenAI
* ChromaDB
* PyPDF

### AI Models

#### Embedding Model

* Gemini Embedding Model (`models/gemini-embedding-001`)

#### Large Language Model

* Gemini 2.5 Flash

---

## RAG Architecture

```text
PDF Document
      │
      ▼
Document Loading
      │
      ▼
Document Cleaning
      │
      ▼
Chunking
      │
      ▼
Embeddings
      │
      ▼
Chroma Vector Database
      │
      ▼
User Query
      │
      ▼
Query Embedding
      │
      ▼
Similarity Search
      │
      ▼
Top Relevant Chunks
      │
      ▼
Context Creation
      │
      ▼
Prompt Augmentation
      │
      ▼
Gemini 2.5 Flash
      │
      ▼
Final Answer
```

---

## How It Works

### Step 1: Load PDF

The chatbot loads PDF documents using `PyPDFLoader`.

### Step 2: Clean Document

Repeated headers and unnecessary text are removed to improve retrieval quality.

### Step 3: Chunking

Documents are split into manageable chunks using:

```python
chunk_size = 500
chunk_overlap = 100
```

### Step 4: Generate Embeddings

Each chunk is converted into a high-dimensional vector representation using Gemini Embeddings.

### Step 5: Create Vector Database

Embeddings are stored in Chroma Vector Database for efficient similarity search.

### Step 6: User Query

The user enters a question.

### Step 7: Retrieval

The query is converted into an embedding and matched against stored vectors.

Top relevant chunks are retrieved.

### Step 8: Context Creation

Retrieved chunks are combined to create contextual information.

### Step 9: Prompt Augmentation

Context and user question are added to a prompt.

### Step 10: Generation

Gemini 2.5 Flash generates a grounded response using retrieved information.

---

## Example Questions

* What is RAG?
* What are Embeddings?
* What is Chunking?
* What is Chroma?
* What is Semantic Search?
* How does Retrieval work?

---

## Sample Output

User Query:

```text
What is RAG?
```

Retrieved Context:

```text
Retrieval-Augmented Generation combines information retrieval with large language models.
```

Generated Answer:

```text
RAG enables language models to access external knowledge sources during inference, improving factual accuracy and reducing hallucinations.
```

---

## Learning Outcomes

Through this project I learned:

* RAG Architecture
* PDF Processing
* Document Cleaning
* Chunking Strategies
* Embeddings
* Vector Databases
* Semantic Search
* Similarity Search
* Retrieval-Augmented Generation
* LangChain Fundamentals
* Chroma Vector Store
* Prompt Engineering
* Gemini Integration

---

## Future Improvements

* Multi-PDF Support
* Multi-Source RAG
* Website Integration
* Excel and CSV Integration
* Metadata-Based Retrieval
* Conversational Memory
* FastAPI Integration
* LangGraph Integration
* Docker Deployment
* Azure Deployment
* Streamlit User Interface

---

## Author

**Pankaj Kumar Das**

Aspiring GenAI Engineer | NLP | RAG | Prompt Engineering | Python | AI Data Operations

GitHub:
https://github.com/pankajKxyz2018
