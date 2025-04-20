# Flask MVC Basic Application

This is a basic Flask application implementing the MVC (Model-View-Controller) pattern. Currently, it demonstrates the Create operation from CRUD (Create, Read, Update, Delete) operations.

## Project Structure

```
app/
├── controllers/     # Contains the route handlers and business logic
│   └── main.py     # Main controller with routes
├── models/         # Contains database models
│   └── user.py     # User model definition
├── views/          # Contains the templates
│   └── templates/  # HTML templates
│       ├── base.html
│       ├── index.html
│       └── add_user.html
└── __init__.py     # Application factory
```

## Features Implemented

1. **Create Operation**
   - Add new users through a form
   - Store user data in SQLite database
   - Display success/error messages

## CRUD Operations Status

Currently, only the Create operation is implemented. The following operations need to be developed:

1. **Create**: Implemented
   - Add new users
   - Form validation
   - Database insertion

2. **Read**: To be implemented
   

3. **Update**: To be implemented
   

4. **Delete**: To be implemented

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python run.py
   ```

## Learning Objectives

1. Understanding MVC pattern in Flask
2. Working with SQLAlchemy for database operations
3. Form handling and validation
4. Template inheritance with Jinja2
5. Flash messages for user feedback

## Next Steps

To complete the CRUD application, you should implement:

1. **Read Operations**
   - Add a user details page
   - Implement user listing with pagination
   - Add search functionality

2. **Update Operations**
   - Create an edit user form
   - Implement update logic in the controller
   - Add validation for updates

3. **Delete Operations**
   - Add delete confirmation
   - Implement soft or hard delete
   - Handle related data cleanup

## Contributing

Feel free to implement the remaining CRUD operations and submit pull requests. This is a learning project, so any improvements or suggestions are welcome! 