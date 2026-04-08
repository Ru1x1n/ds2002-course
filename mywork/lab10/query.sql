USE ama8us_db;

SELECT songs.title, singers.name, singers.birth_year
FROM songs
JOIN singers
ON songs.singer_id = singers.singer_id
WHERE singers.birth_year = 1999;