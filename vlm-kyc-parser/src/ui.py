import streamlit as st

def setup_page_header(page_title: str = "VERIX | Enterprise KYC Intelligence"):
    """
    Applies global dark-green theme across ALL pages with bright readable text,
    renders sidebar branding, and adds the top telemetry header.
    """
    st.set_page_config(
        page_title=page_title,
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

        /* ==========================================
           1. GLOBAL DARK GREEN BACKGROUND & BRIGHT TEXT
        ========================================== */
        html, body, [data-testid="stAppViewContainer"], .stApp { 
            font-family: 'Plus Jakarta Sans', sans-serif !important; 
            background-color: #041B13 !important; /* Deep Royal Green */
            color: #F8FAFC !important; /* Bright White Text */
        }

        [data-testid="stMainBlockContainer"], .main, .block-container {
            background-color: #041B13 !important;
            padding-top: 0.5rem !important;
            padding-bottom: 2rem !important;
            margin-top: 0rem !important;
            max-width: 98% !important;
        }

        /* Hide Streamlit Header Gap */
        header[data-testid="stHeader"] {
            display: none !important;
            height: 0px !important;
        }

        /* ==========================================
           2. UNIVERSAL BRIGHT TEXT OVERRIDES
        ========================================== */
        h1, h2, h3, h4, h5, h6, 
        p, span, label, div, 
        .stMarkdown, .stMarkdown p, 
        [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
            color: #F8FAFC !important;
        }

        /* Subtitles & Descriptions */
        p, .stMarkdown p {
            color: #A7F3D0 !important; /* Soft Mint Green for Secondary Text */
        }

        /* ==========================================
           3. DEEP GREEN SIDEBAR STYLING
        ========================================== */
        [data-testid="stSidebar"], [data-testid="stSidebar"] > div {
            background-color: #02120C !important;
            border-right: 1px solid #0B3C2A !important;
        }

        [data-testid="stSidebar"] * {
            color: #E2E8F0 !important;
        }

        [data-testid="stSidebar"] > div:first-child {
            padding-top: 0.6rem !important;
        }

        /* Sidebar Logo Header Box */
        .sidebar-brand-card {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.25) 0%, rgba(4, 27, 19, 0.9) 100%);
            border: 1px solid rgba(16, 185, 129, 0.4);
            border-radius: 12px;
            padding: 12px 14px;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 12px;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4);
        }

        .sidebar-brand-name {
            font-size: 1.1rem;
            font-weight: 800;
            color: #FFFFFF !important;
            letter-spacing: -0.3px;
            line-height: 1.1;
        }

        .sidebar-brand-tag {
            font-size: 0.68rem;
            color: #34D399 !important;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
        }

        /* Capitalize Streamlit Sidebar Navigation Labels */
        div[data-testid="stSidebarNavSeparator"],
        div[data-testid="stSidebarNav"] span {
            text-transform: capitalize !important;
            color: #E2E8F0 !important;
        }

        /* Active Navigation Item */
        div[data-testid="stSidebarNav"] a[aria-current="page"] {
            background-color: #0B3C2A !important;
            border-radius: 8px !important;
        }

        /* ==========================================
           4. FORM INPUTS, SELECTBOXES & BUTTONS
        ========================================== */
        /* Inputs & Select Boxes */
        div[data-baseweb="select"] > div, input, textarea {
            background-color: #0B2B1F !important;
            border: 1px solid #144D37 !important;
            color: #FFFFFF !important;
            border-radius: 8px !important;
        }

        /* Dropdown options text */
        div[data-baseweb="menu"] * {
            background-color: #07261B !important;
            color: #FFFFFF !important;
        }

        /* File Uploader Container */
        div[data-testid="stFileUploader"] {
            background-color: #07261B !important;
            border: 2px dashed #10B981 !important;
            border-radius: 12px !important;
            padding: 16px !important;
        }

        div[data-testid="stFileUploader"] * {
            color: #E2E8F0 !important;
        }

        div[data-testid="stFileUploader"] button {
            background-color: #059669 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 700 !important;
        }

        /* Cards / Container Containers */
        [data-testid="stVerticalBlock"] > div[style*="background"] {
            background-color: #07261B !important;
            border: 1px solid #0E5238 !important;
            border-radius: 12px !important;
        }

        /* ==========================================
           5. TOP TELEMETRY BAR (FULL WIDTH)
        ========================================== */
        .top-app-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: linear-gradient(180deg, #072B1E 0%, #03170F 100%);
            border: 1px solid #0E5238;
            border-radius: 12px;
            padding: 12px 24px;
            margin-bottom: 22px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
            width: 100%;
            gap: 16px;
            overflow-x: auto;
        }

        .header-section {
            display: flex;
            align-items: center;
            gap: 16px;
        }
        
        .brand-badge {
            background: linear-gradient(135deg, #059669 0%, #10B981 100%);
            color: #FFFFFF !important;
            font-weight: 800;
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 0.9rem;
            letter-spacing: 0.5px;
            display: inline-block;
            box-shadow: 0 2px 10px rgba(16, 185, 129, 0.35);
        }

        .header-metric-group {
            display: flex;
            align-items: center;
            gap: 20px;
            background: rgba(2, 18, 12, 0.7);
            border: 1px solid #0D4730;
            padding: 8px 20px;
            border-radius: 10px;
        }

        .metric-item {
            display: flex;
            flex-direction: column;
        }

        .metric-label {
            font-size: 0.65rem;
            color: #6EE7B7 !important;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.6px;
        }

        .metric-value {
            font-size: 0.88rem;
            color: #FFFFFF !important;
            font-weight: 800;
        }

        .metric-divider {
            width: 1px;
            height: 24px;
            background: #0D4730;
        }
        
        .status-pill {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #02140D;
            border: 1px solid #0E5238;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.78rem;
            font-weight: 600;
            color: #E2E8F0 !important;
        }
        
        .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background-color: #10B981;
            box-shadow: 0 0 8px #10B981;
        }

        .security-badge {
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid #059669;
            color: #34D399 !important;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 6px 14px;
            border-radius: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        </style>
    """, unsafe_allow_html=True)

    # 1. Sidebar Top Logo Box
    with st.sidebar:
        st.markdown("""
            <div class="sidebar-brand-card">
                <svg width="34" height="34" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect width="40" height="40" rx="10" fill="#059669"/>
                    <path d="M12 14L20 28L28 14" stroke="white" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M20 20L25 11" stroke="#34D399" stroke-width="3" stroke-linecap="round"/>
                </svg>
                <div>
                    <div class="sidebar-brand-name">VERIX AI</div>
                    <div class="sidebar-brand-tag">Compliance Engine</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # 2. Full-Width Top Header Telemetry Banner
    st.markdown("""
        <div class="top-app-header">
            <!-- Left Branding -->
            <div class="header-section">
                <div class="brand-badge">VERIX SOVEREIGN</div>
                <div style="display: flex; flex-direction: column;">
                    <span style="font-weight: 800; color: #FFFFFF; font-size: 0.98rem; line-height: 1.2;">Vision-Language Compliance Engine</span>
                    <span style="font-size: 0.76rem; color: #34D399; font-weight: 600;">v2.4-peft-lora • Multimodal Grounding v3</span>
                </div>
            </div>

            <!-- Middle Telemetry Metrics -->
            <div class="header-section">
                <div class="header-metric-group">
                    <div class="metric-item">
                        <span class="metric-label">Inference Latency</span>
                        <span class="metric-value" style="color: #34D399 !important;">142 ms</span>
                    </div>
                    <div class="metric-divider"></div>
                    <div class="metric-item">
                        <span class="metric-label">Grounding Accuracy</span>
                        <span class="metric-value">99.84%</span>
                    </div>
                    <div class="metric-divider"></div>
                    <div class="metric-item">
                        <span class="metric-label">Docs Processed</span>
                        <span class="metric-value">12,480</span>
                    </div>
                    <div class="metric-divider"></div>
                    <div class="metric-item">
                        <span class="metric-label">Active Schema</span>
                        <span class="metric-value" style="color: #A7F3D0 !important;">ISO/IEC 27001</span>
                    </div>
                </div>
            </div>

            <!-- Right Cluster Badges -->
            <div class="header-section">
                <div class="status-pill">
                    <div class="status-dot"></div> GPU CUDA: RTX 4090
                </div>
                <div class="status-pill" style="border-color: #059669; color: #34D399 !important;">
                    QLoRA 4-bit
                </div>
                <div class="security-badge">
                    🔒 SOC2 / HIPAA
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)