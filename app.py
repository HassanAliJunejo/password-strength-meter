import streamlit as st
import zxcvbn as zxcvbn  # Password strength checker

def check_password_strength(password):
    result = zxcvbn.zxcvbn(password)
    score = result['score']  # Strength score (0 to 4)
    feedback = result['feedback']['suggestions'] if 'feedback' in result and 'suggestions' in result['feedback'] else []
    return score, feedback

# Streamlit App Styling
st.markdown(
    """
    <style>
        body { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', sans-serif; }
        .stTextInput>div>div>input { background-color: #161b22; color: #c9d1d9; border-radius: 8px; border: 1px solid #30363d; padding: 10px; }
        .stButton>button { background-color: #238636; color: white; border-radius: 8px; padding: 10px; font-weight: bold; border: none; }
        .stButton>button:hover { background-color: #2ea043; }
        .stMarkdown { color: #58a6ff; }
        .stSubheader { color: #ffa657; }
        .password-box { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔒 Password Strength Meter")
st.write("Enter a password to check its strength.")

password = st.text_input("Enter Password", type="password")

if password:
    score, feedback = check_password_strength(password)
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    
    st.subheader(f"Strength: {strength_levels[score]}")
    
    # Show feedback if any
    if feedback:
        st.write("**Suggestions:**")
        for tip in feedback:
            st.markdown(f"- {tip}", unsafe_allow_html=True)
