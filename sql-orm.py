from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base()

class Artist(base):
    __tablename__ = "Artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)

class Album(base):
    __tablename__ = "Album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("Artist.artist_id"))

class Track(base):
    __tablename__ = "Track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("Album.album_id"))
    media_type_id = Column(Integer, primary_key=False)
    genre_id = Column(Integer, primary_key=False)
    composer = Column(String)
    milliseconds = Column(Integer, primary_key=False)
    bytes = Column(Integer, primary_key=False)
    unit_price = Column(Float)

Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)

# Query 1 - select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select only the "Name" column from the "Artist" table
#artists = session.query(Artist)
#for artist in artists:
#    print(artist.name)

# Query 3 - select only "Queen" from the "Artist" table
artist = session.query(Artist).filter_by(name="Queen").first()
print(artist.artist_id, artist.name, sep=" | ")

# Query 4 - select only by "ArtistId" #51 from the "Artist" table


# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table


# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
