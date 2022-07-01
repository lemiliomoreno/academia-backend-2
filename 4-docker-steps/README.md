You can create steps in a container so you don't have to copy unnecessary files to the built image.

Instructions:

1. Build and run, check the steps, first `npm` is installing the dependencies and creating a `build`, in second step we are using `nginx` to publish that build, instead of passing all `node_modules` folder and making the image bigger:
```bash
docker build . -t 4-docker-steps
docker run -p 80:80 -d 4-docker-steps
```

2. Visit `127.0.0.1` in your browser to view the React app.
