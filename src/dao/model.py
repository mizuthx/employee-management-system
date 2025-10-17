# silly script, only for model_chx() of database
base_chx:str = ("""
SELECT COUNT(*) as tablas_existentes
FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = DATABASE() 
AND TABLE_NAME IN (?, ?);
""")
    
