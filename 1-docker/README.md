Instructions:

1. Build `v1` container and run:
```bash
docker build . -t sample-nginx:v1
docker run -p 80:80 -d sample-nginx:v1
```

2. Change `index.html` file, build `v2` container and run
```bash
docker build . -t sample-nginx:v2
docker run -p 8080:80 -d sample-nginx:v2
```

3. Visit `127.0.0.1` and `127.0.0.1:8080` in the browser, should show `v1` and `v2` respectively
