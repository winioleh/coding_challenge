PG_CONN=postgresql://postgres:password12345@localhost:5432

wingtel-migrate: ## [docker] wingtel migrate
	sh -c "docker-compose run --rm wingtel_web python manage.py migrate"

wingtel-makemigrations: ## [docker] wingtel migrate
	sh -c "docker-compose run --rm wingtel_web python manage.py makemigrations agg_metric core plans purchases subscriptions usage"

wingtel-sqldump: ## [docker] wingtel sql dump
	sh -c "mkdir -p dumps"
	sh -c "pg_dump $(PG_CONN)/wingtel > dumps/wingtel-$(slug).sql"

wingtel-sqldrop: ## [docker] wingtel sql flush
	sh -c "psql $(PG_CONN) -c 'drop database wingtel;'"

wingtel-sqlcreate: ## [docker] wingtel sql create
	sh -c "psql $(PG_CONN) -c 'create database wingtel;'"

wingtel-sqlcreate: ## [docker] wingtel sql create
	sh -c "psql $(PG_CONN) -c 'create database wingtel;'"

wingtel-sqlimport: ## [docker] wingtel sql import
	sh -c "psql $(PG_CONN)/wingtel < dumps/wingtel-$(slug).sql"

wingtel-pgcli: ## [docker] wingtel pgcli
	sh -c "pgcli $(PG_CONN)/wingtel"

wingtel-bash: ## [docker] wingtel bash
	sh -c "docker-compose run --rm wingtel_web bash"

wingtel-djangoshell: ## [docker] wingtel django shell
	sh -c "docker-compose run --rm wingtel_web python manage.py shell"

wingtel-pytest: ## [docker] ebill django test all test files (with pytest!)
	bash -c "time docker-compose run --rm wingtel_web bash -c 'pytest'"
