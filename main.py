import os

from dotenv import load_dotenv

from app import create_app

load_dotenv()  # This loads the .env file


app = create_app()

if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG', 'False').lower() in ('true', '1', 't'),
            port=int(os.environ.get('PORT', 5000)))
