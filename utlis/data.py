from db.models import Region, HabitCategory, HabitStatus, ProfileType
from faker import Faker
from datetime import datetime
from .full import male_names, female_names, domains
import random


faker = Faker()


def fake_user():
    if random.random() < 0.5:
        name = random.choice(male_names)
    else:
        name = random.choice(female_names)
    username = (
        name.lower()
        .replace(" ", "")
        .replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
        .replace("ñ", "n")
    )
    domain = random.choice(domains)
    email = f"{username}{random.randint(1, 99)}{domain}"
    return {
        "name": name,
        "email": email,
        "age": random.randint(12, 70),
        "region": random.choice(list(Region)),
    }


def fake_habit():
    return {
        "name": faker.word(),
        "category": random.choice(list(HabitCategory)),
        "description": faker.sentence(),
    }


def fake_user_habit(user_id, habit_id):
    return {
        "userId": user_id,
        "habitId": habit_id,
        "status": random.choice(list(HabitStatus)),
        "scheduledTime": f"{random.randint(6, 22)}:00",
        "completedAt": None,
    }


def fake_profile(user_id):
    return {"userId": user_id, "profileType": random.choice(list(ProfileType))}


def fake_recommendation(user_id):
    messages = [
        "Hora de apagar las luces",
        "Recuerda cerrar la llave del agua",
        "Evita usar bolsas de plastico hoy",
        "Desconecta los aparatos que no uses",
        "Recuerda llevar tu bolsa reutilizable",
        "Hora de caminar en lugar de usar el coche",
    ]
    now = datetime.now()

    return {
        "userId": user_id,
        "message": random.choice(messages),
        "shownTime": now.strftime("%H:%M"),
    }
