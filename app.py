import MyFramework.Informations     as Infos

import MySQLite.MySQLite            as MySQLite
import MySQLite.DrawIOIntegration   as MySQLiteDrawIO
import json

Infos.Informations(Infos.Informations.Verbosity.PrintBulky)

mySQLite = MySQLite.MySQLite()
result = mySQLite.openConnection("Test.db")

drawIO = MySQLiteDrawIO.DrawIOIntegration(mySQLite)
drawIO.createDrawIOFile("./Test.drawio")


# tableDefintion = {
#     "name" : "TEST_TABELLE",
#     "if not exists" : True,
#     "fields" : [
#         {
#             "name" :        "product_id",
#             "type" :        "INTEGER",
#             "constraint" :  "PRIMARY KEY"
#         },
#         {
#             "name" :        "product_name",
#             "type" :        "TEXT",
#             "constraint" :  "NOT NULL"
#         },
#         {
#             "name" :        "list_price",
#             "type" :        "DECIMAL (10, 2)",
#             "constraint" :  "NOT NULL"
#         },
#         {
#             "name" :        "discount",
#             "type" :        "DECIMAL (10, 2)",
#             "constraint" :  "NOT NULL DEFAULT 0",
#         }
#     ],
#     "contraints" : "CHECK (list_price >= discount AND discount >= 0 AND list_price >= 0)"
# }

# result = mySQLite.createMainTable(tableDefintion)

# result = mySQLite.getTablenames()

# result = mySQLite.getSchema(tableDefintion["name"])

# print(json.dumps(result, indent=3))

# result = mySQLite.closeConnection()
