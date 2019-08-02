from PyDbLite import Base

db = Base()
db.create("Acc", "Gyro")

db.insert(Acc = "136", Gyro = "162")

print(db)