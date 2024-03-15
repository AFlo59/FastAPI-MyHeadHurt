#!/bin/sh

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "En attente de la disponibilité de Postgres..."
  sleep 1
done

# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --no-input

gunicorn webapp.wsgi:application --workers=4 --bind=0.0.0.0:8006

# Start the Django development server
# echo "Starting Django development server..."
# python manage.py runserver 0.0.0.0:8000
# #!/bin/sh

# # Effectuer les migrations
# echo "Effectuer les migrations de la base de données..."
# python manage.py makemigrations && python manage.py migrate
# python manage.py runserver 0.0.0.0:8000