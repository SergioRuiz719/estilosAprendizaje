import mysql.connector
import requests
from cuestionario import realizar_test_estilo_aprendizaje

estilo_dominante = realizar_test_estilo_aprendizaje()

# Imprime resultados
print(f"Estilo de aprendizaje dominante: {estilo_dominante}")
