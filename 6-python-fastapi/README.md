Instructions:

1. Run database:
`docker run -p 5432:5432 --env-file .env -v C:\development\repos\6-python-fastapi\data\db:/var/lib/postgresql/data -d postgres:14`

2. Run the api:
`poetry run python main:app --reload`
