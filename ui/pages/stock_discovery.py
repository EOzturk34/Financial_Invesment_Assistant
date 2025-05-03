# ui/pages/stock_discovery.py - Stock discovery page
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

def show_stock_discovery():
    """Display the stock discovery page"""
    st.header("🔎 Stock Discovery")
    
    # Search and filter section
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        search_query = st.text_input("Search stocks by name or symbol", placeholder="e.g., AAPL, Tesla")
    
    with col2:
        sector_filter = st.selectbox(
            "Filter by sector",
            ["All", "Technology", "Healthcare", "Finance", "Consumer Goods", "Energy", "Manufacturing"]
        )
    
    with col3:
        risk_level = st.selectbox(
            "Filter by risk level",
            ["All", "Low", "Medium", "High"]
        )
    
    # Main content area with tabs
    tab1, tab2, tab3 = st.tabs(["📊 Recommended Stocks", "🎯 Match with Your Profile", "📈 Market Overview"])
    
    with tab1:
        st.subheader("Recommended Stocks")
        
        # Sample stock data (replace with real data later)
        stock_data = pd.DataFrame({
            'Symbol': ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META'],
            'Company': ['Apple Inc.', 'Microsoft Corp.', 'Alphabet Inc.', 'Amazon.com Inc.', 'Meta Platforms'],
            'Price': [178.25, 338.11, 2819.89, 175.75, 321.22],
            'Change': ['+1.2%', '+0.8%', '-0.5%', '+1.8%', '+2.1%'],
            'Sector': ['Technology', 'Technology', 'Technology', 'Consumer Goods', 'Technology'],
            'Risk': ['Medium', 'Medium', 'Medium', 'Medium', 'High']
        })
        
        # Apply filters
        filtered_stocks = stock_data.copy()
        if sector_filter != "All":
            filtered_stocks = filtered_stocks[filtered_stocks['Sector'] == sector_filter]
        if risk_level != "All":
            filtered_stocks = filtered_stocks[filtered_stocks['Risk'] == risk_level]
        
        # Display stock cards
        for idx, stock in filtered_stocks.iterrows():
            with st.container():
                col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
                
                with col1:
                    st.markdown(f"**{stock['Symbol']}** - {stock['Company']}")
                    st.caption(f"Sector: {stock['Sector']}")
                
                with col2:
                    st.metric("Price", f"${stock['Price']}", stock['Change'])
                
                with col3:
                    risk_color = {"Low": "green", "Medium": "orange", "High": "red"}[stock['Risk']]
                    st.markdown(f"Risk: <span style='color: {risk_color}'>{stock['Risk']}</span>", unsafe_allow_html=True)
                
                with col4:
                    if st.button("View Details", key=f"btn_{stock['Symbol']}"):
                        st.session_state.selected_stock = stock['Symbol']
                        st.experimental_rerun()
                
                st.divider()
        
        # Detailed view for selected stock
        if hasattr(st.session_state, 'selected_stock'):
            show_stock_details(st.session_state.selected_stock)
    
    with tab2:
        st.subheader("Stocks That Match Your Profile")
        
        if st.session_state.user_profile['risk_profile'] in st.session_state.user_profile:
            risk_profile = st.session_state.user_profile['risk_profile']
            
            st.markdown(f"Based on your **{risk_profile}** risk profile:")
            
            # Generate recommendations based on risk profile
            matched_stocks = generate_profile_matched_stocks(risk_profile)
            
            for stock in matched_stocks:
                st.markdown(f"- **{stock['name']}** ({stock['symbol']}) - {stock['reason']}")
        else:
            st.info("Please complete your risk profile first to see personalized recommendations.")
            if st.button("Go to Profile", use_container_width=True):
                st.session_state.current_page = "Profile"
                st.experimental_rerun()
    
    with tab3:
        st.subheader("Market Overview")
        
        # Market indices display
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("S&P 500", "5,872", "+1.2%")
        with col2:
            st.metric("NASDAQ", "19,372", "+0.8%")
        with col3:
            st.metric("DOW", "39,432", "+0.5%")
        with col4:
            st.metric("VIX", "12.45", "-0.3%")
        
        # Market heatmap (placeholder)
        st.subheader("Sector Performance")
        create_sector_heatmap()
        
        # Market news (placeholder)
        st.subheader("Market News")
        show_market_news()

def show_stock_details(symbol):
    """Show detailed information for a specific stock"""
    st.header(f"📈 {symbol} - Stock Details")
    
    # Create sample stock chart
    dates = pd.date_range(start='2023-11-01', end='2024-05-03', freq='B')
    prices = generate_sample_price_data(symbol, dates)
    
    fig = go.Figure(data=[go.Candlestick(x=dates,
                open=prices['Open'],
                high=prices['High'],
                low=prices['Low'],
                close=prices['Close'])])
    
    fig.update_layout(
        title=f'{symbol} Price Chart',
        yaxis_title='Price (USD)',
        xaxis_title='Date',
        xaxis_rangeslider_visible=False,
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Stock details
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Key Metrics")
        st.metric("Market Cap", "$2.8T")
        st.metric("P/E Ratio", "28.5")
        st.metric("EPS", "$6.16")
        st.metric("Dividend Yield", "0.55%")
    
    with col2:
        st.subheader("Technical Indicators")
        st.metric("RSI (14)", "65.7")
        st.metric("MACD", "1.23")
        st.metric("50-day MA", "$175.32")
        st.metric("200-day MA", "$168.45")
    
    with col3:
        st.subheader("Analyst Ratings")
        st.metric("Target Price", "$195.00")
        st.markdown("**Consensus:** Hold")
        st.markdown("🟢 Buy: 12")
        st.markdown("🟡 Hold: 18")
        st.markdown("🔴 Sell: 3")
    
    # AI Analysis (placeholder)
    st.subheader("🤖 AI Analysis")
    st.info("""
    Based on current market conditions and technical analysis, this stock shows:
    - Strong momentum in the past 30 days
    - Support levels holding well at $170-175 range
    - Positive sentiment from recent earnings report
    - Consider entry points near support levels for long-term positions
    """)
    
    if st.button("Back to Discovery", use_container_width=True):
        del st.session_state.selected_stock
        st.experimental_rerun()

def generate_sample_price_data(symbol, dates):
    """Generate sample price data for visualization"""
    import numpy as np
    
    # Base prices for different stocks
    base_prices = {'AAPL': 178, 'MSFT': 338, 'GOOGL': 2820, 'AMZN': 176, 'META': 321}
    base_price = base_prices.get(symbol, 100)
    
    # Generate random walk for prices
    np.random.seed(42)  # For reproducibility
    returns = np.random.randn(len(dates)) * 0.01 + 0.0002
    price_series = base_price * np.exp(np.cumsum(returns))
    
    # Create OHLC data
    ohlc_data = pd.DataFrame(index=dates)
    ohlc_data['Close'] = price_series
    ohlc_data['Open'] = ohlc_data['Close'].shift(1) * (1 + np.random.randn(len(dates)) * 0.002)
    ohlc_data['High'] = ohlc_data[['Open', 'Close']].max(axis=1) * (1 + np.abs(np.random.randn(len(dates))) * 0.01)
    ohlc_data['Low'] = ohlc_data[['Open', 'Close']].min(axis=1) * (1 - np.abs(np.random.randn(len(dates))) * 0.01)
    
    return ohlc_data

def generate_profile_matched_stocks(risk_profile):
    """Generate stock recommendations based on risk profile"""
    stock_recommendations = {
        "Very Conservative": [
            {"name": "Johnson & Johnson", "symbol": "JNJ", "reason": "Healthcare leader with stable dividends"},
            {"name": "Procter & Gamble", "symbol": "PG", "reason": "Consumer staples with consistent growth"},
            {"name": "Coca-Cola", "symbol": "KO", "reason": "Strong moat and reliable income"}
        ],
        "Conservative": [
            {"name": "Microsoft", "symbol": "MSFT", "reason": "Tech leader with strong fundamentals"},
            {"name": "Apple", "symbol": "AAPL", "reason": "Stable cash flows and innovation"},
            {"name": "Visa", "symbol": "V", "reason": "Growing payment network"}
        ],
        "Moderate": [
            {"name": "Amazon", "symbol": "AMZN", "reason": "Growth potential in cloud and retail"},
            {"name": "Alphabet", "symbol": "GOOGL", "reason": "Dominant in search and emerging AI"},
            {"name": "Meta", "symbol": "META", "reason": "Social media leader with metaverse potential"}
        ],
        "Aggressive": [
            {"name": "NVIDIA", "symbol": "NVDA", "reason": "AI chip leader with growth potential"},
            {"name": "Tesla", "symbol": "TSLA", "reason": "EV market leader and energy innovator"},
            {"name": "Palantir", "symbol": "PLTR", "reason": "AI and data analytics growth story"}
        ],
        "Very Aggressive": [
            {"name": "Advanced Micro Devices", "symbol": "AMD", "reason": "AI and processor market challenger"},
            {"name": "MicroStrategy", "symbol": "MSTR", "reason": "Bitcoin treasury strategy"},
            {"name": "Roblox", "symbol": "RBLX", "reason": "Metaverse and gaming platform"}
        ]
    }
    
    return stock_recommendations.get(risk_profile, stock_recommendations["Moderate"])

def create_sector_heatmap():
    """Create a sector performance heatmap"""
    sectors = ['Technology', 'Healthcare', 'Finance', 'Consumer Goods', 'Energy', 'Manufacturing', 'Real Estate', 'Utilities']
    performance = [2.1, 1.5, 0.8, -0.3, -1.2, 0.5, 1.8, 0.3]
    
    fig = go.Figure(data=go.Heatmap(
        z=[performance],
        x=sectors,
        y=['Performance (%)'],
        colorscale='RdYlGn',
        showscale=True
    ))
    
    fig.update_layout(
        title='Sector Performance Today',
        height=300
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_market_news():
    """Display market news feed"""
    news_items = [
        {
            "title": "Fed Maintains Interest Rates at 5.25%",
            "source": "Reuters",
            "time": "2 hours ago",
            "summary": "Federal Reserve keeps rates unchanged, signals data-dependent approach to future decisions."
        },
        {
            "title": "Tech Giants Report Better-than-Expected Earnings",
            "source": "CNBC",
            "time": "4 hours ago",
            "summary": "Apple, Microsoft, and Google exceed earnings forecasts, driving tech sector rally."
        },
        {
            "title": "Global Markets React to Economic Data",
            "source": "Bloomberg",
            "time": "6 hours ago",
            "summary": "Asian markets climb on positive economic indicators from China and Japan."
        }
    ]
    
    for news in news_items:
        with st.container():
            st.markdown(f"**{news['title']}**")
            st.caption(f"{news['source']} • {news['time']}")
            st.markdown(news['summary'])
            st.divider()