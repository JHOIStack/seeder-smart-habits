from db.connection import SessionLocal
from db.models import User, Region
from utlis.data import fake_user
import random
from sqlalchemy.exc import IntegrityError

def seed_users(num_users=10):
    session = SessionLocal()

    regiones = [
        Region.NORTE,
        Region.CENTRO,
        Region.SUR,
        Region.OCCIDENTE,
        Region.SURESTE,
        Region.CDMX,
        Region.INTERNACIONAL
    ]
    pesos = [0.15, 0.15, 0.05, 0.15, 0.15, 0.25, 0.10]

    created = 0
    attempts = 0
    max_attempts = num_users * 10  

    while created < num_users and attempts < max_attempts:
        data = fake_user()
        data["region"] = random.choices(regiones, weights=pesos, k=1)[0]
        user = User(**data)
        session.add(user)
        try:
            session.commit()
            created += 1
        except IntegrityError:
            session.rollback() 
        attempts += 1

    session.close()
    print(f"{created} usuarios han sido creados exitosamente.")
