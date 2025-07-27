# Contact Book 📞

A sleek, animated web-based contact management application built with Flask and vanilla JavaScript. Features a smooth, responsive UI with sliding panels and real-time contact display.

## ✨ Features

- **Add Contacts**: Create new contacts with name, surname, phone, and email
- **View Contacts**: Browse all contacts in an organized list
- **Contact Details**: Click any contact to view full information
- **Smooth Animations**: CSS transitions and transforms for a polished UX
- **Responsive Design**: Clean, modern interface that adapts beautifully
- **SQLite Database**: Lightweight, file-based data storage
- **RESTful API**: Clean endpoints for contact operations

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip

### Installation

1. **Clone or download the project files**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
contact-book/
├── app.py                 # Main Flask application
├── connection_manager.py  # Database connection context manager
├── requirements.txt       # Python dependencies
├── .users.db             # SQLite database (created after setup)
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── style.css         # Styling and animations
    └── index.js          # Frontend JavaScript
```

## 🛠️ How It Works

### Backend (Flask)
- **`app.py`**: Main application with routes for home, user creation, and user management
- **`connection_manager.py`**: Context manager for safe database connections with automatic rollback
- **Database**: Simple SQLite setup with a single `users` table

### Frontend
- **Animated UI**: Three sliding panels that smoothly transition based on user interaction
- **Form Handling**: Clean form submission for adding new contacts
- **AJAX Requests**: Fetch contact details without page refresh
- **Responsive Design**: Modern CSS with nested selectors and smooth transitions

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page with contact form and list |
| POST | `/` | Create new contact |
| GET | `/user/<id>` | Get specific contact details |
| DELETE | `/user/<id>` | Delete a contact |

## 🎨 UI/UX Features

- **Three-Panel Layout**: Form, contact list, and detail view
- **Smooth Transitions**: 1-second CSS transitions with easing
- **Color Scheme**: Dark violet theme with clean white backgrounds
- **Interactive Elements**: Hover effects and click animations
- **Responsive Typography**: Scalable fonts from 20px to 70px

## 🔧 Customization

### Styling
Edit `static/style.css` to modify:
- Colors (currently using `darkviolet`)
- Animation timing and easing
- Layout dimensions
- Typography

### Database Schema
The current schema is simple:
```sql
CREATE TABLE users (
    name TEXT,
    surname TEXT, 
    email TEXT,
    phone_number TEXT
);
```

Add fields by modifying:
1. Database schema
2. `info_names` tuple in `app.py`
3. Form fields in `index.html`
4. Display logic in `index.js`

## 🐛 Known Issues & Limitations

- No user authentication
- No data validation beyond required fields
- Delete functionality exists in API but not in UI
- No search/filter functionality
- Fixed layout dimensions (not fully responsive)

## 📝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📄 License

This project is open source and available under the MIT License.