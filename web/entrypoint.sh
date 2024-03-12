#!/bin/sh

# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --no-input

# gunicorn webapp.wsgi:app --workers=1 --bind=0.0.0.0:80 --reload

# Start the Django development server
echo "Starting Django development server..."
python manage.py runserver 0.0.0.0:8000
# #!/bin/sh

# # Effectuer les migrations
# echo "Effectuer les migrations de la base de données..."
# python manage.py makemigrations && python manage.py migrate
# python manage.py runserver 0.0.0.0:8000