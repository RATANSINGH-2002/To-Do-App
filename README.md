# To-Do App

A simple and efficient To-Do application built with **Flask** and **PostgreSQL**.  
This app allows users to manage their daily tasks with an intuitive web interface.

## Features

- Add, edit, and delete tasks
- Mark tasks as completed or pending
- User-friendly web UI
- Persistent data storage with PostgreSQL
- Responsive design with HTML, CSS, and JavaScript

## Tech Stack

- **Backend:** Python (Flask)
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL
- pip (Python package manager)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/RATANSINGH-2002/To-Do-App.git
    cd To-Do-App
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the database:**
    - Create a PostgreSQL database (e.g., `todo_db`)
    - Update the database URI in your Flask app configuration:
      ```python
      SQLALCHEMY_DATABASE_URI = 'postgresql://<username>:<password>@localhost/todo_db'
      ```

4. **Initialize the database:**
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. **Run the app:**
    ```bash
    flask run
    ```

6. **Access the app:**
    Open your browser and go to [http://localhost:5000](http://localhost:5000)

## Folder Structure

```
To-Do-App/
│
├── app.py
├── requirements.txt
├── templates/
│   └── ...
├── static/
│   └── ...
└── README.md
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).
