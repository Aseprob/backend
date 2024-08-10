# ASEProb Backend

ASEProb Backend is a Flask-based RESTful API for managing clients, products, and orders. It uses MongoDB as its database and provides JWT authentication for secure access to the API endpoints.

## Features

- RESTful API endpoints for clients, products, and orders
- MongoDB integration for data persistence
- JWT authentication for secure API access
- Dockerized application for easy deployment and scaling
- Environment-based configuration for flexibility across different deployment environments

## Prerequisites

- Python 3.9+
- Docker
- MongoDB (for local development without Docker)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/aseprob-backend.git
   cd aseprob-backend
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your environment variables:
   ```env
   SECRET_KEY=your_secret_key
   MONGO_URI=mongodb://your_mongodb_uri
   DEBUG=True
   PORT=5000
   JWT_SECRET_KEY=your_jwt_secret_key
   JWT_ACCESS_TOKEN_EXPIRES=3600
   ```

## Running the Application

### Local Development

1. Ensure MongoDB is running locally or update the `MONGO_URI` in your `.env` file.

2. Run the Flask application:

   ```sh
   python main.py
   ```

3. The API will be available at `http://localhost:5000`.

### Using Docker

1. Build the Docker image:

   ```sh
   ./build.sh
   ```

2. Run the Docker container:

   ```sh
   ./run.sh
   ```

3. To build and run in one step:
   ```sh
   ./build_and_run.sh
   ```

The API will be available at `http://localhost:5000`.

## API Endpoints

- `/clients` - GET (list all clients), POST (create a new client)
- `/clients/<client_id>` - GET, PUT, DELETE operations for a specific client
- `/products` - GET (list all products), POST (create a new product)
- `/products/<product_id>` - GET, PUT, DELETE operations for a specific product
- `/orders` - GET (list all orders), POST (create a new order)
- `/orders/<order_id>` - GET, PUT, DELETE operations for a specific order

All endpoints require JWT authentication.

## Authentication

To access the API endpoints, you need to include a JWT token in the Authorization header of your requests:

```
Authorization: Bearer <your_jwt_token>
```

## Development

- The `app/` directory contains the core application code.
- Models are defined in `app/models/`.
- Route handlers are in `app/routes/`.
- Authentication logic is in `app/services/auth.py`.
- Database connection is managed in `app/database.py`.

## Testing

(Add information about running tests when you implement them)

## Deployment

This application is containerized and can be easily deployed to any Docker-compatible hosting service. Make sure to set the appropriate environment variables in your production environment.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
