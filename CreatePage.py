from dominate.tags import *
import Parser
from DataModel import *

def create_page(xml):
    """
    Функция создания страницы для HANA CV
    """

    cv = Parser.parse_column_view(xml)

    page = ''

    list_viewNodes = ol()
    list_viewNodes['type'] = 1
    list_items = []

    for viewNode in cv.viewNodes:
        # Собираем элементы списка
        list_item = li()

        match viewNode.xsi_type:
            case 'View:Projection':
                first_line = p(strong(str(viewNode.name)))
                list_item.add(first_line)

                second_line = p('Из ')
                strong_name = strong()
                strong_name.add_raw_string(viewNode.inputs[0].entity[4:]) # Необходимо использовать метод add_raw_string, так как иначе происходит экранирование кавычек при рендеринге
                second_line.add(strong_name)
                list_item.add(second_line)

                # Вставляем таблицу со списком используемых столбцов
                columns, rows, row_style = get_columns_rows_from_elements(viewNode.elements)
                list_item.add(create_table(columns, rows, row_style))

                if(viewNode.filterExpression != None):
                    filter = create_filter_block(viewNode.filterExpression)
                    list_item.add(filter)

            case 'View:JoinNode':
                list_item.add( p('БЛОК НЕ ОПРЕДЕЛЕН'))

            case 'View:Aggregation':
                list_item.add(p('БЛОК НЕ ОПРЕДЕЛЕН'))

            case _:
                list_item.add(p('БЛОК НЕ ОПРЕДЕЛЕН'))

        list_item.add(p()) # Делаем отступ в конце каждого элемента списка
        list_items.append(list_item)

    list_viewNodes.add(*list_items)
    page = list_viewNodes    

    # t = table()
    # table_body = tbody()
    # row = []
    # row.append(tr())
    # row[0].add(td('First', style='background-color: #FAE99F;'))
    # row.append(tr())
    # row[1].add(td('First', style='background-color: #FFFFFF;'))
    
    # table_body.add(*row)
    # t.add(table_body)    

    # row[0][0]['style'] = 'background-color: #FFFFFF;'
    
    # doc.add(body_tag)

    return page

def get_columns_rows_from_elements(elements: List[Element]):
    """
    Функция для получения столбцов и строк таблицы из элементов блока viewNode
    """
    columns = ['Наименование поля', 'Тип данных', 'Вычисляемый столбец', 'Формула']
    rows = []
    row_style = []

    for element in elements:
        row = []
        row.append(element.name)
        datatype = element.inlineType.primitiveType
        if(element.inlineType.length != None):
            datatype += '(' + str(element.inlineType.length) + ')'
        row.append(datatype)
        language = element.calculationDefinition.language if element.calculationDefinition != None else ''
        row.append(language)
        formula = element.calculationDefinition.formula if element.calculationDefinition != None else ''
        row.append(formula)
        rows.append(row)

        style = 'background-color: #FAE99F;' if element.calculationDefinition != None else ''
        row_style.append(style)

    return columns, rows, row_style

def create_table(columns: List, rows: List[List], row_style: List = None):
    """
    Функция сборки таблицы из наименнования столбцов и строк
    """
    tbl = table()
    tbl_body = tbody()

    # Создаем заголовки столбцов
    headers = tr()

    for item in columns:
        column = th(item, scope='col')
        headers.add(column)
    
    tbl_body.add(headers)

    # Создаем строки
    tbl_rows = []

    for row in rows:
        tbl_tr = tr()
        for cell in row:
            tbl_td = td()
            tbl_td.add_raw_string(cell)
            tbl_tr.add(tbl_td)
        tbl_rows.append(tbl_tr)
    
    if(row_style != None):
        # Применяем стили к строкам
        for index, style in enumerate(row_style):
            tbl_rows[index]['style'] = style

    tbl_body.add(tbl_rows)
    tbl.add(tbl_body)

    return tbl

def create_filter_block(filter: FilterExpression):
    """
    Функция создания блока фильтра
    """
    filter_block = p()
    filter_block.add((p('Устанавливается фильтр:')))
    columns = ['Язык', 'Формула']
    rows = []
    row = []
    row.append(filter.language)
    row.append(filter.formula)
    rows.append(row)
    tbl = create_table(columns, rows)
    filter_block.add(tbl)

    return filter_block