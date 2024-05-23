# Food Orders

The Food Orders Backend is a robust and scalable API designed to power the Food Orders application, enabling seamless food ordering experiences. This backend service handles user authentication, manages restaurant menus, processes orders, and provides real-time updates on order statuses.

Key features of the Food Orders Backend include:
- **User Authentication:** Secure user registration and login functionalities using JWT (JSON Web Tokens).
- **Restaurant Management:** APIs for adding, updating, and retrieving restaurant information and menus.
- **Order Processing:** Endpoints for placing new orders, updating order statuses, and retrieving order history.
- **Payment Integration:** Secure payment processing integration to handle various payment methods.
- **Real-Time Notifications:** WebSocket or push notifications to provide users with real-time updates on their orders.
- **Scalability:** Designed to handle high traffic loads with efficient database management and caching strategies.

Built with modern web technologies, the Food Orders Backend ensures a smooth and secure operation for the Food Orders application.

## Technologies Used

- **Python** and **Flask**: For building the API endpoints.
- **SQLAlchemy**: For ORM and database management.
- **JWT**: For secure user authentication.
- **PostgreSQL**: As the primary database.
- **Docker**: For containerization and ease of deployment.

## Getting Started

Make sure you have the following installed on your machine:
- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/)

## Installation and Setup

Follow these steps to configure your environment and install the necessary dependencies.

### 1. Install Poetry

If you haven't installed Poetry yet, you can install it by running the following command:

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

### 2. Setup Virtual Environment

```sh
poetry config --local virtualenvs.in-project true
```
### 3. Install Dependencies

```sh
poetry install
```

### 4. Setup Environment Variables

Create a .env file in the root directory of your project. You can use the .env_example file as a template. Fill in the necessary fields in the .env file.

```sh
cp .env_example .env
```

### 5. Run Application
```sh
poetry run flask run
```