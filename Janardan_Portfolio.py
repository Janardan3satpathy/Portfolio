import streamlit as st
import pandas as pd
from datetime import datetime
import os
import requests
from streamlit_lottie import st_lottie

# --- Configuration ---
PAGE_TITLE = "Janardan's Profile"
PAGE_ICON = "👋"
NAME = "Janardan Satapathy"
DESCRIPTION = """
Highly proficient in Python and possessing a strong theoretical foundation in Computer Science Engineering (CSE). 
Currently developing expertise in Artificial Intelligence (AI), specifically focusing on Machine Learning (ML) 
methodologies and their integration into robust software solutions. Active in full-stack web development.
"""
EMAIL = "janardan7satapathy@gmail.com" 
RESUME_FILE = "Janardan_Satapathy_Resume.pdf"
PROFILE_PIC = "Photo.jpg"

# --- Page Setup ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")

# --- Helper Function for Lottie Animations ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Load Assets
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_contact = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_u25cckyh.json")

# --- Custom CSS for Styling & Animations ---
st.markdown("""
    <style>
    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Custom Text Styling */
    h1, h2, h3 {
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    p, li, div {
        color: #f0f0f0;
        font-weight: 500;
    }
    /* This targets standard markdown links inside the main app */
    div[data-testid="stMarkdownContainer"] a {
        color: #ffffff !important; /* Force White Text */
        font-weight: bold;
        text-decoration: none;
        background-color: rgba(0, 0, 0, 0.4); /* Semi-transparent black background */
        padding: 4px 10px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
        display: inline-block;
        margin-right: 5px;
    }

    .name-text { 
        color: #FFD700; 
        font-weight: bold; 
        font-style: italic; 
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .name-text:hover {
        color: #fff;
        text-shadow: 0px 0px 10px rgba(255, 215, 0, 0.8);
        transform: scale(1.1);
    }
    
    .contact-header { 
        color: #FF6B6B; 
        font-weight: bold; 
        font-style: italic;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3); 
    }
    
    /* Remove default Streamlit anchor styling to allow our custom footer buttons to work */
    .footer-link {
        text-decoration: none !important;
        color: white !important;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: bold;
        transition: transform 0.2s, opacity 0.2s;
        display: inline-block;
        margin: 5px;
    }
    .footer-link:hover {
        transform: scale(1.05);
        opacity: 0.9;
        color: white !important;
    }

    /* Custom Gradient Divider Line */
    .custom-line {
        border: 0;
        height: 2px;
        background-image: linear-gradient(to right, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.75), rgba(255, 255, 255, 0));
        margin: 25px 0;
    }
    
    /* Input Fields Styling */
    .stTextInput input, .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.9);
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Helper function for custom divider
def gradient_divider():
    st.markdown('<hr class="custom-line">', unsafe_allow_html=True)

# --- Database Helper Functions ---
def save_data(name, email, number, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data = {
        "Timestamp": timestamp,
        "Name": name,
        "Email": email,
        "Number": number,
        "Message": message
    }
    
    # 1. Try Google Sheets (Cloud Database)
    if "gcp_service_account" in st.secrets:
        try:
            import gspread
            from oauth2client.service_account import ServiceAccountCredentials
            
            # Authenticate
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds_dict = dict(st.secrets["gcp_service_account"])
            creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
            client = gspread.authorize(creds)
            
            # Open Sheet
            sheet = client.open("ContactFormResponses").sheet1
            sheet.append_row([timestamp, name, email, number, message])
            return "success_cloud"
        except Exception as e:
            return f"error_cloud: {str(e)}"
            
    # 2. Fallback to Local CSV
    else:
        file_path = "contact_submissions.csv"
        df_new = pd.DataFrame([new_data])
        if not os.path.exists(file_path):
            df_new.to_csv(file_path, index=False)
        else:
            df_new.to_csv(file_path, mode='a', header=False, index=False)
        return "success_local"

# --- Main Layout ---

# Sidebar
with st.sidebar:
    st.header("Downloads")
    if os.path.exists(RESUME_FILE):
        with open(RESUME_FILE, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name=RESUME_FILE,
            mime='application/octet-stream'
        )
    else:
        st.warning("Resume PDF not found.")

# Header Section with Animation
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"<h1 style='text-align: left;'>Welcome to {NAME}'s World</h1>", unsafe_allow_html=True)
        st.write(DESCRIPTION)
    with col2:
        if lottie_coding:
            st_lottie(lottie_coding, height=200, key="coding")

    gradient_divider()

# About Me
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists(PROFILE_PIC):
            st.image(PROFILE_PIC, caption="Janardan's Pic", width=200)
        else:
            st.image("https://placehold.co/200x200?text=Janardan", caption="Janardan's Pic", width=200)
            
    with col2:
        st.header("About Me")
        st.markdown(f"""
        My Name is <span class='name-text'>{NAME}</span>. I'm born & brought up in Bhubaneswar, Odisha.
        
        I am a 7th Semester **B.Tech (CSE)** student at Rajiv Gandhi Prodyogiki Vishwavidyalaya, Bhopal, with a minor in **Artificial Intelligence** from IIT Ropar.
        
        I am eager to apply my skills in intelligent systems development, data analysis, and AI-driven applications.
        """, unsafe_allow_html=True)

# Resume / Stats Section
gradient_divider()
st.header("🎓 Resume & Qualifications")
tab1, tab2, tab3 = st.tabs(["Education", "Experience", "Skills"])

with tab1:
    st.subheader("Education")
    st.write("**B. Tech in Computer Science & Engineering (CSE)**")
    st.caption("Rajiv Gandhi Prodyogiki Vishwavidyalaya, Bhopal | 08/2022 - Present | CGPA: 7.8")
    st.write("**Minor in Artificial Intelligence (AI)**")
    st.caption("Indian Institute Of Technology (IIT), Ropar | 10/2024 - 10/2025")
    st.write("**Class XII (Science)**")
    st.caption("D.A.V Public School Pokhariput, Bhubaneswar | 04/2020 - 03/2022 | 76.2%")
    st.write("**Class X**")
    st.caption("D.A.V Public School Pokhariput, Bhubaneswar | 04/2008 - 03/2020 | 93%")


with tab2:
    st.subheader("Internships")
    st.write("**Python Programming Language** @ Scortek")
    st.caption("08/2024 - 09/2024 | IAST, Bhopal")
    st.write("- Developed and implemented Python-based solutions.")
    
    st.markdown("---")
    
    st.write("**Full Stack Web Development** @ Pantech")
    st.caption("04/2024 - 07/2024 | Pantech Prolabs India")
    st.write("- Built and maintained innovative web applications (Front-end & Back-end).")

with tab3:
    st.subheader("Technical Skills")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("Python")
        st.progress(90)
        st.write("HTML/CSS")
        st.progress(85)
        st.write("JavaScript")
        st.progress(75)
    with col_b:
        st.write("SQL / MySQL")
        st.progress(80)
        st.write("Machine Learning")
        st.progress(70)

# Projects Section
gradient_divider()
st.header("💻 Featured Projects")

with st.expander("Opinion Evaluation", expanded=True):
    st.write("A structured process of examining unstructured customer feedback to identify patterns and gauge sentiment.")
    st.markdown("[View on GitHub](https://github.com/Janardan3satpathy/Opinion-Evaluation) | [🚀 Live App](https://opinion-evaluation.streamlit.app/)")

with st.expander("Name Matcher"):
    st.write("A name-matching system that finds the most similar names from a dataset when a user inputs a name.")
    st.markdown("[View on GitHub](https://github.com/Janardan3satpathy/Name-Matcher) | [🚀 Live App](https://namematcherjanardan.streamlit.app/)")

with st.expander("Recipe Chat Bot"):
    st.write("An AI-based Recipe Chat BOT that is used to provide recipes by only using the ingredients.")
    st.markdown("[View on GitHub](https://github.com/Janardan3satpathy/Receipe-bot) | [🚀 Live App](https://receipebotjanardan.streamlit.app/)")

with st.expander("AI in Market Analysis (Global AI Job Market)"):
    st.write("Developed an advanced ML regression model to accurately predict and analyze global salaries based on key professional and geographic factors.")

gradient_divider()

# Contact Form
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<h2 class='contact-header'>Need Me to Contact You?</h2>", unsafe_allow_html=True)
        st.write("Please fill out the form below.")

        with st.form("contact_form", clear_on_submit=True):
            col_form_1, col_form_2 = st.columns(2)
            with col_form_1:
                name = st.text_input("Name")
                email = st.text_input("E-Mail")
            with col_form_2:
                number = st.text_input("Mobile Number")
            
            message = st.text_area("Message")
            submitted = st.form_submit_button("Submit")
            
            if submitted:
                if not name or not email:
                    st.warning("Please fill in at least Name and Email.")
                else:
                    status = save_data(name, email, number, message)
                    
                    if status == "success_cloud":
                        st.success("Message sent!")
                    elif status == "success_local":
                        st.success("Message saved locally! (CSV)")
                        st.info("Tip: Setup Google Sheets for cloud storage. See setup_guide.md")
                    elif status.startswith("error_cloud"):
                        st.error(f"Cloud Error: {status.split(': ')[1]}")
                        save_data(name, email, number, message) # Retry local save
    with col2:
        if lottie_contact:
            st_lottie(lottie_contact, height=250, key="contact_anim")

gradient_divider()

# Footer / Socials (Refined for proper Mailto function)
with st.container():
    st.markdown("<h3 style='text-align: center;'>Connect with Me</h3>", unsafe_allow_html=True)
    
    # Using HTML/CSS flexbox for the footer ensures the links don't get cut off and the "mailto" works reliably.
    st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center; gap: 15px; flex-wrap: wrap;">
        <a href="mailto:{EMAIL}" class="footer-link" style="background-color: #D44638;">📧 EMAIL</a>
        <a href="https://github.com/Janardan3satpathy" target="_blank" class="footer-link" style="background-color: #333;">💻 GitHub</a>
        <a href="https://www.linkedin.com/in/janardan-satapathy-48189b328/" target="_blank" class="footer-link" style="background-color: #0077B5;">🔗 LinkedIn</a>
        <a href="https://www.instagram.com/_king_of_all_acids_?igsh=MTJrd2dsMHN2b25pYw==" target="_blank" class="footer-link" style="background-color: #E1306C;">📸 Instagram</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.caption("© Developed & Maintained By Janardan Satapathy")






