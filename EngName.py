# -*- coding:utf-8 -*-
import pinyin



class EnglishName:
    def __init__(self, ChineseName):
        self.ChineseName = ChineseName
        self.engname1 = ''
        self.engname2 = ''
        self.engname3 = ''
        self.engname4 = ''
        self.Polyphone={}

    def getAllName(self):
        self.Polyphone['曾'] = 'zeng'
        self.Polyphone['单'] = 'shan'
        self.getEngName1()
        self.getEngName2()
        self.getEngName3()
        self.getEngName4()
        allName = []
        allName.append(self.engname1)
        allName.append(self.engname2)
        allName.append(self.engname3)
        allName.append(self.engname4)
        # print(allName)
        return allName

    def getEngName1(self):
        name = pinyin.get(self.ChineseName, format="strip", delimiter=" ")
        name = name.split(' ')
        surname = name[0]
        first_name = ''
        for i in range(1, len(name)):
            first_name = first_name + name[i]
        first_name = first_name.strip()
        for key in self.Polyphone:
            if key.decode('utf-8') == self.ChineseName[0]:
                surname = self.Polyphone[key]
        self.engname1 = first_name + ' ' + surname



    def getEngName2(self):
        name = pinyin.get(self.ChineseName, format="strip", delimiter=" ")
        name = name.split(' ')
        surname = name[0]
        first_name = ''
        for i in range(1, len(name)):
            first_name = first_name + name[i]
        first_name = first_name.strip()
        for key in self.Polyphone:
            if key.decode('utf-8') == self.ChineseName[0]:
                surname = self.Polyphone[key]
        self.engname2 = surname + ' ' + first_name


    def getEngName3(self):
        name = pinyin.get(self.ChineseName, format="strip", delimiter=" ")
        name = name.split(' ')
        surname = name[0]
        name = pinyin.get_initial(self.ChineseName)
        name = name.split(' ')
        first_name = ''
        for i in range(1, len(name)):
            first_name = first_name + name[i]
        first_name = first_name.strip()
        for key in self.Polyphone:
            if key.decode('utf-8') == self.ChineseName[0]:
                surname = self.Polyphone[key]
        self.engname3 = first_name + '.' + surname

    def getEngName4(self):
        name = pinyin.get(self.ChineseName, format="strip", delimiter=" ")
        name = name.split(' ')
        surname = name[0]
        first_name = ''
        for i in range(1, len(name)):
            first_name = first_name + name[i]
        first_name = first_name.strip()
        for key in self.Polyphone:
            if key.decode('utf-8') == self.ChineseName[0]:
                surname = self.Polyphone[key]
        self.engname4 = first_name + ' ' + surname[0]

# .decode('utf-8')

if __name__ == '__main__':
    a = EnglishName('曾德泽')
    a.getAllName()
    b = EnglishName('王琦')
    b.getAllName()
    c = EnglishName('单国志')
    c.getAllName()
