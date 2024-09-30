from dominate.tags import *
import Parser
from DataModel import *
import re

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

                if(viewNode.inputs[0].entity != None):
                    strong_name.add(re.sub('#/?./','',str(viewNode.inputs[0].entity)))
                else:
                    strong_name.add(re.sub('#/?./','',str(viewNode.inputs[0].viewNode)))
                    
                second_line.add(strong_name)
                list_item.add(second_line)

                # Вставляем таблицу со списком используемых столбцов
                columns, rows, row_style = get_columns_rows_from_elements_projection(viewNode.elements)
                list_item.add(create_table(columns, rows, row_style))

                if(viewNode.filterExpression != None):
                    filter = create_filter_block(viewNode.filterExpression)
                    list_item.add(filter)

            case 'View:JoinNode':
                first_line = p(strong(str(viewNode.name)))
                list_item.add(first_line)

                second_line = p('Соединение ')
                first_strong_name = strong()
                first_strong_name.add(re.sub('#/?./','',str(viewNode.inputs[0].viewNode)))
                second_line.add(first_strong_name)
                second_line.add(' и ')
                second_strong_name = strong()
                second_strong_name.add(re.sub('#/?./','',str(viewNode.inputs[1].viewNode)))
                second_line.add(second_strong_name)
                strong_join_type = strong()
                strong_join_type.add(viewNode.join.joinType.upper().replace('OUTER', '') + ' JOIN')
                second_line.add(' по типу ')
                second_line.add(strong_join_type)
                list_item.add(second_line)
                
                # Формируем таблицу с типом джойна 
                columns, rows, row_style = get_columns_rows_from_join(viewNode.join)
                tbl_join = create_table(columns, rows, row_style)
                list_item.add(tbl_join)

                # Формируем таблицу со списком используемых столбцов
                list_item.add(p('Исходящие поля'))
                columns_2, rows_2, row_style_2 = get_columns_rows_from_elements_for_join(viewNode)
                tbl_join_fields = create_table(columns_2, rows_2, row_style_2)
                list_item.add(tbl_join_fields)

                if(viewNode.filterExpression != None):
                    list_item.add(p())
                    filter = create_filter_block(viewNode.filterExpression)
                    list_item.add(filter)

            case 'View:Aggregation':
                first_line = p(strong(str(viewNode.name)))
                list_item.add(first_line)

                second_line = p('Агрегация из ')
                strong_name = strong()
                strong_name.add(re.sub('#/?./','',str(viewNode.inputs[0].viewNode))) 
                second_line.add(strong_name)
                list_item.add(second_line)

                # Вставляем таблицу со списком используемых столбцов
                columns, rows, row_style = get_columns_rows_from_elements_aggregation(viewNode.elements)
                list_item.add(create_table(columns, rows, row_style))

                if(viewNode.filterExpression != None):
                    list_item.add(p())
                    filter = create_filter_block(viewNode.filterExpression)
                    list_item.add(filter)

            case 'View:Union':
                first_line = p(strong(str(viewNode.name)))
                list_item.add(first_line)

                second_line = p('Объединение ')

                quantity_inputs = len(viewNode.inputs)

                for index, input in enumerate(viewNode.inputs):
                    name = strong()
                    name.add(re.sub('#/?./','',str(input.viewNode)))
                    second_line.add(name)

                    if(index != quantity_inputs - 1):
                        second_line.add(' и ')
                    
                list_item.add(second_line)

                # Формируем таблицу со списком объединения полей
                columns, rows, rows_style = get_columns_rows_for_union(viewNode)
                tbl_union = create_table(columns, rows, rows_style)
                list_item.add(tbl_union)

                if(viewNode.filterExpression != None):
                    list_item.add(p())
                    filter = create_filter_block(viewNode.filterExpression)
                    list_item.add(filter)

            case 'View:Rank':
                first_line = p(strong(str(viewNode.name)))
                list_item.add(first_line)

                second_line = p('Из ')
                strong_name = strong()

                if(viewNode.inputs[0].entity != None):
                    strong_name.add(re.sub('#/?./','',str(viewNode.inputs[0].entity)))
                else:
                    strong_name.add(re.sub('#/?./','',str(viewNode.inputs[0].viewNode)))

                second_line.add(strong_name)
                list_item.add(second_line)

                # 

                # Вставляем таблицу со списком используемых столбцов
                columns, rows, row_style = get_columns_rows_for_rank(viewNode)
                list_item.add(create_table(columns, rows, row_style))


            case _:
                list_item.add(p('Неизвестный блок, необходимо произвести доработку парсинга'))

        list_item.add(p()) # Делаем отступ в конце каждого элемента списка
        list_items.append(list_item)

    list_viewNodes.add(*list_items)
    page = list_viewNodes

    # page = str(page) + '''
    #             <br/>
    #             <br/>
    #             <ac:structured-macro ac:macro-id="39bc6723-d1c7-4f9a-914e-49f2594f3885" ac:name="expand" ac:schema-version="1">
    #             <ac:parameter ac:name="title">XML</ac:parameter>
    #             <ac:rich-text-body>
    #                 <p>''' + xml + '''</p>
    #             </ac:rich-text-body>
    #             </ac:structured-macro>
    #         '''

    return page

def get_columns_rows_from_elements_projection(elements: List[Element]):
    """
    Функция для получения столбцов и строк таблицы из элементов блока viewNode типа Projection
    """
    columns = ['Наименование поля', 'Тип данных', 'Вычисляемый столбец', 'Формула']
    rows = []
    rows_style = []

    for element in elements:
        row = []
        # Наименование поля
        row.append(element.name)
        # Тип данных
        datatype = element.inlineType.primitiveType
        if(element.inlineType.length != None and datatype not in {'DATE', 'TIMESTAMP'}):
            datatype += '(' + str(element.inlineType.length) + ')'
        row.append(datatype)
        # Вычисляемый столбец
        language = element.calculationDefinition.language if element.calculationDefinition != None else ''
        row.append(language)
        # Формула
        formula = element.calculationDefinition.formula if element.calculationDefinition != None else ''
        row.append(formula)
        rows.append(row)

        style = 'background-color: #FAE99F;' if element.calculationDefinition != None else ''
        rows_style.append([style, style, style, style])

    return columns, rows, rows_style

def get_columns_rows_from_elements_aggregation(elements: List[Element]):
    """
    Функция для получения столбцов и строк таблицы из элементов блока viewNode типа Aggregation
    """
    columns = ['Наименование поля', 'Тип данных', 'Функция агрегации', 'Вычисляемый столбец', 'Формула']
    rows = []
    rows_style = []

    for element in elements:
        row = []
        # Наименование поля
        row.append(element.name)
        # Тип данных
        datatype = element.inlineType.primitiveType
        if(element.inlineType.length != None and datatype not in {'DATE', 'TIMESTAMP'}):
            datatype += '(' + str(element.inlineType.length) + ')'
        row.append(datatype)
        # Функция агрегации
        aggregationBehavior = element.aggregationBehavior if element.aggregationBehavior not in {None, 'NONE'} else '-'
        row.append(aggregationBehavior)
        # Вычисляемый столбец
        language = element.calculationDefinition.language if element.calculationDefinition != None else ''
        row.append(language)
        # Формула
        formula = element.calculationDefinition.formula if element.calculationDefinition != None else ''
        row.append(formula)
        rows.append(row)

        row_style = []
        style = 'background-color: #FAE99F;' if element.calculationDefinition != None else ''
        for _ in range(0, len(columns)):
            row_style.append(style)
        rows_style.append(row_style)

    return columns, rows, rows_style

def create_table(columns: List, rows: List[List], row_style: List[List] = None):
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
            # tbl_td.add_raw_string(cell)
            tbl_td.add(cell)
            tbl_tr.add(tbl_td)
        tbl_rows.append(tbl_tr)
    
    if(row_style != None):
        # Применяем стили к ячейкам
        for column in range(0, len(row_style)):
            for row in range(0, len(row_style[column])):
                tbl_rows[column][row]['style'] = row_style[column][row]

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

def get_columns_rows_from_join(join: Join):
    """
    Функция для сбора столбцов, строк и стилей для таблицы блока Join
    """
    columns = ['Левая таблица', 'Левое поле', 'Правое поле', 'Правая таблица']
    rows = []
    rows_style = []
    columns_style = []
    left_table = re.sub('#/?./','',str(join.leftInput))
    left_table = left_table[left_table.find('/') + 1:]
    right_table = re.sub('#/?./','',str(join.rightInput))
    right_table = right_table[right_table.find('/') + 1:]

    for index in range(0, len(join.leftElementName)):
        row = []
        row.append(left_table)
        row.append(join.leftElementName[index])
        row.append(join.rightElementName[index])
        row.append(right_table)
        rows.append(row)

    match join.joinType:
        case 'leftOuter':
            columns_style.extend([0,1])
        case 'inner':
            columns_style.extend([1,2])
        case 'rightOuter':
            columns_style.extend([2,3])        
    
    for row in range(0, len(rows)):
        row_style = []

        for column in range(0, len(columns)):  
            # Собираем стили ячеек строки (по столбцам)          
            if(column in columns_style):
                row_style.append('background-color: #99e3dd;')
            else:
                row_style.append('')
            
        rows_style.append(row_style)

    return columns, rows, rows_style

def get_columns_rows_from_elements_for_join(viewNode: ViewNode ): #elements: List[Element], inputs: List[Input]):
    """
    Функция для сбора столбцов, строк и стилей для таблицы блока Join со списком полей
    """
    columns = ['Исходная нода', 'Наименование поля', 'Тип данных', 'Вычисляемый столбец', 'Формула']
    rows = []
    rows_style = []

    for element in viewNode.elements:
        row = []

        # Исходная нода
        name = element.name
        node = ''        
        for input in viewNode.inputs:
            for map in input.mappings:
                if(map.targetName == name):
                    node = re.sub('#/?./','',str(input.viewNode))
        row.append(node)

        # Наименование поля
        row.append(name)

        # Тип данных
        datatype = element.inlineType.primitiveType
        if(element.inlineType.length != None and datatype not in {'DATE', 'TIMESTAMP'}):
            datatype += '(' + str(element.inlineType.length) + ')'
        row.append(datatype)

        # Вычисляемый столбец
        language = element.calculationDefinition.language if element.calculationDefinition != None else ''
        row.append(language)

        # Формула
        formula = element.calculationDefinition.formula if element.calculationDefinition != None else ''
        row.append(formula)
        rows.append(row)

        style = 'background-color: #FAE99F;' if element.calculationDefinition != None else ''
        rows_style.append([style, style, style, style, style])

    return columns, rows, rows_style

def get_columns_rows_for_union(viewNode):
    """
    Функция для сбора столбцов, строк и стилей для таблицы блока Union со списком полей
    """
    columns = ['Целевое поле']
    rows = []
    rows_style = []

    for input in viewNode.inputs:
        columns.append(re.sub('#/?./','',str(input.viewNode)))
    
    # Собираем строки
    for element in viewNode.elements:
        row = [element.name]

        for input in viewNode.inputs:
            field = ''
            for mapping in input.mappings:
                if(element.name == mapping.targetName and mapping.xsi_type != 'Type:ConstantElementMapping'):
                    field = mapping.sourceName
            row.append(field)
        
        rows.append(row)    

    return columns, rows, rows_style

def get_columns_rows_for_rank(viewNode):
    """
    Функция для сбора столбцов, строк и стилей для таблицы блока Rank со списком полей
    """
    columns = ['Наименование поля', 'Тип данных']
    rows = []
    rows_style = []

    rank_column = re.sub('#/?./','',str(viewNode.windowFunction.rankElement))
    rank_column = rank_column[rank_column.find('/') + 1:]

    for element in viewNode.elements:
        row = []
        # Наименование поля
        row.append(element.name)
        # Тип данных
        datatype = element.inlineType.primitiveType
        if(element.inlineType.length != None and datatype not in {'DATE', 'TIMESTAMP'}):
            datatype += '(' + str(element.inlineType.length) + ')'
        row.append(datatype)

        rows.append(row)

        style = 'background-color: #FAE99F;' if element.name == rank_column else ''
        rows_style.append([style, style])




    return columns, rows, rows_style