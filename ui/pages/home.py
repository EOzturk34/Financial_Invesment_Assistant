# ui/pages/home.py - Home page for the application
import streamlit as st

def show_home_page():
    """Display the home page content"""
    st.header("Welcome to Your Financial Investment Assistant")
    
    st.markdown("""
    This intelligent assistant helps you make informed investment decisions based on:
    
    * **Your personal risk profile**
    * **Current market conditions**
    * **Latest financial news**
    * **Data-driven predictions**
    
    The assistant uses advanced AI technologies including Retrieval Augmented Generation (RAG)
    and TensorFlow models to provide personalized recommendations and insights.
    """)
    
    # Feature columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🎯 Personalized Advice")
        st.markdown("""
        * Risk tolerance assessment
        * Goal-based recommendations
        * Portfolio alignment
        * Custom investment strategies
        """)
    
    with col2:
        st.subheader("📊 Market Intelligence")
        st.markdown("""
        * Real-time market data
        * Latest financial news
        * Trend analysis
        * Sector performance
        """)
    
    with col3:
        st.subheader("🧠 AI-Powered Insights")
        st.markdown("""
        * Predictive analytics
        * Sentiment analysis
        * Pattern recognition
        * Decision support
        """)
    
    # Quick start section
    st.subheader("🚀 Get Started")
    st.markdown("""
    1. **Complete your risk profile** - Tell us about your investment goals and risk tolerance
    2. **Explore the assistant** - Ask questions about investment opportunities or market trends
    3. **Discover stocks** - Use our tools to find stocks that match your profile
    4. **Track your portfolio** - Monitor performance and get recommendations
    """)
    
    # Call to action buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Set up profile", use_container_width=True):
            st.session_state.current_page = "Profile"
            st.experimental_rerun()
    
    with col2:
        if st.button("Start investing", use_container_width=True):
            st.session_state.current_page = "Assistant"
            st.experimental_rerun()
    
    with col3:
        if st.button("Explore stocks", use_container_width=True):
            st.session_state.current_page = "Stock Discovery"
            st.experimental_rerun()
    
    # Success stories section
    st.markdown("---")
    st.subheader("💡 Example Insights")
    
    example_insights = [
        {
            "title": "Portfolio Diversification",
            "content": "Based on your moderate risk profile, consider diversifying across 3-4 different sectors to balance growth with stability.",
            "type": "📈"
        },
        {
            "title": "Market Opportunity",
            "content": "Current market analysis suggests tech sector stocks showing strong fundamentals and growth potential.",
            "type": "🎯"
        },
        {
            "title": "Risk Management",
            "content": "Given recent market volatility, maintaining 15-20% cash position could provide flexibility for future opportunities.",
            "type": "⚖️"
        }
    ]
    
    cols = st.columns(len(example_insights))
    for i, insight in enumerate(example_insights):
        with cols[i]:
            st.markdown(f"**{insight['type']} {insight['title']}**")
            st.markdown(insight["content"])
    
    # Quick stats display
    st.markdown("---")
    st.subheader("📈 Quick Market Overview")
    
    # Placeholder for real-time data (you can implement this later)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("S&P 500", "5,872", "+1.2%", delta_color="normal")
    with col2:
        st.metric("NASDAQ", "19,372", "+0.8%", delta_color="normal")
    with col3:
        st.metric("USD/EUR", "0.93", "-0.2%", delta_color="inverse")
    with col4:
        st.metric("Gold", "$2,318", "-0.5%", delta_color="inverse")
    
    # Info box
    st.info("Navigate to the 'Profile' page to set up your investment preferences, or go directly to the 'Assistant' page to start asking financial questions.")