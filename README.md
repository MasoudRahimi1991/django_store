## 🎬 Demo Video

Watch the live demo of the Django E-Commerce Project here:  
▶️ [Click to watch on GitHub Releases](https://github.com/MasoudRahimi1991/django_shop/releases/tag/v1.0)


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

Admin Panel → http://127.0.0.1:8000/admin/

Shop Homepage → http://127.0.0.1:8000/



---

🗂️ Project Structure

store/
 ┣ myapp/
 ┃ ┣ views/                # home, product_detail, cart, orders, account
 ┃ ┣ templates/
 ┃ ┣ models.py
 ┃ ┣ urls.py
 ┃ ┗ forms.py
 ┗ manage.py


---

📸 UX Highlights

Product gallery with thumbnails and modal zoom.

Display of average rating stars on home and product pages.

Compact order cards with product image, price, and status badge.

“Write Review” form as a collapsible section for a cleaner layout.

Clear separation between user area and admin area.



---

👨‍💻 Author

Masoud Rahimi
Backend Developer – Python | Django
GitHub Profile


---

🇩🇪 Django Shop Projekt

Ein vollständiges E-Commerce-Projekt auf Basis von Django, das sowohl im Backend als auch im Frontend professionell umgesetzt wurde.


---

✨ Hauptfunktionen

👤 Benutzerkonto (User Account)

Profil: Anzeigen und Bearbeiten von Name, E-Mail, Telefonnummer und Adresse.

Favoriten (Favorites): Produkte zu Favoriten hinzufügen oder entfernen.

Warenkorb (Cart): Produkte hinzufügen, Menge ändern, Artikel löschen, Gesamtsumme berechnen.

Bestellungen (Orders): Übersicht aller Bestellungen mit Status (Pending / Paid / Shipped / Delivered / Cancelled) und Detailansicht.

Zahlung (Payment): Übersicht aller offenen Zahlungen und Bestätigung als "Paid".

Bewertungen (Reviews): Sternebewertungen und Kommentare mit Durchschnittsberechnung.


🧩 Produkte & Kategorien

Startseite: Produktkarten mit Bild, Preis, Sternbewertung und Detailansicht.

Produktdetailseite: Bildergalerie mit Thumbnails, Modal-Zoom, „Add to Cart“ & „Add to Favorites“.

Suchfunktion und Kategoriefilter in der Navigationsleiste.


🔐 Admin-Panel

Alle Funktionen können im Django-Adminbereich gesteuert werden:

Verwaltung von Produkten, Kategorien, Preisen und Bildern.

Verwaltung von Bestellungen, Bewertungen, Benutzern und Favoriten.

Statusänderungen von Bestellungen (Pending, Paid, Shipped, Delivered, Cancelled).

Unterstützt Such- und Filterfunktionen sowie Benutzerrechte.


🎨 Benutzeroberfläche (UI)

Erstellt mit Bootstrap 5 und Custom CSS.

Vollständig responsive für Desktop, Tablet und Mobilgeräte.

Stilvolle Karten, Schatteneffekte, Status-Badges und moderne Typografie.



---

🛠️ Technologien

Bereich	Technologie

Backend	Python 3, Django
Frontend	HTML5, Bootstrap 5, CSS, JavaScript
Datenbank	SQLite (standardmäßig), leicht austauschbar mit PostgreSQL/MySQL



---

🚀 Installation

git clone <repo-url>
cd store
python -m venv env
env\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Admin-Panel → http://127.0.0.1:8000/admin/

Shop-Startseite → http://127.0.0.1:8000/



---

🗂️ Projektstruktur

store/
 ┣ myapp/
 ┃ ┣ views/
 ┃ ┣ templates/
 ┃ ┣ models.py
 ┃ ┣ urls.py
 ┃ ┗ forms.py
 ┗ manage.py


---

📸 Benutzererlebnis (UX)

Produktgalerie mit Thumbnails & Modal-Zoom.

Anzeige der durchschnittlichen Bewertung auf Home & Detailseite.

Kompakte Bestellkarten mit Produktbild, Preis und Status-Badge.

„Review schreiben“-Formular als ausklappbare Sektion.

Saubere Trennung zwischen Benutzerbereich und Adminbereich.



---

👨‍💻 Autor

Masoud Rahimi
Backend Entwickler – Python | Django
GitHub Profil

---

