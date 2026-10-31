from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
def salamlama():
    return {"mesaj": "Salam Dunya"}


@app.get("/hava/baku")
def hava_al():
    return {"sheher": "Bakı", "temp": 25}

@app.post("/kitab")
def kitab_sifarisi():
    return {"mesaj":"10 kitab elave edildi"}

@app.get("/istifadeciler/{id}")
def istifadecini_tap(id:int):
    return f"Istifadeci tapildi, nomre : {id}"

@app.get("/istifadeciler")
def istifadechi_tap2(id:int=9):
    return f"Istifadechi tapildi , nomre : {id}"


class Istifadeci(BaseModel):
    yash: int
    name: str

@app.post("/istifadechi")
def istifadechi_elave(insan:Istifadeci):
    return insan.yash,insan.name


from fastapi import FastAPI


@app.get("/kvadrat/{eded}")
def kvadrat_hesabla(eded: int):
    return {"eded": eded, "kvadrat": eded ** 2}



from fastapi import FastAPI
from pydantic import BaseModel



class Mehsul(BaseModel):
    ad: str
    qiymet: float

@app.post("/mehsul")
def mehsul_elave_et(mehsul: Mehsul):
    return {"mesaj": f"{mehsul.ad} məhsulu {mehsul.qiymet} AZN qiymətə əlavə edildi"}















