# ui/pages/assistant.py - Chat assistant interface
import streamlit as st
import time
from datetime import datetime

# Placeholder for the actual RAG assistant (will be implemented later)
def get_assistant_response(query, user_profile):
    """
    Placeholder function that will be replaced with actual RAG-based response generation
    
    Args:
        query (str): User's question
        user_profile (dict): User's profile information
    
    Returns:
        dict: Response containing answer and sources
    """
    # This is just a placeholder
    time.sleep(1)  # Simulate processing time
    
    if "bitcoin" in query.lower():
        return {
            "answer": "Based on current market conditions, Bitcoin is showing high volatility. Given your moderate risk profile, I'd recommend limiting cryptocurrency exposure to no more than 5% of your portfolio.",
            "sources": [
                {"title": "Cryptocurrency Market Update", "url": "https://example.com/crypto-update"},
                {"title": "Bitcoin Analysis", "url": "https://example.com/bitcoin-analysis"}
            ]
        }
    elif "stock" in query.lower() or "invest" in query.lower():
        return {
            "answer": f"Based on your {user_profile['risk_profile']} risk profile, I would recommend diversifying your portfolio across different sectors. Your focus on {user_profile['investment_goals']} aligns with a strategy of...",
            "sources": [
                {"title": "Investment Basics", "url": "https://example.com/investment-basics"},
                {"title": "Market Analysis Q2 2023", "url": "https://example.com/market-analysis"}
            ]
        }
    else:
        return {
            "answer": "I'm currently in development mode and have limited knowledge. Please ask me about investments or stocks!",
            "sources": []
        }

def show_assistant():
    """Display the chat assistant interface"""
    st.header("💬 Investment Assistant")
    
    # Add info about what the assistant can do
    with st.expander("ℹ️ How to use the assistant"):
        st.markdown("""
        The AI Investment Assistant can help you with:
        - Investment recommendations based on your risk profile
        - Market analysis and insights
        - Portfolio suggestions
        - General investment questions
        
        Just type your question below and press Enter!
        """)
    
    # Display user profile summary
    with st.expander("👤 Your Profile Summary"):
        st.write(f"**Risk Profile:** {st.session_state.user_profile['risk_profile']}")
        st.write(f"**Investment Goals:** {st.session_state.user_profile['investment_goals']}")
        if st.session_state.user_profile.get('preferred_sectors'):
            st.write(f"**Preferred Sectors:** {', '.join(st.session_state.user_profile['preferred_sectors'])}")
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message.get("sources"):
                with st.expander("📚 Sources"):
                    for source in message["sources"]:
                        st.markdown(f"- [{source['title']}]({source['url']})")
    
    # Chat input
    if prompt := st.chat_input("Ask a question about investments..."):
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": prompt, "timestamp": datetime.now().isoformat()})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_assistant_response(prompt, st.session_state.user_profile)
                st.markdown(response["answer"])
                
                # Show sources if available
                if response.get("sources"):
                    with st.expander("📚 Sources"):
                        for source in response["sources"]:
                            st.markdown(f"- [{source['title']}]({source['url']})")
        
        # Add assistant response to chat history
        st.session_state.chat_history.append({
            "role": "assistant", 
            "content": response["answer"], 
            "sources": response.get("sources", []),
            "timestamp": datetime.now().isoformat()
        })
    
    # Clear chat history button
    if st.session_state.chat_history:
        if st.button("Clear Chat History", type="secondary"):
            st.session_state.chat_history = []
            st.experimental_rerun()