# Seeder Smart Habits

Este proyecto permite poblar y limpiar la base de datos del sistema SmartEcoWatch con datos de prueba de manera sencilla.

## Requisitos

- Python 3.10 o superior
- PostgreSQL
- Variables de entorno configuradas en un archivo `.env` (ver ejemplo abajo)

## Instalación

1. **Clona el repositorio:**
   ```sh
   git clone https://github.com/JHOIStack/seeder-smart-habits
   cd seeder-smart-habits
   ```

2. **Crea y activa un entorno virtual (opcional pero recomendado):**
   - **En Windows:**
     ```sh
     python -m venv venv
     venv\Scripts\activate
     ```
   - **En Mac/Linux:**
     ```sh
     python3 -m venv venv
     source venv/bin/activate

3. **Instala las dependencias:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configura el archivo `.env`:**

   Crea un archivo `.env` en la raíz del proyecto con la configuración de tu base de datos. Ejemplo:
   ```
    DATABASE_URL="postgresql://postgres:1234@localhost:5432/smart_habits"
   ```

## Ejecución

1. **Inicia la aplicación:**
   ```sh
   streamlit run main.py
   ```

2. **Uso:**
   - Se abrirá una interfaz web.
   - Puedes limpiar la base de datos o generar datos de prueba (usuarios, hábitos, relaciones, perfiles, recomendaciones e interacciones).
   - Usa los botones para poblar la base según lo que necesites.

## Notas

- Asegúrate de que la base de datos esté creada y accesible antes de ejecutar el seeder.
- Puedes ajustar la cantidad de datos a generar desde la interfaz.

---
