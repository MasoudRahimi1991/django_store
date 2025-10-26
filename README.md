# 🛍️ Django Shop Project

A complete **E-Commerce website** built with **Django**, featuring a clean UI, full admin control, and responsive Bootstrap 5 design.

---

## ✨ Key Features

### 👤 User Account
- **Profile:** View and edit username, e-mail, phone, and address.  
- **Favorites:** Add or remove products from your favorites list.  
- **Cart:** Add products, adjust quantities, delete items, and view total price in real time.  
- **Orders:** Track all orders with detailed status (*Pending / Paid / Shipped / Delivered / Cancelled*).  
- **Payment:** Checkout page with total amount summary and payment confirmation.  
- **Reviews:** Rate products with stars and comments; average rating is automatically calculated.

### 🧩 Products & Categories
- **Home Page:** Product cards showing image, price, and average star rating.  
- **Product Details:** Image gallery with thumbnails and modal zoom, “Add to Cart”, “Add to Favorites”.  
- **Search & Filter:** Global search bar and category dropdown in the navigation bar.

### 🔐 Admin Panel
Everything can be controlled from the **Django Admin Panel**:
- Manage **products**, **categories**, **images**, and **prices**.  
- Manage **orders**, **reviews**, **users**, and **favorites**.  
- Change order status (*Pending, Paid, Shipped, Delivered, Cancelled*).  
- Built-in search, filters, and role-based permissions.

### 🎨 User Interface (UI)
- Built with **Bootstrap 5** + custom CSS.  
- Fully **responsive** for desktop, tablet, and mobile.  
- Clean design with hover effects, badges, and modern typography.

---

## 🛠️ Technologies

| Area | Technology |
|------|-------------|
| **Backend** | Python 3, Django |
| **Frontend** | HTML5, Bootstrap 5, CSS, JavaScript |
| **Database** | SQLite (default) – easily switchable to PostgreSQL/MySQL |

---

## 🚀 Installation / Setup

```bash
git clone <repo-url>
cd store
python -m venv env
env\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver