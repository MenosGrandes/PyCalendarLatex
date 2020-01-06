
from pylatex import Document, Section, Subsection, Tabular, MultiColumn, MultiRow

doc = Document("multirow")
section = Section('Multirow Test')

test1 = Subsection('MultiColumn')
test2 = Subsection('MultiRow')
test3 = Subsection('MultiColumn and MultiRow')
test4 = Subsection('Vext01')
DAYS =['TUE','WED', 'THU', 'FRI', 'SAT','SUN']
tabular = '|'
tabular = tabular + '|'.join([''.join('c') for x in range(len(DAYS)+1)])+ '|'
print(tabular)
#week1
table2= Tabular(tabular)
table2.add_hline()

table2.add_row((MultiColumn(1,data='    '), *DAYS))
table2.add_hline()
table2.add_row( ('WEEK1','W','S','C','P','S','N'))
#for x in DAYS:
#    table2.add_empty_row()
#    table2.add_hline()

test2.append(table2)
section.append(test2)










#test2.append(table_week_header)
#test2.append(table_week1_row)
#section.append(table_week_header)
#section.append(table_week1_row)
doc.append(section)
doc.generate_pdf(clean_tex=True)
