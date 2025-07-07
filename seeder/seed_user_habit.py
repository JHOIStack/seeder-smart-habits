from db.connection import SessionLocal
from db.models import UserHabit, User, Habit
from utlis.data import fake_user_habit
import random


def seed_user_habits(num_user_habits=10):
    session = SessionLocal()

    try:
        users = session.query(User).all()
        habits = session.query(Habit).all()

        if not users or not habits:
            print("No hay usuarios o hábitos disponibles para crear relaciones.")
            return

        for _ in range(num_user_habits):
            user = random.choice(users)
            habit = random.choice(habits)

            data = fake_user_habit(user_id=user.id, habit_id=habit.id)
            user_habit = UserHabit(**data)
            session.add(user_habit)

        session.commit()
        print(
            f"{num_user_habits} relaciones de usuario-hábito han sido creadas exitosamente."
        )
    except Exception as e:
        session.rollback()
        print(f"Error al crear relaciones de usuario-hábito: {e}")
    finally:
        session.close()
