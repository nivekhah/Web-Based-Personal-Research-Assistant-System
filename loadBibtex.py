# -*- coding:utf-8 -*-
import bibtexparser
import csv



# bibtex_str.replace('{', '')
# bibtex_str.replace('}', '')

class LoadBibtex:
    def __init__(self, BibtexfilePath, show_entry, myself, types):
        with open(BibtexfilePath) as bibtex_file:
            bibtex_str = bibtex_file.read()
        self.bib_database = bibtexparser.loads(bibtex_str)
        self.all_entry = []
        # self.show_entry = ['Author', 'Title', 'Journal', 'Year, Volume(Number)', 'Author Order']
        self.show_entry = show_entry
        # self.myself = 'Deze Zeng'
        self.meself = myself
        self.types = types
        self.all_row = []
    def getInfo(self):
        show_entrys = []
        if self.types == 'proceedings':
            self.all_entry = ['Author', 'Title', 'Publisher', 'Year', 'Volume', 'Number', 'Pages', 'Month']
            for i in range(len(self.show_entry)):
                if self.show_entry[i] == 'Journal':
                    show_entrys.append('Publisher')
                else:
                    show_entrys.append(self.show_entry[i])
        elif self.types == 'article':
            for i in range(len(self.show_entry)):
                show_entrys.append(self.show_entry[i])
            self.all_entry = ['Author', 'Title', 'Journal', 'Year', 'Volume', 'Number', 'Pages', 'Month']
        elif self.types == 'inproceedings':
            self.all_entry = ['Author', 'Title', 'Booktitle', 'Year', 'Volume', 'Number', 'Pages', 'Month']
            for i in range(len(self.show_entry)):
                if self.show_entry[i] == 'Journal':
                    show_entrys.append('Booktitle')
                else:
                    show_entrys.append(self.show_entry[i])
        for bib_entry in self.bib_database.entries:
            if bib_entry['ENTRYTYPE'] == self.types:
                row = {}
                for show in show_entrys:
                    if show in self.all_entry:
                        temp = show.lower()
                        if bib_entry.has_key(temp):
                            if temp == 'publisher':
                                row['journal'] = bib_entry[temp]
                            elif temp == 'booktitle':
                                row['journal'] = bib_entry[temp]
                            else:
                                row[temp] = bib_entry[temp]
                        else:
                            row[temp] = ''
                    elif show == 'Author Order':
                        # authors = bib_entry['author'].replace(' and\n', ',')
                        authors = bib_entry['author'].replace(' and\n', ' and ')
                        # author_list = bib_entry['author'].split('and ')
                        author_list = authors.split('and ')
                        # print(author_list)
                        num = 0
                        for author in author_list:
                            # print(author.strip())
                            author = author.strip()
                            # print(len(author))
                            num = num + 1
                            for myself in self.meself:
                                if author.lower() == myself:
                                    row['author order'] = num
                    else:
                        combination_entry = []
                        symbol_entry = []
                        alpha = []
                        others = []
                        all = []
                        all.append(-1)
                        for i in range(len(show)-1):
                            # print(show[i])

                            if show[i].isalpha() and not show[i+1].isalpha():
                                all.append(i)
                                alpha.append(i)
                            if not show[i].isalpha() and show[i+1].isalpha():
                                all.append(i)
                                others.append(i)
                        # print(alpha)
                        # print(others)
                        alphamim = min(alpha)
                        othersmim = min(others)

                        x = 0
                        y = 0
                        # r如果字母在前，则temp首先为字母，应添加到combination_entry
                        if alphamim < othersmim:
                            x = 0
                            y = 0
                        else:
                            x = 1
                            y = 1
                        # print(all)
                        for i in range(len(all)-1):
                            temp = ''
                            for j in range(all[i]+1, all[i+1]+1):
                                temp = temp + show[j]
                            if x % 2 == 0:
                                combination_entry.append(temp)
                            else:
                                symbol_entry.append(temp)
                            x = x + 1
                        last = ''
                        for i in range(all[-1]+1, len(show)):
                            last = last + show[i]
                        if x % 2 == 0:
                            combination_entry.append(last)
                        else:
                            symbol_entry.append(last)
                        Max = 0
                        Min = 0
                        if len(combination_entry) >= len(symbol_entry):
                            Max = len(combination_entry)
                            Min = len(symbol_entry)
                        else:
                            Max = len(symbol_entry)
                            Min = len(combination_entry)

                        combination_value = []
                        for combination in combination_entry:
                            temp = combination.lower()
                            # print(temp)
                            if bib_entry.has_key(temp):
                                combination_value.append(bib_entry[temp])
                            else:
                                combination_value.append('')
                        # print(combination_value)
                        text = ''
                        if y == 0:
                            for i in range(Min):
                                text = text + combination_value[i] + symbol_entry[i]
                            if len(combination_entry) > len(symbol_entry):
                                text = text + combination_value[-1]
                            elif len(combination_entry) < len(symbol_entry):
                                text = text + symbol_entry[-1]
                        elif y == 1:
                            for i in range(Min):
                                # print(i)
                                text = text + symbol_entry[i] + combination_value[i]
                            # print(text)
                            if len(combination_entry) > len(symbol_entry):
                                text = text + combination_value[-1]
                            elif len(combination_entry) < len(symbol_entry):
                                text = text + symbol_entry[-1]
                        # print(text)
                        row[show.lower()] = text
                        # print('------------------------------------')
                if bib_entry.has_key('year'):
                    row['year'] = bib_entry['year']
                if row.has_key('journal'):
                    row['journal'] = row['journal'].replace('{', '')
                    row['journal'] = row['journal'].replace('}', '')
                else:
                    row['year'] = 0
                self.all_row.append(row)
            #if bib_entry['ENTRYTYPE'] == 'inproceedings' or 'proceedings':

        return self.all_row

        #all_row = sorted(all_row, key=lambda x:x['year'])

#with open('publications.csv', 'w') as publication_csv_file:
#    csv_writer = csv.DictWriter(publication_csv_file,
#                                fieldnames=['title', 'journal', 'yearvolnopages', 'author', 'year'],
#                                delimiter=',')
#
#    for row in all_row:
#        csv_writer.writerow(row)
#
#publication_csv_file.close()
