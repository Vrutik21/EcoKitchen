# EcoKitchen 🍽️🌱

EcoKitchen is a web application designed to promote sustainability by helping users manage food items, create recipes, and track their usage history. The application provides an intuitive interface to reduce food waste and streamline kitchen operations.

---

## Features

- **Food Item Management**: Add, update, delete, and export food items with ease.
- **Recipe Integration**: Save, view, and create recipes with a detailed breakdown of ingredients.
- **User History**: Track the history of food usage to monitor and minimize waste.
- **Dashboard Statistics**: Visualize food usage and inventory with clean and interactive charts.
- **Authentication**: Secure user login and logout functionality for personalized experiences.

---

## Project Structure

```
EcoKitchen/
├── Project/
│   └── (Contains project-wide configurations and settings)
├── core/
│   └── (Core functionalities and app logic)
├── .gitignore
├── .prettierrc
├── README.md
├── manage.py
```

---

## Tech Stack

- **Frontend**: HTML5, CSS3, TailwindCSS
- **Backend**: Django
- **Database**: PostgreSQL
- **Charts**: Chart.js for interactive visualizations

---

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/Vrutik21/EcoKitchen.git
   cd EcoKitchen
   ```

2. Set up the virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the server:

   ```bash
   python manage.py runserver
   ```

6. Access the app at:  
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Academic Context

This project was submitted as a course project for **COMP8347 - Internet Applications/Distributed Systems** at **Univerity of Windsor**.
