# Django Calculator

This is a simple **calculator** web application built using **Django**. It provides a REST API for performing basic arithmetic operations like addition, subtraction, multiplication, and division.

## **Features**
- Perform basic arithmetic operations: **Addition, Subtraction, Multiplication, Division**
- REST API powered by Django
- Frontend for user interaction

---

## **Installation & Setup**
### **1. Clone the Repository**
```sh
git clone https://github.com/umeshyadav7988/Django_Calculator.git
cd Django_Calculator
```

### **2. Create & Activate Virtual Environment**
```sh
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Apply Migrations**
```sh
python manage.py migrate
```

### **5. Run the Server**
```sh
python manage.py runserver
```
The server will start at **http://127.0.0.1:8000/**.

---

## **API Endpoints**
| Method | Endpoint               | Description |
|--------|------------------------|-------------|
| POST   | `/api/calculate/`      | Perform calculations |

### **Example Request**
```sh
curl -X POST http://127.0.0.1:8000/api/calculate/ \
     -H "Content-Type: application/json" \
     -d '{"num1": 10, "num2": 5, "operation": "add"}'
```

### **Example Response**
```json
{
  "result": 15
}
```

---

## **Contributing**
Contributions are welcome! Follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

---

## **Contact**
📧 Email: [umeshyadav7988@gmail.com](mailto:umeshyadav7988@gmail.com)  
🔗 GitHub: [umeshyadav7988](https://github.com/umeshyadav7988)

---

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

