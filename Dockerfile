FROM nginx:1.23.0

ENV MARIADB_USERNAME emilio
ENV MARIADB_PASSWORD mysupersecretpassword

COPY index.html /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
