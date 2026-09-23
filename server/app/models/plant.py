from app.db import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import Mapped,mapped_column 

class Plant(db.Model,SerializerMixin):
    __tablename__="plants"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    image:Mapped[str]
    price:Mapped[int]


    def __repr__(self):
        return f"<Plant {self.id}  {self.name}>"