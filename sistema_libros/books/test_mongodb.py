# test_mongodb.py
from pymongo import MongoClient

def test_connection():
    try:
        # Intentar conectar a MongoDB
        client = MongoClient('localhost', 27017)
        
        # Probar la conexión
        client.server_info()
        
        print("✅ Conexión exitosa a MongoDB!")
        
        # Listar bases de datos disponibles
        dbs = client.list_database_names()
        print("Bases de datos disponibles:", dbs)
        
    except Exception as e:
        print("❌ Error al conectar a MongoDB:", e)

if __name__ == "__main__":
    test_connection()