build:
	sudo docker compose up --build

rebuild:
	sudo docker compose down -v
	sudo docker compose up --build

db:
	sudo docker exec -it abronia-db-1 mysql -u root -p
