# 💳 QuickPay – UPI QR Generator
A modern SaaS-style web application to generate UPI payment QR codes instantly.
Built with a clean UI and deployed live on the internet.

## 🚀 Live Demo
https://web-production-2ac5e.up.railway.app/

## 📌 Features
⚡ Instant UPI QR code generation
💰 Add custom amount and payment note
📱 Works with all UPI apps (Google Pay, PhonePe, Paytm)
⬇ Download QR code as image
🎨 Modern SaaS-style UI (responsive design)
🖼 Logo support inside QR
🌐 Deployed and accessible online

## 🛠 Tech Stack
**Backend:** Flask
**Frontend:** HTML, CSS
**QR Generation:** qrcode (Python library)
**Image Processing:** Pillow
**Deployment:** Railway

## 📂 Project Structure
```
upi-qr-generator/
│
├── app.py
├── requirements.txt
├── Procfile
├── logo.png
├── templates/
│   └── index.html
└── static/
```

## ⚙️ Installation & Setup (Run Locally)

```bash
git clone https://github.com/ganeshagani10/QR-Code-Generator
cd upi-qr-generator
pip install -r requirements.txt
python app.py
```

## 🌍 Deployment
This project is deployed using Railway.
Steps followed:
- Pushed code to GitHub
- Connected repository to Railway
- Configured start command using Gunicorn
- Deployed as a live web service


## 👨‍💻 Author
Ganesha R

## ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub!!
