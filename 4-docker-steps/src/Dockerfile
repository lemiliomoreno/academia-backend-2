FROM node:16-buster-slim AS build
WORKDIR /frontend
COPY app/ .
RUN npm ci
RUN npm run build

FROM nginx:1.21.0-alpine
COPY --from=build /frontend/build/ /usr/share/nginx/html
COPY --from=build /frontend/nginx/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
