echo "Waiting for postgres ...."

while ! nc -z user-db 5432; do
    sleep 0.1
done

echo "Posrgres started"

python manage.py run -h 0.0.0.0
