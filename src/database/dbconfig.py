from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg://bbcxkzwq:kAGRBX_cZegi16YmVvc3YYIYAyJU8zQ1@tuffi.db.elephantsql.com/bbcxkzwq")

Base = declarative_base()
session = Session(engine)