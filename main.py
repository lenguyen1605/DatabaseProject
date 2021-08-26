from typing import List

from fastapi import *
from sqlalchemy.orm import Session
import requests
from starlette.staticfiles import StaticFiles
import models, schemas
from models import Cat
from database import SessionLocal, engine
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/{number}")
def return_images(number: int):
    urls = []
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")
    print(path)
    if not os.path.exists(path):
        os.mkdir(path)
    for i in range(number):
        location = os.path.join(path, 'cat' + str(i) + '.jpg')
        r = requests.get('https://cataas.com/cat')
        with open(location, 'wb') as f:
            f.write(r.content)
        urls.append("http://127.0.0.1:8000/static/cat" + str(i) + ".jpg")
    return str(urls)

@app.post("/", response_model=schemas.Cat)
def create_link(cat: schemas.Cat, db: Session = Depends(get_db)):
    cat_data = Cat(id=cat.id, link=cat.link)
    db.add(cat_data)
    db.commit()
    db.refresh(cat_data)
    return {
        "code": "success",
        "message":"link created"
    }

@app.get("/cats/{cat_id}", response_model=schemas.Cat)
def read_link(cat_id: int, db: Session = Depends(get_db)):
    return db.query(models.Cat).filter(models.Cat.id == cat_id).first()





    
