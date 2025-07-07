from db.connection import engine
from sqlalchemy import text


def clean_database():
    with engine.connect() as conn:
        trans = conn.begin()
        try:
            conn.execute(
                text(
                    'TRUNCATE TABLE "Interaction", "Recommendation", "UserHabit", "Profile", "User", "Habit" RESTART IDENTITY CASCADE;'
                )
            )
            trans.commit()
            print("Base de datos limpiada exitosamente.")
        except Exception as e:
            trans.rollback()
            print(f"Error al limpiar la base de datos: {e}")
