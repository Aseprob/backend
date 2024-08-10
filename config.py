import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
    MONGO_URI = os.environ.get(
        'MONGO_URI', 'mongodb://localhost:27017/db')

    # Add more configuration variables as needed
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 't')
    PORT = int(os.environ.get('PORT', 5000))

    # JWT configuration
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'your-jwt-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.environ.get(
        'JWT_ACCESS_TOKEN_EXPIRES', 3600))  # 1 hour by default
