import pymysql

class Information():
    def __init__(self,name,idS,idB,band,type,flag):
        self.name= name
        self.idS= idS
        self.idB= idB
        self.band= band
        self.type= type
        self.flag= flag
    def show(self):
        print(self.name)
        print(self.type)
        print(self.band)
        print(self.flag)

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user='root',
            password= '12345',
            db= 'sinsong'
        )
        self.cursor= self.connection.cursor()
    def addSong(self,name,link):

        try:

            sql = 'INSERT INTO song (link , name) VALUES({},{})'
            sql= sql.format(link,name)
            self.cursor.execute(sql)
            self.connection.commit()
            print("ADD SONG")
        except Exception as e:
            raise
    def addBand(self,name,type):
        try:

            sql = 'INSERT INTO  band(type , name) VALUES({},{})'
            sql = sql.format(type, name)
            self.cursor.execute(sql)
            self.connection.commit()
            print("ADD BAND")
        except Exception as e:
            raise
    def addUnion(self,idBand,idSong):
        try:
            sql = 'INSERT INTO `union` (`idSong`, `idBand`, `flag`) VALUES ({},{},{})'
            sql= sql.format(idSong,str(idBand).replace(",",""),"(1)")
            self.cursor.execute(sql)
            self.connection.commit()
            print("ADD  UNION")
        except Exception as e:
            raise
    def searchIdBand(self,nameBand):
        sql= 'SELECT id FROM band WHERE name= {}'
        sql= sql.format(nameBand)
        try:
            self.cursor.execute(sql)
            id = self.cursor.fetchone()
        except Exception as e:
            raise
        if id !=None:
            id= str(id).replace(",","")
        return id
    def searchIdSong(self,nameSong):
        sql= 'SELECT id FROM song WHERE name= {}'
        sql= sql.format(nameSong)
        try:
            self.cursor.execute(sql)
            id = self.cursor.fetchone()
        except Exception as e:
            raise
        if id != None:
            id = str(id).replace(",", "")
        return id
dataBase= DataBase()
def addplus(text):
    text= str("'"+text+"'")
    return text

def ingresarCancion(dataBase):
    print("-----------------------------")
    name= input("NAME SONG:")
    link= input("LINK:")
    band= input("BAND:")
    type= input("TYPE:")
    name = addplus(name.lower())
    band = addplus(band.lower())
    type= addplus(type.lower())
    link= addplus(link)
    idS= dataBase.searchIdSong(name)
    if  idS is None:
        dataBase.addSong(name,link)
        idS= dataBase.searchIdSong(name)
    idB= dataBase.searchIdBand(band)
    if idB is None:
        dataBase.addBand(band,type)
        idB = dataBase.searchIdBand(band)

    dataBase.addUnion(idB,idS)


ingresarCancion(dataBase)



