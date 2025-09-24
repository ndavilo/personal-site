# Personal Portfolio Website

This is the personal portfolio website of **Engr. Chukwunonso David Ilonze**.  
It showcases professional background, skills, and projects.  

---

## 🚀 Features
- Flask-powered backend
- Dynamic project listing from `projects.csv`
- Responsive design with custom CSS
- SEO and Open Graph meta tags for better search ranking

---

## 📂 Project Structure
```
personal-site/
├── .gitignore
├── app.py
├── requirements.txt
├── README.md
├── __pycache__/
├── venv/
├── data/
│   └── projects.csv
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── D.ico
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/personal-site.git
cd personal-site
```

### 2. Create and activate a virtual environment
Windows (PowerShell):
```powershell
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run locally
```bash
python app.py
```
Open your browser at `http://127.0.0.1:5000`.

---

## 📦 Deployment (AWS EC2)
1. Push code to GitHub.
2. SSH into your EC2 instance.
3. Clone your repository:
   ```bash
   git clone https://github.com/<your-username>/personal-site.git
   cd personal-site
   ```
4. Setup Python environment & install requirements.
5. Use a production server (e.g., Gunicorn + Nginx) for deployment.

---

## 📊 Data
All projects are stored in `data/projects.csv`.  
You can easily add, update, or remove projects without touching HTML.  

---

## 👨‍💻 Author
**Engr. Chukwunonso David Ilonze**  
AWS Certified Professional | Cybersecurity Specialist | Technology Solutions Architect  
[LinkedIn](https://www.linkedin.com/in/chukwunonso-ilonze/) | [Portfolio](https://chukwunonsodavidilonze.ictlagos.com/)
