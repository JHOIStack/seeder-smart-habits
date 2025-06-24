from db.connection import SessionLocal
from db.models import User, Habit, UserHabit, Profile, Recommendation

def clean_database():
    session = SessionLocal()
    session.query(Recommendation).delete()
    session.query(UserHabit).delete()
    session.query(Profile).delete()
    session.query(User).delete()
    session.query(Habit).delete()
    session.commit()
    session.close()
    print("Base de datos limpiada exitosamente.")
