from db.connection import SessionLocal
from db.models import Recommendation
from utlis.data import fake_recommendation
from db.models import User
import random


def seed_recommendations(num_recommendations=10):
    session = SessionLocal()
    users = session.query(User).all()
    if not users:
        print("No hay usuarios para crear recomendaciones.")
        return

    for _ in range(num_recommendations):
        user = random.choice(users)
        data = fake_recommendation(user.id)
        recommendation = Recommendation(**data)
        session.add(recommendation)

    session.commit()
    session.close()
    print(f"{num_recommendations} recomendaciones se han creado exitosamente.")
