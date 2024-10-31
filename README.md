# My Django Capstone Project

## Setup with Virtual Environment
1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project folder.
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run the application: `python manage.py runserver`

## Setup with Docker
1. Build the Docker image: `docker build -t my-django-app .`
2. Run the container: `docker run -p 8000:8000 my-django-app`

## Additional Notes
- Ensure you don’t commit sensitive information.
