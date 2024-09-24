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

editorInput = Text(wrap="word")
editorInput.pack(fill="both")
InsertTextToOutput(editorInput, cv_stock)

btnConvertion = ttk.Button(text="Конвертировать", command=ClickbtnConvertion)
btnConvertion.pack()

editorOutput = Text(wrap="word")
editorOutput.pack(fill="both")


root.mainloop()
