# SkillPay 🔥
**Africa's Gig HR Platform for Youth & MSMEs**  
*Connecting unemployed youth with e-commerce gigs via blockchain-secured escrow payments.*

[![Demo](https://img.shields.io/badge/Demo-Live-green)](https://your-demo-link.com)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

---

## 🌍 Problem
- **Youth Unemployment**: 60% of African youth lack formal jobs despite digital skills.
- **MSME Struggles**: Small businesses can’t afford full-time staff for e-commerce tasks.
- **Payment Distrust**: Freelancers fear non-payment; employers fear poor work quality.

## 🚀 Solution
SkillPay is a **WhatsApp/USSD-powered platform** where:
1. **MSMEs** post micro-tasks (e.g., *"Upload 50 Jumia products – ₦5,000"*).
2. **Youth Workers** accept gigs via mobile (no smartphone needed).
3. **Blockchain Escrow** holds payment until work is verified.
4. **Flutterwave/Paystack** enables instant mobile money payouts.

---

## 🔥 Key Features
| Feature                | Tech Used           | Impact                          |
|------------------------|---------------------|---------------------------------|
| USSD/WhatsApp Job Matching | Africa’s Talking API | Reaches low-end phone users     |
| Solana Smart Contracts | Anchor Framework    | Transparent escrow payments     |
| AI Gig Recommendations | Python + Gemini API | Matches skills to jobs          |
| Mobile Money Payouts   | Flutterwave SDK     | Instant withdrawals to M-Pesa   |

---

## 🛠️ Tech Stack
- **Frontend**: Streamlit (Python) / Flutter (mobile)
- **Backend**: Firebase Firestore (NoSQL)
- **Blockchain**: Solana (Anchor) / Celo (for mobile crypto)
- **APIs**: Africa’s Talking (SMS), Flutterwave (payments)

---

## 📌 How to Run (MVP)
```bash
# Clone repo
git clone https://github.com/Dammytidsoft/skillpay.git
cd skillpay

# Install dependencies
pip install -r requirements.txt  # Python: streamlit, firebase-admin, solana-py

# Run Streamlit app (Job Posting UI)
streamlit run app.py

# Simulate Escrow (Solana testnet)
python escrow.py
