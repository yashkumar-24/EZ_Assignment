from app.models.user import Base
from app.models.file import File
from app.db import engine

Base.metadata.create_all(bind=engine)