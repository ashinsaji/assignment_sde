from sqlalchemy.orm import Session
import models, schemas

# This function creates a new configuration in the database
# by adding a new entry with the provided configuration data
def create_configuration(db: Session, configuration: schemas.ConfigurationCreate):
    db_configuration = models.Configuration(**configuration.model_dump())
    db.add(db_configuration)
    db.commit()
    db.refresh(db_configuration)
    return db_configuration


# This function retrieves a configuration from the database based on the provided country code
# and returns the first matching configuration
def get_configuration(db: Session, country_code: str):
    return db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()


# This function updates a configuration in the database based on the provided configuration data
# by modifying the existing entry with the matching country code
def update_configuration(db: Session, configuration: schemas.ConfigurationUpdate):
    db_configuration = get_configuration(db, configuration.country_code)
    if db_configuration:
        for key, value in configuration.model_dump().items():
            setattr(db_configuration, key, value)
        db.commit()
        db.refresh(db_configuration)
        return db_configuration
    return None


# This function deletes a configuration from the database based on the provided country code
# by removing the entry with the matching country code
def delete_configuration(db: Session, country_code: str):
    db_configuration = get_configuration(db, country_code)
    if db_configuration:
        db.delete(db_configuration)
        db.commit()
        return True
    return False
