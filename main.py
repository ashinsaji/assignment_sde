from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/create_configuration/", response_model=schemas.Configuration)
def create_configuration(configuration: schemas.ConfigurationCreate, db: Session = Depends(get_db)):
    db_configuration = crud.get_configuration(db, configuration.country_code)
    if db_configuration:
        raise HTTPException(status_code=400, detail="Configuration already exists for this country")
    return crud.create_configuration(db=db, configuration=configuration)


@app.get("/get_configuration/{country_code}", response_model=schemas.Configuration)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_configuration = crud.get_configuration(db, country_code)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration


@app.post("/update_configuration/", response_model=schemas.Configuration)
def update_configuration(configuration: schemas.ConfigurationUpdate, db: Session = Depends(get_db)):
    db_configuration = crud.update_configuration(db=db, configuration=configuration)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration


@app.delete("/delete_configuration/", response_model=bool)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    success = crud.delete_configuration(db=db, country_code=country_code)
    if not success:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return success
