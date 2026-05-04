Docker Full-Stack Application with Nginx Reverse Proxy

A production-style multi-container application built using Docker and Docker Compose, demonstrating real-world DevOps concepts like reverse proxying, service communication, and container orchestration.

🧠 Project Overview

This project consists of:
🌐 Frontend – Static web UI (HTML, JS)
⚙️ Backend – API service (Python Flask)
🔁 Nginx – Reverse proxy & single entry point
🐳 Docker Compose – Multi-container orchestration

🏗️ Architecture
User (Browser)
      ↓
   Nginx (Port 8080)
     /        \
Frontend     Backend API
 (Static)     (Flask)

🔥 Key Features
✅ Multi-container setup using Docker Compose
✅ Nginx reverse proxy for routing traffic
✅ Frontend & backend communication via internal Docker network
✅ Single entry point (no direct backend exposure)
✅ Real-world debugging (routing issues, CORS, container failures)
✅ Clean and modular project structure

📁 Project Structure

docker-fullstack-app/
├── backend/
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   └── script.js
│
├── nginx/
│   ├── Dockerfile
│   └── default.conf
│
├── docker-compose.yml
└── README.md

⚙️ How It Works
User sends request to localhost:8080
Nginx:
Serves frontend (HTML/JS)
Routes /api requests to backend
Backend processes request and returns response
Frontend displays data dynamically

🚀 Getting Started
🔧 Prerequisites
Docker installed
Docker Compose installed

▶️ Run the Application
docker-compose up --build

🌐 Access the App

Open in browser:
http://localhost:8080
🧪 API Endpoints
Endpoint	Description
/	Frontend UI
/api	Backend API

🛠️ Technologies Used
🐳 Docker
📦 Docker Compose
🌐 Nginx
🐍 Python (Flask)
💻 HTML, JavaScript

💡 Key Learnings
Reverse proxy implementation using Nginx
Container networking in Docker
Debugging real-world issues (routing, JSON errors, container crashes)
Building scalable multi-container architecture
Separation of concerns between services

📌 Future Improvements
Add database integration
Implement CI/CD pipeline
Add authentication
Scale backend with load balancing
Add monitoring/logging

🤝 Connect
If you found this project useful or have suggestions, feel free to connect!

⭐ Support
If you like this project, give it a ⭐ on GitHub!
