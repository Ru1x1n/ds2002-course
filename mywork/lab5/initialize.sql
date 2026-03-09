USE ama8us_db;

DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS singers;

CREATE TABLE singers (
    singer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    birth_year INT
);

CREATE TABLE songs (
    song_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    singer_id INT,
    FOREIGN KEY (singer_id) REFERENCES singers(singer_id)
);

INSERT INTO singers (name, birth_year) VALUES ('A', 1999);
INSERT INTO singers (name, birth_year) VALUES ('B', 1999);
INSERT INTO singers (name, birth_year) VALUES ('C', 1999);
INSERT INTO singers (name, birth_year) VALUES ('D', 1999);
INSERT INTO singers (name, birth_year) VALUES ('E', 1999);
INSERT INTO singers (name, birth_year) VALUES ('F', 2000);
INSERT INTO singers (name, birth_year) VALUES ('G', 2000);
INSERT INTO singers (name, birth_year) VALUES ('H', 2000);
INSERT INTO singers (name, birth_year) VALUES ('I', 2001);
INSERT INTO singers (name, birth_year) VALUES ('J', 2001);

INSERT INTO songs (title, singer_id) VALUES ('L', 1);
INSERT INTO songs (title, singer_id) VALUES ('M', 2);
INSERT INTO songs (title, singer_id) VALUES ('N', 3);
INSERT INTO songs (title, singer_id) VALUES ('O', 4);
INSERT INTO songs (title, singer_id) VALUES ('P', 5);
INSERT INTO songs (title, singer_id) VALUES ('Q', 6);
INSERT INTO songs (title, singer_id) VALUES ('R', 7);
INSERT INTO songs (title, singer_id) VALUES ('S', 8);
INSERT INTO songs (title, singer_id) VALUES ('T', 9);
INSERT INTO songs (title, singer_id) VALUES ('U', 10);
