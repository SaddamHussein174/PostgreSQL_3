import binary as binary
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.dialects.postgresql import psycopg2
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

engine = sqlalchemy.create_engine("postgresql://postgres:*******@localhost:5432/postgres", encoding='UTF=8', echo=True)

connection = engine.connect()

connection_2 = psycopg2.connect(user="postgres", password="*******")
connection_2.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()
sql_create_database = 1
cursor.execute('create database postgres')
cursor.close()
connection.close()

# Исполнители

connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(1,'Michael Jackson');""")
connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(2,'Armin van Buren');""")
connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(3,'The Beatles');""")
connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(4,'Louis Armstrong');""")
connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(5,'Britney Spears');""")
connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(6,'Katy Perry');""")
connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(7,'Ace Of Base');""")
connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(8,'Christina Aguilera');""")

#  жанры

connection.execute("""INSERT INTO Жанры(id_genre, Название_жанра) VALUES(1,'Pop');""")
connection.execute("""INSERT INTO Жанры(id_genre, Название_жанра) VALUES(2,'Trance');""")
connection.execute("""INSERT INTO Жанры(id_genre, Название_жанра) VALUES(3,'Rock');""")
connection.execute("""INSERT INTO Жанры(id_genre, Название_жанра) VALUES(4,'Jazz');""")
connection.execute("""INSERT INTO Жанры(id_genre, Название_жанра) VALUES(5,'Retro');""")

# Создаем Альбомы

connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(1,'Thriller','1982');""")
connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(2,'A State Of Trance Classics','2009');""")
connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(3,'Revolver','1966');""")
connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(4,'The California Concerts','1992');""")
connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(5,'In the Zone','2003');""")
connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(6,'Prism','2013');""")
connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(7,'The Ultimate Collection','2005');""")
connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(8,'Liberation','2018');""")


#  Треки

connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(1,'Beat It','00:04:58',1);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(2,'Bad','00:04:16',1);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(3,'Our Origin','00:04:17',2);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(4,'This Is A Test','00:03:45',2);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(5,'Get Back','00:05:19',3);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(6,'Summertime','00:05:35',4);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(7,'Summertime','00:04:35',4);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(8,'Toxic','00:03:21',5);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(9,'Oops!…I Did It Again','00:03:55',5);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(10,'Roar','00:04:48',6);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(11,'My Dark Horse','00:03:18',6);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(12,'The Sign','00:03:02',7);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(13,'Lucky Love','00:04:11',7);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(14,'Hurt','00:04:27',8);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(15,'Fighter','00:04:29',8);""")


#  Сборники

connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(1,'Сборник_1','2016');""")
connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(2,'Сборник_2','2019');""")
connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(3,'Сборник_3','1982');""")
connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(4,'Сборник_4','2012');""")
connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(5,'Сборник_5','2003');""")
connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(6,'Сборник_6','2001');""")
connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(7,'Сборник_7','2018');""")
connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(8,'Сборник_8','1966');""")

#   Заполнение Альбомы

connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(1, 1);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(2, 1);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(3, 1);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(4, 2);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(5, 3);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(6, 4);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(7, 6);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(8, 7);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(9, 8);""")

#  Заполнение Жанры

connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(1,1);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(1,2);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(1,3);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(1,8);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(1,5);""")

connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(2,3);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(2,6);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(2,7);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(2,8);""")

connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(3,1);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(3,3);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(3,8);""")

connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(4,2);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(4,4);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(4,5);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(4,6);""")

connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(5,1);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(5,2);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(5,3);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(5,6);""")

# Заполнение Сборники

connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,1);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,2);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,3);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,4);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,5);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,8);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,10);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,11);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,15);""")

connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,1);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,2);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,6);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,7);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,8);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,10);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,11);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,16);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,17);""")

connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,1);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,5);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,7);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,8);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,9);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,13);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,14);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,15);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,16);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,17);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,17);""")









