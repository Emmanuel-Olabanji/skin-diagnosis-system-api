from decouple import config

MONGO_USERNAME = config("MONGO_USERNAME", default="")
MONGO_PASSWORD = config("MONGO_PASSWORD", default="")
MONGO_CLUSTER = config("MONGO_CLUSTER", default="")
DB_NAME = config("DB_NAME", default="Skin_Cancer_Diagnosis")
CASES_DB_COLLECTION = config("CASES_DB_COLLECTION", default="Cases")
DOCTORS_DB_COLLECTION = config("DOCTORS_DB_COLLECTION", default="Doctors")
PATIENTS_DB_COLLECTION = config("PATIENTS_DB_COLLECTION", default="Patients")
API_DB_COLLECTION = config("API_DB_COLLECTION", default="Users-API-Keys")
IMAGES_DB_COLLECTION = config("IMAGES_DB_COLLECTION", default="Images")
ML_API_URL = config("ML_API_URL", default="http://localhost:8000/predict")

SECRET_KEY = config("SECRET_KEY", default="dev_secret_key")
ALGORITHM = config("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(config("ACCESS_TOKEN_EXPIRE_MINUTES", default=60))
BCRYPT_SALT_ROUNDS = int(config("BCRYPT_SALT_ROUNDS", default=12))
PORT = int(config("PORT", default=8000))
LOGGING_ENABLED = config("LOGGING_ENABLED", default="FALSE").upper() == "TRUE"

MONGO_URI = (
    f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/"
    f"?retryWrites=true&w=majority"
)
