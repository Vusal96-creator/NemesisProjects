import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from sqlalchemy import select

engine = create_engine("sqlite:///./qeyd.db")

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Kitab(Base):
    __tablename__ = "qeydler"
    id: Mapped[int] = mapped_column(primary_key=True,nullable=False)
    ad: Mapped[str] = mapped_column(nullable=False)
    muellif:Mapped[str] =mapped_column(nullable=False)

Base.metadata.create_all(engine)

app=FastAPI()

def session_ac():
    session = SessionLocal()
    try :
        yield session
    finally:
        session.close()

class YeniKitab(BaseModel):
    ad : str
    muellif : str

@app.post("/kitab")
def kitab_yarat(kitab:YeniKitab,session: Session = Depends(session_ac)):
    kitab=Kitab(ad=kitab.ad,muellif=kitab.muellif)
    session.add(kitab)
    session.commit()
    session.refresh(kitab)
    return kitab.ad,kitab.muellif


@app.get("/kitablar")
def kitab_yarat2(session: Session = Depends(session_ac)):
    kitablar=session.execute(select(Kitab)).scalars().all()
    return kitablar


import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

@app.get("/hava")
def hava_goster(sheher: str):
    keshde = r.get(sheher)

    if keshde:
        return {"temp": keshde, "menbe": "kesh"}

    temp = "25°C"

    r.set(sheher, temp, ex=3600)

    return {"temp": temp, "menbe": "yeni"}




