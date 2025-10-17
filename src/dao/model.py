# silly script, only for model_chx() of database
model:dict = {
    'model_base': ("""
SELECT COUNT(*) as tablas_existentes
FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = DATABASE() 
AND TABLE_NAME IN (?, ?);
"""),
    
    'model_data': ("empleado", 'telefono'),
    
    'model_views': ""
}