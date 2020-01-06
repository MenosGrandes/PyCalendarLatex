
from pylatex import Document, Section, Subsection, Tabular, MultiColumn, MultiRow
class Week:
    def __init__(self):
        pass

doc = Document("multirow")
section = Section('Multirow Test')

test1 = Subsection('MultiColumn')
test2 = Subsection('MultiRow')
test3 = Subsection('MultiColumn and MultiRow')
test4 = Subsection('Vext01')
DAYS =['TUE','WED', 'THU', 'FRI', 'SAT','SUN']
tabular = '|'
tabular = tabular + '|'.join([''.join('c') for x in range(len(DAYS)+1)])+ '|'

table4 = Tabular(tabular)
table4.add_hline()
table4.add_row((MultiColumn(1,align = '|c|', data=''), *DAYS))
table4.add_hline()
col1_cell = MultiRow(2, data='WEEK 1')
table4.add_row((col1_cell,*DAYS))
table4.add_hline(start=2)
table4.add_row("1","2","3","4","5","6","7")
table4.add_hline()
#for x in DAYS:
#    table2.add_empty_row()
#    table2.add_hline()

test2.append(table4)
section.append(table4)










#test2.append(table_week_header)
#test2.append(table_week1_row)
#section.append(table_week_header)
#section.append(table_week1_row)
doc.append(section)
doc.generate_pdf(clean_tex=True)
