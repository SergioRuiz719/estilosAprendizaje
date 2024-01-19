from pymongo import MongoClient

# Reemplaza <username>, <password>, y <cluster_name> con tus credenciales de MongoDB Atlas
username = "skillroot"
password = "tecno123"
cluster_name = "SKILLFORGE"

# Crea la cadena de conexión para MongoDB Atlas
uri = f"mongodb+srv://{username}:{password}@{cluster_name}.mongodb.net/test?retryWrites=true&w=majority"

# Conecta a la base de datos
client = MongoClient(uri)

# Accede a una base de datos y a una colección
db = client.test_database
collection = db.test_collection

# Ahora puedes realizar operaciones en la colección
