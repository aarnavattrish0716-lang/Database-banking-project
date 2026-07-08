# 🏦 Banking Management System

A **role-based Banking Management System** built using **Python, Streamlit, and MySQL**. The application provides separate dashboards and functionalities for **Admin**, **Staff**, and **Customer** users, enabling secure banking operations such as account management, deposits, withdrawals, fund transfers, loan management, and transaction tracking.

---

## 🚀 Features

### 🔐 Authentication
- Secure login system
- Role-Based Access Control (RBAC)
- Separate dashboards for:
  - 👨‍💼 Admin
  - 👨‍💻 Staff
  - 👤 Customer
- Session-based authentication using Streamlit Session State

---

### 👨‍💼 Admin Module
- Dashboard with banking statistics
- Manage Users
  - Add User
  - View Users
  - Delete Users
- Manage Branches
  - Add Branch
  - View Branches
  - Delete Branches
- Manage Accounts
  - Create Account
  - Freeze/Activate Account
  - View Accounts
- Manage Loans
  - View Loan Requests
  - Approve/Reject Loans
- View All Transactions

---

## 🛠 Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### Database
- MySQL

### Database Features
- Stored Procedures
- Triggers
- Views
- Transactions
- Foreign Keys
- Constraints

### Tools
- Git
- GitHub
- VS Code

---

## 📂 Project Structure

```
Banking-Management-System/
│
├── admin/
│   ├── 1_home.py
│   ├── 2_users.py
│   ├── 3_accounts.py
│   ├── 4_branches.py
│   ├── 5_loans.py
│   └── 6_transactions.py
│
├── staff/
│   ├── 1_home.py
│   ├── 2_deposit.py
│   ├── 3_withdraw.py
│   └── 4_transfer.py
│
├── customer/
│   ├── 1_home.py
│   ├── 2_accounts.py
│   ├── 3_transfer.py
│   └── 4_transactions.py
│
├── app.py
├── auth.py
├── db.py
├── utils.py
├── database.sql
├── requirements.txt
└── README.md
```

---

## 🗄 Database Design

### Tables

- Users
- Branches
- Accounts
- Transactions
- Loans

### Views

- `customer_account_view`
- `customer_transactions_view`

### Stored Procedures

- `deposit_money()`
- `withdraw_money()`
- `transfer_money()`

### Trigger

- Prevent negative account balances

---

## 🔒 Role Permissions

### Admin
- Full access to the system
- Manage users
- Manage branches
- Manage accounts
- Approve/Reject loans
- View transactions

### Staff
- Deposit money
- Withdraw money
- Transfer money
- View accounts and transactions

### Customer
- View own accounts
- View transaction history
- Transfer funds
- Apply for loans

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/Banking-Management-System.git
cd Banking-Management-System
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

- Create a MySQL database.
- Execute `database.sql`.
- Update the database credentials in `db.py`.

Example:

```python
host="localhost"
user="root"
password="your_password"
database="bankingsystem"
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

---


## 📚 Concepts Demonstrated

- CRUD Operations
- Role-Based Access Control (RBAC)
- Session Management
- SQL Joins
- Stored Procedures
- Database Transactions
- Triggers
- Views
- Foreign Key Constraints
- ACID Properties
- Streamlit Multi-Page Navigation

---

## 📈 Future Improvements

- Password hashing using bcrypt
- Email notifications
- Charts and analytics dashboard
---


