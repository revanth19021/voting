# 🗳️ Online Voting System (Django)

A secure and user-friendly **Online Voting System** built using Django where users can register, view elections, vote for candidates, and admins can monitor results.

---

## 🚀 Features

### 👤 Authentication

* User Registration & Login
* Role-based access:

  * **Admin**
  * **Voter**
* Secure logout functionality

---

### 🗳️ Voting System

* View available elections
* View candidates for each election
* Cast vote for a candidate
* Restriction: **One user → One vote per election**

---

### 📊 Admin Features

* Admin can:

  * View all elections
  * View candidates
  * See voting results
  * Monitor vote counts

---

### 🎯 Core Functionalities

* Role-based dashboards
* Election-wise candidate listing
* Voting validation (no duplicate votes)
* Result calculation

---

### 🎨 UI Features

* Responsive design
* Card-based election display
* Navigation bar across pages
* Clean dashboard UI

---

## 🏗️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS (Internal styling)
* **Database:** SQLite
* **Authentication:** Django built-in auth system

---

## 📁 Project Structure

```text
voting/
│
├── accounts/        # User authentication & profile
├── elections/       # Elections, candidates, votes
├── templates/       # HTML templates
├── static/          # (optional)
├── manage.py
└── db.sqlite3
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/revanth19021/voting
cd voting
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run Server

```bash
python manage.py runserver
```

---

## 🌐 Access URLs

* Home: http://127.0.0.1:8000/
* Login: http://127.0.0.1:8000/accounts/login/
* Elections: http://127.0.0.1:8000/elections/
* Admin Panel: http://127.0.0.1:8000/admin/

---

## 🗳️ How Voting Works

1. User registers and logs in
2. User views available elections
3. Selects an election
4. Views candidates
5. Casts vote
6. Vote is stored and cannot be changed

---

## 🔐 Voting Logic

* Each user can vote **only once per election**
* Duplicate voting is prevented using database checks
* Admin can view total votes per candidate

---

## 🧪 Sample Flow

```text
Register → Login → View Elections → Select Election → Vote → Logout
```

---

## 🔮 Future Enhancements

* 📊 Graphical results (charts)
* 📧 Email verification
* 🔐 OTP-based voting
* 🌍 Deployment (Render / AWS)
* 📱 Mobile optimization

---

## 👨‍💻 Author

Developed by **E Naga Sai Revanth**

---

## ⭐ Support

If you like this project:

* ⭐ Star this repo
* 🍴 Fork it
* 📢 Share with others

---

## 📌 Note

This project is built for **educational purposes** and demonstrates a real-world voting workflow.

---

# 🗳️ Secure Voting Made Simple!
