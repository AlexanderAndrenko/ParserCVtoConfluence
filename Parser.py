from DataModel import *
import xml.etree.ElementTree as ET

# Парсер для InlineType
def parse_inline_type(element) -> InlineType:
    return InlineType(
        name=element.get("name"),
        primitiveType=element.get("primitiveType"),
        length=int(element.get("length")) if element.get("length") else None,
        precision=int(element.get("precision")) if element.get("precision") else None,
        scale=int(element.get("scale")) if element.get("scale") else None
    )

# Парсер для CalculationDefinition
def parse_calculation_definition(element) -> CalculationDefinition:
    return CalculationDefinition(
        language=element.get("language"),
        formula=element.find('formula').text
    )

# Парсер для Element
def parse_element(element) -> Element:
    inline_type_elem = element.find("inlineType")
    inline_type = parse_inline_type(inline_type_elem) if inline_type_elem is not None else None
    
    calc_def_elem = element.find("calculationDefinition")
    calc_def = parse_calculation_definition(calc_def_elem) if calc_def_elem is not None else None
    
    return Element(
        name=element.get("name"),
        endUserTexts=element.get("endUserTexts"),
        inlineType=inline_type,
        calculationDefinition=calc_def,
        aggregationBehavior=element.get("aggregationBehavior")
    )

# Парсер для Mapping
def parse_mapping(element) -> Mapping:
    return Mapping(
        targetName=element.get("targetName"),
        sourceName=element.get("sourceName")
    )

# Парсер для Input
def parse_input(element) -> Input:
    mappings = [parse_mapping(m) for m in element.findall("mapping")]
    return Input(
        entity=element.find('entity').text if element.find('entity') != None else None,
        viewNode=element.find('viewNode').text if element.find('viewNode') != None else None,
        mappings=mappings
    )

# Парсер для FilterExpression
def parse_filter_expression(element) -> FilterExpression:
    return FilterExpression(
        language=element.get("language"),
        formula=element.find('formula').text
    )

# Парсер для Join
def parse_join(element) -> Join:
    left_elements = [e.text for e in element.findall(".//leftElementName")]
    right_elements = [e.text for e in element.findall(".//rightElementName")]
    return Join(
        leftInput=element.get("leftInput"),
        rightInput=element.get("rightInput"),
        joinType=element.get("joinType"),
        leftElementName=left_elements,
        rightElementName=right_elements
    )

# Парсер для ViewNode
def parse_view_node(element) -> ViewNode:
    elements = [parse_element(e) for e in element.findall("element")]
    inputs = [parse_input(i) for i in element.findall("input")]
    
    filter_expr_elem = element.find("filterExpression")
    filter_expression = parse_filter_expression(filter_expr_elem) if filter_expr_elem is not None else None
    
    join_elem = element.find("join")
    join = parse_join(join_elem) if join_elem is not None else None
    
    return ViewNode(
        name=element.get("name"),
        xsi_type=element.get("{http://www.w3.org/2001/XMLSchema-instance}type"),
        endUserTexts=element.get("endUserTexts"),
        elements=elements,
        inputs=inputs,
        filterExpression=filter_expression,
        layout=None,  # Assuming layout isn't defined in the provided XML structure
        join=join,
        joinOrder=element.get("joinOrder")
    )

# Парсер для Parameter
def parse_parameter(element) -> Parameter:
    inline_type_elem = element.find("inlineType")
    inline_type = parse_inline_type(inline_type_elem)
    
    return Parameter(
        xsi_type=element.get("{http://www.w3.org/2001/XMLSchema-instance}type"),
        name=element.get("name"),
        mandatory=element.get("mandatory") == "true",
        multipleSelections=element.get("multipleSelections") == "true",
        endUserTexts=element.get("endUserTexts"),
        inlineType=inline_type,
        defaultValue=element.get("defaultValue"),
        derivationRule=None  # Assuming derivationRule isn't defined in the provided XML structure
    )

# Парсер для ColumnView
def parse_column_view(xml_string: str) -> ColumnView:

    root = ET.fromstring(xml_string)
    
    parameters = [parse_parameter(p) for p in root.findall("parameter")]
    view_nodes = [parse_view_node(vn) for vn in root.findall("viewNode")]
    
    return ColumnView(
        schemaVersion=root.get("schemaVersion"),
        name=root.get("name"),
        dataCategory=root.get("dataCategory"),
        hierarchiesSQLEnabled=root.get("hierarchiesSQLEnabled") == "true",
        defaultNode=root.get("defaultNode"),
        clientDependent=root.get("clientDependent") == "true",
        applyPrivilegeType=root.get("applyPrivilegeType"),
        translationRelevant=root.get("translationRelevant") == "true",
        endUserTexts=root.get("endUserTexts"),
        origin=root.get("origin"),
        parameters=parameters,
        executionHints=root.get("executionHints"),
        viewNodes=view_nodes
    )