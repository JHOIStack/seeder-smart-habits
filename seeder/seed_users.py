from db.connection import SessionLocal
from db.models import User
from utlis.data import fake_user


def seed_users(num_users=10):
    session = SessionLocal()

    for _ in range(num_users):
        data = fake_user()
        users = User(**data)
        session.add(users)
    session.commit()
    session.close()
    print(f"{num_users} usuarios han sido creados exitosamente.")
