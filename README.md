# Price Alert Application

This Price Alert Application is designed to monitor cryptocurrency prices and send email alerts to users when their specified price targets are reached. It utilizes FastAPI for the backend, PostgreSQL for data storage, and Redis for caching.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Running the Project

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/garvit2435/price-tracker-fastapi.git
    ```

2. Navigate to the project directory:
    ```bash
    cd price_alert_app
    ```

3. Build and run the application using Docker Compose:
    ```bash
    docker-compose up --build
    ```

    This command starts all the services defined in your `docker-compose.yml`, including the FastAPI application and PostgreSQL database.

4. Access the application at `http://localhost:8000`.

## Endpoints

### User Management

- **POST /register/**: Register a new user.
  - Body: `{"email": "user@example.com", "password": "password"}`

- **POST /token**: Obtain a JWT token for an existing user.
  - Body: `{"username": "user@example.com", "password": "password"}`

### Alerts Management

- **POST /alerts/create/**: Create a new price alert.
  - Requires JWT Authentication.
  - Body: `{"currency_pair": "BTCUSD", "target_price": 33000, "direction": "above"}`

- **DELETE /alerts/delete/{alert_id}**: Delete an existing alert.
  - Requires JWT Authentication.

- **GET /alerts/**: Fetch all alerts for the authenticated user.
  - Requires JWT Authentication.
  - Supports query parameters for pagination and filtering by status.

## Sending Alerts Solution

This application monitors real-time cryptocurrency prices using Binance's WebSocket connection. When the price of a specified cryptocurrency reaches the target set by a user, the application triggers an email alert.

- **Real-time Price Monitoring**: Utilizes WebSocket connections to Binance for live price updates.
- **Email Notification**: On matching the target price, an email is sent to the user using SMTP (configured for Gmail in this project).
- **Alert Status Update**: Once an alert is triggered, its status is updated in the PostgreSQL database to "triggered".

## Technologies Used

- **FastAPI**: For the REST API implementation.
- **PostgreSQL**: For storing user and alert data.
- **Redis**: Used as a caching layer for fetching alerts.
- **Docker & Docker Compose**: For containerization and orchestration.

