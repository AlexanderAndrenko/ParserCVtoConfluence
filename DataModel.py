from typing import List, Optional
from dataclasses import dataclass

# InlineType class definition
@dataclass
class InlineType:
    name: Optional[str]
    primitiveType: str
    length: Optional[int] = None
    precision: Optional[int] = None
    scale: Optional[int] = None

# CalculationDefinition class definition
@dataclass
class CalculationDefinition:
    language: str
    formula: str

# Element class definition
@dataclass
class Element:
    name: str
    endUserTexts: Optional[str] = None
    inlineType: InlineType = None
    calculationDefinition: Optional[CalculationDefinition] = None
    aggregationBehavior: Optional[str] = None

# Mapping class definition
@dataclass
class Mapping:
    targetName: str
    sourceName: str
    xsi_type: str

# Input class definition
@dataclass
class Input:
    entity: Optional[str] = None
    viewNode: Optional[str] = None  # Links to another ViewNode by reference
    mappings: List[Mapping] = None

# FilterExpression class definition
@dataclass
class FilterExpression:
    language: str
    formula: str

# Join class definition
@dataclass
class Join:
    leftInput: str
    rightInput: str
    joinType: str
    leftElementName: List[str]
    rightElementName: List[str]

# Order class definition
@dataclass
class Order:
    byElement: str = None
    direction: str = None

# RankThreshold class definition
@dataclass
class RankThreshold:
    constantValue: str = None
    parameter_value: str = None

# WindowFunction class definition
@dataclass
class WindowFunction:
    partitionElement: str
    order: Order
    rankThreshold: RankThreshold
    rankElement: str 

# ViewNode class definition
@dataclass
class ViewNode:
    name: str
    xsi_type: str
    endUserTexts: Optional[str] = None
    elements: List[Element] = None
    inputs: List[Input] = None
    filterExpression: Optional[FilterExpression] = None
    layout: Optional[dict] = None
    join: Optional[Join] = None
    joinOrder: Optional[str] = None
    windowFunction: WindowFunction = None

# Parameter class definition
@dataclass
class Parameter:
    xsi_type: str
    name: str
    mandatory: bool
    multipleSelections: bool
    endUserTexts: Optional[str]
    inlineType: InlineType
    defaultValue: Optional[str] = None
    derivationRule: Optional[dict] = None

# Main ColumnView class definition
@dataclass
class ColumnView:
    schemaVersion: str
    name: str
    dataCategory: str
    hierarchiesSQLEnabled: bool
    defaultNode: str
    clientDependent: bool
    applyPrivilegeType: str
    translationRelevant: bool
    endUserTexts: Optional[str]
    origin: Optional[str]
    parameters: List[Parameter]
    executionHints: Optional[str]
    viewNodes: List[ViewNode]