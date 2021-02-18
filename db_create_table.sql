CREATE TABLE IF NOT EXISTS events 
(
    id integer UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    start_event integer,
    stop_event integer,
    description varchar(255)
);