import os
import sys

# Fix for Python 3.14 asyncio event loop compatibility in Streamlit
os.environ["ASYNCIO_EVENT_LOOP"] = "select"

import streamlit as st

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION & SYSTEM STYLING
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="VERIX | Enterprise KYC Intelligence",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"], .stMarkdown, p, div, span, input, button {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* Tighten top margin to remove upper dead space */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 92% !important;
    }

    .stApp {
        background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%) !important;
        color: #0F172A !important;
    }

    /* Left Branding Section */
    .brand-header-wrapper {
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 20px;
    }
    .brand-logo-icon {
        width: 52px;
        height: 52px;
        background: linear-gradient(135deg, #1E40AF 0%, #1D4ED8 100%);
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 10px 22px rgba(30, 64, 175, 0.28);
    }
    .brand-title-text {
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: -0.8px;
        color: #0F172A;
        line-height: 1.1;
    }
    .brand-title-text span {
        color: #1E40AF;
    }
    .brand-subtitle {
        font-size: 1.05rem;
        color: #475569;
        font-weight: 500;
        margin-bottom: 28px;
        line-height: 1.5;
    }

    .compliance-banner {
        background-color: #FFF7ED;
        border-left: 4px solid #EA580C;
        padding: 16px 20px;
        border-radius: 8px;
        color: #9A3412;
        font-size: 0.92rem;
        font-weight: 500;
        margin-bottom: 28px;
        box-shadow: 0 2px 8px rgba(234, 88, 12, 0.06);
    }

    .capability-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 14px;
        transition: all 0.2s ease;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    .capability-card:hover {
        border-color: #CBD5E1;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05);
        transform: translateY(-1px);
    }
    .capability-dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background-color: #16A34A;
        flex-shrink: 0;
    }
    .capability-text {
        font-size: 0.95rem;
        font-weight: 600;
        color: #334155;
    }

    /* Auth Card Top Header */
    .auth-header-block {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 8px;
    }
    .auth-header-icon {
        width: 36px;
        height: 36px;
        background: #EFF6FF;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #1E40AF;
    }
    .auth-header-title {
        font-size: 1.4rem;
        font-weight: 800;
        color: #0F172A;
        letter-spacing: -0.4px;
    }
    .auth-sub {
        font-size: 0.88rem;
        color: #64748B;
        margin-bottom: 20px;
    }

    /* Form Fields */
    div[data-baseweb="input"] {
        background-color: #F8FAFC !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
    }
    div[data-baseweb="input"]:focus-within {
        border-color: #1E40AF !important;
        box-shadow: 0 0 0 3px rgba(30, 64, 175, 0.12) !important;
        background-color: #FFFFFF !important;
    }
    div[data-baseweb="input"] input {
        color: #0F172A !important;
        font-weight: 500 !important;
    }

    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #1E40AF 0%, #1D4ED8 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        height: 48px !important;
        border-radius: 8px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(30, 64, 175, 0.25) !important;
        transition: all 0.2s ease !important;
        margin-top: 8px;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #1D4ED8 0%, #2563EB 100%) !important;
        box-shadow: 0 6px 16px rgba(30, 64, 175, 0.35) !important;
        transform: translateY(-1px);
    }

    /* Enterprise Credential Quick Badge */
    .cred-container {
        margin-top: 24px;
        padding: 16px;
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
    }
    .cred-header {
        font-size: 0.75rem;
        font-weight: 800;
        letter-spacing: 0.8px;
        color: #64748B;
        text-transform: uppercase;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .cred-badge-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
    }
    .cred-badge {
        background: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 6px;
        padding: 8px 12px;
    }
    .cred-label {
        font-size: 0.7rem;
        color: #94A3B8;
        font-weight: 600;
        text-transform: uppercase;
    }
    .cred-val {
        font-size: 0.88rem;
        font-weight: 700;
        color: #1E40AF;
        font-family: monospace;
    }
    </style>
""", unsafe_allow_html=True)

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def login():
    if st.session_state.get("username") == "admin" and st.session_state.get("password") == "admin123":
        st.session_state["authenticated"] = True
    else:
        st.error("Authentication failed. Invalid administrator credentials.")

dashboard_page = st.Page("pages/1_Dashboard.py", title="Analytics Dashboard", default=True)
parser_page = st.Page("pages/2_KYC_Parser.py", title="KYC Parser Suite")
synthetic_page = st.Page("pages/3_Synthetic_Data_Studio.py", title="Synthetic Data Studio")
finetune_page = st.Page("pages/4_FineTuning_Studio.py", title="PEFT / LoRA Training")
evaluator_page = st.Page("pages/5_Model_Evaluator.py", title="Model Evaluation Suite")

if st.session_state["authenticated"]:
    st.sidebar.markdown("""
        <div style="padding: 4px 0px 16px 0px; border-bottom: 1px solid #E2E8F0; margin-bottom: 16px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <div style="background: #1E40AF; color: white; width: 28px; height: 28px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 0.85rem;">V</div>
                <div>
                    <div style="font-size: 1.05rem; font-weight: 800; color: #0F172A; letter-spacing: -0.3px; line-height: 1;">VERIX <span style="color:#1E40AF">CORE</span></div>
                    <div style="font-size: 0.72rem; color: #16A34A; font-weight: 700; margin-top: 3px;">● ENGINE ONLINE</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.sidebar.button("Sign Out"):
        st.session_state["authenticated"] = False
        st.rerun()

    pg = st.navigation([dashboard_page, parser_page, synthetic_page, finetune_page, evaluator_page])
    pg.run()

else:
    col_left, col_right = st.columns([1.15, 0.85], gap="large")

    with col_left:
        st.markdown("""
            <div class="brand-header-wrapper">
                <div class="brand-logo-icon">
                    <svg width="26" height="26" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 2L3 7V12C3 17.52 6.84 22.74 12 24C17.16 22.74 21 17.52 21 12V7L12 2Z" fill="white" fill-opacity="0.25"/>
                        <path d="M12 4.18L19 8.07V12C19 16.36 16.03 20.47 12 21.78C7.97 20.47 5 16.36 5 12V8.07L12 4.18ZM12 2L3 7V12C3 17.52 6.84 22.74 12 24C17.16 22.74 21 17.52 21 12V7L12 2Z" fill="white"/>
                        <path d="M10 15.5L7.5 13L8.91 11.59L10 12.67L15.09 7.58L16.5 9L10 15.5Z" fill="white"/>
                    </svg>
                </div>
                <div class="brand-title-text">VERIX <span>PARSER</span></div>
            </div>
            <div class="brand-subtitle">Enterprise Vision Grounding & Document Attribute Extraction Engine</div>
            
            <div class="compliance-banner">
                <b>Protected System Portal:</b> Access restricted to authorized personnel. Operations are recorded for compliance auditing.
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div style="font-size: 0.82rem; font-weight: 700; color: #64748B; letter-spacing: 0.8px; text-transform: uppercase; margin-bottom: 12px;">Core Capabilities</div>
            <div class="capability-card">
                <div class="capability-dot"></div>
                <div class="capability-text">Multi-format document parsing & attribute extraction</div>
            </div>
            <div class="capability-card">
                <div class="capability-dot"></div>
                <div class="capability-text">Sub-pixel spatial bounding box grounding & coordinate mapping</div>
            </div>
            <div class="capability-card">
                <div class="capability-dot"></div>
                <div class="capability-text">Strict schema outputs for core banking & compliance workflows</div>
            </div>
        """, unsafe_allow_html=True)

    with col_right:
        # Streamlit container used to clean up white boxes
        with st.container(border=True):
            st.markdown("""
                <div class="auth-header-block">
                    <div class="auth-header-icon">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5g 0 0 1 10 0v4"></path></svg>
                    </div>
                    <div class="auth-header-title">Administrator Access</div>
                </div>
                <div class="auth-sub">Provide system credentials to authenticate session.</div>
            """, unsafe_allow_html=True)

            st.text_input("Username", key="username", placeholder="Enter administrator ID")
            st.text_input("Password", type="password", key="password", placeholder="Enter secure key")
            
            st.button("Authenticate Session", on_click=login)
            
            # Credential Display Box
            st.markdown("""
                <div class="cred-container">
                    <div class="cred-header">
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
                        Demo Access Credentials
                    </div>
                    <div class="cred-badge-grid">
                        <div class="cred-badge">
                            <div class="cred-label">USER ID</div>
                            <div class="cred-val">admin</div>
                        </div>
                        <div class="cred-badge">
                            <div class="cred-label">PASSWORD</div>
                            <div class="cred-val">admin123</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)