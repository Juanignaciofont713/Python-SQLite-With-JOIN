import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('mi_base_de_datos2.db')
cursor = conexion.cursor()

# Crear la tabla 'empleados' si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS empleados
                  (id INTEGER PRIMARY KEY, nombre TEXT, salario REAL)''')

# Crear la tabla 'departamentos' si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS departamentos
                  (id INTEGER PRIMARY KEY, nombre TEXT)''')

# Insertar datos en la tabla 'departamentos'
cursor.execute("INSERT OR IGNORE INTO departamentos (id, nombre) VALUES (1, 'Recursos Humanos')")
cursor.execute("INSERT OR IGNORE INTO departamentos (id, nombre) VALUES (2, 'Finanzas')")
cursor.execute("INSERT OR IGNORE INTO departamentos (id, nombre) VALUES (3, 'IT')")

# Verificar si la columna 'depto_id' ya existe
cursor.execute("PRAGMA table_info(empleados)")
columnas = cursor.fetchall()
columna_depto_id_existe = any(columna[1] == 'depto_id' for columna in columnas)

# Si la columna 'depto_id' no existe, agregarla
if not columna_depto_id_existe:
    cursor.execute("ALTER TABLE empleados ADD COLUMN depto_id INTEGER")

# Insertar empleados en la tabla 'empleados' si no existen
cursor.execute("INSERT OR IGNORE INTO empleados (id, nombre, salario) VALUES (1, 'Juan Ignacio Font', 2500.00)")
cursor.execute("INSERT OR IGNORE INTO empleados (id, nombre, salario) VALUES (2, 'Geronimo Font', 2700.00)")
cursor.execute("INSERT OR IGNORE INTO empleados (id, nombre, salario) VALUES (3, 'Ayrton Cornaglia', 3000.00)")

# Asignar empleados a un departamento
cursor.execute("UPDATE empleados SET depto_id = 1 WHERE nombre = 'Juan Ignacio Font'")
cursor.execute("UPDATE empleados SET depto_id = 2 WHERE nombre = 'Geronimo Font'")
cursor.execute("UPDATE empleados SET depto_id = 3 WHERE nombre = 'Ayrton Cornaglia'")

# Consultar los empleados y sus departamentos usando un JOIN
cursor.execute('''SELECT empleados.nombre, empleados.salario, departamentos.nombre 
                  FROM empleados 
                  JOIN departamentos ON empleados.depto_id = departamentos.id''')

resultados = cursor.fetchall()

for resultado in resultados:
    print(resultado)

# Cerrar la conexión
conexion.close()