import pyodbc
import sys
conn=pyodbc.connect('Driver={SQL Server};'
                    'Server=AYMEN\SQLEXPRESS;'
                    'GestionS;'
                    'Trusted_Connection=yes;')

cursor = conn.cursor()

requete1="Select *  from GestionS.dbo.Fournisseur"
requete2="UPDATE GestionS.dbo.Fournisseur SET VilleF='Lyon' where NoF=1"
requete3="DELETE GestionS.dbo.Fournisseur where NoF=1"
requete5="INSERT INTO GestionS.dbo.Fournisseur VALUES(6,'MArket_BOSS','Toulon',012343545)"


cursor.execute(requete5)
conn.commit()
cursor.execute(requete1)

for row in cursor:
    print(row)


