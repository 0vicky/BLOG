***My Django Movie Blog Project***

A simple and modern blog application built with Django. This project is designed to manage movie reviews, user authentication, categories, and more. It’s fully customizable and ideal for showcasing movie-related content and reviews.

***Demo***
Check out the live demo at https://vicky0.pythonanywhere.com/

***Features***
- **User Authentication:** Register, login, logout, password reset, and account management.
- **Movie Reviews Management:** Create, edit, publish, and delete movie reviews.
- **Categories:** Reviews organized by movie genres (e.g., Action, Drama, Comedy, etc.).
- **Contact Form:** Allows users to contact the site owner.
- **Admin Panel:** Easily manage users, movie reviews, and categories through Django’s admin interface.
- **Custom Permissions:** Create custom groups (Readers, Authors, Editors) with different access levels.

***Installation***
Follow these steps to set up the project locally:

***Prerequisites***
- Python 3.8 or higher
- Django 5.1.4
- MySQL Database (configured in settings)

***Steps to Clone and Run***
1. **Clone the Repository:**
   git clone https://github.com/your-username/my-django-movie-blog.git
   cd my-django-movie-blog

2. **Create a Virtual Environment:**
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install Dependencies:**
   pip install -r requirements.txt

4. **Configure the Database:**
   Ensure you have a MySQL database and update the database settings in myapp/settings.py:
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'movie_blog',
           'USER': 'your-db-username',
           'PASSWORD': 'your-db-password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }

5. **Migrate the Database:**
   python manage.py migrate

6. **Create Superuser:**
   python manage.py createsuperuser

7. **Run the Development Server:**
   python manage.py runserver
   You can access the application by visiting http://127.0.0.1:8000 in your web browser.

***Usage***
- **Customize:** Modify the content and styles within the src directory to suit your personal or professional needs.
- **Add Movie Reviews:** As an Author or Editor, you can easily create, edit, and publish movie reviews.
- **Manage Categories:** Categories are pre-configured, but you can add, edit, or delete them via the admin panel.
- **Contact Form:** Utilize the contact form to allow users to get in touch.

***Contributing***
Contributions are welcome! Feel free to fork the repository, improve features, and submit pull requests.

***License***
This project is open-source and available under the MIT License.
