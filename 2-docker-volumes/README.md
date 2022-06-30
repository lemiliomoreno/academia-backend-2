Instructions:

1. Build container and run:

```bash
docker build . -t 2-docker-volumes
docker run -p 3307:3306 -d 2-docker-volumes
```

2. Login with your credentials and check for the DB and table created

3. Insert a new record into the `projects` table

```sql
insert into projects (project_name, begin_date, end_date, cost) values ("Project 1", "2022-06-29", "2022-07-29", 1000);
select * from projects;
```

4. Re-build the container and run again

```bash
docker build . -t 2-docker-volumes
docker run -p 3307:3306 -d 2-docker-volumes
```

5. Check the `projects` table, no record will be there

```sql
select * from projects;
```

6. Create a `volume` in the container, name it however you like, in this example we use `host`, located in the host in `D:\development\academia\2-docker-volumes\src\host`

Command should be:
`-v /source/host/volume:/docker/container/folder`

For this example:
`-v D:\development\academia\2-docker-volumes\src\host:/var/lib/mysql`

7. Repeat steps 1-4, data should be persistent
