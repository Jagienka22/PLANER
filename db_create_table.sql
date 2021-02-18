CREATE TABLE IF NOT EXISTS events 
(
    id integer UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    start_event TIME,
    stop_event TIME,
    description varchar(255)
);