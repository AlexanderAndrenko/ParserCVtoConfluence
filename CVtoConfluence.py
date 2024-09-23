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
<View:ColumnView xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:Type="http://www.sap.com/ndb/DataModelType.ecore" xmlns:View="http://www.sap.com/ndb/ViewModelView.ecore" schemaVersion="2.3" name="CV_XTR_ERP_STOCK" dataCategory="CUBE" hierarchiesSQLEnabled="false" defaultNode="#//Aggregation" clientDependent="false" applyPrivilegeType="ANALYTIC_PRIVILEGE" translationRelevant="true">
  <endUserTexts label="CV_XTR_ERP_STOCK"/>
  <origin/>
  <executionHints/>
  <viewNode xsi:type="View:Projection" name="MARC_">
    <endUserTexts label=" "/>
    <element name="MATERIAL">
      <endUserTexts label="MATERIAL"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="PLANT">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TRAME">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="UMLMC">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="GLGMG">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="BWESB">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="RECTOTSTCK" aggregationBehavior="NONE">
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="13" scale="3"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;TRAME&quot;+&quot;UMLMC&quot;+&quot;GLGMG&quot;+&quot;BWESB&quot;</formula>
      </calculationDefinition>
    </element>
    <element name="BATCH" aggregationBehavior="NONE">
      <endUserTexts label="BATCH"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="10"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>''</formula>
      </calculationDefinition>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;PLANT&quot;!='' and &quot;RECTOTSTCK&quot;!=0</formula>
    </filterExpression>
    <input>
      <entity>#//"SAPHANADB".NSDM_V_MARC</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="WERKS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TRAME" sourceName="TRAME"/>
      <mapping xsi:type="Type:ElementMapping" targetName="UMLMC" sourceName="UMLMC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GLGMG" sourceName="GLGMG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BWESB" sourceName="BWESB"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
    </input>
    <layout xCoordinate="22" yCoordinate="779" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="MCHB_">
    <endUserTexts label=" "/>
    <element name="MATERIAL">
      <endUserTexts label="MATERIAL"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="PLANT">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="STOR_LOC">
      <endUserTexts label="STOR_LOC"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="CLABS">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="CINSM">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="CSPEM">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="CUMLM">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="CRETM">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="CEINM">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="RECTOTSTCK" aggregationBehavior="NONE">
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="13" scale="3"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;CLABS&quot;+&quot;CINSM&quot;+&quot;CSPEM&quot;+&quot;CUMLM&quot;+&quot;CRETM&quot;+&quot;CEINM&quot;</formula>
      </calculationDefinition>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;PLANT&quot;!=''  and &quot;RECTOTSTCK&quot;!=0</formula>
    </filterExpression>
    <input>
      <entity>#//"SAPHANADB".NSDM_V_MCHB</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="WERKS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STOR_LOC" sourceName="LGORT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="CHARG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLABS" sourceName="CLABS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CINSM" sourceName="CINSM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CSPEM" sourceName="CSPEM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CUMLM" sourceName="CUMLM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CRETM" sourceName="CRETM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CEINM" sourceName="CEINM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
    </input>
    <layout xCoordinate="417" yCoordinate="1031" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="MARD_">
    <endUserTexts label=" "/>
    <element name="MATERIAL">
      <endUserTexts label="MATERIAL"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="PLANT">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="STOR_LOC">
      <endUserTexts label="STOR_LOC"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LABST">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="INSME">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="SPEME">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="RETME">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="UMLME">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="RECTOTSTCK" aggregationBehavior="NONE">
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="13" scale="3"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;LABST&quot;+&quot;INSME&quot;+&quot;SPEME&quot;+&quot;RETME&quot;+&quot;UMLME&quot;</formula>
      </calculationDefinition>
    </element>
    <element name="BATCH" aggregationBehavior="NONE">
      <endUserTexts label="BATCH"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="10"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>''</formula>
      </calculationDefinition>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;PLANT&quot;!='' and &quot;RECTOTSTCK&quot;!=0</formula>
    </filterExpression>
    <input>
      <entity>#//"SAPHANADB".NSDM_V_MARD</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="WERKS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STOR_LOC" sourceName="LGORT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LABST" sourceName="LABST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="INSME" sourceName="INSME"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SPEME" sourceName="SPEME"/>
      <mapping xsi:type="Type:ElementMapping" targetName="RETME" sourceName="RETME"/>
      <mapping xsi:type="Type:ElementMapping" targetName="UMLME" sourceName="UMLME"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
    </input>
    <layout xCoordinate="176" yCoordinate="953" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="MKOL">
    <endUserTexts label=" "/>
    <element name="MATERIAL">
      <endUserTexts label="MATERIAL"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="PLANT">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="STOR_LOC">
      <endUserTexts label="STOR_LOC"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="SLABS" aggregationBehavior="SUM">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="SINSM" aggregationBehavior="SUM">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="SSPEM" aggregationBehavior="SUM">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="SEINM" aggregationBehavior="SUM">
      <inlineType primitiveType="DECIMAL" length="18" precision="18" scale="3"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="RECTOTSTCK" aggregationBehavior="NONE">
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="13" scale="3"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;SLABS&quot;+&quot;SINSM&quot;+&quot;SSPEM&quot;+&quot;SEINM&quot;</formula>
      </calculationDefinition>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;PLANT&quot;!='' and &quot;RECTOTSTCK&quot;!=0</formula>
    </filterExpression>
    <input>
      <entity>#//"SAPHANADB".NSDM_V_MKOL</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="WERKS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STOR_LOC" sourceName="LGORT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="CHARG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SLABS" sourceName="SLABS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SINSM" sourceName="SINSM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SSPEM" sourceName="SSPEM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SEINM" sourceName="SEINM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
    </input>
    <layout xCoordinate="176" yCoordinate="779" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="Aggregation_1">
    <endUserTexts label=" "/>
    <element name="MATERIAL_MCHB">
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="PLANT">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="STOR_LOC">
      <endUserTexts label="STOR_LOC"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="RECTOTSTCK" aggregationBehavior="SUM">
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="13" precision="0" scale="3"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#//MCHB_</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL_MCHB" sourceName="MATERIAL"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="PLANT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STOR_LOC" sourceName="STOR_LOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="RECTOTSTCK" sourceName="RECTOTSTCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
    </input>
    <layout xCoordinate="330" yCoordinate="953" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="EXCEPT1" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="RECTOTSTCK">
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="13" precision="0" scale="3"/>
    </element>
    <element name="MATERIAL">
      <endUserTexts label="MATERIAL"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="PLANT">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="STOR_LOC">
      <endUserTexts label="STOR_LOC"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="MATERIAL_MCHB">
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="10" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#//MARD_</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="RECTOTSTCK" sourceName="RECTOTSTCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATERIAL"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="PLANT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STOR_LOC" sourceName="STOR_LOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
    </input>
    <input>
      <viewNode xsi:type="View:Aggregation">#//Aggregation_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL_MCHB" sourceName="MATERIAL_MCHB"/>
    </input>
    <layout xCoordinate="330" yCoordinate="857" width="-1" height="-1" expanded="true"/>
    <join leftInput="#//EXCEPT1/MARD_" rightInput="#//EXCEPT1/Aggregation_1" joinType="leftOuter">
      <leftElementName>MATERIAL</leftElementName>
      <leftElementName>PLANT</leftElementName>
      <leftElementName>STOR_LOC</leftElementName>
      <leftElementName>MANDT</leftElementName>
      <rightElementName>MATERIAL_MCHB</rightElementName>
      <rightElementName>PLANT</rightElementName>
      <rightElementName>STOR_LOC</rightElementName>
      <rightElementName>MANDT</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="EXCEPT2">
    <endUserTexts label=" "/>
    <element name="MATERIAL">
      <endUserTexts label="MATERIAL"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="PLANT">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="STOR_LOC">
      <endUserTexts label="STOR_LOC"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="RECTOTSTCK">
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="13" precision="0" scale="3"/>
    </element>
    <element name="MATERIAL_MCHB">
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="10" precision="0" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>isNull(&quot;MATERIAL_MCHB&quot;)</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:JoinNode">#//EXCEPT1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATERIAL"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="PLANT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STOR_LOC" sourceName="STOR_LOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="RECTOTSTCK" sourceName="RECTOTSTCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL_MCHB" sourceName="MATERIAL_MCHB"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
    </input>
    <layout xCoordinate="330" yCoordinate="779" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Union" name="Union_1">
    <endUserTexts label=" "/>
    <element name="MATERIAL">
      <endUserTexts label="MATERIAL"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="PLANT">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="RECTOTSTCK">
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="13" precision="0" scale="3"/>
    </element>
    <element name="STOR_LOC">
      <endUserTexts label="STOR_LOC"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="10" precision="0" scale="0"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:Projection">#//MARC_</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATERIAL"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="PLANT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="RECTOTSTCK" sourceName="RECTOTSTCK"/>
      <mapping xsi:type="Type:ConstantElementMapping" targetName="STOR_LOC" value="" null="true"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
    </input>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:Projection">#//MCHB_</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATERIAL"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="PLANT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="RECTOTSTCK" sourceName="RECTOTSTCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STOR_LOC" sourceName="STOR_LOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
    </input>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:Aggregation">#//MKOL</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATERIAL"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="PLANT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="RECTOTSTCK" sourceName="RECTOTSTCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STOR_LOC" sourceName="STOR_LOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
    </input>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:Projection">#//EXCEPT2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATERIAL"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="PLANT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="RECTOTSTCK" sourceName="RECTOTSTCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STOR_LOC" sourceName="STOR_LOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
    </input>
    <layout xCoordinate="330" yCoordinate="627" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="MARA_">
    <endUserTexts label=" "/>
    <element name="MATNR">
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="SYSTEM_ID">
      <endUserTexts label="SYSTEM_ID"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="BISMT">
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="PRODUCT_ID" aggregationBehavior="NONE">
      <endUserTexts label="PRODUCT_ID"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="40"/>
      <calculationDefinition language="SQL">
        <formula>substr_after(&quot;BISMT&quot;,'\')</formula>
      </calculationDefinition>
    </element>
    <input>
      <entity>#//"SAPHANADB".MARA</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MATNR" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SYSTEM_ID" sourceName="ZZSYSTEM_ID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BISMT" sourceName="BISMT"/>
    </input>
    <layout xCoordinate="484" yCoordinate="549" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="Aggregation_2">
    <endUserTexts label=" "/>
    <element name="MATERIAL">
      <endUserTexts label="MATERIAL"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="PLANT">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="STOR_LOC">
      <endUserTexts label="STOR_LOC"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="10" precision="0" scale="0"/>
    </element>
    <element name="RECTOTSTCK" aggregationBehavior="SUM">
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="13" precision="0" scale="3"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Union">#//Union_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATERIAL"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="PLANT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STOR_LOC" sourceName="STOR_LOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="RECTOTSTCK" sourceName="RECTOTSTCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
    </input>
    <layout xCoordinate="330" yCoordinate="549" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_1" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="SYSTEM_ID">
      <endUserTexts label="SYSTEM_ID"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="MATERIAL">
      <endUserTexts label="MATERIAL"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="PLANT">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="STOR_LOC">
      <endUserTexts label="STOR_LOC"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="10" precision="0" scale="0"/>
    </element>
    <element name="RECTOTSTCK">
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="13" precision="0" scale="3"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="PRODUCT_ID">
      <endUserTexts label="PRODUCT_ID"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="40" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Aggregation">#//Aggregation_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATERIAL"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="PLANT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STOR_LOC" sourceName="STOR_LOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="RECTOTSTCK" sourceName="RECTOTSTCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#//MARA_</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="SYSTEM_ID" sourceName="SYSTEM_ID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PRODUCT_ID" sourceName="PRODUCT_ID"/>
    </input>
    <layout xCoordinate="407" yCoordinate="453" width="0" height="0" expanded="true"/>
    <join leftInput="#//Join_1/Aggregation_2" rightInput="#//Join_1/MARA_" joinType="inner">
      <leftElementName>MATERIAL</leftElementName>
      <leftElementName>MANDT</leftElementName>
      <rightElementName>MATNR</rightElementName>
      <rightElementName>MANDT</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="VBBE_">
    <endUserTexts label=" "/>
    <element name="WERKS">
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="MATNR">
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="LGORT">
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="OD_ERP" aggregationBehavior="SUM">
      <endUserTexts label="OD_ERP"/>
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="3"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="CHARG">
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;OD_ERP&quot;!=0</formula>
    </filterExpression>
    <input>
      <entity>#//"SAPHANADB".VBBE</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="WERKS" sourceName="WERKS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATNR" sourceName="MATNR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGORT" sourceName="LGORT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="OD_ERP" sourceName="OMENG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CHARG" sourceName="CHARG"/>
    </input>
    <layout xCoordinate="561" yCoordinate="453" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_2" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="10" precision="0" scale="0"/>
    </element>
    <element name="STOR_LOC">
      <endUserTexts label="STOR_LOC"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="PLANT">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="MATERIAL">
      <endUserTexts label="MATERIAL"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="RECTOTSTCK">
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="13" precision="0" scale="3"/>
    </element>
    <element name="SYSTEM_ID">
      <endUserTexts label="SYSTEM_ID"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="OD_ERP">
      <endUserTexts label="OD_ERP"/>
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="3"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="PRODUCT_ID">
      <endUserTexts label="PRODUCT_ID"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="40" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#//Join_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STOR_LOC" sourceName="STOR_LOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="PLANT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATERIAL"/>
      <mapping xsi:type="Type:ElementMapping" targetName="RECTOTSTCK" sourceName="RECTOTSTCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SYSTEM_ID" sourceName="SYSTEM_ID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PRODUCT_ID" sourceName="PRODUCT_ID"/>
    </input>
    <input>
      <viewNode xsi:type="View:Aggregation">#//VBBE_</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="OD_ERP" sourceName="OD_ERP"/>
    </input>
    <layout xCoordinate="483" yCoordinate="357" width="0" height="0" expanded="true"/>
    <join leftInput="#//Join_2/Join_1" rightInput="#//Join_2/VBBE_" joinType="leftOuter">
      <leftElementName>PLANT</leftElementName>
      <leftElementName>MATERIAL</leftElementName>
      <leftElementName>STOR_LOC</leftElementName>
      <leftElementName>MANDT</leftElementName>
      <leftElementName>BATCH</leftElementName>
      <rightElementName>WERKS</rightElementName>
      <rightElementName>MATNR</rightElementName>
      <rightElementName>LGORT</rightElementName>
      <rightElementName>MANDT</rightElementName>
      <rightElementName>CHARG</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="TMAPSTLOC_">
    <endUserTexts label=" "/>
    <element name="PLANT">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="STGE_LOC">
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGNUM" aggregationBehavior="MAX">
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="AVLGRP" aggregationBehavior="MAX">
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <input>
      <entity>#//"SAPHANADB"./SCWM/TMAPSTLOC</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="PLANT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STGE_LOC" sourceName="STGE_LOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="AVLGRP" sourceName="AVLGRP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
    </input>
    <layout xCoordinate="637" yCoordinate="357" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="TCAT_">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="AVLGRP">
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="CAT" aggregationBehavior="MAX">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <input>
      <entity>#//"SAPHANADB"./SCWM/TCAT</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="AVLGRP" sourceName="AVLGRP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
    </input>
    <layout xCoordinate="791" yCoordinate="357" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_4" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="PLANT">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="STGE_LOC">
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Aggregation">#//TMAPSTLOC_</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="PLANT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STGE_LOC" sourceName="STGE_LOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
    </input>
    <input>
      <viewNode xsi:type="View:Aggregation">#//TCAT_</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
    </input>
    <layout xCoordinate="637" yCoordinate="261" width="-1" height="-1" expanded="true"/>
    <join leftInput="#//Join_4/TMAPSTLOC_" rightInput="#//Join_4/TCAT_" joinType="inner">
      <leftElementName>LGNUM</leftElementName>
      <leftElementName>AVLGRP</leftElementName>
      <leftElementName>MANDT</leftElementName>
      <rightElementName>LGNUM</rightElementName>
      <rightElementName>AVLGRP</rightElementName>
      <rightElementName>MANDT</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_1">
    <endUserTexts label=" "/>
    <element name="SYSTEM_ID">
      <endUserTexts label="SYSTEM_ID"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="RECTOTSTCK">
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="13" precision="0" scale="3"/>
    </element>
    <element name="MATERIAL">
      <endUserTexts label="MATERIAL"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="PLANT">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="STOR_LOC">
      <endUserTexts label="STOR_LOC"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="10" precision="0" scale="0"/>
    </element>
    <element name="OD_ERP">
      <endUserTexts label="OD_ERP"/>
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="3"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="PRODUCT_ID">
      <endUserTexts label="PRODUCT_ID"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="40" precision="0" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;RECTOTSTCK&quot;!=0 or &quot;OD_ERP&quot;!=0</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:JoinNode">#//Join_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="SYSTEM_ID" sourceName="SYSTEM_ID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="RECTOTSTCK" sourceName="RECTOTSTCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATERIAL"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="PLANT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STOR_LOC" sourceName="STOR_LOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="OD_ERP" sourceName="OD_ERP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PRODUCT_ID" sourceName="PRODUCT_ID"/>
    </input>
    <layout xCoordinate="483" yCoordinate="261" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_3" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="CAT">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="SYSTEM_ID">
      <endUserTexts label="SYSTEM_ID"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="RECTOTSTCK">
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="13" precision="0" scale="3"/>
    </element>
    <element name="MATERIAL">
      <endUserTexts label="MATERIAL"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="PLANT">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="STOR_LOC">
      <endUserTexts label="STOR_LOC"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="BATCH">
      <endUserTexts label="BATCH"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="10" precision="0" scale="0"/>
    </element>
    <element name="OD_ERP_TECH">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="3"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="PRODUCT_ID">
      <endUserTexts label="PRODUCT_ID"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="40" precision="0" scale="0"/>
    </element>
    <element name="OD_ERP" aggregationBehavior="NONE">
      <endUserTexts label="OD_ERP"/>
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="15" scale="3"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>if(isnull(&quot;OD_ERP_TECH&quot;),0, &quot;OD_ERP_TECH&quot;)</formula>
      </calculationDefinition>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#//Projection_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="SYSTEM_ID" sourceName="SYSTEM_ID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="RECTOTSTCK" sourceName="RECTOTSTCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATERIAL"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="PLANT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STOR_LOC" sourceName="STOR_LOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="OD_ERP_TECH" sourceName="OD_ERP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PRODUCT_ID" sourceName="PRODUCT_ID"/>
    </input>
    <input>
      <viewNode xsi:type="View:JoinNode">#//Join_4</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
    </input>
    <layout xCoordinate="560" yCoordinate="165" width="0" height="0" expanded="true"/>
    <join leftInput="#//Join_3/Projection_1" rightInput="#//Join_3/Join_4" joinType="leftOuter">
      <leftElementName>PLANT</leftElementName>
      <leftElementName>STOR_LOC</leftElementName>
      <leftElementName>MANDT</leftElementName>
      <rightElementName>PLANT</rightElementName>
      <rightElementName>STGE_LOC</rightElementName>
      <rightElementName>MANDT</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="Aggregation">
    <element name="MATERIAL" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="MATERIAL"/>
      <inlineType primitiveType="NVARCHAR" length="40" precision="40" scale="0"/>
    </element>
    <element name="SYSTEM_ID" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="SYSTEM_ID"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="PLANT" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="PLANT"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="STOR_LOC" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="STOR_LOC"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="BATCH" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="BATCH"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="10" precision="0" scale="0"/>
    </element>
    <element name="CAT" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="CAT"/>
      <inlineType primitiveType="NVARCHAR" length="2" precision="2" scale="0"/>
    </element>
    <element name="PRODUCT_ID" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="PRODUCT_ID"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="40" precision="0" scale="0"/>
    </element>
    <element name="ALL_ERP" aggregationBehavior="SUM" engineAggregation="SUM">
      <endUserTexts label="ALL_ERP"/>
      <inlineType primitiveType="DECIMAL" length="13" precision="0" scale="3"/>
    </element>
    <element name="OD_ERP" aggregationBehavior="SUM" engineAggregation="SUM">
      <endUserTexts label="OD_ERP"/>
      <inlineType primitiveType="DECIMAL" length="15" precision="0" scale="3"/>
    </element>
    <element name="FREE_ERP" hidden="false" aggregationBehavior="FORMULA" engineAggregation="FORMULA">
      <endUserTexts label="FREE_ERP"/>
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="18" scale="3"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;ALL_ERP&quot;-&quot;OD_ERP&quot;</formula>
      </calculationDefinition>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#//Join_3</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="MATERIAL" sourceName="MATERIAL"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SYSTEM_ID" sourceName="SYSTEM_ID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PLANT" sourceName="PLANT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STOR_LOC" sourceName="STOR_LOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="BATCH" sourceName="BATCH"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CAT" sourceName="CAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PRODUCT_ID" sourceName="PRODUCT_ID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ALL_ERP" sourceName="RECTOTSTCK"/>
      <mapping xsi:type="Type:ElementMapping" targetName="OD_ERP" sourceName="OD_ERP"/>
    </input>
    <layout xCoordinate="560" yCoordinate="87" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewLayout relativeWidthScenario="47"/>
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
InsertTextToOutput(editorInput, cv)

btnConvertion = ttk.Button(text="Конвертировать", command=ClickbtnConvertion)
btnConvertion.pack()

editorOutput = Text(wrap="word")
editorOutput.pack(fill="both")


root.mainloop()
