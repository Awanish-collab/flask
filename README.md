# Flask Project with Organized UI

## Project Description
This project demonstrates the creation of a Flask web application with an organized structure, including static file management and multiple pages (Home, About, Contact). It is designed to be clean, scalable, and easy to maintain.

## Features
- Dynamic URL generation using Flask's `url_for`.
- Organized static files: CSS, JavaScript, and images.
- Multiple pages:
  - **Home Page**: A welcome page with a brief introduction.
  - **About Page**: Information about the project and Flask framework.
  - **Contact Page**: A contact form with name, email, and message fields.
- Shared navigation bar across all pages.
- Contact form with basic validation.

## Directory Structure
```plaintext
project_root/
├── app.py
├── templates/
│   ├── index.html        # Home page
│   ├── about.html        # About page
│   ├── contact.html      # Contact page
├── static/
│   ├── css/
│   │   └── style.css     # CSS styles
│   ├── js/
│   │   └── script.js     # JavaScript file
│   ├── assets/
│   │   ├── images/
│   │   │   └── logo.png  # Logo image
```

# Installation and Setup

## Clone the Repository

```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

## Set Up a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

## Access the Application

Open your browser and navigate to `http://127.0.0.1:5000`.

# How to Use the Application

## 1. Navigating the Pages

The application consists of several main pages:

* **Home Page**: Provides an introduction to the application.
* **About Page**: Details about the project and its purpose.
* **Contact Page**: Includes a contact form for user interaction.

## 2. Contact Form

The contact form on the Contact Page requires the following information:

* **Name**: Your full name
* **Email**: A valid email address
* **Message**: Your message or query

Once filled, the form can be submitted for backend processing (future enhancements include form submission handling).

## 3. Adding New Pages

To add a new page to the application:

1. Create an HTML file in the `templates/` folder
2. Add a route in `app.py` with `@app.route("/new-page")`
3. Use `url_for` to link the new page in the navigation bar
