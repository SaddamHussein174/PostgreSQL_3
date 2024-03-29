import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.dialects.postgresql import psycopg2
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:*****5@localhost/postgres", encoding='UTF=8')

connection = engine.connect()



# название и год выхода альбомов, вышедших в 2018 году;

select_request = connection.execute("""SELECT Название_альбома, Год_выпуска FROM Альбомы
WHERE Год_выпуска = 2018;
""").fetchall()

print(select_request)

# название и продолжительность самого длительного трека;

select_request = connection.execute("""SELECT Название_трека, Длительность FROM Треки
WHERE Длительность = (select max(Длительность) FROM Треки);
""").fetchall()

print(select_request)

# название треков, продолжительность которых не менее 3,5 минуты;

select_request = connection.execute("""SELECT Название_трека, Длительность FROM Треки
WHERE Длительность < '00:03:30';
""").fetchall()

print(select_request)

# названия сборников, вышедших в период с 2018 по 2020 год включительно;

select_request = connection.execute("""SELECT Название_сборника FROM Сборники
WHERE  Год_выпуска BETWEEN 2018 AND 2020;
""").fetchall()

print(select_request)

# исполнители, чье имя состоит из 1 слова;

select_request = connection.execute("""SELECT Имя FROM Исполнители 
WHERE NOT LOWER(Имя) like '%% %%';
""").fetchall()

print(select_request)

# название треков, которые содержат слово "мой"/"my"

select_request = connection.execute("""SELECT Название_трека FROM Треки 
WHERE LOWER(Название_трека) like '%%my%%';
""").fetchall()

print(select_request)

# А все! )))
