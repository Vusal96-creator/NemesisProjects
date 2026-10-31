import psycopg2   # körpü kitabxanamızı çağırırıq

# connect() — Postgres-ə bağlantı yaradır
# Buradakı 5 məlumat DataGrip-də doldurduğumuz eyni 5 xanadır
conn = psycopg2.connect(
    host="localhost",        # database harada yerləşir: öz kompüterimizdə
    port=5432,               # Postgres-in qapı nömrəsi
    database="ai_course2",    # DataGrip-də yaratdığımız database
    user="postgres",         # istifadəçi adı
    password="Vusal9696="   # sizin şifrəniz
)

print("Postgres-ə uğurla qoşulduq!")

conn.close()   # işimiz bitdi — bağlantını bağlayırıq


from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, DateTime


# 1. Engine — bağlantı hovuzunu idarə edir
# echo=True etsəniz, arxa planda gedən SQL-ləri görəcəksiniz (debug üçün)
# postgresql://istifadəçi:şifrə@host:port/database_adı
engine = create_engine("postgresql+psycopg2://postgres:Vusal9696=@localhost:5432/ai_course2")


# 3. Session fabrikası
# autocommit=False → dəyişiklikləri özümüz commit etməliyik
SessionLocal = sessionmaker(bind=engine)

# 4. Baza sinifi — bütün modellərimiz bunu miras alacaq
Base = declarative_base()


from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

class Kitab(Base):
    __tablename__ = "kitablar2"

    id =Column(Integer, primary_key=True)
    name=Column(String)
    muellif=Column(String)

    def __repr__(self):
        return f"<Kitab(id={self.id}, name='{self.name}', muellif='{self.muellif}')>"

Base.metadata.create_all(bind=engine)


db=SessionLocal()
#
k1=Kitab(name="Lost Symbol",muellif="Dan Brown")
db.add(k1)
db.commit()
db.refresh(k1)
#
print("Added book")



# axtardigim_kitab=(db.query(Kitab).filter(Kitab.name=="Bookworm").first())
#
# print("Found book:")
# print(axtardigim_kitab)


# axtardigim_kitab=(db.query(Kitab).filter(Kitab.name=="Bookworm").first())
# axtardigim_kitab.name="metamorfoz2"
# db.commit()
# db.refresh(axtardigim_kitab)
#
# print("Updated book:")
# print(axtardigim_kitab)


# k=db.query(Kitab).filter(Kitab.name=="metamorfoz2").first()
# db.delete(k)
#
# db.commit()
# print("Silindi")



db.close()



