# Flask Application: User Authentication and Session Management

This Flask application provides user authentication and session management functionalities. Users can log in, update their email address, view products, proceed to checkout, and log out. The application also includes error handling and a thank you page for completing a purchase.

## Features

- **User Login**: Users can log in with their name.
- **Session Management**: User sessions are stored to maintain login status.
- **Email Update**: Users can update their email address.
- **Product Viewing**: Users can view available products.
- **Checkout**: Users can proceed to checkout.
- **Error Handling**: Error pages are provided for user convenience.
- **Logout**: Users can log out of their session.

## Installation and Setup

1. Clone the repository to your local machine.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Run the application with `python app.py`.
4. Access the application through a web browser at `http://localhost:5000`.

## File Structure

- `app.py`: Contains the Flask application code, including routes and database configuration.
- `templates/`: Directory containing HTML templates for rendering pages.
- `static/`: Directory containing static files such as CSS and JavaScript.

## Dependencies

- Flask: Micro web framework for Python.
- Flask-SQLAlchemy: Flask extension for database integration.
- Jinja2: Templating engine for Python.

## Usage

1. Navigate to `http://localhost:5000` in your web browser.
2. Log in with your name or create a new account.
3. Update your email address if necessary.
4. Explore the available products and add items to your cart.
5. Proceed to checkout to complete your purchase.
6. Log out of your session when finished.

## Author

This Flask application was developed by Adam Piątek.

If you have any questions or feedback, feel free to reach out!

