from app import create_app
import os

from dotenv import load_dotenv

load_dotenv()  # This loads the .env file


app = create_app()

if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', 'False').lower() in ('true', '1', 't'),
            port=int(os.getenv('PORT', 5000)))
