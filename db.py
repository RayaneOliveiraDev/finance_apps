from sqlalchemy import create_engine
from sqlalchemy.orm  import DeclarativeBase, sessionmaker
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql.sqltypes import String


class Base(DeclarativeBase):
    pass

engine = create_engine("mysql+pymysql://root:")

class User(Base):
    __tablename__ = "users"
    id: mapped_column[int] = mapped_column(primary_key=True)
    name: mapped_column[str] = mapped_column(String(50))
    email: mapped_column[str] = mapped_column(String(50))
    password: mapped_column[str] = mapped_column(String(50))