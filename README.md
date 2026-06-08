<img width="1920" height="1020" alt="Screenshot 2026-06-08 151122" src="https://github.com/user-attachments/assets/2b149336-014e-4668-8de5-0beb42b9e9be" /># 📘 Previous Papers Chatbot

A web-based chatbot application that helps students quickly search and access previous year question papers using subject, year, and semester filters. The system provides an easy-to-use interface with searchable subject selection, paper viewing, and PDF download functionality.

---

## 🚀 Features

* 🔍 Searchable Subject Dropdown
* 📅 Filter papers by Year
* 🎓 Filter papers by Semester
* 📄 View question papers directly in the browser
* ⬇️ Download question papers as PDF
* 🎨 Responsive and user-friendly interface using Tailwind CSS
* ⚡ Fast paper retrieval using Flask backend and JSON dataset

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* Tailwind CSS
* JavaScript

### Backend

* Python
* Flask

### Data Storage

* JSON

---

## 📂 Project Structure

```text
Chatbot_Project/
│
├── app.py
│
├── data/
│   └── papers.json
│
├── static/
│   └── papers/
│       ├── paper1.pdf
│       ├── paper2.pdf
│       └── ...
│
├── templates/
│   └── index.html
│
└── README.md
```

---

## 📋 Dataset Format

The papers are stored in a JSON file.

Example:

```json
[
  {
    "subject": "Mathematics",
    "year": "2024",
    "semester": "2",
    "title": "Linear Algebra and Calculus",
    "url": "static/papers/23BM101T-LAC.pdf"
  },
  {
    "subject": "BEEE",
    "year": "2024",
    "semester": "1",
    "title": "Basic Electrical and Electronics Engineering",
    "url": "static/papers/23EE101T-BEEE.pdf"
  }
]
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Previous-Papers-Chatbot.git
```

### 2. Navigate to Project Directory

```bash
cd Previous-Papers-Chatbot
```

### 3. Install Dependencies

```bash
pip install flask
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

```text
http://127.0.0.1:5000
```

---

## 🔄 Workflow

1. User enters a query.
2. Subject filter appears.
3. User searches and selects a subject.
4. Available years are loaded.
5. User selects year and semester.
6. Matching papers are displayed.
7. User can:

   * View PDF
   * Download PDF

---

## 🎯 Project Objectives

* Simplify access to previous year question papers.
* Reduce time spent searching for academic resources.
* Provide a centralized repository of examination papers.
* Improve student preparation through easy paper availability.

---

## 🔮 Future Enhancements

* AI-powered chatbot responses
* Natural language query support
* Paper recommendations
* Voice search
* User authentication
* Admin panel for paper uploads
* Database integration (MongoDB/MySQL)
* Cloud deployment

## 👩‍💻 Author

**Geethika Polisetti**

B.Tech Student | Computer Science and Engineering

---

## 📄 License

This project is developed for educational and academic purposes.

---

⭐ If you find this project useful, consider giving it a star on GitHub.
