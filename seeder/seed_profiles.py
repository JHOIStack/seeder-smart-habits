import random
from db.connection import SessionLocal
from db.models import User, Profile
from utlis.data import fake_profile


def seed_profile(num_profiles=1):
    session = SessionLocal()

    try:
        users_without_profile = (
            session.query(User)
            .filter(~User.id.in_(session.query(Profile.userId)))
            .all()
        )

        if not users_without_profile:
            print("No hay usuarios sin perfil para crear perfiles")
            return

        selected_users = random.sample(
            users_without_profile, min(num_profiles, len(users_without_profile))
        )

        count = 0
        for user in selected_users:
            data = fake_profile(user_id=user.id)
            profile = Profile(**data)
            session.add(profile)
            count += 1

        session.commit()
        print(f"{count} perfiles han sido creados exitosamente.")
    except Exception as e:
        session.rollback()
        print(f"Error al crear perfiles {e}")
    finally:
        session.close()
