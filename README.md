# Intelligent Complaint Analysis for Financial Services (RAG-Powered Chatbot)

This project is part of **10 Academy - KAIM Week 6 Challenge**, aimed at building an **AI-powered complaint analysis chatbot** for **CrediTrust Financial** using **Retrieval-Augmented Generation (RAG)**.

The system helps internal teams quickly understand customer pain points across five major financial products by transforming raw complaint narratives into actionable insights.

## 🚀 Business Objective

CrediTrust receives thousands of customer complaints monthly. The goal is to:

- Reduce the time it takes to identify key complaint trends.
- Empower non-technical teams to get answers without data specialists.
- Enable proactive issue resolution based on real-time feedback.

## 🏗 Project Overview

The project involves:

1. **Exploratory Data Analysis (EDA) & Preprocessing**
2. **Text Chunking, Embedding & Vector Store Indexing**
3. **RAG Pipeline Development & Evaluation**
4. **Interactive Chatbot Interface with Gradio/Streamlit**

## 📊 Data

The system uses **Consumer Financial Protection Bureau (CFPB)** complaint data:

- Products: Credit Cards, Personal Loans, BNPL, Savings Accounts, Money Transfers
- Complaint Narratives as core input

## 🗂 Folder Structure

financial-complaint-rag/
├── data/ # Filtered dataset
├── notebooks/ # Jupyter Notebooks for EDA & Preprocessing
├── src/
│ ├── chunking.py
│ ├── embedding.py
│ └── rag_pipeline.py
├── vector_store/ # FAISS or ChromaDB storage
├── app.py # Streamlit or Gradio app
├── requirements.txt
├── README.md
└── .gitignore

## ⚙️ Setup Instructions

1. Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/financial-complaint-rag.git
cd financial-complaint-rag
```

2. Create virtual environment and activate:

```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Download dataset and place it inside `/data` folder.

## 📌 Key Technologies

- **Python**
- **Pandas, Numpy, Matplotlib, Seaborn**
- **LangChain, FAISS/ChromaDB**
- **Sentence Transformers**
- **Gradio or Streamlit**
- **OpenAI/Hugging Face LLMs**

---

## 📅 Project Timeline

| Day   | Milestone                                |
| ----- | ---------------------------------------- |
| Day 1 | EDA, Preprocessing, Embedding & Indexing |
| Day 2 | Build RAG Pipeline + Initial Evaluation  |
| Day 3 | Build UI + Final Report + Submission     |

---

- Project by: **MMW**

---
