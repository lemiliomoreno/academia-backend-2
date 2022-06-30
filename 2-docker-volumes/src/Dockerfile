FROM mariadb:10.8.3

ENV MARIADB_ROOT_PASSWORD root
ENV MARIADB_USER emilio
ENV MARIADB_PASSWORD emilio
ENV MARIADB_DATABASE test_db

COPY a.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

CMD ["mysqld"]
