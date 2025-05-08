# Financial Investment Assistant

A smart financial assistant that combines AI-powered RAG (Retrieval Augmented Generation) with real-time market data to provide personalized investment recommendations.

## Features

🔍 Real-time market data from multiple sources
📊 Stock price tracking and historical data
🤖 AI-powered investment recommendations (coming soon)
📈 Market trend analysis (coming soon)
💼 Portfolio management tools (coming soon)

## Tech Stack

- **Data Collection**: 
  - Alpha Vantage API
  - Yahoo Finance API
  - Finnhub API
- **Data Processing**: Pandas, NumPy
- **Frontend**: Streamlit (in progress)
- **AI/ML**: TensorFlow, Scikit-learn (coming soon)
- **NLP**: Sentence Transformers, LangChain (coming soon)
- **Database**: ChromaDB for vector storage (coming soon)

## Installation

1. Clone the repository
```bash
git clone https://github.com/EOzturk34/Financial_Invesment_Assistant.git
cd Financial_Assistant
```

2. Create virtual environment
```bash
python3.11 -m venv venvFinancial
source venvFinancial/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up API keys
Create a `config.py` file in the root directory with your API keys:
```python
ALPHA_VANTAGE_API_KEY = "your_alpha_vantage_key"
FINNHUB_API_KEY = "your_finnhub_key"
```
⚠️ Never commit your `config.py` file to version control!

## Usage

### Testing Data Loaders
```bash
python data/loaders/stock_loader.py
```
This will fetch current stock prices from all configured data sources.

### Available Data Sources
- Alpha Vantage
- Yahoo Finance
- Finnhub

### Supported Operations
- Get current stock prices
- Get historical stock data with different intervals:
  - Daily
  - Weekly
  - Monthly

## Current Status
- ✅ Data loaders implemented and working
- 🚧 Streamlit interface in development
- ⏳ AI/ML features coming soon
- ⏳ RAG system coming soon
- ⏳ Portfolio management coming soon

