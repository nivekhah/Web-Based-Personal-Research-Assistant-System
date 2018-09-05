# -*- coding:utf-8 -*-

import bibtexparser
import re


class BibtexParser:
    def __init__(self, BibtexfilePath):
        self.BibtexfilePath = BibtexfilePath
        self.BibTeXtype={}
        self.show_properties=['author','editor','title','journal','publisher','booktitle','year','volume','number','pages','month']
        self.BibTeXtype['article']={'required':['author','title','journal','year'],'optional':['volume','number','pages','month','note']}
        self.BibTeXtype['book'] = {'required': ['author', 'title', 'publisher', 'year'],
                              'optional': ['volume', 'series', 'address', 'edition', 'month', 'note']}
        self.BibTeXtype['booklet'] = {'required': ['title'],
                                 'optional': ['author', 'howpublished', 'address', 'month', 'year', 'note']}
        self.BibTeXtype['inbook'] = {'required': ['author', 'title', 'chapter', 'publisher', 'year'],
                                'optional': ['volume', 'series', 'type', 'address', 'edition', 'month', 'note']}
        self.bibtex=''
        self.allbibtex=[]

    def openfile(self):
        with open(self.BibtexfilePath) as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
            #print(bib_database.entries)
            ENTRYTYPE = bib_database.entries[0]['ENTRYTYPE']
            #print(ENTRYTYPE)
            self.bibtex = bib_database.entries[0]
            self.allbibtex = bib_database.entries
            #print(self.bibtex['title'])

    def getRealName(self, string):
        # print '删除空格之前长度',len(string)
        string = string.strip()  # 删除字符串收尾的空格
        # print string
        # print len(string)
        name = re.split('[, .]', string)  # 用','' ''.'将名字进行分割
        # print name
        num = len(name)
        namenew = []
        # 移除list里空白字符
        for i in range(0, num):
            # print name[i]
            if name[i] != '':
                # name.remove('')
                namenew.append(name[i])
        # print namenew
        # print len(namenew)
        name = ''
        for i in range(0, len(namenew)):
            if i == 0:
                name = namenew[i] + ' '
            elif i == len(namenew[i]) - 1:  # 第一个单词取全拼，其余选首字母并大写
                name = name + namenew[i][0].upper()
            else:
                name = name + namenew[i][0].upper() + ' '
        # print name
        return name.strip()

    def getTitle(self, string):
        return string

    def getJournal(self, string):
        return string

    def get(self):
        self.openfile()
        text = ''
        for show_property in self.show_properties:
            if self.bibtex.has_key(show_property):
                name = ''
                if show_property == 'author':
                    names = self.bibtex[show_property].split(' and ')
                    # getRealName(names[0])
                    for i in range(0, len(names)):
                        temp_name = self.getRealName(names[i])
                        # print temp_name
                        if i < 3:
                            name = name + temp_name + ', '
                        elif i >= 3:
                            name = name + 'et al. '
                            break
                    #     print type(name)
                    name = name.strip()
                    #     print type(name)
                    if name[-1] == ',':
                        # name=name.ToString().Substring(0,name.length-1)
                        # name_temp=list[name]
                        # name_temp.pop()
                        # name_temp.append('.')
                        # name=''.join(name_temp)
                        name = name.strip(',') + '. '
                    text = text + name
                title = ''
                if show_property == 'title':
                    title = self.getTitle(self.bibtex[show_property]) + '. '
                    text = text + title
                if show_property == 'journal' or show_property == 'publisher':
                    journal = self.getJournal(self.bibtex[show_property]) + ', '
                #print(journal)
                    text = text + journal
                if show_property == 'year':
                    year = self.bibtex[show_property] + ', '
                    text = text + year
                if show_property == 'volume':
                    volume = self.bibtex[show_property]
                    text = text + volume
                if show_property == 'number':
                    number = '(' + self.bibtex[show_property] + ')'
                    text = text + number
                if show_property == 'pages':
                    pages = ':' + self.bibtex[show_property]
                    text = text + pages
        text = text.strip()
        text = text.strip(',')
        #print(text + '.')
        return text+'.'

    def getTextTitle(self):
        with open(self.BibtexfilePath) as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
            allbibtex = bib_database.entries
            titles=[]
            for i in range(0, len(allbibtex)):
                bibtex = allbibtex[i]
                if bibtex.has_key('title'):
                    titles.append(bibtex['title'])
                else:
                    titles.append('')
        return titles


    def getkey(self):
        with open(self.BibtexfilePath) as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
            allbibtex = bib_database.entries
            keys = []
            for i in range(0, len(allbibtex)):
                bibtex = allbibtex[i]
                if bibtex['ENTRYTYPE'] == 'proceedings':
                    continue
                if bibtex.has_key('ID'):
                    keys.append(bibtex['ID'])
                else:
                    keys.append('')
        return keys


    def gettextbykey(self):
        self.openfile()
        result = []
        keys = []
        titles = []
        years = []
        for i in range(0, len(self.allbibtex)):
            bibtex = self.allbibtex[i]
            #print(bibtex['ENTRYTYPE'])
            if bibtex['ENTRYTYPE'] == 'proceedings':
                continue
            keys.append(bibtex['ID'])
            text = ''
            for show_property in self.show_properties:
                if bibtex.has_key(show_property):
                    name = ''
                    if show_property == 'author' or show_property == 'editor':
                        # print(bibtex[show_property])
                        author = bibtex[show_property].replace("\n", " ")
                        # print(author)
                        names = author.split(' and ')
                        # getRealName(names[0])
                        for i in range(0, len(names)):
                            temp_name = self.getRealName(names[i])
                            # print temp_name
                            if i < 3:
                                name = name + temp_name + ', '
                            elif i >= 3:
                                name = name + 'et al.'
                                break
                    #     print type(name)
                        name = name.strip()
                    #     print type(name)
                        if name[-1] == ',':
                        # name=name.ToString().Substring(0,name.length-1)
                        # name_temp=list[name]
                        # name_temp.pop()
                        # name_temp.append('.')
                        # name=''.join(name_temp)
                            name = name.strip(',') + '. '
                        if name[-1] == '.':
                            name = name + ' '
                        text = text + name
                    #title = ''
                    if show_property == 'title':
                        title = self.getTitle(bibtex[show_property]) + '. '
                        title = title.replace('\n',' ')
                        titles.append(title)
                        text = text + title
                    if show_property == 'journal' or show_property == 'booktitle' or show_property == 'publisher':
                        journal = self.getJournal(bibtex[show_property]) + ', '
                        #print(journal)
                        journal = journal.replace('\n', ' ')
                        journal = journal.replace('{', '')
                        journal = journal.replace('}', '')
                        text = text + journal
                    if show_property == 'year':
                        year = bibtex[show_property] + ', '
                        years.append(bibtex[show_property])
                        text = text + year
                    if show_property == 'volume':
                        volume = bibtex[show_property]
                        text = text + volume
                    if show_property == 'number':
                        number = '(' + bibtex[show_property] + ')'
                        text = text + number
                    if show_property == 'pages':
                        pages = ':' + bibtex[show_property]
                        text = text + pages
            text = text.strip()
            text = text.strip(',')
            #print(text + '.')
            result.append(text+'.')
        return result, keys, titles, years
