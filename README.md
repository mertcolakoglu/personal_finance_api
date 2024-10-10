# Personal Finance Management API

A comprehensive personal finance management solution built with Django and Django Rest Framework. This API provides a robust backend for tracking expenses, managing budgets, setting financial goals, and gaining insights into personal financial health.

## Table of Contents
- [Personal Finance Management API]
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
  - [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- **User Management**
  - Custom user model with email-based authentication
  - JWT authentication for secure API access
- **Account Management**
  - Multiple account types (checking, savings, credit cards)
  - Balance tracking and updates
- **Transaction Tracking**
  - Income and expense logging
  - Transaction categorization
- **Budget Planning**
  - Create and manage budgets for different categories
  - Track spending against budget limits
- **Financial Goals**
  - Set and track progress towards savings goals
  - Deadline and target amount management
- **Dashboard and Analytics**
  - Overview of financial health
  - Income vs. Expenses analysis
  - Budget adherence insights
- **Category Management**
  - Custom categories for income and expenses
  - Hierarchical category structure

## Technologies Used

- Django
- Django Rest Framework
- Djoser and SimpleJWT for authentication
- python-dateutil for date manipulations
- SQLite (easily adaptable to other databases)

## Project Structure

The project is organized into several Django apps, each responsible for specific functionalities:

- `users`: User authentication and management
- `accounts`: Bank account and credit card management
- `categories`: Income and expense category management
- `transactions`: Transaction logging and tracking
- `budgets`: Budget creation and management
- `goals`: Financial goal setting and tracking
- `dashboard`: Analytics and financial overview

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/mertcolakoglu/personal_finance_api.git
   cd personal_finance_api
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   - Create a `.env` file in the project root
   - Add the following variables:
     ```
     SECRET_KEY=your_secret_key_here
     DEBUG=True
     ```

5. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

## Usage

1. Start the development server:
   ```
   python manage.py runserver
   ```

2. Access the admin panel at `http://localhost:8000/admin/` to manage users, accounts, and other data.

3. Use the API endpoints to interact with the personal finance management system programmatically.

## API Endpoints

Here are some of the main API endpoints:

- User Registration: `POST /auth/users/`
- User Login: `POST /auth/jwt/create/`
- Account List: `GET /api/accounts/`
- Create Transaction: `POST /api/transactions/`
- Budget List: `GET /api/budgets/`
- Create Goal: `POST /api/goals/`
- Dashboard Overview: `GET /api/dashboard/`

For a full list of endpoints and their usage, please refer to the API documentation (TODO: Add link to API docs).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
