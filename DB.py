#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb


class DB:
    def __init__(self, host, user, passwd, db, port):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
        self.db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, port=self.port, use_unicode=True,
                     charset="utf8")
        self.cursor = self.db.cursor()

    def test(self):
        sql = 'select * from user'
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        #print(datas)

    def InsertIntoPeopleByBassicInfo(self, realname, EnglishRealname, email, username, domainName, researchInterest, myself):
        sql = 'insert into people (realname, EnglishRealname, email, username, domainName, researchInterest, myself) values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')'%(realname, EnglishRealname, email, username, domainName, researchInterest, myself)
        #print(sql)
        self.cursor.execute(sql)
        self.db.commit()

    def InsertIntoPeopleByWorkInfo(self, Research_institutions, department, position, username):
        sql = 'update people set Research_institutions=\'%s\',department=\'%s\',position=\'%s\' where username = \'%s\''%(Research_institutions,department,position,username)
        #print(sql)
        self.cursor.execute(sql)
        self.db.commit()

    def InsertIntoPeopleByPicPath(self, ProfilePicturePath, username):
        sql = 'update people set ProfilePicturePath=\'%s\' where username = \'%s\''%(ProfilePicturePath,username)
        self.cursor.execute(sql)
        self.db.commit()

    def InsertIntoPeopleByBibtex(self, username, bibtex):
        sql = 'update people set bibtex=\'%s\' where username = \'%s\'' % (bibtex, username)
        self.cursor.execute(sql)
        self.db.commit()

    def selectBibtexFromPeople(self, username):
        sql = 'select bibtex from people where username=\'%s\''%(username)
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        # print(datas[0][0])
        return datas[0][0]

    def selectAllFromPeople(self, domainName):
        sql = 'select * from people where domainName = \'%s\''%(domainName)
        #print(sql)
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        # print(datas[0])
        return datas[0]

    def selectAllFromPeopleByusername(self, username):
        sql = 'select * from people where username = \'%s\''%(username)
        #print(sql)
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        # print(datas[0])
        return datas[0]


    def selectUsernameFromPeople(self):
        sql = 'select username from people'
        #print(sql)
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        # print(datas)
        return datas


    def selectDomainFromPeople(self):
        sql = 'select domainName from people'
        #print(sql)
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        # print(datas)
        return datas


    def UpdateBasicInfoByUsername(self,realname,EnglishRealname,email,Research_institutions,department,position,domainName,researchInterest,myself,username):
        sql = 'update people set realname=\'%s\', EnglishRealname=\'%s\',email=\'%s\',Research_institutions=\'%s\',department=\'%s\',position=\'%s\',domainName=\'%s\',researchInterest=\'%s\',myself=\'%s\' where username = \'%s\'' % (realname, EnglishRealname,email,Research_institutions,department,position,domainName,researchInterest,myself,username)
        #print(sql)
        self.cursor.execute(sql)
        self.db.commit()


    def SelectAllFromPeopleByKeyValue(self,keyvalue):
        sql = 'select * from people where Research_institutions like \'%'+keyvalue+"%\'"
        # print(sql)
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        # print(datas)
        return datas






    def InsertIntoBibtexByUsername(self, username, bibtex):
        sql = 'insert into bibtex(username,bibtex) values (\'%s\',\'%s\')'%(username,bibtex)
        self.cursor.execute(sql)
        self.db.commit()


    def SelectAllBibtexByUsername(self, username):
        sql = 'select * from bibtex where username = \'%s\''%(username)
        #print(sql)
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        return datas


    def SelectAllBibtexByUsernameAndbibtex(self, username,bibtex):
        sql = 'select * from bibtex where username = \'%s\' and bibtex = \'%s\''%(username,bibtex)
        #print(sql)
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        return datas


    def UpdateBibtexByUsernameAndBibtex(self,pdfpath ,username, bibtex):
        sql = 'update bibtex set pdfpath=\'%s\'where username=\'%s\' and bibtex=\'%s\''%(pdfpath,username,bibtex)
        #print(sql)
        self.cursor.execute(sql)
        self.db.commit()


    def DeleteBibtexByUsernameAndBibtex(self,username, bibtex):
        sql = 'delete from bibtex where username=\'%s\' and bibtex=\'%s\''%(username,bibtex)
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()



    def InsertIntoBibtexByUsernameAndbibtex(self, username, bibtex,pdfpath):
        sql = 'insert into bibtex(username,bibtex,pdfpath) values (\'%s\',\'%s\',\'%s\')'%(username,bibtex,pdfpath)
        self.cursor.execute(sql)
        self.db.commit()

    def InsertIntoBibtexByUsernameWithoutpdfpath(self, username, bibtex):
        sql = 'insert into bibtex(username,bibtex) values (\'%s\',\'%s\')'%(username, bibtex)
        self.cursor.execute(sql)
        self.db.commit()