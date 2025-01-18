# To-Do App Backend

This repository contains the backend of the To-Do application, developed using Django. It exposes a RESTful API for managing tasks, including creating, retrieving, and updating task statuses.

## Features

- **Create Tasks**: API endpoint to add new tasks.
- **Retrieve Tasks**: API endpoint to fetch all existing tasks.
- **Update Task Status**: API endpoint to toggle the completion status of tasks.

## Getting Started

Follow these steps to set up and run the backend locally.

### Prerequisites

- [Python](https://www.python.org/) (v3.8 or later)
- [pip](https://pip.pypa.io/en/stable/installation/) (v20 or later)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (optional but recommended)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/RamiB1234/my_todo_project.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd my_todo_project
   ```
3. **Create a Virtual Environment** (optional but recommended):
   ```bash
   virtualenv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

1. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```
2. **Create a Superuser** (for accessing the Django admin interface):
   ```bash
   python manage.py createsuperuser
   ```

### Running the Server

Start the development server:
```bash
python manage.py runserver
```
The API will be accessible at `http://127.0.0.1:8000/api/`.

## API Endpoints

- **`GET /api/tasks/`**: Retrieve all tasks.
- **`POST /api/tasks/add/`**: Add a new task.
- **`PUT /api/tasks/set-completed/`**: Update the completion status of a task.

## CORS Configuration

Ensure that Cross-Origin Resource Sharing (CORS) is configured to allow requests from the frontend. This can be set up using the `django-cors-headers` package.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
