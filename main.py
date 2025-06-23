from seeder.seed_users import seed_users
from seeder.seed_habits import seed_habits
from seeder.seed_user_habit import seed_user_habits
from seeder.seed_profiles import seed_profile
from seeder.clean_database import clean_database
from seeder.seed_recommendation import seed_recommendations

def main():
    seed_habits(num_habits=10)
    seed_users(num_users=10)
    seed_profile(num_profiles=10)
    seed_user_habits(num_user_habits=10)
    seed_recommendations(num_recommendations=10)
    # clean_database()


if __name__ == "__main__":
    main()
