import streamlit as st
from newspaper import Article
from textblob import TextBlob
import nltk

nltk.download('punkt')

# Set page config
st.set_page_config(
    page_title="News Summarizer",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS with animations and icons
st.markdown("""
    <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes buttonHover {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        .reportview-container {
            background: #f0f2f6;
        }
        
        .header {
            color: #2c3e50;
        }
        
        .stTextInput>div>div>input {
            border: 2px solid #4a90e2;
            border-radius: 25px;
            padding: 10px 20px;
            transition: all 0.3s ease;
        }
        
        .stButton>button {
            background-color: #4a90e2;
            color: white;
            border: none;
            border-radius: 25px;
            padding: 12px 28px;
            font-weight: bold;
            transition: all 0.3s ease !important;
        }
        
        .stButton>button:hover {
            background-color: #357abd;
            animation: buttonHover 0.5s ease;
        }
        
        .metric-box {
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 10px 0;
            animation: fadeIn 0.6s ease-out;
            transition: transform 0.3s ease;
        }
        
        .metric-box:hover {
            transform: translateY(-5px);
        }
        
        .social-button {
            display: inline-flex;
            align-items: center;
            padding: 12px 25px;
            margin: 10px;
            border-radius: 25px;
            color: white !important;
            text-decoration: none !important;
            transition: all 0.3s ease;
            transform-origin: center;
            gap: 10px;
        }

        .social-button i {
            font-size: 1.2em;
        }

        .social-button span {
            display: inline-block;
        }

        @media (max-width: 480px) {
            .social-button span {
                display: none;
            }
            .social-button {
                padding: 12px 15px;
            }
        }
        
        .linkedin {
            background: #0A66C2;
        }
        
        .github {
            background: #333;
        }
        
        .social-button:hover {
            transform: scale(1.1);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .fade-in {
            animation: fadeIn 0.8s ease-out;
        }
    </style>
""", unsafe_allow_html=True)

# App header with animation
st.markdown('<div class="fade-in">', unsafe_allow_html=True)
st.title("📰 News Analytics Pro")
st.markdown("---")
st.markdown('</div>', unsafe_allow_html=True)

# URL input
url = st.text_input(
    "Enter News Article URL:",
    placeholder="Paste article URL here...",
    key="url_input"
)

if st.button("Analyze Article"):
    if not url:
        st.warning("Please enter a valid URL.")
    else:
        with st.spinner("📥 Downloading and analyzing article..."):
            try:
                article = Article(url)
                article.download()
                article.parse()
                article.nlp()

                # Display results with animations
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
                    st.subheader("📝 Article Content")
                    with st.expander("View Full Text", expanded=False):
                        st.write(article.text)
                    
                    st.subheader("📌 Key Summary")
                    st.info(article.summary if article.summary else "No summary available.")
                    st.markdown('</div>', unsafe_allow_html=True)

                with col2:
                    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
                    st.subheader("🔍 Metadata")
                    
                    # Article metrics
                    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
                    st.markdown("**📛 Title**")
                    st.write(article.title or "No title available")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
                    st.markdown("**👤 Authors**")
                    if article.authors:
                        st.write("\n".join([f"- {author}" for author in article.authors]))
                    else:
                        st.write("No authors available")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
                    st.markdown("**📅 Publication Date**")
                    st.write(article.publish_date.strftime("%B %d, %Y") if article.publish_date else "Date unavailable")
                    st.markdown('</div>', unsafe_allow_html=True)

                    # Sentiment analysis
                    analysis = TextBlob(article.text)
                    polarity = analysis.polarity
                    sentiment_class = ""
                    if polarity > 0:
                        sentiment_class = "sentiment-positive"
                        emoji = "😊"
                    elif polarity < 0:
                        sentiment_class = "sentiment-negative"
                        emoji = "😠"
                    else:
                        sentiment_class = "sentiment-neutral"
                        emoji = "😐"

                    st.markdown(f'<div class="metric-box {sentiment_class}">', unsafe_allow_html=True)
                    st.markdown("**🧠 Sentiment Analysis**")
                    st.metric("Polarity", f"{polarity:.2f}")
                    st.markdown(f"**Sentiment:** {emoji}")
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Footer with social links and logos
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h3>Connect with Me</h3>
        <a href="https://www.linkedin.com/in/abdullahwaqar/" target="_blank" class="social-button linkedin">
            <i class="fab fa-linkedin"></i>
            <span>LinkedIn</span>
        </a>
        <a href="https://github.com/vanix056" target="_blank" class="social-button github">
            <i class="fab fa-github"></i>
            <span>GitHub</span>
        </a>
    </div>
""", unsafe_allow_html=True)

st.caption("Developed by vanix056")