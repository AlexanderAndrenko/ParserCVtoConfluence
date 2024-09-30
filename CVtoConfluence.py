from tkinter import *
from tkinter import ttk
# from xml.dom import minidom
import xml.etree.ElementTree as ET
import ParseXMLtoConfluence as p
import CreatePage

root = Tk()
root.title("Convert CV XML to text for Confluence")
root.geometry("1280x1024")


def InsertTextToOutput(editor ,text):
    editor.insert("1.0", text)

def ClickbtnConvertion():
    xml = editorInput.get("1.0", "end")    
    titles = CreatePage.create_page(xml) 
    # titles = p.parse_CV_XML_to_Confluence(xml)
    InsertTextToOutput(editorOutput, titles)
    
cv_stock = '''<?xml version="1.0" encoding="UTF-8"?>
<View:ColumnView xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:Param="http://www.sap.com/ndb/ViewModelParameter.ecore" xmlns:Type="http://www.sap.com/ndb/DataModelType.ecore" xmlns:View="http://www.sap.com/ndb/ViewModelView.ecore" schemaVersion="2.3" name="CV_LOSS_PICK_MAIN_01" dataCategory="DIMENSION" hierarchiesSQLEnabled="false" defaultNode="#/0/Projection" clientDependent="false" applyPrivilegeType="ANALYTIC_PRIVILEGE" translationRelevant="true">
  <endUserTexts label="CV_LOSS_PICK"/>
  <origin/>
  <parameter xsi:type="Param:DerivedParameter" name="IP_MANDT" mandatory="false" multipleSelections="false">
    <endUserTexts label="IP_MANDT"/>
    <inlineType name="CHAR" primitiveType="CHAR"/>
    <defaultValue xsi:nil="true"/>
    <derivationRule inputEnabled="false">
      <scriptObject>#/1</scriptObject>
    </derivationRule>
  </parameter>
  <executionHints/>
  <viewNode xsi:type="View:Projection" name="W597_EXSTKCAT">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="PACKNM">
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="PARNM">
      <inlineType primitiveType="NVARCHAR" length="15" precision="15" scale="0"/>
    </element>
    <element name="VALLOW">
      <inlineType primitiveType="NVARCHAR" length="255" precision="255" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>(&quot;MANDT&quot;='$$IP_MANDT$$')&#xD;
and (&quot;PACKNM&quot;='ZSBL_W597')&#xD;
and (&quot;PARNM&quot;='EXSTKCAT')</formula>
    </filterExpression>
    <input>
      <entity>#/0/"SAPHANADB".ZRBST_UPARVAL</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PACKNM" sourceName="PACKNM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARNM" sourceName="PARNM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VALLOW" sourceName="VALLOW"/>
    </input>
    <layout xCoordinate="22" yCoordinate="1845" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_4">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="QUAN">
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="MATID">
      <endUserTexts label="MATID"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <input>
      <entity>#/0/REPORTING.LOSS::CV_LOSS_PICK_INV</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
    </input>
    <layout xCoordinate="99" yCoordinate="1941" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="Aggregation_4">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="FLGHUTO">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="CAT">
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="MATID">
      <endUserTexts label="MATID"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="CREATED_AT">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="CREATED_AT_UTC" aggregationBehavior="NONE">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;CREATED_AT&quot;</formula>
      </calculationDefinition>
    </element>
    <element name="CONFIRMED_AT_UTC" aggregationBehavior="NONE">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;CONFIRMED_AT&quot;</formula>
      </calculationDefinition>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>(&quot;MANDT&quot;='$$IP_MANDT$$')</formula>
    </filterExpression>
    <input>
      <entity>#/0/"SAPHANADB"./SCWM/ORDIM_C</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="FLGHUTO" sourceName="FLGHUTO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT" sourceName="CREATED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
    </input>
    <layout xCoordinate="253" yCoordinate="1941" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_2" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="FLGHUTO">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="CAT">
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="MATID">
      <endUserTexts label="MATID"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="QUAN">
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_4</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
    </input>
    <input>
      <viewNode xsi:type="View:Aggregation">#/0/Aggregation_4</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="FLGHUTO" sourceName="FLGHUTO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="176" yCoordinate="1845" width="0" height="0" expanded="true"/>
    <join leftInput="#/0/Join_2/Projection_4" rightInput="#/0/Join_2/Aggregation_4" joinType="inner">
      <leftElementName>LGNUM</leftElementName>
      <leftElementName>TANUM</leftElementName>
      <rightElementName>LGNUM</rightElementName>
      <rightElementName>TANUM</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_4" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="FLGHUTO">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="CAT">
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="EXSTKCAT">
      <inlineType primitiveType="NVARCHAR" length="255" precision="255" scale="0"/>
    </element>
    <element name="MATID">
      <endUserTexts label="MATID"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="QUAN">
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="FLGHUTO" sourceName="FLGHUTO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/W597_EXSTKCAT</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="EXSTKCAT" sourceName="VALLOW"/>
    </input>
    <layout xCoordinate="100" yCoordinate="1749" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_4/Join_2" rightInput="#/0/Join_4/W597_EXSTKCAT" joinType="leftOuter">
      <leftElementName>CAT</leftElementName>
      <rightElementName>VALLOW</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_2">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="FLGHUTO">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="EXSTKCAT">
      <inlineType primitiveType="NVARCHAR" length="255" precision="255" scale="0"/>
    </element>
    <element name="MATID">
      <endUserTexts label="MATID"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>isNull(&quot;EXSTKCAT&quot;)</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_4</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="FLGHUTO" sourceName="FLGHUTO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="EXSTKCAT" sourceName="EXSTKCAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="100" yCoordinate="1671" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="PRODTO">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="FLGHUTO">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="MATID">
      <endUserTexts label="MATID"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;FLGHUTO&quot;=''</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="FLGHUTO" sourceName="FLGHUTO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="100" yCoordinate="377" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="HUTO">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="FLGHUTO">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="MATID">
      <endUserTexts label="MATID"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;FLGHUTO&quot;='X'</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="FLGHUTO" sourceName="FLGHUTO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="190" yCoordinate="1593" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="HUTO_WITHMAT">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="MATID">
      <endUserTexts label="MATID"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>ltrim(&quot;MATID&quot;,'0')!=''</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:Projection">#/0/HUTO</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="254" yCoordinate="377" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="HUTO_WITHOUTMAT">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="MATID">
      <endUserTexts label="MATID"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>ltrim(&quot;MATID&quot;,'0')=''</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:Projection">#/0/HUTO</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="365" yCoordinate="1515" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_10">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_STOCK">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_STOCK0">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;MANDT&quot;='$$IP_MANDT$$'</formula>
    </filterExpression>
    <input>
      <entity>#/0/"SAPHANADB"./SCWM/QUAN</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_STOCK" sourceName="GUID_STOCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_STOCK0" sourceName="GUID_STOCK0"/>
    </input>
    <layout xCoordinate="597" yCoordinate="647" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_11">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="GUID_STOCK">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="MATID">
      <endUserTexts label="MATID"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;MANDT&quot;='$$IP_MANDT$$'</formula>
    </filterExpression>
    <input>
      <entity>#/0/"SAPHANADB"./SCWM/AQUA</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_STOCK" sourceName="GUID_STOCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
    </input>
    <layout xCoordinate="597" yCoordinate="551" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="CopyOfProjection_12">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>(&quot;MANDT&quot;='$$IP_MANDT$$')&#xD;
and (&quot;TYPE&quot;='H')&#xD;
and in(&quot;TYPE_PARENT&quot;,'H','L')</formula>
    </filterExpression>
    <input>
      <entity>#/0/"SAPHANADB"./LIME/NTREE</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE" sourceName="TYPE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
    </input>
    <layout xCoordinate="519" yCoordinate="1515" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_10" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/HUTO_WITHOUTMAT</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/CopyOfProjection_12</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
    </input>
    <layout xCoordinate="453" yCoordinate="1419" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_10/HUTO_WITHOUTMAT" rightInput="#/0/Join_10/CopyOfProjection_12" joinType="inner">
      <leftElementName>SGUID_HU</leftElementName>
      <rightElementName>GUID</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_13">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT_L">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;TYPE_PARENT&quot;='L'</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_10</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT_L" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="453" yCoordinate="1071" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_14">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT_H">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;TYPE_PARENT&quot;='H'</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_10</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT_H" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="541" yCoordinate="1341" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="CopyOfCopyOfProjection_12">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>(&quot;MANDT&quot;='$$IP_MANDT$$')&#xD;
and (&quot;TYPE&quot;='H')&#xD;
and in(&quot;TYPE_PARENT&quot;,'H','L')</formula>
    </filterExpression>
    <input>
      <entity>#/0/"SAPHANADB"./LIME/NTREE</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE" sourceName="TYPE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
    </input>
    <layout xCoordinate="695" yCoordinate="1341" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_11" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT_H">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_14</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT_H" sourceName="GUID_PARENT_H"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/CopyOfCopyOfProjection_12</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
    </input>
    <layout xCoordinate="607" yCoordinate="1245" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_11/Projection_14" rightInput="#/0/Join_11/CopyOfCopyOfProjection_12" joinType="inner">
      <leftElementName>GUID_PARENT_H</leftElementName>
      <rightElementName>GUID</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_15">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT_L">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;TYPE_PARENT&quot;='L'</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_11</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT_L" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="607" yCoordinate="1071" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_16">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT_H">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;TYPE_PARENT&quot;='H'</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_11</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT_H" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="695" yCoordinate="1167" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="CopyOfCopyOfCopyOfProjection_12">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>(&quot;MANDT&quot;='$$IP_MANDT$$')&#xD;
and (&quot;TYPE&quot;='H')&#xD;
and (&quot;TYPE_PARENT&quot;='L')</formula>
    </filterExpression>
    <input>
      <entity>#/0/"SAPHANADB"./LIME/NTREE</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE" sourceName="TYPE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
    </input>
    <layout xCoordinate="849" yCoordinate="1167" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_12" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT_L">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_16</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/CopyOfCopyOfCopyOfProjection_12</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT_L" sourceName="GUID_PARENT"/>
    </input>
    <layout xCoordinate="761" yCoordinate="1071" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_12/Projection_16" rightInput="#/0/Join_12/CopyOfCopyOfCopyOfProjection_12" joinType="inner">
      <leftElementName>GUID_PARENT_H</leftElementName>
      <rightElementName>GUID</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Union" name="Union_4">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID" transparentFilter="false">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT_L">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:Projection">#/0/Projection_13</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT_L" sourceName="GUID_PARENT_L"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:Projection">#/0/Projection_15</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT_L" sourceName="GUID_PARENT_L"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:JoinNode">#/0/Join_12</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT_L" sourceName="GUID_PARENT_L"/>
      <mapping xsi:type="Type:ConstantElementMapping" targetName="TYPE_PARENT" value="" null="true"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="519" yCoordinate="937" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Copy_2_Of_CopyOfProjection_12">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>(&quot;MANDT&quot;='$$IP_MANDT$$')&#xD;
and (&quot;TYPE&quot;='H')&#xD;
and (&quot;TYPE_PARENT&quot;='H')</formula>
    </filterExpression>
    <input>
      <entity>#/0/"SAPHANADB"./LIME/NTREE</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE" sourceName="TYPE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
    </input>
    <layout xCoordinate="278" yCoordinate="1071" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_13" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/HUTO_WITHOUTMAT</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Copy_2_Of_CopyOfProjection_12</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
    </input>
    <layout xCoordinate="365" yCoordinate="937" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_13/HUTO_WITHOUTMAT" rightInput="#/0/Join_13/Copy_2_Of_CopyOfProjection_12" joinType="inner">
      <leftElementName>SGUID_HU</leftElementName>
      <rightElementName>GUID_PARENT</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_14" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT_L">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_13</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <input>
      <viewNode xsi:type="View:Union">#/0/Union_4</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT_L" sourceName="GUID_PARENT_L"/>
    </input>
    <layout xCoordinate="432" yCoordinate="841" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_14/Join_13" rightInput="#/0/Join_14/Union_4" joinType="inner">
      <leftElementName>LGNUM</leftElementName>
      <leftElementName>TANUM</leftElementName>
      <rightElementName>LGNUM</rightElementName>
      <rightElementName>TANUM</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Union" name="Union_5">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT_L">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:Union">#/0/Union_4</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT_L" sourceName="GUID_PARENT_L"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:JoinNode">#/0/Join_14</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT_L" sourceName="GUID_PARENT_L"/>
      <mapping xsi:type="Type:ConstantElementMapping" targetName="TYPE_PARENT" value="" null="true"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="478" yCoordinate="725" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_3">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT_L">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>not(isNull(&quot;GUID&quot;))</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:Union">#/0/Union_5</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT_L" sourceName="GUID_PARENT_L"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="443" yCoordinate="647" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_7" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT_L">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_STOCK">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_STOCK0">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_3</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT_L" sourceName="GUID_PARENT_L"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_10</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_STOCK" sourceName="GUID_STOCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_STOCK0" sourceName="GUID_STOCK0"/>
    </input>
    <layout xCoordinate="443" yCoordinate="551" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_7/Projection_3" rightInput="#/0/Join_7/Projection_10" joinType="inner">
      <leftElementName>GUID</leftElementName>
      <rightElementName>GUID_PARENT</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_8" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT_L">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_STOCK">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_STOCK0">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="MATID">
      <endUserTexts label="MATID"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_7</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT_L" sourceName="GUID_PARENT_L"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_STOCK" sourceName="GUID_STOCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_STOCK0" sourceName="GUID_STOCK0"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_11</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
    </input>
    <layout xCoordinate="443" yCoordinate="455" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_8/Join_7" rightInput="#/0/Join_8/Projection_11" joinType="inner">
      <leftElementName>GUID_STOCK0</leftElementName>
      <leftElementName>GUID_PARENT_L</leftElementName>
      <rightElementName>GUID_STOCK</rightElementName>
      <rightElementName>GUID_PARENT</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="Aggregation_2">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="MATID">
      <endUserTexts label="MATID"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY" aggregationBehavior="SUM">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_8</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="408" yCoordinate="377" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Union" name="Union_1">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="MATID">
      <endUserTexts label="MATID"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_BY" transparentFilter="false">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC" transparentFilter="false">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:Projection">#/0/PRODTO</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:Projection">#/0/HUTO_WITHMAT</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:Aggregation">#/0/Aggregation_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="254" yCoordinate="243" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="Aggregation_1">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="MATID">
      <endUserTexts label="MATID"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="VLPLA">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY" aggregationBehavior="SUM">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY" transparentFilter="false">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC" transparentFilter="false">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Union">#/0/Union_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="254" yCoordinate="165" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection">
    <element name="LGNUM" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_DOC" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="GUID_DOC"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_YEAR" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="DOC_YEAR"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_NUMBER" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_NO" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="ITEM_NO"/>
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="TANUM" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="MATID" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="MATID"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="VLPLA" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="VLPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="VLENR" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="VLENR"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="QUANTITY" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CREATED_AT_UTC" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY" transparentFilter="false" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_UTC" transparentFilter="false" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="CREATED_AT_UTC"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Aggregation">#/0/Aggregation_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLENR" sourceName="VLENR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT_UTC" sourceName="CREATED_AT_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_UTC" sourceName="CONFIRMED_AT_UTC"/>
    </input>
    <layout xCoordinate="254" yCoordinate="87" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewLayout relativeWidthScenario="44"/>
</View:ColumnView>
'''


cv = '''<?xml version="1.0" encoding="UTF-8"?>
<View:ColumnView xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:Column="http://www.sap.com/ndb/DataModelFilter.ecore" xmlns:Type="http://www.sap.com/ndb/DataModelType.ecore" xmlns:View="http://www.sap.com/ndb/ViewModelView.ecore" schemaVersion="2.3" name="CV_IN_OUT_POSTED" dataCategory="CUBE" hierarchiesSQLEnabled="false" defaultNode="#//Aggregation" clientDependent="false" applyPrivilegeType="ANALYTIC_PRIVILEGE" translationRelevant="true">
  <endUserTexts label="CV_IN_OUT_POSTED"/>
  <origin/>
  <parameter name="IP_PREV_TST" mandatory="false" multipleSelections="false">
    <endUserTexts label="IP_PREV_TST"/>
    <inlineType name="DECIMAL" primitiveType="DECIMAL" length="15" scale="0"/>
    <defaultValue xsi:nil="true"/>
    <defaultExpression language="COLUMN_ENGINE">
      <formula>fixed(adddays(utcnow(),-2),15,0)</formula>
    </defaultExpression>
    <defaultRange lowValue="fixed(adddays(utcnow(),-2),15,0)" lowExpression="true"/>
  </parameter>
  <executionHints/>
  <viewNode xsi:type="View:Projection" name="Projection_1">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="PROCTY">
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="VSOLM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_AT">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <elementFilter elementName="CONFIRMED_AT">
      <valueFilter xsi:type="Column:SingleValueFilter" operator="GT" including="true" value="$$IP_PREV_TST$$"/>
    </elementFilter>
    <input>
      <entity>#//"SAPHANADB"./SCWM/ORDIM_C</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PROCTY" sourceName="PROCTY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
    </input>
    <layout xCoordinate="22" yCoordinate="609" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_2">
    <endUserTexts label=" "/>
    <element name="PACKNM">
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="PARNM">
      <inlineType primitiveType="NVARCHAR" length="15" precision="15" scale="0"/>
    </element>
    <element name="VALLOW">
      <inlineType primitiveType="NVARCHAR" length="255" precision="255" scale="0"/>
    </element>
    <elementFilter elementName="PACKNM">
      <valueFilter xsi:type="Column:SingleValueFilter" including="true" value="ZSBL_W319"/>
    </elementFilter>
    <elementFilter elementName="PARNM">
      <valueFilter xsi:type="Column:SingleValueFilter" including="true" value="PTWYWPT"/>
    </elementFilter>
    <input>
      <entity>#//"SAPHANADB".ZRBST_UPARVAL</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="PACKNM" sourceName="PACKNM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARNM" sourceName="PARNM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VALLOW" sourceName="VALLOW"/>
    </input>
    <layout xCoordinate="176" yCoordinate="531" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="Aggregation_1">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="VSOLM" aggregationBehavior="SUM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="PROCTY">
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CONFIRMED_AT">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#//Projection_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PROCTY" sourceName="PROCTY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
    </input>
    <layout xCoordinate="22" yCoordinate="531" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_1" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="VSOLM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_AT">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Aggregation">#//Aggregation_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
      <layout xCoordinate="50" yCoordinate="30"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#//Projection_2</viewNode>
      <layout xCoordinate="336" yCoordinate="30"/>
    </input>
    <layout xCoordinate="99" yCoordinate="435" width="-1" height="-1" expanded="true"/>
    <join leftInput="#//Join_1/Aggregation_1" rightInput="#//Join_1/Projection_2" joinType="inner">
      <leftElementName>PROCTY</leftElementName>
      <rightElementName>VALLOW</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_3">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TZONE">
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <input>
      <entity>#//REPORTING.PREPARE::CV_SCMB_TOENTITY</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TZONE" sourceName="TZONE"/>
    </input>
    <layout xCoordinate="253" yCoordinate="435" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_2" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="VSOLM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_AT">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="TZONE">
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="DATE" aggregationBehavior="NONE">
      <endUserTexts label="DATE"/>
      <inlineType name="DATE" primitiveType="DATE"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>utctolocal(date(&quot;CONFIRMED_AT&quot;),&quot;TZONE&quot;)</formula>
      </calculationDefinition>
    </element>
    <element name="TST" aggregationBehavior="NONE">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>utctolocal(date(&quot;CONFIRMED_AT&quot;),&quot;TZONE&quot;)</formula>
      </calculationDefinition>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#//Join_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
      <layout xCoordinate="50" yCoordinate="30"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#//Projection_3</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="TZONE" sourceName="TZONE"/>
      <layout xCoordinate="336" yCoordinate="30"/>
    </input>
    <layout xCoordinate="176" yCoordinate="339" width="0" height="0" expanded="true"/>
    <join leftInput="#//Join_2/Join_1" rightInput="#//Join_2/Projection_3" joinType="leftOuter">
      <leftElementName>LGNUM</leftElementName>
      <rightElementName>LGNUM</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_4">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="NOW_SHIFT_TST">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="NOW_SHIFT_START">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="NOW_SHIFT_END">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="PREV_SHIFT_END">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="PREV_SHIFT_START">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <input>
      <entity>#//REPORTING.PREPARE::CV_ZTLM_WH_CUST</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NOW_SHIFT_TST" sourceName="NOW_SHIFT_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NOW_SHIFT_START" sourceName="NOW_SHIFT_START"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NOW_SHIFT_END" sourceName="NOW_SHIFT_END"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PREV_SHIFT_END" sourceName="PREV_SHIFT_END"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PREV_SHIFT_START" sourceName="PREV_SHIFT_START"/>
    </input>
    <layout xCoordinate="22" yCoordinate="339" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_3" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DATE">
      <endUserTexts label="DATE"/>
      <inlineType name="DATE" primitiveType="DATE" length="0" precision="0" scale="0"/>
    </element>
    <element name="VSOLM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="LGNUM_1">
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="NOW_SHIFT_TST">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="NOW_SHIFT_START">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="NOW_SHIFT_END">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="PREV_SHIFT_END">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="PREV_SHIFT_START">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="SHIFT" aggregationBehavior="NONE">
      <endUserTexts label="SHIFT"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="1"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>if( &#xD;
&quot;TST&quot; >= &quot;NOW_SHIFT_START&quot; and &quot;TST&quot; &lt;= &quot;NOW_SHIFT_TST&quot;,&#xD;
'N',&#xD;
   if(&#xD;
   &quot;TST&quot; >= &quot;PREV_SHIFT_START&quot; and &quot;TST&quot; &lt;=&quot;PREV_SHIFT_END&quot;,&#xD;
   'P',&#xD;
   ''&#xD;
   )&#xD;
)</formula>
      </calculationDefinition>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#//Join_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DATE" sourceName="DATE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TST" sourceName="TST"/>
      <layout xCoordinate="50" yCoordinate="30"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#//Projection_4</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM_1" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NOW_SHIFT_TST" sourceName="NOW_SHIFT_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NOW_SHIFT_START" sourceName="NOW_SHIFT_START"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NOW_SHIFT_END" sourceName="NOW_SHIFT_END"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PREV_SHIFT_END" sourceName="PREV_SHIFT_END"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PREV_SHIFT_START" sourceName="PREV_SHIFT_START"/>
      <layout xCoordinate="336" yCoordinate="30"/>
    </input>
    <layout xCoordinate="99" yCoordinate="243" width="0" height="0" expanded="true"/>
    <join leftInput="#//Join_3/Join_2" rightInput="#//Join_3/Projection_4" joinType="leftOuter">
      <leftElementName>LGNUM</leftElementName>
      <rightElementName>LGNUM</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_5">
    <endUserTexts label=" "/>
    <element name="VSOLM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="DATE">
      <endUserTexts label="DATE"/>
      <inlineType name="DATE" primitiveType="DATE" length="0" precision="0" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="SHIFT">
      <endUserTexts label="SHIFT"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="1" precision="0" scale="0"/>
    </element>
    <elementFilter elementName="SHIFT">
      <valueFilter xsi:type="Column:ListValueFilter" operator="IN" including="true">
        <operands value="N"/>
        <operands value="P"/>
      </valueFilter>
    </elementFilter>
    <input>
      <viewNode xsi:type="View:JoinNode">#//Join_3</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DATE" sourceName="DATE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SHIFT" sourceName="SHIFT"/>
    </input>
    <layout xCoordinate="99" yCoordinate="165" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="Aggregation">
    <element name="VSOLM" aggregationBehavior="SUM" engineAggregation="SUM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="DATE" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="DATE"/>
      <inlineType name="DATE" primitiveType="DATE" length="0" precision="0" scale="0"/>
    </element>
    <element name="LGNUM" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="SHIFT" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="SHIFT"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="1" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#//Projection_5</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="DATE" sourceName="DATE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SHIFT" sourceName="SHIFT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
    </input>
    <layout xCoordinate="99" yCoordinate="87" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewLayout relativeWidthScenario="27"/>
</View:ColumnView>
'''

cv_rank = '''<?xml version="1.0" encoding="UTF-8"?>
<View:ColumnView xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:Column="http://www.sap.com/ndb/DataModelFilter.ecore" xmlns:Param="http://www.sap.com/ndb/ViewModelParameter.ecore" xmlns:Type="http://www.sap.com/ndb/DataModelType.ecore" xmlns:View="http://www.sap.com/ndb/ViewModelView.ecore" schemaVersion="2.3" name="CV_XTR_TD_SKIP_PIKING" dataCategory="DIMENSION" hierarchiesSQLEnabled="false" defaultNode="#/0/Projection" clientDependent="false" applyPrivilegeType="ANALYTIC_PRIVILEGE" translationRelevant="true">
  <endUserTexts label="CV_XTR_TD_SKIP_PIKING"/>
  <origin/>
  <parameter xsi:type="Param:DerivedParameter" name="IP_MANDT" mandatory="false" multipleSelections="false">
    <endUserTexts label="IP_MANDT"/>
    <inlineType name="CHAR" primitiveType="CHAR"/>
    <defaultValue xsi:nil="true"/>
    <derivationRule inputEnabled="false">
      <scriptObject>#/1</scriptObject>
    </derivationRule>
  </parameter>
  <executionHints/>
  <viewNode xsi:type="View:Projection" name="EXCEPTION">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="VSOLM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="TIMESTAMP">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <elementFilter elementName="MANDT">
      <valueFilter xsi:type="Column:SingleValueFilter" including="true" value="$$IP_MANDT$$"/>
    </elementFilter>
    <input>
      <entity>#/0/"SAPHANADB".ZTW075_EXCEPTION</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TIMESTAMP" sourceName="TIMESTAMP"/>
    </input>
    <layout xCoordinate="23" yCoordinate="1011" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="MAR">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="MATNR">
      <endUserTexts label="MATNR"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="SCM_MATID_GUID16">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <input>
      <entity>#/0/"SAPHANADB".MARA</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATNR" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SCM_MATID_GUID16" sourceName="SCM_MATID_GUID16"/>
    </input>
    <layout xCoordinate="177" yCoordinate="1011" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="ORDIM_C">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NISTM">
      <endUserTexts label="NISTM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="BATCHID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="CONFIRMED_AT">
      <endUserTexts label="CONFIRMED_AT"/>
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <input>
      <entity>#/0/"SAPHANADB"./SCWM/ORDIM_C</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NISTM" sourceName="NISTM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCHID" sourceName="BATCHID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
    </input>
    <layout xCoordinate="254" yCoordinate="915" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_1" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="VSOLM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="MATNR">
      <endUserTexts label="MATNR"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TIMESTAMP">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/EXCEPTION</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TIMESTAMP" sourceName="TIMESTAMP"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/MAR</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MATNR" sourceName="MATNR"/>
    </input>
    <layout xCoordinate="100" yCoordinate="915" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_1/EXCEPTION" rightInput="#/0/Join_1/MAR" joinType="leftOuter">
      <leftElementName>MANDT</leftElementName>
      <leftElementName>MATID</leftElementName>
      <rightElementName>MANDT</rightElementName>
      <rightElementName>SCM_MATID_GUID16</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_2" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="VSOLM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="MATNR">
      <endUserTexts label="MATNR"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="CONFIRMED_AT">
      <endUserTexts label="CONFIRMED_AT"/>
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="NISTM">
      <endUserTexts label="NISTM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TIMESTAMP">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATNR" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TIMESTAMP" sourceName="TIMESTAMP"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/ORDIM_C</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NISTM" sourceName="NISTM"/>
    </input>
    <layout xCoordinate="176" yCoordinate="819" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_2/Join_1" rightInput="#/0/Join_2/ORDIM_C" joinType="leftOuter">
      <leftElementName>MANDT</leftElementName>
      <leftElementName>LGNUM</leftElementName>
      <leftElementName>TANUM</leftElementName>
      <leftElementName>BATCH</leftElementName>
      <leftElementName>ENTITLED</leftElementName>
      <leftElementName>MATID</leftElementName>
      <rightElementName>MANDT</rightElementName>
      <rightElementName>LGNUM</rightElementName>
      <rightElementName>TANUM</rightElementName>
      <rightElementName>BATCHID</rightElementName>
      <rightElementName>ENTITLED</rightElementName>
      <rightElementName>MATID</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="EXCEPTION_2">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="TIMESTAMP">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <elementFilter elementName="MANDT">
      <valueFilter xsi:type="Column:SingleValueFilter" including="true" value="$$IP_MANDT$$"/>
    </elementFilter>
    <input>
      <entity>#/0/"SAPHANADB".ZTW075_EXCEPTION</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TIMESTAMP" sourceName="TIMESTAMP"/>
    </input>
    <layout xCoordinate="330" yCoordinate="819" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="LOG_HEAD">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOC_NUMBER">
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="DOC_YEAR">
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <input>
      <entity>#/0/"SAPHANADB"./LIME/PI_LOGHEAD</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_NUMBER" sourceName="DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_YEAR" sourceName="DOC_YEAR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
    </input>
    <layout xCoordinate="484" yCoordinate="819" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_3" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="TIMESTAMP">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/EXCEPTION_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TIMESTAMP" sourceName="TIMESTAMP"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/LOG_HEAD</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
    </input>
    <layout xCoordinate="390" yCoordinate="723" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_3/EXCEPTION_2" rightInput="#/0/Join_3/LOG_HEAD" joinType="leftOuter">
      <leftElementName>MANDT</leftElementName>
      <leftElementName>PI_DOC_NUMBER</leftElementName>
      <leftElementName>DOC_YEAR</leftElementName>
      <leftElementName>LGNUM</leftElementName>
      <rightElementName>MANDT</rightElementName>
      <rightElementName>DOC_NUMBER</rightElementName>
      <rightElementName>DOC_YEAR</rightElementName>
      <rightElementName>LGNUM</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="PI_IT_BIZ">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="LGNUM_HU">
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="HUIDENT">
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="ITEM_TYPE">
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <elementFilter elementName="ITEM_TYPE">
      <valueFilter xsi:type="Column:SingleValueFilter" including="true" value="P"/>
    </elementFilter>
    <input>
      <entity>#/0/"SAPHANADB"./LIME/PI_IT_BIZ</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM_HU" sourceName="LGNUM_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_TYPE" sourceName="ITEM_TYPE"/>
    </input>
    <layout xCoordinate="544" yCoordinate="723" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_4" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="TIMESTAMP">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_3</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TIMESTAMP" sourceName="TIMESTAMP"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/PI_IT_BIZ</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
    </input>
    <layout xCoordinate="451" yCoordinate="627" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_4/Join_3" rightInput="#/0/Join_4/PI_IT_BIZ" joinType="leftOuter">
      <leftElementName>MANDT</leftElementName>
      <leftElementName>GUID_DOC</leftElementName>
      <leftElementName>LGNUM</leftElementName>
      <leftElementName>LGPLA</leftElementName>
      <rightElementName>MANDT</rightElementName>
      <rightElementName>GUID_DOC</rightElementName>
      <rightElementName>LGNUM_HU</rightElementName>
      <rightElementName>HUIDENT</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="PI_IT_BIZ_2">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="LINE_IDX">
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ITEM_TYPE">
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <elementFilter elementName="ITEM_TYPE">
      <valueFilter xsi:type="Column:SingleValueFilter" including="true" value="P"/>
    </elementFilter>
    <input>
      <entity>#/0/"SAPHANADB"./LIME/PI_IT_BIZ</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LINE_IDX" sourceName="LINE_IDX"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_TYPE" sourceName="ITEM_TYPE"/>
    </input>
    <layout xCoordinate="297" yCoordinate="627" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_5" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="LINE_IDX">
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="TIMESTAMP">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_4</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TIMESTAMP" sourceName="TIMESTAMP"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/PI_IT_BIZ_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LINE_IDX" sourceName="LINE_IDX"/>
    </input>
    <layout xCoordinate="359" yCoordinate="531" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_5/Join_4" rightInput="#/0/Join_5/PI_IT_BIZ_2" joinType="leftOuter">
      <leftElementName>MANDT</leftElementName>
      <leftElementName>GUID_DOC</leftElementName>
      <leftElementName>ITEM_NO</leftElementName>
      <leftElementName>MATID</leftElementName>
      <rightElementName>MANDT</rightElementName>
      <rightElementName>GUID_DOC</rightElementName>
      <rightElementName>ITEM_NO</rightElementName>
      <rightElementName>MATID</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="PI_DOC_IT">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="LINE_IDX">
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="ITEM_TYPE">
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="COUNT_USER">
      <endUserTexts label="COUNT_USER"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="COUNT_DATE">
      <endUserTexts label="COUNT_DATE"/>
      <inlineType primitiveType="DECIMAL" length="21" precision="21" scale="7"/>
    </element>
    <element name="DOC_STATUS">
      <endUserTexts label="DOC_STATUS"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <elementFilter elementName="ITEM_TYPE">
      <valueFilter xsi:type="Column:SingleValueFilter" including="true" value="D"/>
    </elementFilter>
    <input>
      <entity>#/0/"SAPHANADB"./LIME/PI_DOC_IT</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LINE_IDX" sourceName="LINE_IDX"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_TYPE" sourceName="ITEM_TYPE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_USER" sourceName="COUNT_USER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_DATE" sourceName="COUNT_DATE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_STATUS" sourceName="DOC_STATUS"/>
    </input>
    <layout xCoordinate="513" yCoordinate="531" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_6" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="COUNT_USER">
      <endUserTexts label="COUNT_USER"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="LINE_IDX">
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="COUNT_DATE">
      <endUserTexts label="COUNT_DATE"/>
      <inlineType primitiveType="DECIMAL" length="21" precision="21" scale="7"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="DOC_STATUS">
      <endUserTexts label="DOC_STATUS"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TIMESTAMP">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_5</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LINE_IDX" sourceName="LINE_IDX"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TIMESTAMP" sourceName="TIMESTAMP"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/PI_DOC_IT</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_USER" sourceName="COUNT_USER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_DATE" sourceName="COUNT_DATE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_STATUS" sourceName="DOC_STATUS"/>
    </input>
    <layout xCoordinate="421" yCoordinate="435" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_6/Join_5" rightInput="#/0/Join_6/PI_DOC_IT" joinType="leftOuter">
      <leftElementName>MANDT</leftElementName>
      <leftElementName>LINE_IDX</leftElementName>
      <leftElementName>GUID_DOC</leftElementName>
      <leftElementName>ITEM_NO</leftElementName>
      <rightElementName>MANDT</rightElementName>
      <rightElementName>LINE_IDX</rightElementName>
      <rightElementName>GUID_DOC</rightElementName>
      <rightElementName>ITEM_NO</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="PI_DOC_TB">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="LINE_IDX">
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="ITEM_TYPE">
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <elementFilter elementName="ITEM_TYPE">
      <valueFilter xsi:type="Column:SingleValueFilter" including="true" value="D"/>
    </elementFilter>
    <input>
      <entity>#/0/"SAPHANADB"./LIME/PI_DOC_TB</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LINE_IDX" sourceName="LINE_IDX"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_TYPE" sourceName="ITEM_TYPE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
    </input>
    <layout xCoordinate="267" yCoordinate="435" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_7" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_USER">
      <endUserTexts label="COUNT_USER"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="COUNT_DATE">
      <endUserTexts label="COUNT_DATE"/>
      <inlineType primitiveType="DECIMAL" length="21" precision="21" scale="7"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="DOC_STATUS">
      <endUserTexts label="DOC_STATUS"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TIMESTAMP">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_6</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_USER" sourceName="COUNT_USER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_DATE" sourceName="COUNT_DATE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_STATUS" sourceName="DOC_STATUS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TIMESTAMP" sourceName="TIMESTAMP"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/PI_DOC_TB</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
    </input>
    <layout xCoordinate="330" yCoordinate="339" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_7/Join_6" rightInput="#/0/Join_7/PI_DOC_TB" joinType="leftOuter">
      <leftElementName>MANDT</leftElementName>
      <leftElementName>GUID_DOC</leftElementName>
      <leftElementName>ITEM_NO</leftElementName>
      <leftElementName>LINE_IDX</leftElementName>
      <rightElementName>MANDT</rightElementName>
      <rightElementName>GUID_DOC</rightElementName>
      <rightElementName>ITEM_NO</rightElementName>
      <rightElementName>LINE_IDX</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="ORDIM_C_2">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="BATCHID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="VLPLA">
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="NISTM">
      <endUserTexts label="NISTM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="TRART">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT">
      <endUserTexts label="CONFIRMED_AT"/>
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>(&quot;TRART&quot; ='2') and (&quot;NISTM&quot; > 0)</formula>
    </filterExpression>
    <input>
      <entity>#/0/"SAPHANADB"./SCWM/ORDIM_C</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCHID" sourceName="BATCHID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VLPLA" sourceName="VLPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NISTM" sourceName="NISTM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TRART" sourceName="TRART"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
    </input>
    <layout xCoordinate="22" yCoordinate="819" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_9" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="VSOLM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="MATNR">
      <endUserTexts label="MATNR"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="CONFIRMED_AT">
      <endUserTexts label="CONFIRMED_AT"/>
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="NISTM">
      <endUserTexts label="NISTM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TANUM_1">
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_1">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="CONFIRMED_BY_1">
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="TIMESTAMP">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="TEST_FLAG" aggregationBehavior="NONE">
      <inlineType name="VARCHAR" primitiveType="VARCHAR" length="1"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>if(&quot;CONFIRMED_AT_1&quot;>&quot;CONFIRMED_AT&quot;,'X','N')</formula>
      </calculationDefinition>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATNR" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NISTM" sourceName="NISTM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TIMESTAMP" sourceName="TIMESTAMP"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/ORDIM_C_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM_1" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_1" sourceName="CONFIRMED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY_1" sourceName="CONFIRMED_BY"/>
    </input>
    <layout xCoordinate="89" yCoordinate="723" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_9/Join_2" rightInput="#/0/Join_9/ORDIM_C_2" joinType="leftOuter">
      <leftElementName>MANDT</leftElementName>
      <leftElementName>LGNUM</leftElementName>
      <leftElementName>BATCH</leftElementName>
      <leftElementName>ENTITLED</leftElementName>
      <leftElementName>LGPLA</leftElementName>
      <leftElementName>CAT</leftElementName>
      <leftElementName>MATID</leftElementName>
      <rightElementName>MANDT</rightElementName>
      <rightElementName>LGNUM</rightElementName>
      <rightElementName>BATCHID</rightElementName>
      <rightElementName>ENTITLED</rightElementName>
      <rightElementName>VLPLA</rightElementName>
      <rightElementName>CAT</rightElementName>
      <rightElementName>MATID</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_1">
    <endUserTexts label=" "/>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="VSOLM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="MATNR">
      <endUserTexts label="MATNR"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="CONFIRMED_AT">
      <endUserTexts label="CONFIRMED_AT"/>
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="NISTM">
      <endUserTexts label="NISTM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TEST_FLAG">
      <inlineType name="VARCHAR" primitiveType="VARCHAR" length="1" precision="0" scale="0"/>
    </element>
    <element name="TANUM_1">
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_1">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="CONFIRMED_BY_1">
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="TIMESTAMP">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>(&quot;TEST_FLAG&quot; = 'X')</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_9</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATNR" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NISTM" sourceName="NISTM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TEST_FLAG" sourceName="TEST_FLAG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM_1" sourceName="TANUM_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_1" sourceName="CONFIRMED_AT_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY_1" sourceName="CONFIRMED_BY_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TIMESTAMP" sourceName="TIMESTAMP"/>
    </input>
    <layout xCoordinate="89" yCoordinate="627" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Rank" name="Rank_1">
    <endUserTexts label=" "/>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="VSOLM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="MATNR">
      <endUserTexts label="MATNR"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="CONFIRMED_AT">
      <endUserTexts label="CONFIRMED_AT"/>
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="NISTM">
      <endUserTexts label="NISTM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TEST_FLAG">
      <inlineType name="VARCHAR" primitiveType="VARCHAR" length="1" precision="0" scale="0"/>
    </element>
    <element name="TANUM_1">
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_1">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="CONFIRMED_BY_1">
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="TIMESTAMP">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="Rank_Column" aggregationBehavior="NONE">
      <inlineType primitiveType="BIGINT"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATNR" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NISTM" sourceName="NISTM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TEST_FLAG" sourceName="TEST_FLAG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM_1" sourceName="TANUM_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_1" sourceName="CONFIRMED_AT_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY_1" sourceName="CONFIRMED_BY_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TIMESTAMP" sourceName="TIMESTAMP"/>
      <layout xCoordinate="70" yCoordinate="30"/>
    </input>
    <layout xCoordinate="89" yCoordinate="531" width="-1" height="-1" expanded="true"/>
    <windowFunction>
      <partitionElement>#/0/Rank_1/TANUM</partitionElement>
      <order byElement="#/0/Rank_1/TANUM" direction="DESC"/>
      <rankThreshold>
        <constantValue>2000000</constantValue>
      </rankThreshold>
      <rankElement>#/0/Rank_1/Rank_Column</rankElement>
    </windowFunction>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_3">
    <endUserTexts label=" "/>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="VSOLM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="MATNR">
      <endUserTexts label="MATNR"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="CONFIRMED_AT">
      <endUserTexts label="CONFIRMED_AT"/>
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="NISTM">
      <endUserTexts label="NISTM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TEST_FLAG">
      <inlineType name="VARCHAR" primitiveType="VARCHAR" length="1" precision="0" scale="0"/>
    </element>
    <element name="TANUM_1">
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_1">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="Rank_Column">
      <inlineType primitiveType="BIGINT" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_BY_1">
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="TIMESTAMP">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <elementFilter elementName="Rank_Column">
      <valueFilter xsi:type="Column:SingleValueFilter" including="true" value="1"/>
    </elementFilter>
    <input>
      <viewNode xsi:type="View:Rank">#/0/Rank_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATNR" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NISTM" sourceName="NISTM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TEST_FLAG" sourceName="TEST_FLAG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM_1" sourceName="TANUM_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_1" sourceName="CONFIRMED_AT_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="Rank_Column" sourceName="Rank_Column"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY_1" sourceName="CONFIRMED_BY_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TIMESTAMP" sourceName="TIMESTAMP"/>
    </input>
    <layout xCoordinate="89" yCoordinate="435" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_11" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="VSOLM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="MATNR">
      <endUserTexts label="MATNR"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="CONFIRMED_AT">
      <endUserTexts label="CONFIRMED_AT"/>
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="NISTM">
      <endUserTexts label="NISTM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TANUM_1">
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_1">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="CONFIRMED_BY_1">
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="TIMESTAMP">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATNR" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NISTM" sourceName="NISTM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TIMESTAMP" sourceName="TIMESTAMP"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_3</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM_1" sourceName="TANUM_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_1" sourceName="CONFIRMED_AT_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY_1" sourceName="CONFIRMED_BY_1"/>
    </input>
    <layout xCoordinate="176" yCoordinate="339" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_11/Join_2" rightInput="#/0/Join_11/Projection_3" joinType="leftOuter">
      <leftElementName>LGNUM</leftElementName>
      <leftElementName>BATCH</leftElementName>
      <leftElementName>ENTITLED</leftElementName>
      <leftElementName>TANUM</leftElementName>
      <leftElementName>LGPLA</leftElementName>
      <leftElementName>CAT</leftElementName>
      <leftElementName>VSOLM</leftElementName>
      <leftElementName>CONFIRMED_BY</leftElementName>
      <rightElementName>LGNUM</rightElementName>
      <rightElementName>BATCH</rightElementName>
      <rightElementName>ENTITLED</rightElementName>
      <rightElementName>TANUM</rightElementName>
      <rightElementName>LGPLA</rightElementName>
      <rightElementName>CAT</rightElementName>
      <rightElementName>VSOLM</rightElementName>
      <rightElementName>CONFIRMED_BY</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_8" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="COUNT_USER">
      <endUserTexts label="COUNT_USER"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="COUNT_DATE">
      <endUserTexts label="COUNT_DATE"/>
      <inlineType primitiveType="DECIMAL" length="21" precision="21" scale="7"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="VSOLM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="MATNR">
      <endUserTexts label="MATNR"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="CONFIRMED_AT">
      <endUserTexts label="CONFIRMED_AT"/>
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="NISTM">
      <endUserTexts label="NISTM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="MATID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TANUM_1">
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_1">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="CONFIRMED_BY_1">
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="DOC_STATUS">
      <endUserTexts label="DOC_STATUS"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TIMESTAMP">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_11</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATNR" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NISTM" sourceName="NISTM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATID" sourceName="MATID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM_1" sourceName="TANUM_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_1" sourceName="CONFIRMED_AT_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY_1" sourceName="CONFIRMED_BY_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TIMESTAMP" sourceName="TIMESTAMP"/>
    </input>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_7</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_USER" sourceName="COUNT_USER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_DATE" sourceName="COUNT_DATE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_STATUS" sourceName="DOC_STATUS"/>
    </input>
    <layout xCoordinate="253" yCoordinate="243" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_8/Join_11" rightInput="#/0/Join_8/Join_7" joinType="leftOuter">
      <leftElementName>MANDT</leftElementName>
      <leftElementName>LGNUM</leftElementName>
      <leftElementName>BATCH</leftElementName>
      <leftElementName>ENTITLED</leftElementName>
      <leftElementName>TANUM</leftElementName>
      <leftElementName>LGPLA</leftElementName>
      <leftElementName>CAT</leftElementName>
      <leftElementName>MATID</leftElementName>
      <leftElementName>PI_DOC_NUMBER</leftElementName>
      <leftElementName>TIMESTAMP</leftElementName>
      <rightElementName>MANDT</rightElementName>
      <rightElementName>LGNUM</rightElementName>
      <rightElementName>BATCH</rightElementName>
      <rightElementName>ENTITLED</rightElementName>
      <rightElementName>TANUM</rightElementName>
      <rightElementName>LGPLA</rightElementName>
      <rightElementName>CAT</rightElementName>
      <rightElementName>MATID</rightElementName>
      <rightElementName>PI_DOC_NUMBER</rightElementName>
      <rightElementName>TIMESTAMP</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Final">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="MATNR">
      <endUserTexts label="MATNR"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="BATCH_OLD">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ENTITLED">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_OLD">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="TANUM">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="VSOLM">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="NISTM">
      <endUserTexts label="NISTM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_BY">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="TANUM_CONF">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_CONF_OLD">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="COUNT_USER">
      <endUserTexts label="COUNT_USER"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="COUNT_DATE">
      <endUserTexts label="COUNT_DATE"/>
      <inlineType primitiveType="DECIMAL" length="21" precision="21" scale="7"/>
    </element>
    <element name="QUANTITY">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_BY_1">
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="DOC_STATUS">
      <endUserTexts label="DOC_STATUS"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="BATCH" aggregationBehavior="NONE">
      <endUserTexts label="BATCH"/>
      <inlineType name="VARBINARY" primitiveType="VARBINARY" length="16"/>
      <calculationDefinition language="SQL">
        <formula>&quot;BATCH_OLD&quot;</formula>
      </calculationDefinition>
    </element>
    <element name="CONFIRMED_AT" aggregationBehavior="NONE">
      <endUserTexts label="CONFIRMED_AT"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;CONFIRMED_AT_OLD&quot;</formula>
      </calculationDefinition>
    </element>
    <element name="CONFIRMED_AT_CONF" aggregationBehavior="NONE">
      <endUserTexts label="CONFIRMED_AT_CONF"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;CONFIRMED_AT_CONF_OLD&quot;</formula>
      </calculationDefinition>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_8</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATNR" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH_OLD" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_OLD" sourceName="CONFIRMED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NISTM" sourceName="NISTM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM_CONF" sourceName="TANUM_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_CONF_OLD" sourceName="CONFIRMED_AT_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_USER" sourceName="COUNT_USER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_DATE" sourceName="COUNT_DATE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY_1" sourceName="CONFIRMED_BY_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_STATUS" sourceName="DOC_STATUS"/>
    </input>
    <layout xCoordinate="253" yCoordinate="165" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection">
    <element name="LGNUM" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGPLA" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="MATNR" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="MATNR"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="BATCH" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="BATCH"/>
      <inlineType name="VARBINARY" primitiveType="VARBINARY" length="16" precision="0" scale="0"/>
    </element>
    <element name="ENTITLED" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="ENTITLED"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="CAT" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="CONFIRMED_AT" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="CONFIRMED_AT"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="TANUM" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="VSOLM" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="VSOLM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="NISTM" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="NISTM"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CONFIRMED_BY" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="PI_DOC_NUMBER" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="PI_DOC_NUMBER"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="TANUM_CONF" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="TANUM"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_BY_CONF" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="CONFIRMED_BY"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="CONFIRMED_AT_CONF" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="CONFIRMED_AT_CONF"/>
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="COUNT_USER" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="COUNT_USER"/>
      <inlineType primitiveType="NVARCHAR" length="12" precision="12" scale="0"/>
    </element>
    <element name="COUNT_DATE" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="COUNT_DATE"/>
      <inlineType primitiveType="DECIMAL" length="21" precision="21" scale="7"/>
    </element>
    <element name="QUANTITY" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="QUANTITY"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="DOC_STATUS" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="DOC_STATUS"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Final</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATNR" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ENTITLED" sourceName="ENTITLED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM" sourceName="TANUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="VSOLM" sourceName="VSOLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NISTM" sourceName="NISTM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY" sourceName="CONFIRMED_BY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PI_DOC_NUMBER" sourceName="PI_DOC_NUMBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TANUM_CONF" sourceName="TANUM_CONF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_BY_CONF" sourceName="CONFIRMED_BY_1"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT_CONF" sourceName="CONFIRMED_AT_CONF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_USER" sourceName="COUNT_USER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_DATE" sourceName="COUNT_DATE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUANTITY" sourceName="QUANTITY"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOC_STATUS" sourceName="DOC_STATUS"/>
    </input>
    <layout xCoordinate="253" yCoordinate="87" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewLayout relativeWidthScenario="45"/>
</View:ColumnView>
'''

editorInput = Text(wrap="word")
editorInput.pack(fill="both")
InsertTextToOutput(editorInput, cv_rank)

btnConvertion = ttk.Button(text="Конвертировать", command=ClickbtnConvertion)
btnConvertion.pack()

editorOutput = Text(wrap="word")
editorOutput.pack(fill="both")


root.mainloop()
