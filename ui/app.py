# ui/app.py - Main Streamlit application for the financial assistant
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from config import PAGE_TITLE, PAGE_ICON, THEME

# Import page modules
from ui.pages.home import show_home_page
from ui.pages.risk_profile import show_risk_profile
from ui.pages.assistant import show_assistant
from ui.pages.stock_discovery import show_stock_discovery
from ui.pages.portfolio import show_portfolio

def main():
    """Main Streamlit application entry point"""
    # Configure the Streamlit page
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'About': "# Financial Investment Assistant\nPersonalized financial advisor powered by AI"
        }
    )
    
    # Session state initialization
    if "user_profile" not in st.session_state:
        st.session_state.user_profile = {
            "risk_profile": "Moderate",
            "investment_goals": "Long-term growth",
            "preferred_sectors": []
        }
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Add custom CSS for better styling
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 8px;
        }
        .reportview-container {
            background: #f0f2f6;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Add header/title to the main page
    st.title("📈 Financial Investment Assistant")
    
    # Create sidebar navigation
    st.sidebar.title("🔍 Navigation")
    page = st.sidebar.radio(
        "Select a page",
        ["Home", "Profile", "Assistant", "Stock Discovery", "Portfolio"]
    )
    
    # Display the appropriate page
    if page == "Home":
        show_home_page()
    elif page == "Profile":
        show_risk_profile()
    elif page == "Assistant":
        show_assistant()
    elif page == "Stock Discovery":
        show_stock_discovery()
    elif page == "Portfolio":
        show_portfolio()
    
    # Add footer
    st.sidebar.markdown("---")
    st.sidebar.info(
        "This application is a demonstration of a financial assistant "
        "using RAG and TensorFlow for personalized investment advice."
    )
    
    # Version info
    st.sidebar.caption("Version 0.1.0 - Development Mode")

if __name__ == "__main__":
    main()