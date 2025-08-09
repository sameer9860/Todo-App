

# Todo-App

A simple and intuitive Todo application built with Django, allowing users to manage their tasks efficiently.

## Features

- **User Authentication**: Secure login and registration system.
- **CRUD Operations**: Create, Read, Update, and Delete tasks.
- **Task Prioritization**: Mark tasks as important.
- **Due Dates**: Set deadlines for tasks.
- **Task Completion**: Mark tasks as completed.
- **Responsive Design**: Mobile-friendly interface.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sameer9860/Todo-App.git
cd Todo-App(if you are in another dir)
````

### 2. Set Up Virtual Environment

```bash
python -m venv env
.\env\Scripts\activate  # Windows
source env/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the admin account.

### 6. Run the Development Server

```bash
python manage.py runserver
```

Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).


## License

This project is licensed under the Sameer9860 git License.


