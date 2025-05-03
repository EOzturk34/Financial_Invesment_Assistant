# ui/pages/portfolio.py - Portfolio tracking page
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

def show_portfolio():
   """Display the portfolio tracking page"""
   st.header("💼 Portfolio Management")
   
   # Portfolio tabs
   tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "📈 Holdings", "📋 Watchlist", "⚡ Rebalancing"])
   
   with tab1:
       portfolio_overview()
   
   with tab2:
       portfolio_holdings()
   
   with tab3:
       portfolio_watchlist()
   
   with tab4:
       portfolio_rebalancing()

def portfolio_overview():
   """Display portfolio overview and performance"""
   st.subheader("Portfolio Overview")
   
   # Portfolio metrics
   col1, col2, col3, col4 = st.columns(4)
   
   with col1:
       st.metric("Portfolio Value", "$125,750", "+$5,840 (4.9%)")
   with col2:
       st.metric("Day's Gain/Loss", "+$1,420", "+1.14%")
   with col3:
       st.metric("Total Gain/Loss", "+$15,230", "+13.8%")
   with col4:
       st.metric("Dividend Income", "$1,240", "+12.5%")
   
   # Portfolio performance chart
   st.subheader("Portfolio Performance")
   
   # Generate sample portfolio data
   dates = pd.date_range(start='2023-01-01', end='2024-05-03', freq='D')
   portfolio_value = generate_portfolio_data(dates)
   
   fig = go.Figure()
   
   # Portfolio line
   fig.add_trace(go.Scatter(
       x=dates,
       y=portfolio_value,
       name='Portfolio',
       line=dict(color='#2E86C1', width=3)
   ))
   
   # S&P 500 comparison
   sp500_value = portfolio_value * (0.85 + 0.03 * (dates - dates[0]).days / 365)
   fig.add_trace(go.Scatter(
       x=dates,
       y=sp500_value,
       name='S&P 500',
       line=dict(color='#E74C3C', width=2, dash='dash')
   ))
   
   fig.update_layout(
       title='Portfolio Performance vs S&P 500',
       xaxis_title='Date',
       yaxis_title='Value ($)',
       height=500,
       hovermode='x unified'
   )
   
   st.plotly_chart(fig, use_container_width=True)
   
   # Asset allocation pie chart
   col1, col2 = st.columns(2)
   
   with col1:
       st.subheader("Asset Allocation")
       allocation_data = pd.DataFrame({
           'Asset': ['Stocks', 'Bonds', 'Cash', 'Commodities'],
           'Value': [75200, 30100, 15450, 5000],
           'Percentage': [60, 24, 12, 4]
       })
       
       fig_pie = go.Figure(data=[go.Pie(
           labels=allocation_data['Asset'],
           values=allocation_data['Percentage'],
           hole=.4,
           textposition='inside',
           textinfo='label+percent'
       )])
       
       fig_pie.update_layout(height=400)
       st.plotly_chart(fig_pie, use_container_width=True)
   
   with col2:
       st.subheader("Sector Allocation")
       sector_data = pd.DataFrame({
           'Sector': ['Technology', 'Healthcare', 'Finance', 'Consumer', 'Others'],
           'Percentage': [35, 20, 15, 15, 15]
       })
       
       fig_sector = go.Figure(data=[go.Pie(
           labels=sector_data['Sector'],
           values=sector_data['Percentage'],
           hole=.4,
           textposition='inside',
           textinfo='label+percent'
       )])
       
       fig_sector.update_layout(height=400)
       st.plotly_chart(fig_sector, use_container_width=True)

def portfolio_holdings():
   """Display detailed portfolio holdings"""
   st.subheader("Current Holdings")
   
   # Holdings data
   holdings_data = pd.DataFrame({
       'Symbol': ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'JNJ', 'BRK.B', 'V', 'LLY', 'TSLA'],
       'Company': ['Apple Inc.', 'Microsoft Corp.', 'Alphabet Inc.', 'Amazon.com Inc.', 
                   'Meta Platforms', 'Johnson & Johnson', 'Berkshire Hathaway', 'Visa Inc.',
                   'Eli Lilly', 'Tesla Inc.'],
       'Shares': [50, 25, 5, 30, 20, 40, 25, 35, 15, 10],
       'Avg Cost': [145.50, 280.25, 2450.00, 145.80, 280.50, 155.25, 480.75, 240.30, 480.90, 250.00],
       'Current Price': [178.25, 338.11, 2819.89, 175.75, 321.22, 160.45, 525.80, 268.50, 532.75, 245.60],
       'Market Value': [8912.50, 8452.75, 14099.45, 5272.50, 6424.40, 6418.00, 13145.00, 9397.50, 7991.25, 2456.00],
       'Gain/Loss ($)': [1637.50, 1446.50, 1849.45, 898.50, 814.40, 208.00, 1126.25, 987.00, 778.75, -44.00],
       'Gain/Loss (%)': [22.5, 20.7, 15.1, 20.5, 14.5, 3.4, 9.3, 11.7, 14.4, -1.7]
   })
   
   # Search and filter
   col1, col2 = st.columns([3, 1])
   with col1:
       search_term = st.text_input("Search holdings", placeholder="Search by symbol or company name")
   with col2:
       sort_by = st.selectbox("Sort by", ["Current Value", "Gain/Loss %", "Gain/Loss $", "Symbol"])
   
   # Apply search filter
   if search_term:
       mask = (holdings_data['Symbol'].str.contains(search_term, case=False) | 
               holdings_data['Company'].str.contains(search_term, case=False))
       holdings_data = holdings_data[mask]
   
   # Sort data
   if sort_by == "Current Value":
       holdings_data = holdings_data.sort_values('Market Value', ascending=False)
   elif sort_by == "Gain/Loss %":
       holdings_data = holdings_data.sort_values('Gain/Loss (%)', ascending=False)
   elif sort_by == "Gain/Loss $":
       holdings_data = holdings_data.sort_values('Gain/Loss ($)', ascending=False)
   else:
       holdings_data = holdings_data.sort_values('Symbol')
   
   # Display holdings
   for idx, holding in holdings_data.iterrows():
       with st.container():
           col1, col2, col3, col4, col5, col6 = st.columns([1.5, 2, 1, 1.5, 1.5, 1])
           
           with col1:
               st.markdown(f"**{holding['Symbol']}**")
               st.caption(holding['Company'])
           
           with col2:
               st.markdown(f"Shares: {holding['Shares']}")
               st.caption(f"Avg Cost: ${holding['Avg Cost']:.2f}")
           
           with col3:
               change_color = "green" if holding['Gain/Loss (%)'] > 0 else "red"
               st.metric("Current", f"${holding['Current Price']:.2f}")
           
           with col4:
               st.metric("Market Value", f"${holding['Market Value']:,.2f}")
           
           with col5:
               gain_loss_color = "green" if holding['Gain/Loss ($)'] > 0 else "red"
               st.markdown(f"<h4 style='color: {gain_loss_color}'>${holding['Gain/Loss ($)']:,.2f}</h4>", unsafe_allow_html=True)
               st.markdown(f"<p style='color: {gain_loss_color}'>{holding['Gain/Loss (%)']:.1f}%</p>", unsafe_allow_html=True)
           
           with col6:
               if st.button("📈", key=f"chart_{holding['Symbol']}", help="View Chart"):
                   show_stock_chart(holding['Symbol'])
               if st.button("📝", key=f"edit_{holding['Symbol']}", help="Edit Position"):
                   edit_position(holding['Symbol'])
           
           st.divider()
   
   # Performance summary
   st.subheader("Holdings Performance Summary")
   col1, col2, col3 = st.columns(3)
   
   with col1:
       st.metric("Total Invested", f"${holdings_data['Avg Cost'].sum() * holdings_data['Shares'].sum():.2f}")
   with col2:
       st.metric("Current Value", f"${holdings_data['Market Value'].sum():.2f}")
   with col3:
       total_gain = holdings_data['Gain/Loss ($)'].sum()
       total_gain_pct = (total_gain / (holdings_data['Avg Cost'].sum() * holdings_data['Shares'].sum())) * 100
       st.metric("Total Gain/Loss", f"${total_gain:.2f}", f"{total_gain_pct:.1f}%")

def portfolio_watchlist():
   """Display and manage watchlist"""
   st.subheader("Watchlist")
   
   # Add to watchlist
   col1, col2 = st.columns([2, 1])
   with col1:
       new_symbol = st.text_input("Add to watchlist", placeholder="Enter stock symbol")
   with col2:
       if st.button("Add", use_container_width=True):
           if 'watchlist' not in st.session_state:
               st.session_state.watchlist = []
           if new_symbol and new_symbol not in st.session_state.watchlist:
               st.session_state.watchlist.append(new_symbol.upper())
               st.success(f"Added {new_symbol.upper()} to watchlist")
   
   # Display watchlist
   if 'watchlist' in st.session_state and st.session_state.watchlist:
       watchlist_data = generate_watchlist_data(st.session_state.watchlist)
       
       for idx, stock in watchlist_data.iterrows():
           with st.container():
               col1, col2, col3, col4, col5 = st.columns([1.5, 1.5, 1.5, 1, 1])
               
               with col1:
                   st.markdown(f"**{stock['Symbol']}**")
                   st.caption(stock['Company'])
               
               with col2:
                   st.metric("Price", f"${stock['Price']:.2f}", stock['Change'])
               
               with col3:
                   st.metric("Volume", f"{stock['Volume']:,}")
               
               with col4:
                   st.metric("Market Cap", stock['Market Cap'])
               
               with col5:
                   if st.button("Remove", key=f"remove_{stock['Symbol']}"):
                       st.session_state.watchlist.remove(stock['Symbol'])
                       st.experimental_rerun()
               
               st.divider()
               
       # Watchlist alerts
       st.subheader("Price Alerts")
       col1, col2, col3 = st.columns(3)
       
       with col1:
           alert_symbol = st.selectbox("Symbol", st.session_state.watchlist)
       with col2:
           alert_type = st.selectbox("Alert Type", ["Price Above", "Price Below", "Volume > 2x avg"])
       with col3:
           if alert_type in ["Price Above", "Price Below"]:
               alert_value = st.number_input("Price", min_value=0.01, value=100.00)
           else:
               alert_value = None
       
       if st.button("Set Alert", use_container_width=True):
           st.success(f"Alert set for {alert_symbol}")
   else:
       st.info("Your watchlist is empty. Add some stocks to track!")

def portfolio_rebalancing():
   """Portfolio rebalancing suggestions"""
   st.subheader("Portfolio Rebalancing")
   
   # Current vs Target allocation
   col1, col2 = st.columns(2)
   
   with col1:
       st.markdown("**Current Allocation**")
       current_allocation = pd.DataFrame({
           'Asset': ['Stocks', 'Bonds', 'Cash', 'Commodities', 'Real Estate'],
           'Current (%)': [60, 24, 12, 4, 0],
           'Target (%)': [65, 20, 10, 3, 2]
       })
       
       for idx, row in current_allocation.iterrows():
           col_a, col_b, col_c = st.columns([2, 1, 1])
           with col_a:
               st.markdown(row['Asset'])
           with col_b:
               st.markdown(f"{row['Current (%)']}%")
           with col_c:
               st.markdown(f"{row['Target (%)']}%")
   
   with col2:
       st.markdown("**Rebalancing Actions**")
       actions = []
       for idx, row in current_allocation.iterrows():
           diff = row['Target (%)'] - row['Current (%)']
           if abs(diff) > 1:  # Threshold for rebalancing
               action = "Buy" if diff > 0 else "Sell"
               amount = abs(diff) * 1257.50  # 1% of portfolio
               actions.append({
                   'Action': action,
                   'Asset': row['Asset'],
                   'Amount': amount,
                   'Percentage': abs(diff)
               })
       
       if actions:
           for action in actions:
               color = "green" if action['Action'] == "Buy" else "red"
               st.markdown(f"<span style='color: {color}'>{action['Action']}</span> "
                          f"{action['Asset']}: ${action['Amount']:.2f} "
                          f"({action['Percentage']:.1f}%)", unsafe_allow_html=True)
       else:
           st.success("Portfolio is well-balanced!")
   
   # Tax-loss harvesting
   st.subheader("Tax-Loss Harvesting Opportunities")
   
   # Find holdings with losses
   holdings_data = get_holdings_data()
   loss_opportunities = holdings_data[holdings_data['Gain/Loss ($)'] < 0].copy()
   
   if not loss_opportunities.empty:
       loss_opportunities['Loss Amount'] = loss_opportunities['Gain/Loss ($)'].abs()
       loss_opportunities = loss_opportunities.sort_values('Loss Amount', ascending=False)
       
       for idx, holding in loss_opportunities.head(3).iterrows():
           st.markdown(f"**{holding['Symbol']}** - Potential tax savings: ${holding['Loss Amount'] * 0.25:.2f}")
           st.caption(f"Loss: ${holding['Loss Amount']:.2f} ({holding['Gain/Loss (%)']:.1f}%)")
   else:
       st.info("No significant tax-loss harvesting opportunities at this time.")
   
   # Rebalancing history
   st.subheader("Rebalancing History")
   
   rebalancing_history = pd.DataFrame({
       'Date': ['2024-04-01', '2024-01-15', '2023-10-20', '2023-07-01'],
       'Action': ['Trimmed tech stocks', 'Added bonds allocation', 'Increased cash position', 'Rebalanced to target allocation'],
       'Impact': ['+2.3% performance', 'Reduced portfolio volatility', 'Prepared for market shift', 'Aligned with risk profile']
   })
   
   for idx, action in rebalancing_history.iterrows():
       st.markdown(f"**{action['Date']}** - {action['Action']}")
       st.caption(f"Impact: {action['Impact']}")
       st.divider()

def generate_portfolio_data(dates):
   """Generate sample portfolio value data"""
   import numpy as np
   
   np.random.seed(42)
   daily_returns = np.random.randn(len(dates)) * 0.01 + 0.0003
   cumulative_returns = np.exp(np.cumsum(daily_returns))
   portfolio_value = 110000 * cumulative_returns
   
   return portfolio_value

def generate_watchlist_data(symbols):
   """Generate sample watchlist data"""
   sample_data = {
       'AAPL': {'Company': 'Apple Inc.', 'Price': 178.25, 'Change': '+1.2%', 'Volume': '52.3M', 'Market Cap': '$2.8T'},
       'MSFT': {'Company': 'Microsoft Corp.', 'Price': 338.11, 'Change': '+0.8%', 'Volume': '35.7M', 'Market Cap': '$2.5T'},
       'GOOGL': {'Company': 'Alphabet Inc.', 'Price': 2819.89, 'Change': '-0.5%', 'Volume': '1.2M', 'Market Cap': '$1.7T'},
       'AMZN': {'Company': 'Amazon.com Inc.', 'Price': 175.75, 'Change': '+1.8%', 'Volume': '45.8M', 'Market Cap': '$1.7T'},
       'NVDA': {'Company': 'NVIDIA Corp.', 'Price': 422.77, 'Change': '+3.2%', 'Volume': '65.4M', 'Market Cap': '$1.0T'},
       'TSLA': {'Company': 'Tesla Inc.', 'Price': 245.60, 'Change': '-0.7%', 'Volume': '89.2M', 'Market Cap': '$780B'},
   }
   
   data = []
   for symbol in symbols:
       if symbol in sample_data:
           data.append({
               'Symbol': symbol,
               'Company': sample_data[symbol]['Company'],
               'Price': sample_data[symbol]['Price'],
               'Change': sample_data[symbol]['Change'],
               'Volume': sample_data[symbol]['Volume'],
               'Market Cap': sample_data[symbol]['Market Cap']
           })
       else:
           data.append({
               'Symbol': symbol,
               'Company': f'{symbol} Company',
               'Price': 100.00,
               'Change': '+0.0%',
               'Volume': '1.0M',
               'Market Cap': '$100B'
           })
   
   return pd.DataFrame(data)

def show_stock_chart(symbol):
   """Show a chart for the selected stock"""
   st.subheader(f"{symbol} Price Chart")
   
   # Generate sample data for the chart
   dates = pd.date_range(start='2024-01-01', end='2024-05-03', freq='D')
   prices = generate_sample_stock_data(symbol, dates)
   
   fig = go.Figure()
   
   fig.add_trace(go.Candlestick(
       x=dates,
       open=prices['Open'],
       high=prices['High'],
       low=prices['Low'],
       close=prices['Close'],
       name='Price'
   ))
   
   fig.update_layout(
       title=f'{symbol} Price Chart',
       xaxis_title='Date',
       yaxis_title='Price ($)',
       xaxis_rangeslider_visible=False,
       height=400
   )
   
   st.plotly_chart(fig, use_container_width=True)

def edit_position(symbol):
   """Edit a portfolio position"""
   st.subheader(f"Edit Position: {symbol}")
   
   col1, col2 = st.columns(2)
   
   with col1:
       action = st.radio("Action", ["Buy", "Sell"], horizontal=True)
       shares = st.number_input("Number of Shares", min_value=1, value=10)
   
   with col2:
       price = st.number_input("Price per Share", min_value=0.01, value=100.00)
       date = st.date_input("Transaction Date", value=datetime.now())
   
   if st.button("Submit", use_container_width=True):
       st.success(f"{action} order submitted for {shares} shares of {symbol} at ${price:.2f}")

def get_holdings_data():
   """Get portfolio holdings data"""
   return pd.DataFrame({
       'Symbol': ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'JNJ', 'BRK.B', 'V', 'LLY', 'TSLA'],
       'Company': ['Apple Inc.', 'Microsoft Corp.', 'Alphabet Inc.', 'Amazon.com Inc.', 
                   'Meta Platforms', 'Johnson & Johnson', 'Berkshire Hathaway', 'Visa Inc.',
                   'Eli Lilly', 'Tesla Inc.'],
       'Shares': [50, 25, 5, 30, 20, 40, 25, 35, 15, 10],
       'Avg Cost': [145.50, 280.25, 2450.00, 145.80, 280.50, 155.25, 480.75, 240.30, 480.90, 250.00],
       'Current Price': [178.25, 338.11, 2819.89, 175.75, 321.22, 160.45, 525.80, 268.50, 532.75, 245.60],
       'Market Value': [8912.50, 8452.75, 14099.45, 5272.50, 6424.40, 6418.00, 13145.00, 9397.50, 7991.25, 2456.00],
       'Gain/Loss ($)': [1637.50, 1446.50, 1849.45, 898.50, 814.40, 208.00, 1126.25, 987.00, 778.75, -44.00],
       'Gain/Loss (%)': [22.5, 20.7, 15.1, 20.5, 14.5, 3.4, 9.3, 11.7, 14.4, -1.7]
   })

def generate_sample_stock_data(symbol, dates):
   """Generate sample stock price data"""
   import numpy as np
   
   # Base prices for different stocks
   base_prices = {'AAPL': 178, 'MSFT': 338, 'GOOGL': 2820, 'AMZN': 176, 'META': 321}
   base_price = base_prices.get(symbol, 100)
   
   # Generate random walk for prices
   np.random.seed(42)
   returns = np.random.randn(len(dates)) * 0.01 + 0.0002
   price_series = base_price * np.exp(np.cumsum(returns))
   
   # Create OHLC data
   ohlc_data = pd.DataFrame(index=dates)
   ohlc_data['Close'] = price_series
   ohlc_data['Open'] = ohlc_data['Close'].shift(1) * (1 + np.random.randn(len(dates)) * 0.002)
   ohlc_data['High'] = ohlc_data[['Open', 'Close']].max(axis=1) * (1 + np.abs(np.random.randn(len(dates))) * 0.01)
   ohlc_data['Low'] = ohlc_data[['Open', 'Close']].min(axis=1) * (1 - np.abs(np.random.randn(len(dates))) * 0.01)
   
   return ohlc_data