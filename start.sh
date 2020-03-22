docker-compose exec api python manager.py db init
docker-compose exec api python manager.py db migrate
docker-compose exec api python manager.py db upgrade