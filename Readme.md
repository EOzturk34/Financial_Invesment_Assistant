Financial Investment Assistant
A smart financial assistant that combines AI-powered RAG (Retrieval Augmented Generation) with TensorFlow models to provide personalized investment recommendations.
Features

🔍 Real-time market data analysis
📊 Personalized risk assessment
🤖 AI-powered investment recommendations
📈 Market trend analysis and predictions
💼 Portfolio management tools

Tech Stack

Frontend: Streamlit
Machine Learning: TensorFlow, Scikit-learn
NLP: Sentence Transformers, LangChain
Data: Pandas, NumPy
Database: ChromaDB for vector storage

Project Structure
Financial_Assistant/
├── data/              # Data collection and processing
├── models/            # ML and AI models
├── rag/               # RAG system implementation
├── ui/                # User interface
└── utils/             # Utility functions
Installation

Clone the repository

bashgit clone https://github.com/EOzturk34/Financial_Invesment_Assistant.git
cd Financial_Assistant

Create virtual environment

bashpython3.11 -m venv venvFinancial
source venvFinancial/bin/activate

Install dependencies

bashpip install -r requirements.txt

Run the application

bashstreamlit run ui/app.py
Usage

Set up your risk profile
Ask financial questions
Get personalized investment recommendations
Track and manage your portfolio