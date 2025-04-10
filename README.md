

# 🕒 ZCLOCK Reborn  
### *Phishing Awareness Trainer | Red Team Simulation Framework*

> ⚡ **Creator:** Y4BN  
> 🔐 Ethical Hacker | Cybersecurity Enthusiast  
> 🧠 Tool built for education, simulation & awareness

---

### 🧠 What is ZCLOCK?

ZCLOCK Reborn is a **highly customizable phishing simulation trainer** designed for:

- 🧪 Ethical hacking labs  
- 🛡️ Cybersecurity awareness campaigns  
- 🧰 Red teaming engagements  
- 🏫 Classroom training environments

---

## ⚠️ Legal Disclaimer

> 🛑 This tool is intended **strictly for educational use**.  
> Do not use on individuals, systems, or networks **without proper consent**.  
> Unauthorized usage may violate laws and terms of service.

---

## ⚙️ Core Features

✅ Cloneable fake login pages:  
`Facebook | Instagram | Twitter | LinkedIn | TikTok | Snapchat`

✅ Realistic 2FA prompt simulation

✅ Live credentials capture via **Telegram Bot API**

✅ Lightweight Flask webserver with customizable UI

✅ Easy deployment with [ngrok](https://ngrok.com)

---

## 🚀 Quick Start

### 🔽 1. Clone the Repo

```bash
git clone https://github.com/yabuna/ZCLOCK_Reborn
cd ZCLOCK_Reborn/ZCLOCK_Reborn
```

---

### 🧪 2. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 🤖 3. Set Up Telegram Bot (Live Alerts)

**Create a bot:**

- Open [@BotFather](https://t.me/BotFather) on Telegram  
- Send: `/newbot`  
- Follow the prompts to name your bot  
- You’ll receive a token like:  
  ```
  123456789:ABCdefGhIjKlMnOpQrStUvWxYz
  ```

**Create a Telegram Group:**

- Add your bot to a new group  
- Use [@userinfobot](https://t.me/userinfobot) to get your group's `chat_id`  
  (Format: `-1001234567890`)

---

### 🔑 4. Configure `.env`

Update your `.env` file:

```env
TELEGRAM_TOKEN=your_bot_token_here
CHAT_ID=-100your_chat_id_here
```

---

### 🏁 5. Run the App

```bash
python app.py
```

> It runs on: `http://127.0.0.1:5000`

Use [ngrok](https://ngrok.com/) to go public:

```bash
ngrok http 5000
```

---

## 🗂 Folder Structure

```
ZCLOCK_Reborn/
├── app.py                  # Main Flask App
├── .env                    # Telegram Bot Config
├── requirements.txt        # Dependencies
├── static/                 # CSS, JS, Logos
│   ├── css/styles.css
│   ├── js/loading.js
│   └── logos/
├── templates/              # HTML phishing templates
│   ├── facebook_login.html
│   ├── instagram_login.html
│   └── ...
└── README.md
```

---

## 🧑‍💻 Author – Y4BN

> “**Teach before breach. Simulate before they're infiltrated.**”

💻 GitHub: [github.com/yabuna](https://github.com/yabuna)

---

## 🧬 Want a Portable .exe or One-file Version?

DM Y4BN or drop an issue on the repo and we’ll hook you up with:

- 🔒 Windows Executable  
- 🌐 Self-hosted Docker version  
- 💾 Auto-ngrok deployer
