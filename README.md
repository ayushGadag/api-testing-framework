# 🚀 API Testing Framework (Python + Pytest)

## 📌 Project Overview

This project is a **REST API Automation Testing Framework** built using Python.
It is designed to test APIs by validating response status codes and response data.

---

## 🛠️ Tech Stack

* Python
* Pytest
* Requests
* JSON

---

## 📁 Project Structure

```
api-testing-framework/
│
├── tests/              # Test cases
├── utils/              # API client (reusable code)
├── data/               # Test data (JSON files)
├── reports/            # Test reports
│
├── requirements.txt    # Dependencies
├── pytest.ini          # Pytest config
├── README.md           # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/ayushGadag/api-testing-framework.git
cd api-testing-framework
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run Tests

```
python -m pytest
```

---

## ✅ Sample Test Case

* Validate GET Users API
* Check status code = 200
* Verify response contains "users"

---

## 🎯 Features

* API request handling using Requests
* Automated test execution using Pytest
* Structured framework (scalable)
* Easy to extend for more APIs

---

## 🚀 Future Improvements

* Add POST, PUT, DELETE APIs
* Add schema validation
* Integrate Allure reports
* Add CI/CD (GitHub Actions)

---

## 👨‍💻 Author

Ayush Gadag
