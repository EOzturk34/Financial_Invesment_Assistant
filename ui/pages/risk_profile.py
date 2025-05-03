# ui/pages/risk_profile.py - Risk profile assessment page
import streamlit as st

def show_risk_profile():
    """Display the risk profile assessment page"""
    st.header("🎯 Risk Profile Assessment")
    
    st.markdown("""
    Let's understand your investment preferences to provide personalized recommendations.
    This assessment will help us determine your risk tolerance and investment style.
    """)
    
    # Risk Profile Form
    with st.form("risk_profile_form"):
        st.subheader("Personal Information")
        
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", min_value=18, max_value=100, value=35)
            experience = st.selectbox(
                "Investment Experience",
                ["Beginner", "Intermediate", "Advanced", "Expert"]
            )
        
        with col2:
            income = st.selectbox(
                "Annual Income",
                ["Under $50K", "$50K-$100K", "$100K-$200K", "Over $200K"]
            )
            investment_timeline = st.selectbox(
                "Investment Timeline",
                ["Less than 1 year", "1-3 years", "3-5 years", "5-10 years", "More than 10 years"]
            )
        
        st.subheader("Investment Preferences")
        
        risk_tolerance = st.radio(
            "How would you describe your risk tolerance?",
            ["Very Conservative", "Conservative", "Moderate", "Aggressive", "Very Aggressive"],
            index=2  # Default to "Moderate"
        )
        
        investment_goals = st.multiselect(
            "What are your primary investment goals?",
            ["Capital preservation", "Income generation", "Long-term growth", 
             "Short-term gains", "Portfolio diversification", "Retirement planning"],
            default=["Long-term growth"]
        )
        
        preferred_sectors = st.multiselect(
            "Do you have any preferred sectors?",
            ["Technology", "Healthcare", "Finance", "Consumer Goods", 
             "Real Estate", "Energy", "Manufacturing", "Services"],
            default=[]
        )
        
        max_loss_tolerance = st.slider(
            "What's the maximum portfolio loss you can tolerate in a year?",
            min_value=0, max_value=50, value=15, step=5,
            format="%d%%"
        )
        
        st.subheader("Market Scenario")
        
        market_sentiment = st.radio(
            "If the market suddenly dropped 20%, what would you do?",
            [
                "Sell all investments to prevent further losses",
                "Sell some investments to reduce risk",
                "Hold current positions",
                "Buy more investments at lower prices",
                "Significantly increase investments"
            ],
            index=2
        )
        
        submitted = st.form_submit_button("Save Profile", use_container_width=True)
        
        if submitted:
            # Update session state with the profile
            st.session_state.user_profile = {
                "age": age,
                "experience": experience,
                "income": income,
                "investment_timeline": investment_timeline,
                "risk_profile": risk_tolerance,
                "investment_goals": ", ".join(investment_goals),
                "preferred_sectors": preferred_sectors,
                "max_loss_tolerance": max_loss_tolerance,
                "market_sentiment": market_sentiment
            }
            
            st.success("✅ Profile saved successfully!")
            
            # Provide quick analysis
            st.subheader("Quick Profile Analysis")
            
            risk_score = calculate_risk_score(
                risk_tolerance, market_sentiment, max_loss_tolerance
            )
            
            st.markdown(f"**Your Risk Score:** {risk_score}/10")
            st.progress(risk_score / 10)
            
            # Recommendations based on profile
            recommendations = generate_basic_recommendations(
                risk_tolerance, investment_timeline, investment_goals
            )
            
            st.markdown("### Based on your profile, we recommend:")
            for rec in recommendations:
                st.markdown(f"• {rec}")
            
            st.info("👉 Navigate to the Assistant page to get personalized investment advice!")

def calculate_risk_score(risk_tolerance, market_sentiment, max_loss_tolerance):
    """Calculate a simple risk score based on responses"""
    risk_mapping = {
        "Very Conservative": 1,
        "Conservative": 3,
        "Moderate": 5,
        "Aggressive": 7,
        "Very Aggressive": 9
    }
    
    sentiment_mapping = {
        "Sell all investments to prevent further losses": 1,
        "Sell some investments to reduce risk": 3,
        "Hold current positions": 5,
        "Buy more investments at lower prices": 7,
        "Significantly increase investments": 9
    }
    
    risk_score = risk_mapping.get(risk_tolerance, 5)
    sentiment_score = sentiment_mapping.get(market_sentiment, 5)
    
    # Weight the scores
    total_score = (risk_score * 0.4 + sentiment_score * 0.3 + 
                   (max_loss_tolerance / 10) * 0.3)
    
    return round(total_score, 1)

def generate_basic_recommendations(risk_tolerance, timeline, goals):
    """Generate basic investment recommendations"""
    recommendations = []
    
    if risk_tolerance in ["Very Conservative", "Conservative"]:
        recommendations.append("Focus on government bonds and high-quality corporate bonds")
        recommendations.append("Consider money market funds for short-term needs")
    elif risk_tolerance == "Moderate":
        recommendations.append("Balanced portfolio of 60% stocks and 40% bonds")
        recommendations.append("Include blue-chip stocks and investment-grade bonds")
    else:
        recommendations.append("Growth-focused portfolio with higher stock allocation")
        recommendations.append("Consider emerging markets and growth stocks")
    
    if "Income generation" in goals:
        recommendations.append("Include dividend-paying stocks and bonds")
    
    if "5-10 years" in timeline or "More than 10 years" in timeline:
        recommendations.append("Consider dollar-cost averaging for long-term positions")
    
    return recommendations