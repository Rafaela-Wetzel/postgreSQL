from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class MusicGenres(base):
    __tablename__ = "Music Genres"
    id = Column(Integer, primary_key=True)
    genre = Column(String)
    favorite_band = Column(String)
    nationality = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Progammer table

death_metal = MusicGenres(
    genre = "Death Metal",
    favorite_band = "Excoriate",
    nationality = "German"
)

black_metal = MusicGenres(
    genre = "Black Metal",
    favorite_band = "Mayhem",
    nationality = "Norway"
)

thrash_metal = MusicGenres(
    genre = "Thrash Metal",
    favorite_band = "Destruction",
    nationality = "German"
)

heavy_metal = MusicGenres(
    genre = "Heavy Metal",
    favorite_band = "Judas Priest",
    nationality = "United Kingdon"
)

doom_metal = MusicGenres(
    genre = "Doom Metal",
    favorite_band = "Electric Wizard",
    nationality = "United States"
)

#session.add(death_metal)
#session.add(black_metal)
#session.add(thrash_metal)
#session.add(heavy_metal)
#session.add(doom_metal)

#session.commit()

music_genres = session.query(MusicGenres)
for music_genre in music_genres:
    if music_genre.nationality == "German":
        music_genre.nationality = "Germany"
    session.commit()




#music_genres = session.query(MusicGenres)
#for music_genre in music_genres:
#    session.delete(music_genre)
#    session.commit()   

# query the database to find all music genres
music_genres = session.query(MusicGenres)
for genre in music_genres:
   print(
       genre.id,
       genre.favorite_band,
       genre.nationality,
       sep=" | "
   )
