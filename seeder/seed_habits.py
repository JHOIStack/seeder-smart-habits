from db.connection import SessionLocal
from db.models import Habit
from utlis.data import fake_habit


def seed_habits(num_habits=10):
    session = SessionLocal()

    for _ in range(num_habits):
        data = fake_habit()
        habit = Habit(**data)
        session.add(habit)

    session.commit()
    session.close()
    print(f"{num_habits} hábitos han sido creados exitosamente.")
