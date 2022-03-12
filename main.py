import pymysql
import webbrowser as o

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user='root',
            password= '',
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
            sql = 'INSERT INTO `union` (`idSong`, `idBand`) VALUES ({},{})'

            sql= sql.format(str(idSong),str(idBand))
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
    if idS is None:
        dataBase.addSong(name,link)
        idS= dataBase.searchIdSong(name)

    idB= dataBase.searchIdBand(band)
    print(idB)
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
    if link!= "None":
        showSong(link)
    else:
        print("the song doesn´t exist")

def searchBands(dataBase):
    bands = dataBase.searchsBands()
    for i in range(len(bands)):
        print("*" + correction(bands[i]))
    if bands== ():
        print("You haven´t bands")

def searchSongs(dataBase):
    name= input("NAME BAND: ")
    name= addplus(name)
    idSong = dataBase.searchIdbandUnion(name)
    if idSong != None:
        for i in range(len(idSong)):
            name = dataBase.searchSongWithid(idSong[i])
            print("*" + correction(name))
    else:
        print("This name is´t valid")


def auxiInt(op):
    rta= False
    list=["1","2","3","4","5"]
    for i in range(len(list)):
        if op== list[i]:
            rta= True
    return rta
def funtionprincipal(dataBase):
    rta ="SI"

    while rta == "SI":
         op= input("1.open song\n2.show bands\n3.show songs\n4.add\n5.close\n")
         if auxiInt(op):
                op=int(op)
                if op == 1:
                 searchSong(dataBase)
                elif op== 2:
                    searchBands(dataBase)
                elif op==3:
                    searchSongs(dataBase)
                elif op==4:
                    addSong(dataBase)
                elif op==5:
                    rta="NO"
                else:
                    print("invalid")
         else:
            print("INVALID OPTION")

funtionprincipal(dataBase)