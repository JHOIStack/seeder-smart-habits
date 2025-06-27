from db.connection import SessionLocal
from db.models import Interaction, User, Recommendation, InteractionType
from utlis.data import fake_interaction
import random
from collections import defaultdict


def seed_interactions(num_interactions=10):
    session = SessionLocal()

    users = session.query(User).all()
    recommendations = session.query(Recommendation).all()

    if not users or not recommendations:
        print("Faltan usuarios o recomendaciones para generar interacciones.")
        return

    recommendation_map = defaultdict(list)
    for rec in recommendations:
        recommendation_map[rec.userId].append(rec)

    interactions = []

    # TYPES COMO EN TYPECRIPTs
    interaction_types = [
        InteractionType.CLICK,
        InteractionType.IGNORE,
        InteractionType.COMPLETE,
        InteractionType.SKIP,
    ]
    weights = [0.2, 0.4, 0.2, 0.2]  # ! IGNORE tiene mas peso EN ESA 

    for _ in range(num_interactions):
        user = random.choice(users)
        user_recommendations = recommendation_map.get(user.id)

        if not user_recommendations:
            continue

        recommendation = random.choice(user_recommendations)
        chosen_type = random.choices(interaction_types, weights=weights, k=1)[0]
        data = fake_interaction(user.id, recommendation.id)
        data["type"] = chosen_type  # ! => FUERZA DE TIPO
        interaction = Interaction(**data)
        interactions.append(interaction)

    session.bulk_save_objects(interactions)
    session.commit()
    session.close()

    print(f"{len(interactions)} interacciones creadas exitosamente.")
