use test_db;

create table projects(
    project_id int auto_increment,
    project_name varchar(255) not null,
    begin_date date,
    end_date date,
    cost decimal(15,2) not null,
    created_at timestamp default current_timestamp,
    primary key(project_id)
);