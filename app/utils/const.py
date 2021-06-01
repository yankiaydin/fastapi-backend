

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7


DB_HOST = "localhost"
DB_USER = "admin"
DB_PASSWORD = "admin"
DB_NAME = "firm"
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

UPLOAD_KEY = "6810820ea15a7eb8eca3b2b26a5329c5"
UPLOAD_URL = f"https://api.imgbb.com/1/upload?key={UPLOAD_KEY}"

REDIS_URL = "redis://localhost"
TEST_REDIS_URL = "redis://localhost"

TESTING = False


TEST_DB_HOST = "localhost"
TEST_DB_USER = "test"
TEST_DB_PASSWORD = "test"
TEST_DB_NAME = "test"
TEST_DB_URL = f"postgresql://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_HOST}/{TEST_DB_NAME}"



