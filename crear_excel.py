import pandas as pd

# -----------------------
# Datos de ejemplo
# -----------------------
data = {
    "Proveedor": ["Alimentos S.A.", "TechGlobal", "Ferretería Lima", "Servimédica"],
    "RUC": ["20100012345", "20567890123", "20458963214", "20334455667"],
    "Categoría": ["Alimentos", "Tecnología", "Construcción", "Salud"],
    "Monto (S/.)": [3500.50, 9800.00, 1250.75, 4100.00],
    "Fecha de Registro": ["2024-01-15", "2024-03-01", "2024-05-10", "2024-06-20"]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Guardar como archivo Excel (en la misma carpeta)
df.to_excel("Proveedores_BSP.xlsx", index=False, sheet_name="Proveedores")

print("✅ Archivo 'Proveedores_BSP.xlsx' creado correctamente.")
