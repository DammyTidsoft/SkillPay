# app.py (Streamlit Frontend)
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("path/to/firebase-key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Post a job
st.title("SkillPay MVP")
title = st.text_input("Job Title (e.g., 'Upload 50 Jumia Products')")
pay = st.number_input("Payment (NGN)", min_value=1000)
if st.button("Post Job"):
    doc_ref = db.collection("jobs").add({
        "title": title,
        "pay": pay,
        "status": "open"
    })
    st.success(f"Job posted! ID: {doc_ref.id}")
