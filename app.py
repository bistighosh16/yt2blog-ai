"""
🎬 YT2Blog AI - Transform YouTube videos into beautiful blog posts!
Made with 💜 by Vivi ✨
"""

import streamlit as st
import random
from utils import (
    extract_video_id,
    get_transcript,
    generate_blog_post,
    generate_seo_metadata,
    generate_twitter_thread,
    generate_linkedin_post
)

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="YT2Blog AI 💜",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 🎨 THEME DEFINITIONS
# ==========================================
THEMES = {
    "💜 Cosmic Purple": {
        "primary": "#9B59B6",
        "secondary": "#E056FD",
        "accent": "#C77DFF",
        "bg1": "#0a0a0f",
        "bg2": "#1a0a2e",
        "bg3": "#2d1b4e",
        "text": "#c8c8e0",
        "particle1": "rgba(155, 89, 182, 0.5)",
        "particle2": "rgba(224, 86, 253, 0.4)",
    },
    "🌌 Aurora": {
        "primary": "#FF6B9D",
        "secondary": "#00D9FF",
        "accent": "#C77DFF",
        "bg1": "#0a0a1f",
        "bg2": "#1a0a3e",
        "bg3": "#1b2d4e",
        "text": "#d0d8f5",
        "particle1": "rgba(255, 107, 157, 0.5)",
        "particle2": "rgba(0, 217, 255, 0.4)",
    },
    "🌙 Midnight": {
        "primary": "#4A90E2",
        "secondary": "#7FB3F0",
        "accent": "#B8D4F0",
        "bg1": "#050810",
        "bg2": "#0a1428",
        "bg3": "#1a2540",
        "text": "#c0d0e0",
        "particle1": "rgba(74, 144, 226, 0.5)",
        "particle2": "rgba(127, 179, 240, 0.4)",
    },
}

if "selected_theme" not in st.session_state:
    st.session_state.selected_theme = "💜 Cosmic Purple"

theme = THEMES[st.session_state.selected_theme]


# ==========================================
# 🎉 CONFETTI CELEBRATION FUNCTION
# ==========================================
def show_confetti():
    """Drops beautiful confetti when blog is generated! 💜"""
    colors = [theme['primary'], theme['secondary'], '#FFFFFF', theme['accent']]
    emojis = ['💜', '✨', '🎉', '⭐', '🪄', '🌸']
    
    confetti_pieces = ""
    for i in range(50):
        left = random.randint(0, 100)
        delay = round(random.uniform(0, 2), 2)
        size = random.randint(16, 26)
        
        if i % 2 == 0:
            emoji = random.choice(emojis)
            confetti_pieces += f'<div class="confetti-piece" style="left:{left}%;animation-delay:{delay}s;font-size:{size}px;">{emoji}</div>'
        else:
            color = random.choice(colors)
            confetti_pieces += f'<div class="confetti-piece" style="left:{left}%;animation-delay:{delay}s;width:{size//2}px;height:{size//2}px;background:{color};border-radius:50%;box-shadow:0 0 10px {color};"></div>'
    
    full_html = f"""
    <style>
    @keyframes confettiFall {{
        0% {{ transform: translateY(-100vh) rotate(0deg); opacity: 1; }}
        100% {{ transform: translateY(100vh) rotate(720deg); opacity: 0; }}
    }}
    .confetti-container {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 9999;
        overflow: hidden;
    }}
    .confetti-piece {{
        position: absolute;
        animation: confettiFall 3s linear forwards;
    }}
    </style>
    <div class="confetti-container">{confetti_pieces}</div>
    """
    
    st.markdown(full_html, unsafe_allow_html=True)


# ==========================================
# 🎨 DYNAMIC THEME COLORS (CSS VARIABLES)
# ==========================================
st.markdown(f"""
<style>
    :root {{
        --primary: {theme['primary']};
        --secondary: {theme['secondary']};
        --accent: {theme['accent']};
        --bg1: {theme['bg1']};
        --bg2: {theme['bg2']};
        --bg3: {theme['bg3']};
        --text-color: {theme['text']};
        --particle1: {theme['particle1']};
        --particle2: {theme['particle2']};
    }}
</style>
""", unsafe_allow_html=True)


# ==========================================
# CUSTOM CSS - GLASSMORPHISM MAGIC ✨
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    /* ANIMATED GRADIENT BACKGROUND */
    .stApp {
        background: linear-gradient(-45deg, var(--bg1), var(--bg2), var(--bg3), var(--bg2), var(--bg1));
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* FLOATING PARTICLES */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20% 30%, var(--particle1), transparent),
            radial-gradient(2px 2px at 60% 70%, var(--particle2), transparent),
            radial-gradient(1px 1px at 50% 50%, rgba(255, 255, 255, 0.3), transparent),
            radial-gradient(1px 1px at 80% 10%, var(--particle1), transparent),
            radial-gradient(2px 2px at 90% 60%, var(--particle2), transparent),
            radial-gradient(1px 1px at 33% 80%, rgba(255, 255, 255, 0.2), transparent);
        background-size: 200% 200%;
        animation: particleFloat 20s linear infinite;
        pointer-events: none;
        z-index: 0;
    }
    
    @keyframes particleFloat {
        0% { background-position: 0% 0%; }
        100% { background-position: 100% 100%; }
    }
    
    /* HERO TITLE */
    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 5rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 25%, #FFFFFF 50%, var(--secondary) 75%, var(--primary) 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -3px;
        animation: shimmer 4s linear infinite, fadeInDown 1s ease;
        text-shadow: 0 0 80px var(--particle1);
    }
    
    @keyframes shimmer {
        to { background-position: 200% center; }
    }
    
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        text-align: center;
        color: var(--text-color);
        margin-bottom: 2rem;
        font-weight: 300;
        animation: fadeInUp 1.2s ease;
        letter-spacing: 0.5px;
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* FEATURE BADGES */
    .feature-badge {
        display: inline-block;
        background: linear-gradient(135deg, var(--particle1), var(--particle2));
        color: var(--secondary);
        padding: 0.4rem 1rem;
        border-radius: 25px;
        font-size: 0.9rem;
        margin: 0.3rem;
        border: 1px solid var(--particle1);
        backdrop-filter: blur(10px);
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: default;
        font-weight: 500;
        animation: fadeInUp 1.5s ease;
    }
    
    .feature-badge:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 10px 25px var(--particle1);
        border-color: var(--secondary);
    }
    
    /* GLASS CARDS */
    .glass-card {
        background: linear-gradient(135deg, var(--particle1), var(--particle2));
        backdrop-filter: blur(25px) saturate(180%);
        -webkit-backdrop-filter: blur(25px) saturate(180%);
        border: 1px solid var(--particle1);
        border-radius: 24px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px 0 var(--particle1), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
        animation: cardSlideIn 0.8s ease;
    }
    
    @keyframes cardSlideIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .glass-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, var(--particle2), transparent);
        transition: left 0.6s ease;
    }
    
    .glass-card:hover::before {
        left: 100%;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        border-color: var(--secondary);
        box-shadow: 0 20px 40px var(--particle1), inset 0 1px 0 rgba(255, 255, 255, 0.2);
    }
    
    /* INPUT FIELDS */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1.5px solid var(--particle1) !important;
        border-radius: 14px !important;
        color: white !important;
        padding: 0.9rem 1.2rem !important;
        font-size: 1.05rem !important;
        transition: all 0.3s ease !important;
        font-family: 'Poppins', sans-serif !important;
    }
    
    .stTextInput > div > div > input:hover {
        border-color: var(--secondary) !important;
        background: rgba(255, 255, 255, 0.08) !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--secondary) !important;
        box-shadow: 0 0 0 3px var(--particle2), 0 0 30px var(--particle2) !important;
        background: rgba(255, 255, 255, 0.1) !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.4) !important;
    }
    
    /* BUTTONS */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 50%, var(--primary) 100%) !important;
        background-size: 200% auto !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 0.9rem 2.5rem !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        font-family: 'Poppins', sans-serif !important;
        letter-spacing: 0.5px !important;
        transition: all 0.4s ease !important;
        box-shadow: 0 4px 15px var(--particle1), inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
        position: relative !important;
        overflow: hidden !important;
        text-transform: none !important;
    }
    
    .stButton > button:hover {
        background-position: right center !important;
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 10px 30px var(--particle2), 0 0 50px var(--particle1), inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) scale(0.98) !important;
    }
    
    /* DOWNLOAD BUTTON */
    .stDownloadButton > button {
        background: linear-gradient(135deg, var(--particle1), var(--particle2)) !important;
        color: var(--secondary) !important;
        border: 1.5px solid var(--secondary) !important;
        border-radius: 12px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s ease !important;
    }
    
    .stDownloadButton > button:hover {
        background: linear-gradient(135deg, var(--primary), var(--secondary)) !important;
        color: white !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px var(--particle2) !important;
    }
    
    /* SELECTBOX */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1.5px solid var(--particle1) !important;
        border-radius: 12px !important;
        color: white !important;
        transition: all 0.3s ease !important;
    }
    
    .stSelectbox > div > div:hover {
        border-color: var(--secondary) !important;
        background: rgba(255, 255, 255, 0.08) !important;
    }
    
    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--bg1), var(--bg2)) !important;
        border-right: 1px solid var(--particle1);
        backdrop-filter: blur(20px);
    }
    
    [data-testid="stSidebar"] h3 {
        color: var(--secondary) !important;
        font-weight: 700 !important;
    }
    
    /* METRIC CARDS */
    .metric-card {
        background: linear-gradient(135deg, var(--particle1), var(--particle2));
        border: 1px solid var(--particle1);
        border-radius: 18px;
        padding: 1.5rem;
        text-align: center;
        backdrop-filter: blur(15px);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.8s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px) scale(1.03);
        border-color: var(--secondary);
        box-shadow: 0 15px 35px var(--particle2);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 50%, #FFFFFF 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmer 3s linear infinite;
    }
    
    .metric-label {
        color: var(--text-color);
        font-size: 0.9rem;
        margin-top: 0.5rem;
        font-weight: 500;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    
    /* ALERTS */
    .stSuccess, .stError, .stInfo, .stWarning {
        border-radius: 16px !important;
        backdrop-filter: blur(15px) !important;
        border: 1px solid var(--particle1) !important;
        animation: fadeInUp 0.5s ease !important;
    }
    
    /* SPINNER */
    .stSpinner > div {
        border-color: var(--secondary) transparent transparent transparent !important;
    }
    
    /* TABS */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: var(--particle1);
        border-radius: 14px;
        padding: 6px;
        border: 1px solid var(--particle1);
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px !important;
        color: var(--text-color) !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        padding: 0.5rem 1.5rem !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--primary), var(--secondary)) !important;
        color: white !important;
        box-shadow: 0 4px 15px var(--particle1) !important;
    }
    
    /* SCROLLBAR */
    ::-webkit-scrollbar { width: 10px; height: 10px; }
    ::-webkit-scrollbar-track { background: var(--bg1); border-radius: 10px; }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, var(--primary), var(--secondary));
        border-radius: 10px;
        border: 2px solid var(--bg1);
    }
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, var(--secondary), var(--primary));
    }
    
    /* FOOTER */
    .footer {
        text-align: center;
        padding: 3rem 0 1rem 0;
        color: var(--text-color);
        font-size: 0.95rem;
        animation: fadeInUp 1s ease;
    }
    
    .footer-heart {
        color: var(--secondary);
        font-size: 1.3rem;
        display: inline-block;
        animation: heartbeat 1.5s ease-in-out infinite;
    }
    
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.2); }
    }
    
    /* HEADERS */
    h1, h2, h3 {
        font-family: 'Space Grotesk', sans-serif !important;
    }
    
    h3 {
        background: linear-gradient(135deg, var(--secondary), #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700 !important;
    }
    
    /* HIDE STREAMLIT BRANDING */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* VIDEO PLAYER */
    .stVideo {
        border-radius: 20px !important;
        overflow: hidden !important;
        box-shadow: 0 20px 60px var(--particle1) !important;
        border: 1px solid var(--particle1) !important;
    }
    
    .stCodeBlock {
        border-radius: 14px !important;
        border: 1px solid var(--particle1) !important;
    }
    
    label {
        color: var(--text-color) !important;
        font-weight: 500 !important;
    }
    
    .stMarkdown {
        color: #e8e8f5;
    }
    
    .stMarkdown h1 {
        background: linear-gradient(135deg, var(--secondary), #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800 !important;
    }
    
    .stMarkdown h2 {
        color: var(--secondary) !important;
        margin-top: 2rem !important;
    }
    
    .stMarkdown a {
        color: var(--secondary) !important;
        text-decoration: none !important;
        border-bottom: 1px dashed var(--particle2);
        transition: all 0.3s ease;
    }
    
    .stMarkdown a:hover {
        color: #FFFFFF !important;
        border-bottom-color: #FFFFFF;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# HERO SECTION
# ==========================================
st.markdown('<h1 class="hero-title">🎬 YT2Blog AI</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="hero-subtitle">Transform any YouTube video into a beautiful, '
    'SEO-optimized blog post in seconds ✨</p>',
    unsafe_allow_html=True
)

# Feature badges
st.markdown("""
<div style="text-align: center; margin-bottom: 2.5rem;">
    <span class="feature-badge">⚡ Powered by Groq</span>
    <span class="feature-badge">🧠 Llama 3.3 70B</span>
    <span class="feature-badge">🎨 4 Tones</span>
    <span class="feature-badge">📝 Markdown</span>
    <br>
    <span class="feature-badge">🎯 SEO</span>
    <span class="feature-badge">🐦 Twitter Ready</span>
    <span class="feature-badge">💼 LinkedIn Ready</span>
</div>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    # 🎨 THEME SWITCHER
    st.markdown("### 🎨 Choose Your Vibe")
    selected = st.selectbox(
        "Theme",
        list(THEMES.keys()),
        index=list(THEMES.keys()).index(st.session_state.selected_theme),
        label_visibility="collapsed",
        key="theme_selector"
    )
    
    if selected != st.session_state.selected_theme:
        st.session_state.selected_theme = selected
        st.rerun()
    
    st.markdown("---")
    
    st.markdown("### ⚙️ Blog Settings")
    st.markdown("---")
    
    tone = st.selectbox(
        "🎨 Writing Tone",
        ["Professional", "Casual", "Technical", "Storytelling"],
        help="Choose the vibe of your blog post"
    )
    
    length = st.selectbox(
        "📏 Blog Length",
        ["Short", "Medium", "Detailed"],
        index=1,
        help="Short ~500 words | Medium ~1000 | Detailed ~1500+"
    )
    
    include_seo = st.checkbox(
        "🎯 Generate SEO Metadata",
        value=True,
        help="Get SEO title, meta description, and tags"
    )
    
    include_twitter = st.checkbox(
        "🐦 Generate Twitter Thread",
        value=False,
        help="Convert blog into a viral Twitter thread"
    )
    
    include_linkedin = st.checkbox(
        "💼 Generate LinkedIn Post",
        value=False,
        help="Create a professional LinkedIn post"
    )
    
    st.markdown("---")
    st.markdown("### 💡 Pro Tips")
    st.info(
        "✨ Works best with educational, tutorial, "
        "and informative videos!\n\n"
        "🎬 Make sure the video has captions enabled."
    )
    
    st.markdown("---")
    st.markdown(
        '<div style="text-align: center; color: #b8b8d1; font-size: 0.85rem;">'
        'Made with 💜 by<br>'
        '<a href="https://github.com/bistighosh16" target="_blank" '
        'style="color: #E056FD; text-decoration: none; font-weight: 600;">Vivi ✨</a>'
        '</div>',
        unsafe_allow_html=True
    )

# ==========================================
# HOW IT WORKS - 3 STEP CARDS
# ==========================================
st.markdown("### ✨ How It Works")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="glass-card" style="text-align: center; padding: 1.5rem;">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">📎</div>
        <div style="font-size: 1.2rem; font-weight: 700; color: var(--secondary); margin-bottom: 0.5rem;">
            Step 1
        </div>
        <div style="color: var(--text-color); font-size: 0.95rem;">
            Paste any YouTube video URL
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card" style="text-align: center; padding: 1.5rem;">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">🪄</div>
        <div style="font-size: 1.2rem; font-weight: 700; color: var(--secondary); margin-bottom: 0.5rem;">
            Step 2
        </div>
        <div style="color: var(--text-color); font-size: 0.95rem;">
            AI works its magic ✨
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="glass-card" style="text-align: center; padding: 1.5rem;">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">🎁</div>
        <div style="font-size: 1.2rem; font-weight: 700; color: var(--secondary); margin-bottom: 0.5rem;">
            Step 3
        </div>
        <div style="color: var(--text-color); font-size: 0.95rem;">
            Get blog + posts ready!
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# MAIN INPUT SECTION
# ==========================================
st.markdown("""
<div style="text-align: center; margin: 2rem 0 1rem 0;">
    <h2 style="background: linear-gradient(135deg, var(--secondary), #FFFFFF); 
               -webkit-background-clip: text; 
               -webkit-text-fill-color: transparent;
               background-clip: text;
               font-family: 'Space Grotesk', sans-serif;
               font-weight: 700;
               font-size: 2rem;">
        🎬 Drop Your YouTube Link
    </h2>
    <p style="color: var(--text-color); font-size: 1rem;">
        Paste any video URL and watch the magic happen ✨
    </p>
</div>
""", unsafe_allow_html=True)

# Two tabs: YouTube URL OR Paste Transcript
input_tab1, input_tab2 = st.tabs(["📎 YouTube URL", "📝 Paste Transcript"])

with input_tab1:
    url = st.text_input(
        "YouTube URL",
        placeholder="🔗 https://www.youtube.com/watch?v=...",
        label_visibility="collapsed",
        key="url_input"
    )
    st.caption("⚡ Works best on local. Cloud version may face YouTube IP blocks — use the next tab!")

with input_tab2:
    pasted_transcript = st.text_area(
        "Paste your transcript here",
        placeholder="Paste the YouTube transcript here...\n\n💡 Tip: On YouTube, click '...' under the video → 'Show transcript' → copy all text!",
        height=200,
        label_visibility="collapsed",
        key="transcript_input"
    )
    st.caption("💜 Pro tip: This works with ANY text — articles, notes, anything!")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate_btn = st.button("✨ Generate Blog Post", use_container_width=True)

# ==========================================
# GENERATE BLOG
# ==========================================
if generate_btn:
    transcript = None
    error = None
    video_id = None
    
    # Determine which input was used
    if pasted_transcript and pasted_transcript.strip():
        # User pasted a transcript directly
        transcript = pasted_transcript.strip()
        video_id = "manual_input"
        st.info("📝 Using your pasted transcript!")
    elif url and url.strip():
        # User provided a YouTube URL
        with st.spinner("🔍 Extracting video info..."):
            video_id = extract_video_id(url)
        
        if not video_id:
            st.error("❌ Invalid YouTube URL. Please check and try again!")
            st.stop()
        
        st.markdown("### 🎥 Video Preview")
        st.video(f"https://www.youtube.com/watch?v={video_id}")
        
        with st.spinner("📜 Fetching transcript..."):
            transcript, error = get_transcript(video_id)
    else:
        st.error("🚨 Please paste a YouTube URL OR a transcript first, bestie! 💜")
        st.stop()
    
    if error:
        st.error(error)
    elif transcript:
        # Generate everything!
        word_count = len(transcript.split())
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{word_count:,}</div>
                <div class="metric-label">Transcript Words</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{tone}</div>
                <div class="metric-label">Selected Tone</div>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{length}</div>
                <div class="metric-label">Blog Length</div>
            </div>
            """, unsafe_allow_html=True)
        
        with st.spinner("✨ Crafting your blog post... This is the magic part! 💜"):
            blog_content = generate_blog_post(transcript, tone, length)
        
        # 🎉 CELEBRATE!
        show_confetti()
        st.success("🎉 Blog post generated successfully! Enjoy your masterpiece! 💜")
        
        if include_seo:
            with st.spinner("🎯 Generating SEO metadata..."):
                seo = generate_seo_metadata(blog_content)
            
            st.markdown("### 🎯 SEO Metadata")
            with st.expander("📊 View SEO Details", expanded=True):
                st.markdown(f"**📌 SEO Title:** {seo['title']}")
                st.markdown(f"**📝 Meta Description:** {seo['meta']}")
                st.markdown(f"**🏷️ Tags:** {seo['tags']}")
        
        st.markdown("---")
        st.markdown("### 📝 Your Blog Post")
        
        tab1, tab2 = st.tabs(["📖 Preview", "📄 Markdown"])
        
        with tab1:
            st.markdown(blog_content)
        
        with tab2:
            st.code(blog_content, language="markdown")
        
        st.download_button(
            label="⬇️ Download Blog as Markdown",
            data=blog_content,
            file_name=f"blog_post_{video_id}.md",
            mime="text/markdown",
            use_container_width=True
        )
        
        # TWITTER THREAD
        if include_twitter:
            st.markdown("---")
            st.markdown("### 🐦 Twitter Thread")
            with st.spinner("🐦 Crafting viral tweets..."):
                twitter_thread = generate_twitter_thread(blog_content)
            
            with st.container():
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown(twitter_thread)
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.download_button(
                label="⬇️ Download Twitter Thread",
                data=twitter_thread,
                file_name=f"twitter_thread_{video_id}.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        # LINKEDIN POST
        if include_linkedin:
            st.markdown("---")
            st.markdown("### 💼 LinkedIn Post")
            with st.spinner("💼 Writing your LinkedIn post..."):
                linkedin_post = generate_linkedin_post(blog_content)
            
            with st.container():
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown(linkedin_post)
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.download_button(
                label="⬇️ Download LinkedIn Post",
                data=linkedin_post,
                file_name=f"linkedin_post_{video_id}.txt",
                mime="text/plain",
                use_container_width=True
            )
# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.markdown("""
<div class="footer">
    Made with <span class="footer-heart">💜</span> by 
    <a href="https://github.com/bistighosh16" target="_blank" 
       style="color: var(--secondary); text-decoration: none; font-weight: 600;">Vivi ✨</a>
    <br>
    <small>Powered by Groq ⚡ • Llama 3.3 🧠 • Streamlit 🎈</small>
</div>
""", unsafe_allow_html=True)