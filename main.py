import pymysql
import webbrowser as o

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
    def searchLinkSong(self,nameSong):
        sql= 'SELECT link FROM song WHERE name={}'
        sql=sql.format(nameSong)
        try:
            self.cursor.execute(sql)
            link= self.cursor.fetchone()
        except Exception as e:
            raise
        return link

    def searchsBands(self):
        sql= 'SELECT name FROM band'
        try:
            self.cursor.execute(sql)
            bands= self.cursor.fetchall()
        except Exception as e:
            raise
        return bands

    def searchIdbandUnion(self, name):
        id = self.searchIdBand(name)
        rta=id
        if id != None:
            sql = 'SELECT idSong FROM sinsong.union WHERE idBand= {}'
            sql= sql.format(id)

            try:
                self.cursor.execute(sql)
                ids = self.cursor.fetchone()
                rta=ids
            except Exception as e:
                raise
        return rta
    def searchSongWithid(self,id):
        sql='SELECT name FROM song WHERE id={}'
        sql= sql.format(str(id).replace(",",""))
        try:
            self.cursor.execute(sql)
            name= self.cursor.fetchone()
        except Exception as e:
            raise
        return  name


dataBase= DataBase()
def addplus(text):
    text= str("'"+text+"'")
    return text

def addSong(dataBase):
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

def correction(text):
    text= str(text)
    text=text.replace("('","")
    text= text.replace("',)","")
    return text
#ingresarCancion(dataBase)
def showSong(link):
    o.open(link)
def searchSong(database):
    name = input("NAME SONG:")
    name = addplus(name.lower())
    link= database.searchLinkSong(name)
    link= correction(link)
    if link!= None:
        showSong(link)
    else:
        print("the song doesn´t exist")

def searchBands(dataBase):
    bands = dataBase.searchsBands()
    for i in range(len(bands)):
        print("*" + correction(bands[i]))

def searchSongs(dataBase,name):
    idSong = dataBase.searchIdbandUnion(name)
    if idSong != None:
        for i in range(len(idSong)):
            name = dataBase.searchSongWithid(idSong[i])
            print("*" + correction(name))


