import xml.etree.ElementTree as ET
import dominate as dom
from dominate.tags import *

def parse_CV_XML_to_Confluence(xml):
    """
    Функция для парсинга XML кода CV HANA в html код для вставки в страницу Confluence
    """

    rootNode = ET.fromstring(xml)

    page = ''
    list_of_steps = []

    for child in rootNode:
        if(child.tag == "viewNode" and child.get("{http://www.w3.org/2001/XMLSchema-instance}type") == 'View:Projection'):
            list_of_steps.append(parse_viewNode_Projection(child))
        elif(child.tag == "viewNode" and child.get("{http://www.w3.org/2001/XMLSchema-instance}type") == 'View:Aggregation'):
            list_of_steps.append(parse_viewNode_Aggregation(child))
        elif(child.tag == "viewNode" and child.get("{http://www.w3.org/2001/XMLSchema-instance}type") == 'View:JoinNode'):
            list_of_steps.append(parse_viewNode_JoinNode(child))

    page += create_list(list_of_steps)

    return page


def convert_to_table(columns, rows, table_type):
    """
    Функция для генерации html кода таблицы из списка столбцов и списка строк
    """

    #Открывающие теги таблицы
    table = '<table class="wrapped">'
    table += '<tbody>'

    
    #region Создаем заголовки столбцов
    table += '<tr>'

    for column in columns:
        table += '<th scope="col">' + column + '</th>'

    table += '</tr>'
    #endregion

    #region Заполняем строки
    for row in range(0, len(rows)):
        #Если остаток от деления индекса значения на кол-во столбцов равен нулю, значит это начало строки
        if( row % len(columns) == 0):
            #Если таблица для блока Projection и в столбце "Вычисляемый солбец" не пусто, то делаем такую строку желтого цвета
            if(table_type == 'projection' and rows[row + 2] != ''):
                table += '<tr style="background-color: #FAE99F;">'        
            else:
                table += '<tr>'
        
        table += '<td>' + rows[row] + '</td>'

        #Если остаток от деления индекса следующего значения на кол-во столбцов равен нулю, значит это конец строки
        if( (row + 1) % len(columns) == 0):
            table += '</tr>'
    #endregion

    #Закрывающие теги
    table += '</tbody>'
    table += '</table>'

    return table

def parse_viewNode_Projection(viewNode):
    """
    Функция для парсинга XML блока viewNode типа Projection
    """
    # Начинаем формировать текст описания
    text = '<h4>' + viewNode.get('name') + '</h4>'
    text += 'Из <strong>' + viewNode.find('input').find('entity').text.replace('\'', '\'')[4:] + '</strong> выбираются поля:'

    # Объявляем списки столбцов и строк будущей таблицы
    columns = ['Наименование поля', 'Тип данных', 'Вычисляемый столбец', 'Формула']
    rows = []

    # Формируем список полей
    for child in viewNode:
        if(child.tag == 'element'):

            element_items = parse_element(child)

            rows.append(element_items['name'])
            rows.append(element_items['data_type'])
            rows.append(element_items['language'])
            rows.append(element_items['formula'])

    text += convert_to_table(columns, rows, 'projection')
    text += '<br/>'
    
    filter_expression = viewNode.find('filterExpression')
    
    # Формируем блок с фильтром
    if(filter_expression != None):
        text += parse_filter_expression(filter_expression)

    text += '<br/>'

    return text

def parse_viewNode_Aggregation(viewNode):     
    """
    Функция для парсинга XML блока viewNode типа Aggregation
    """
    # Начинаем формировать текст описания
    text = '<h4>' + viewNode.get('name') + '</h4>'
    text += 'Агрегация из <strong>' + viewNode.find('input').find('viewNode').text.replace('\'', '\'')[4:] + '</strong> по полям:'

    # Объявляем списки столбцов и строк будущей таблицы
    columns = ['Наименование поля', 'Тип данных', 'Функция агрегации', 'Вычисляемый столбец', 'Формула']
    rows = []

    # Формируем список полей
    for child in viewNode:
        if(child.tag == 'element'):

            element_items = parse_element(child)
                        
            rows.append(element_items['name'])
            rows.append(element_items['data_type'])
            rows.append(element_items['aggregation_behavior'])
            rows.append(element_items['language'])
            rows.append(element_items['formula'])

    text += convert_to_table(columns, rows, 'aggregation')
    text += '<br/>'
    
    filter_expression = viewNode.find('filterExpression')
    
    # Формируем блок с фильтром
    if(filter_expression != None):
        text += parse_filter_expression(filter_expression)

    text += '<br/>'

    return text 

def parse_element(element):
    """
    Функция для парсинга элемента "element"
    """
    rows = {}

    # Первый столбец Имя
    rows['name'] = element.get('name')

    data_type = element.find('inlineType').get('primitiveType')

    if(element.find('inlineType').get('length') != None):
        data_type += '(' + str(element.find('inlineType').get('length')) + ')'

    # Второй столбец Тип данных
    rows['data_type'] = data_type

    cal_def = element.find('calculationDefinition')
    
    if(cal_def != None):
        # Третий столбец Язык формирования столбца
        rows['language'] = cal_def.get('language')
        # Четвертый столбец Формула
        rows['formula'] = cal_def.find('formula').text.replace('\'', '\'')
    else: 
        # Третий столбец Язык формирования столбца
        rows['language'] = ''
        # Четвертый столбец Формула
        rows['formula'] = ''

    aggregation_behavior = element.get('aggregationBehavior')

    if(aggregation_behavior != None):
        rows['aggregation_behavior'] = aggregation_behavior
    else:
        rows['aggregation_behavior'] = '-'

    return rows

def parse_filter_expression(filter_expression):
    """
    Функция для парсинга выражения фильтра (возвращает таблицу)
    """
    text = '<p>Устанавливается фильтр</p>'
    columns = ['Язык', 'Формула']
    rows = []
    rows.append(filter_expression.get('language'))
    rows.append(filter_expression.find('formula').text.replace('\'', '\''))

    text += convert_to_table(columns, rows, 'filter')

    return text

def create_list(list_of_steps):

    text = '<ol>'

    for item in list_of_steps:
        text += '<li>'
        text += item
        text += '</li>'

    text += '</ol>'

    return text

def parse_input(input):
    """
    Функция парсинга блока input
    """

    name = input.find('viewNode').text[4:].replace('\'', '\'')
    fields = {}

    for child in input:
        if(child.tag == "mapping"):
            fields['target_name'] = child.get('targetName')
            fields['source_name'] = child.get('sourceName')

    return [name, fields]


def parse_viewNode_JoinNode(viewNode):
    """
    Функция парсинга блока join из viewNode типа Join
    """

    # Список для хранения данных о входящих таблицах джойна
    joins = []

    for input in viewNode.findall('input'):
        joins.append(parse_input(input))

    # Парсинг типа джойна и полей
    join_parameters = viewNode.find('join')

    parameters = {}
    parameters['left_input'] = join_parameters.get('leftInput').replace('\'', '\'')[4:]
    parameters['right_input'] = join_parameters.get('rightInput').replace('\'', '\'')[4:]
    parameters['join_type'] = join_parameters.get('joinType')

    left_fields = []

    for left in join_parameters.findall('leftElementName'):
        left_fields.append(left.text)

    right_fields = []

    for right in join_parameters.findall('rightElementName'):
        right_fields.append(right.text)

    columns = ['Левая таблица', 'Левое поле', 'Правое поле', 'Правая таблица']
    rows = []

    for i in range(0,len(left_fields)):
        rows.append(parameters['left_input'])
        rows.append(left_fields[i])
        rows.append(right_fields[i])
        rows.append(parameters['right_input'])

    # Начинаем формировать текст описания
    text = '<h4>' + viewNode.get('name') + '</h4>'
    text += '<strong>' + parameters['join_type'].upper() + '</strong><br/>'
    text += 'Соединение <strong>' + joins[0][0] + '</strong> и <strong>' + joins[1][0] + '</strong> по  следующим полям:<br/>'
    text += convert_to_table(columns, rows, 'join_field')


    # # Объявляем списки столбцов и строк будущей таблицы
    # columns = ['Наименование поля', 'Тип данных', 'Функция агрегации', 'Вычисляемый столбец', 'Формула']
    # rows = []

    # # Формируем список полей
    # for child in viewNode:
    #     if(child.tag == 'element'):

    #         element_items = parse_element(child)
                        
    #         rows.append(element_items['name'])
    #         rows.append(element_items['data_type'])
    #         rows.append(element_items['aggregation_behavior'])
    #         rows.append(element_items['language'])
    #         rows.append(element_items['formula'])

    # text += convert_to_table(columns, rows, 'aggregation')
    # text += '<br/>'
    
    # filter_expression = viewNode.find('filterExpression')
    
    # # Формируем блок с фильтром
    # if(filter_expression != None):
    #     text += parse_filter_expression(filter_expression)

    text += '<br/>'

    return text 

    