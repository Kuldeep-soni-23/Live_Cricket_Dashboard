# 🏏 Live Cricket Dashboard

A real-time cricket dashboard that displays live match scores, match information, teams, and score updates using a Cricket API and AWS services.

## 🚀 Features

- 📡 Live cricket score updates
- 🏏 Match details (Teams, Venue, Status)
- 📊 Real-time scoreboard
- ☁️ AWS Lambda integration
- 🌐 API Gateway for public API access
- 💻 Responsive web dashboard
- ⚡ Fast and lightweight interface

---

## 🛠️ Technologies Used

- HTML
- CSS
- JavaScript
- AWS Lambda
- Amazon API Gateway
- Cricket API
- JSON

---

## 📂 Project Structure

```text
Live-Cricket-Dashboard/
│
├── index.html
├── style.css
├── script.js
├── lambda_function.py
├── README.md
└── screenshots/
```

---

## 📸 Screenshots

Add screenshots of your dashboard here.

```text
screenshots/
├── dashboard-home.png
├── live-score.png
```

---

## ⚙️ Architecture

```text
Cricket API
     ↓
AWS Lambda
     ↓
API Gateway
     ↓
Frontend Dashboard
```

---

## 🚀 How It Works

1. User opens the dashboard.
2. Frontend sends a request to API Gateway.
3. API Gateway triggers AWS Lambda.
4. Lambda fetches live cricket data from the Cricket API.
5. Dashboard displays the latest score and match information.

---

## 🔧 Setup Instructions

### Clone Repository

```bash
git clone https://github.com/manasjain087/Live-Cricket-Dashboard.git
cd Live-Cricket-Dashboard
```

### Deploy Backend

- Create an AWS Lambda Function.
- Add your Cricket API code.
- Create an API Gateway endpoint.
- Enable CORS.

### Run Frontend

Simply open:

```text
index.html
```

or deploy it using:

- GitHub Pages
- Netlify
- Vercel

---

## 🎯 Future Improvements

- Match commentary
- Multiple matches support
- Player statistics
- IPL points table
- Dark mode
- Push notifications

---

## 👨‍💻 Author

**Manas Jain**

- GitHub: https://github.com/manasjain087
- LinkedIn: https://www.linkedin.com/in/YOUR-LINKEDIN-USERNAME/

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub.

---

## 📜 License

This project is licensed under the MIT License.
