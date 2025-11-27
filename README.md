# **Janardan's Portfolio Website**

This is a personal portfolio website built with **Python** and **Streamlit**. It features an interactive UI, resume download, and a contact form that integrates with Google Sheets.

Git hub repository link:- https://github.com/Janardan3satpathy/Portfolio

Deployment link :- https://portfolio-janardan.streamlit.app/

## **Features**

* 🎨 **Interactive UI**: Animated background and Lottie animations.  
* 📱 **Responsive Design**: Works on mobile and desktop.  
* 📄 **Resume Download**: Direct download link for my PDF resume.  
* 📧 **Contact Form**: Saves messages to Google Sheets (Cloud) or CSV (Local fallback).  
* 🔗 **Project Links**: Showcase of my GitHub and deployed Streamlit apps.

## **Technologies Used**

* **Streamlit**: For the web interface.  
* **Pandas**: For data handling.  
* **Google Sheets API (gspread)**: For cloud database integration.  
* **Lottie**: For animations.

## **How to Run Locally**

1. Clone the repository:  
   git clone \[https://github.com/Janardan3satpathy/portfolio.git\](https://github.com/Janardan3satpathy/portfolio.git)

2. Install dependencies:  
   pip install \-r requirements.txt

3. Run the app:  
   streamlit run portfolio\_app.py

## **Cloud Deployment (Streamlit Cloud)**

This app is designed to be deployed on **Streamlit Cloud**.

### **Connecting the Database (Google Drive/Sheets)**

To enable the contact form to save data to your Google Sheet instead of a local file, you must add your service account credentials to the Streamlit Cloud "Secrets".

1. Go to your App Dashboard on Streamlit Cloud.  
2. Click **Settings** \> **Secrets**.  
3. Paste your Google Service Account JSON in the following format:

\[gcp\_service\_account\]  
type \= "service\_account"  
project\_id \= "your-project-id"  
private\_key\_id \= "..."  
private\_key \= "-----BEGIN PRIVATE KEY-----..."  
client\_email \= "..."  
client\_id \= "..."  
auth\_uri \= "..."  
token\_uri \= "..."  
auth\_provider\_x509\_cert\_url \= "..."  
client\_x509\_cert\_url \= "..."  
