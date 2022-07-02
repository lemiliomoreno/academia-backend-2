You can specify environment variables in a `.env` file and then call it at container execution.

Instructions:

1. Build and run specifying `.env` file:
```bash
docker build . -t 3-docker-env
docker run -p 3306:3306 --env-file .env -d 3-docker-env
```
