from dominate.tags import *
import Parser

def create_page(xml):

    # cv = Parser.parse_column_view(xml)





    

    t = table()
    table_body = tbody()
    row = []
    row.append(tr())
    row[0].add(td('First', style='background-color: #FAE99F;'))
    row.append(tr())
    row[1].add(td('First', style='background-color: #FFFFFF;'))
    
    table_body.add(*row)
    t.add(table_body)

    

    row[0][0]['style'] = 'background-color: #FFFFFF;'
    
    # doc.add(body_tag)

    print(t)

    return table

def create_table(columns, rows):

    tbl = table()
    tbl_body = tbody()

    # Создаем заголовки столбцов
    headers = tr()

    for item in columns:
        column = td(item, scope='col')
        headers.add(column)
    
    tbl_body.add(headers)

    # Создаем строки
    rows = []
    

    return tbl

create_page('')



