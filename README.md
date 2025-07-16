# 🧠 Python API for Data Validation, Authorization, and Large Dataset Processing

This project is a beginner-friendly Python REST API using **Flask** that supports:

- ✅ JSON data validation
- ✅ Token-based API authorization
- ✅ Efficient large dataset processing with multithreading and map-reduce
- ✅ Descriptive error messages

---

## 📦 Features

- **Validation** of user data and item lists
- **Token Authorization** (`read-token`, `write-token`)
- **Multithreading** and **Map-Reduce** for large dataset processing
- **Error handling** and response formatting

---

## 🛠️ Requirements

- Python 3.8+
- Flask

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/python-api-assessment.git
cd python-api-assessment

2. Create and Activate Virtual Environment (Recommended)
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate


3. Install Dependencies
pip install -r requirements.txt


4.Run the API
python main.py

5. API will run at:
http://localhost:5000

6. Authorization
Authorization: write-token
✅ Valid tokens:

read-token (read-only)

write-token (read + write)


7. Sample curl request:
[
  {
    "user_id": "abc123",
    "email": "user@example.com",
    "timestamp": "2024-09-03T12:30:00Z",
    "items": [
      {"item_id": "item001", "quantity": 2, "price": 9.99}
    ]
  }
]

8.Testing with Postman
Set method to POST

URL: http://localhost:5000/api/data

Add headers:

Content-Type: application/json

Authorization: write-token

In the body, choose raw → JSON and paste your JSON data



9.
api_project/
│
├── main.py           # Flask server
├── validator.py      # JSON validation logic
├── auth.py           # Token authorization
├── processor.py      # Data processing logic
├── sample_data.json  # Sample request body
└── requirements.txt  # Dependencies



