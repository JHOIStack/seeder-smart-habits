from db.models import Region, HabitCategory, HabitStatus, ProfileType, InteractionType
from faker import Faker
from datetime import datetime
from .full import male_names, female_names, domains, habits_by_category
import random


faker = Faker()
used_emails = set()


def fake_user():
    global used_emails

    while True:
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
        email = f"{username}{random.randint(1, 99999)}{domain}"

        if email not in used_emails:
            used_emails.add(email)
            return {
                "name": name,
                "email": email,
                "age": random.randint(12, 70),
                "region": random.choice(list(Region)),
            }


def fake_habit():
    category = random.choice(list(HabitCategory))
    name, description = random.choice(habits_by_category[category.value])

    return {
        "name": name,
        "category": category,
        "description": description,
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


def fake_interaction(user_id, target_id):
    return {
        "userId": user_id,
        "type": random.choice(list(InteractionType)),
        "target": target_id,
        "timestamp": faker.date_time_this_year(),
    }
