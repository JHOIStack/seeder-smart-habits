import streamlit as st
from seeder.seed_users import seed_users
from seeder.seed_habits import seed_habits
from seeder.seed_user_habit import seed_user_habits
from seeder.seed_profiles import seed_profile
from seeder.seed_recommendation import seed_recommendations
from seeder.seed_interaction import seed_interactions
from seeder.clean_database import clean_database

st.title("Seeder SmartEcoWatch")

st.markdown("### Limpieza de base de datos")
if st.button("Limpiar Base de Datos"):
    clean_database()
    st.success("Base de datos limpiada exitosamente.")

st.markdown("---")

st.markdown("### Generar datos de prueba")

num_users = st.number_input("Número de usuarios", min_value=0, value=200000, step=200000)
num_habits = st.number_input("Número de hábitos", min_value=0, value=150000, step=150000)
num_user_habits = st.number_input("Número de relaciones usuario-hábito", min_value=0, value=300000, step=300000)
num_profiles = st.number_input("Número de perfiles", min_value=0, value=100000, step=100000)
num_recommendations = st.number_input("Número de recomendaciones", min_value=0, value=150000, step=150000)
num_interactions = st.number_input("Número de interacciones", min_value=0, value=100000, step=100000)

if st.button("Crear usuarios"):
    seed_users(num_users)
    st.success(f"{num_users} usuarios creados.")

if st.button("Crear hábitos"):
    seed_habits(num_habits)
    st.success(f"{num_habits} hábitos creados.")

if st.button("Crear relaciones usuario-hábito"):
    seed_user_habits(num_user_habits)
    st.success(f"{num_user_habits} relaciones usuario-hábito creadas.")

if st.button("Crear perfiles"):
    seed_profile(num_profiles)
    st.success(f"{num_profiles} perfiles creados.")

if st.button("Crear recomendaciones"):
    seed_recommendations(num_recommendations)
    st.success(f"{num_recommendations} recomendaciones creadas.")

if st.button("Crear interacciones"):
    seed_interactions(num_interactions)
    st.success(f"{num_interactions} interacciones creadas.")

if st.button("Crear todo automáticamente"):
    seed_users(num_users)
    st.success(f"{num_users} usuarios creados.")
    seed_habits(num_habits)
    st.success(f"{num_habits} hábitos creados.")
    seed_user_habits(num_user_habits)
    st.success(f"{num_user_habits} relaciones usuario-hábito creadas.")
    seed_profile(num_profiles)
    st.success(f"{num_profiles} perfiles creados.")
    seed_recommendations(num_recommendations)
    st.success(f"{num_recommendations} recomendaciones creadas.")
    seed_interactions(num_interactions)
    st.success(f"{num_interactions} interacciones creadas.")
