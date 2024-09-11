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
    
cv = '''<?xml version="1.0" encoding="UTF-8"?>
<View:ColumnView xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:Column="http://www.sap.com/ndb/DataModelFilter.ecore" xmlns:Param="http://www.sap.com/ndb/ViewModelParameter.ecore" xmlns:Type="http://www.sap.com/ndb/DataModelType.ecore" xmlns:View="http://www.sap.com/ndb/ViewModelView.ecore" schemaVersion="2.3" name="CV_IN_OUT_REP_03_DETAIL" dataCategory="CUBE" hierarchiesSQLEnabled="false" defaultNode="#/0/Aggregation" clientDependent="false" applyPrivilegeType="ANALYTIC_PRIVILEGE" translationRelevant="true">
  <endUserTexts label="CV_IN_OUT_REP_01">
    <comment text="Показатели:&#xD;&#xA;3&#x9;&#x9;Входящий&#x9;План приемки&#xD;&#xA;12&#x9;Входящий&#x9;В процессе приемки&#xD;&#xA;6&#x9;&#x9;Входящий&#x9;В работе приемки более 10 часов&#xD;&#xA;"/>
  </endUserTexts>
  <origin/>
  <parameter name="IP_PREV_CHG" mandatory="false" multipleSelections="false">
    <endUserTexts label="IP_PREV_CHG"/>
    <inlineType name="DECIMAL" primitiveType="DECIMAL" length="15" scale="0"/>
    <defaultValue xsi:nil="true"/>
    <defaultExpression language="COLUMN_ENGINE">
      <formula>fixed(adddays(utcnow(), -10),15,0)</formula>
    </defaultExpression>
    <defaultRange lowValue="fixed(adddays(utcnow(), -10),15,0)" lowExpression="true"/>
  </parameter>
  <parameter name="IP_NOW_CHG" mandatory="false" multipleSelections="false">
    <endUserTexts label="IP_NOW_CHG"/>
    <inlineType name="DECIMAL" primitiveType="DECIMAL" length="15" scale="0"/>
    <defaultValue xsi:nil="true"/>
    <defaultExpression language="COLUMN_ENGINE">
      <formula>fixed(utcnow(),15,0)</formula>
    </defaultExpression>
    <defaultRange lowValue="fixed(utcnow(),15,0)" lowExpression="true"/>
  </parameter>
  <parameter name="IP_NOW_TST" mandatory="false" multipleSelections="false">
    <endUserTexts label="IP_NOW_TST"/>
    <inlineType name="DECIMAL" primitiveType="DECIMAL" length="15" scale="0"/>
    <defaultValue xsi:nil="true"/>
    <defaultExpression language="COLUMN_ENGINE">
      <formula>fixed(utcnow(),15,0)</formula>
    </defaultExpression>
    <defaultRange lowValue="fixed(utcnow(),15,0)" lowExpression="true"/>
  </parameter>
  <parameter name="IP_PREV_DAY_TST" mandatory="false" multipleSelections="false">
    <endUserTexts label="IP_PREV_DAY_TST"/>
    <inlineType name="DECIMAL" primitiveType="DECIMAL" length="15" scale="0"/>
    <defaultValue xsi:nil="true"/>
    <defaultExpression language="COLUMN_ENGINE">
      <formula>fixed(adddays(utcnow(), -1),15,0)</formula>
    </defaultExpression>
    <defaultRange lowValue="fixed(adddays(utcnow(), -1),15,0)" lowExpression="true"/>
  </parameter>
  <parameter xsi:type="Param:DerivedParameter" name="IP_MANDT" mandatory="false" multipleSelections="false">
    <endUserTexts label="IP_MANDT"/>
    <inlineType name="CHAR" primitiveType="CHAR"/>
    <defaultValue xsi:nil="true"/>
    <derivationRule inputEnabled="false">
      <scriptObject>#/1</scriptObject>
    </derivationRule>
  </parameter>
  <executionHints/>
  <viewNode xsi:type="View:Projection" name="PROCH_I">
    <endUserTexts label=" "/>
    <element name="DOCID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOCTYPE">
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOCCAT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="CHGTST">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>(in (&quot;DOCTYPE&quot;,'ZIGF','ZIMU','ZIGU')) AND (&quot;DOCCAT&quot; ='PDI')</formula>
    </filterExpression>
    <input alias="_SCDL_DB_PROCH_I">
      <entity>#/0/"SAPHANADB"./SCDL/DB_PROCH_I</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCID" sourceName="DOCID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCTYPE" sourceName="DOCTYPE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCCAT" sourceName="DOCCAT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CHGTST" sourceName="CHGTST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
    </input>
    <layout xCoordinate="22" yCoordinate="2055" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_1">
    <endUserTexts label=" "/>
    <element name="GUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOCID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <input>
      <entity>#/0/REPORTING.PREPARE::CV_HUREF</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCID" sourceName="DOCID"/>
    </input>
    <layout xCoordinate="176" yCoordinate="2055" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_1" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="DOCID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/PROCH_I</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCID" sourceName="DOCID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
    </input>
    <layout xCoordinate="99" yCoordinate="1959" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_1/PROCH_I" rightInput="#/0/Join_1/Projection_1" joinType="inner">
      <leftElementName>DOCID</leftElementName>
      <rightElementName>DOCID</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_3">
    <endUserTexts label=" "/>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CREATED_AT">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="CLOSED_DIFF" aggregationBehavior="NONE">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>rounddown( secondsbetween(&quot;CLOSED_TST&quot;, utcnow())/3600,0)</formula>
      </calculationDefinition>
    </element>
    <element name="CLOSED_TST" aggregationBehavior="NONE">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;CREATED_AT&quot;</formula>
      </calculationDefinition>
    </element>
    <input>
      <entity>#/0/REPORTING.PREPARE::CV_ORDIM_03</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CREATED_AT" sourceName="CREATED_AT"/>
      <parameterMapping xsi:type="Param:ParameterMapping" parameterNameOtherView="IP_NOW_TST" parameterName="IP_NOW_TST"/>
      <parameterMapping xsi:type="Param:ParameterMapping" parameterNameOtherView="IP_PREV_DAY_TST" parameterName="IP_PREV_DAY_TST"/>
    </input>
    <layout xCoordinate="96" yCoordinate="1767" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_7">
    <endUserTexts label=" "/>
    <element name="DOCID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="PARTYNO">
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <input>
      <entity>#/0/REPORTING.PREPARE::CV_DB_BPLOC</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCID" sourceName="DOCID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTYNO" sourceName="PARTYNO"/>
    </input>
    <layout xCoordinate="253" yCoordinate="1959" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_6" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="GUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="DOCID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="PARTYNO">
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCID" sourceName="DOCID"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_7</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTYNO" sourceName="PARTYNO"/>
    </input>
    <layout xCoordinate="175" yCoordinate="1863" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_6/Join_1" rightInput="#/0/Join_6/Projection_7" joinType="leftOuter">
      <leftElementName>DOCID</leftElementName>
      <rightElementName>DOCID</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_8">
    <endUserTexts label=" "/>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <input>
      <entity>#/0/REPORTING.PREPARE::CV_BUT000</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
    </input>
    <layout xCoordinate="329" yCoordinate="1863" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_7" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="GUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_6</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_8</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
    </input>
    <layout xCoordinate="250" yCoordinate="1767" width="0" height="0" expanded="true"/>
    <join leftInput="#/0/Join_7/Join_6" rightInput="#/0/Join_7/Projection_8" joinType="leftOuter">
      <leftElementName>PARTYNO</leftElementName>
      <rightElementName>PARTNER</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_3" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="GUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_7</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_3</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
    </input>
    <layout xCoordinate="250" yCoordinate="1671" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_3/Join_7" rightInput="#/0/Join_3/Projection_3" joinType="inner" dynamic="false">
      <leftElementName>GUID_HU</leftElementName>
      <rightElementName>SGUID_HU</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_4">
    <endUserTexts label=" "/>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <input>
      <entity>#/0/REPORTING.PREPARE::CV_NQUAN</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
    </input>
    <layout xCoordinate="239" yCoordinate="1479" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_9">
    <endUserTexts label=" "/>
    <element name="TRART">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;TRART&quot; = '1'</formula>
    </filterExpression>
    <input>
      <entity>#/0/"SAPHANADB"./SCWM/ORDIM_O</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="TRART" sourceName="TRART"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
    </input>
    <layout xCoordinate="404" yCoordinate="1767" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="Aggregation_1">
    <endUserTexts label=" "/>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="SGUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_9</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SGUID_HU" sourceName="SGUID_HU"/>
    </input>
    <layout xCoordinate="404" yCoordinate="1671" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_8" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="GUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_3</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
    </input>
    <input>
      <viewNode xsi:type="View:Aggregation">#/0/Aggregation_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
    </input>
    <layout xCoordinate="322" yCoordinate="1575" width="0" height="0" expanded="true"/>
    <join leftInput="#/0/Join_8/Join_3" rightInput="#/0/Join_8/Aggregation_1" joinType="leftOuter">
      <leftElementName>GUID_HU</leftElementName>
      <rightElementName>SGUID_HU</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_10">
    <endUserTexts label=" "/>
    <element name="GUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <input>
      <entity>#/0/REPORTING.PREPARE::CV_HUHDR</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
    </input>
    <layout xCoordinate="476" yCoordinate="1575" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_9" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_8</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_10</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
    </input>
    <layout xCoordinate="393" yCoordinate="1479" width="0" height="0" expanded="true"/>
    <join leftInput="#/0/Join_9/Join_8" rightInput="#/0/Join_9/Projection_10" joinType="leftOuter" dynamic="false">
      <leftElementName>GUID_HU</leftElementName>
      <rightElementName>GUID_HU</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_4" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="GUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_9</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_4</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
    </input>
    <layout xCoordinate="309" yCoordinate="1383" width="0" height="0" expanded="true"/>
    <join leftInput="#/0/Join_4/Join_9" rightInput="#/0/Join_4/Projection_4" joinType="inner">
      <leftElementName>GUID_HU</leftElementName>
      <rightElementName>GUID_PARENT</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_2">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="TZONE">
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <input>
      <entity>#/0/REPORTING.PREPARE::CV_SCMB_TOENTITY</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TZONE" sourceName="TZONE"/>
    </input>
    <layout xCoordinate="167" yCoordinate="551" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_12">
    <endUserTexts label=" "/>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="GUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_4</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
    </input>
    <layout xCoordinate="309" yCoordinate="1305" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_6">
    <endUserTexts label=" "/>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="TYPE">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="GUID">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>(&quot;MANDT&quot;='$$IP_MANDT$$') and (&quot;TYPE&quot;='H')</formula>
    </filterExpression>
    <input>
      <entity>#/0/"SAPHANADB"./LIME/NTREE</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE" sourceName="TYPE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID" sourceName="GUID"/>
    </input>
    <layout xCoordinate="155" yCoordinate="1305" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_10" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="GUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_12</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_6</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
    </input>
    <layout xCoordinate="309" yCoordinate="1209" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_10/Projection_12" rightInput="#/0/Join_10/Projection_6" joinType="inner">
      <leftElementName>GUID_HU</leftElementName>
      <rightElementName>GUID</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="TP_H">
    <endUserTexts label=" "/>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="GUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;TYPE_PARENT&quot;='H'</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_10</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
    </input>
    <layout xCoordinate="243" yCoordinate="1131" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_11" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="GUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/TP_H</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_6</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
    </input>
    <layout xCoordinate="176" yCoordinate="1035" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_11/TP_H" rightInput="#/0/Join_11/Projection_6" joinType="inner">
      <leftElementName>GUID_PARENT</leftElementName>
      <rightElementName>GUID</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_14">
    <endUserTexts label=" "/>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="GUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>&quot;TYPE_PARENT&quot;!='H'</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_10</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
    </input>
    <layout xCoordinate="330" yCoordinate="1035" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Union" name="Union_2">
    <endUserTexts label=" "/>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="GUID_HU">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:JoinNode">#/0/Join_11</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
    </input>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:Projection">#/0/Projection_14</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_HU" sourceName="GUID_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
    </input>
    <layout xCoordinate="248" yCoordinate="919" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="Aggregation_3">
    <endUserTexts label=" "/>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Union">#/0/Union_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
    </input>
    <layout xCoordinate="248" yCoordinate="841" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_16">
    <endUserTexts label=" "/>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>(&quot;TYPE_PARENT&quot;!='L')</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:Aggregation">#/0/Aggregation_3</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
    </input>
    <layout xCoordinate="248" yCoordinate="667" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_13">
    <endUserTexts label=" "/>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>(&quot;TYPE_PARENT&quot;='L')</formula>
    </filterExpression>
    <input>
      <viewNode xsi:type="View:Aggregation">#/0/Aggregation_3</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
    </input>
    <layout xCoordinate="336" yCoordinate="763" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_15">
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
    <element name="LGTYP">
      <endUserTexts label="LGTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGBER">
      <endUserTexts label="LGBER"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="GUID_LOC">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>(&quot;MANDT&quot;='$$IP_MANDT$$')</formula>
    </filterExpression>
    <input>
      <entity>#/0/"SAPHANADB"./SCWM/LAGP</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGTYP" sourceName="LGTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGBER" sourceName="LGBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_LOC" sourceName="GUID_LOC"/>
    </input>
    <layout xCoordinate="490" yCoordinate="763" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_12" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="TYPE_PARENT">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="GUID_PARENT">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="LGPLA">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="LGTYP">
      <endUserTexts label="LGTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGBER">
      <endUserTexts label="LGBER"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_13</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="TYPE_PARENT" sourceName="TYPE_PARENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_PARENT" sourceName="GUID_PARENT"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_15</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGTYP" sourceName="LGTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGBER" sourceName="LGBER"/>
    </input>
    <layout xCoordinate="402" yCoordinate="667" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_12/Projection_13" rightInput="#/0/Join_12/Projection_15" joinType="leftOuter">
      <leftElementName>GUID_PARENT</leftElementName>
      <leftElementName>LGNUM</leftElementName>
      <rightElementName>GUID_LOC</rightElementName>
      <rightElementName>LGNUM</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Union" name="Union_3">
    <endUserTexts label=" "/>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGPLA" transparentFilter="false">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="LGTYP" transparentFilter="false">
      <endUserTexts label="LGTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGBER" transparentFilter="false">
      <endUserTexts label="LGBER"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:Projection">#/0/Projection_16</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ConstantElementMapping" targetName="LGPLA" value="" null="true"/>
      <mapping xsi:type="Type:ConstantElementMapping" targetName="LGTYP" value="" null="true"/>
      <mapping xsi:type="Type:ConstantElementMapping" targetName="LGBER" value="" null="true"/>
    </input>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:JoinNode">#/0/Join_12</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGTYP" sourceName="LGTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGBER" sourceName="LGBER"/>
    </input>
    <layout xCoordinate="321" yCoordinate="551" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_2" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="TZONE">
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="CLOSED_TST">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGPLA" transparentFilter="false">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="LGTYP" transparentFilter="false">
      <endUserTexts label="LGTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGBER" transparentFilter="false">
      <endUserTexts label="LGBER"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED" aggregationBehavior="NONE">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>utctolocal(&quot;CLOSED_TST&quot;,&quot;TZONE&quot;)</formula>
      </calculationDefinition>
    </element>
    <input>
      <viewNode xsi:type="View:Union">#/0/Union_3</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_TST" sourceName="CLOSED_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGTYP" sourceName="LGTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGBER" sourceName="LGBER"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="TZONE" sourceName="TZONE"/>
    </input>
    <layout xCoordinate="241" yCoordinate="455" width="0" height="0" expanded="true"/>
    <join leftInput="#/0/Join_2/Union_3" rightInput="#/0/Join_2/Projection_2" joinType="leftOuter" dynamic="false">
      <leftElementName>LGNUM</leftElementName>
      <rightElementName>LGNUM</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_5">
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
    <element name="PREV_SHIFT_END">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="PREV_SHIFT_START">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="NOW_SHIFT_END">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <input>
      <entity>#/0/REPORTING.PREPARE::CV_ZTLM_WH_CUST</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NOW_SHIFT_TST" sourceName="NOW_SHIFT_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NOW_SHIFT_START" sourceName="NOW_SHIFT_START"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PREV_SHIFT_END" sourceName="PREV_SHIFT_END"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PREV_SHIFT_START" sourceName="PREV_SHIFT_START"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NOW_SHIFT_END" sourceName="NOW_SHIFT_END"/>
    </input>
    <layout xCoordinate="395" yCoordinate="455" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:JoinNode" name="Join_5" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="NOW_SHIFT_TST">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="NOW_SHIFT_START">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="PREV_SHIFT_END">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="PREV_SHIFT_START">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="NOW_SHIFT_END">
      <inlineType primitiveType="TIMESTAMP" length="27" precision="27" scale="7"/>
    </element>
    <element name="PARTNER1">
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="HUIDENT1">
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="DOCNO1">
      <inlineType primitiveType="NVARCHAR" length="35" precision="35" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="LGPLA" transparentFilter="false">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="LGTYP" transparentFilter="false">
      <endUserTexts label="LGTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGBER" transparentFilter="false">
      <endUserTexts label="LGBER"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="SHIFT" aggregationBehavior="NONE">
      <endUserTexts label="SHIFT"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="1"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>if( &#xD;
&quot;CLOSED&quot; >= &quot;NOW_SHIFT_START&quot; and &quot;CLOSED&quot; &lt;= &quot;NOW_SHIFT_TST&quot;,&#xD;
'N',&#xD;
   if(&#xD;
   &quot;CLOSED&quot; >= &quot;PREV_SHIFT_START&quot; and &quot;CLOSED&quot; &lt;=&quot;PREV_SHIFT_END&quot;,&#xD;
   'P',&#xD;
   ''&#xD;
   )&#xD;
)</formula>
      </calculationDefinition>
    </element>
    <element name="DOCNO" aggregationBehavior="NONE">
      <endUserTexts label="DOCNO"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="35"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>ltrim(&quot;DOCNO1&quot;,'0')</formula>
      </calculationDefinition>
    </element>
    <element name="PARTNER" aggregationBehavior="NONE">
      <endUserTexts label="PARTNER"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="10"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>ltrim(&quot;PARTNER1&quot;,'0')</formula>
      </calculationDefinition>
    </element>
    <element name="HUIDENT" aggregationBehavior="NONE">
      <endUserTexts label="HUIDENT"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="20"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>ltrim(&quot;HUIDENT1&quot;,'0')</formula>
      </calculationDefinition>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED" sourceName="CLOSED"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER1" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT1" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO1" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGTYP" sourceName="LGTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGBER" sourceName="LGBER"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_5</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="NOW_SHIFT_TST" sourceName="NOW_SHIFT_TST"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NOW_SHIFT_START" sourceName="NOW_SHIFT_START"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PREV_SHIFT_END" sourceName="PREV_SHIFT_END"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PREV_SHIFT_START" sourceName="PREV_SHIFT_START"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NOW_SHIFT_END" sourceName="NOW_SHIFT_END"/>
    </input>
    <layout xCoordinate="316" yCoordinate="359" width="0" height="0" expanded="true"/>
    <join leftInput="#/0/Join_5/Join_2" rightInput="#/0/Join_5/Projection_5" joinType="leftOuter">
      <leftElementName>LGNUM</leftElementName>
      <rightElementName>LGNUM</rightElementName>
    </join>
  </viewNode>
  <viewNode xsi:type="View:Projection" name="Projection_11">
    <endUserTexts label=" "/>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="QUAN_3">
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="LGPLA" transparentFilter="false">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="LGBER" transparentFilter="false">
      <endUserTexts label="LGBER"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="20" scale="0"/>
    </element>
    <element name="LGTYP" transparentFilter="false">
      <endUserTexts label="LGTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="NLTYP" transparentFilter="false">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <input>
      <entity>#/0/REPORTING.IN_OUT::CV_IN_OUT_REP_03_STOCK_DETAIL</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN_3" sourceName="QUAN_3"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGBER" sourceName="LGBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGTYP" sourceName="LGTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
    </input>
    <layout xCoordinate="470" yCoordinate="281" width="231" height="64" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="Aggregation_2">
    <endUserTexts label=" "/>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType name="INTEGER" primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="SHIFT">
      <endUserTexts label="SHIFT"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="1" precision="0" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="35" precision="0" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="10" precision="0" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="20" precision="0" scale="0"/>
    </element>
    <element name="LGPLA" transparentFilter="false">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="LGTYP" transparentFilter="false">
      <endUserTexts label="LGTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGBER" transparentFilter="false">
      <endUserTexts label="LGBER"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_5</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SHIFT" sourceName="SHIFT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGTYP" sourceName="LGTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGBER" sourceName="LGBER"/>
    </input>
    <layout xCoordinate="316" yCoordinate="281" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Union" name="Union_1">
    <endUserTexts label=" "/>
    <element name="LGNUM" transparentFilter="false">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="CLOSED_DIFF">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType primitiveType="INTEGER" length="0" precision="0" scale="0"/>
    </element>
    <element name="SHIFT">
      <endUserTexts label="SHIFT"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="1" precision="0" scale="0"/>
    </element>
    <element name="NAME_ORG">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0"/>
    </element>
    <element name="NLTYP">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DOCNO">
      <endUserTexts label="DOCNO"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="35" precision="0" scale="0"/>
    </element>
    <element name="PARTNER">
      <endUserTexts label="PARTNER"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="10" precision="0" scale="0"/>
    </element>
    <element name="HUIDENT">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="0" scale="0"/>
    </element>
    <element name="QUAN">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_POS">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="COUNT_HU">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="LGPLA" transparentFilter="false">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="LGBER" transparentFilter="false">
      <endUserTexts label="LGBER"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGTYP" transparentFilter="false">
      <endUserTexts label="LGTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:Aggregation">#/0/Aggregation_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SHIFT" sourceName="SHIFT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGBER" sourceName="LGBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGTYP" sourceName="LGTYP"/>
    </input>
    <input emptyUnionBehavior="NO_ROW">
      <viewNode xsi:type="View:Projection">#/0/Projection_11</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ConstantElementMapping" targetName="SHIFT" value="" null="true"/>
      <mapping xsi:type="Type:ConstantElementMapping" targetName="NAME_ORG" value="" null="true"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ConstantElementMapping" targetName="DOCNO" value="" null="true"/>
      <mapping xsi:type="Type:ConstantElementMapping" targetName="PARTNER" value="" null="true"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ConstantElementMapping" targetName="COUNT_POS" value="" null="true"/>
      <mapping xsi:type="Type:ConstantElementMapping" targetName="COUNT_HU" value="" null="true"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGBER" sourceName="LGBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGTYP" sourceName="LGTYP"/>
    </input>
    <layout xCoordinate="415" yCoordinate="165" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="Aggregation">
    <element name="QUAN_3" hidden="false" aggregationBehavior="SUM" engineAggregation="SUM" restricted="true">
      <endUserTexts label="QUAN_3"/>
      <inlineType primitiveType="INTEGER"/>
      <calculationDefinition>
        <formula>QUAN</formula>
      </calculationDefinition>
      <restriction element="#/0/Aggregation/CLOSED_DIFF">
        <valueFilter xsi:type="Column:SingleValueFilter" operator="GE" including="true" value="3"/>
      </restriction>
    </element>
    <element name="COUNT_POS_3" hidden="false" aggregationBehavior="SUM" engineAggregation="SUM" restricted="true">
      <endUserTexts label="COUNT_POS_3"/>
      <inlineType primitiveType="INTEGER"/>
      <calculationDefinition>
        <formula>COUNT_POS</formula>
      </calculationDefinition>
      <restriction element="#/0/Aggregation/CLOSED_DIFF">
        <valueFilter xsi:type="Column:SingleValueFilter" operator="GE" including="true" value="3"/>
      </restriction>
    </element>
    <element name="LGNUM" transparentFilter="false" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0" semanticType="empty"/>
    </element>
    <element name="CLOSED_DIFF" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="CLOSED_DIFF"/>
      <inlineType primitiveType="INTEGER" length="0" precision="0" scale="0" semanticType="empty"/>
    </element>
    <element name="SHIFT" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="SHIFT"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="1" precision="0" scale="0"/>
    </element>
    <element name="NAME_ORG" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="NAME_ORG"/>
      <inlineType primitiveType="NVARCHAR" length="160" precision="160" scale="0" semanticType="empty"/>
    </element>
    <element name="NLTYP" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="NLTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0" semanticType="empty"/>
    </element>
    <element name="DOCNO" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="DOCNO"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="35" precision="0" scale="0"/>
    </element>
    <element name="PARTNER" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="PARTNER"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="10" precision="0" scale="0"/>
    </element>
    <element name="HUIDENT" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="HUIDENT"/>
      <inlineType primitiveType="NVARCHAR" length="20" precision="0" scale="0"/>
    </element>
    <element name="QUAN" aggregationBehavior="SUM" engineAggregation="SUM">
      <endUserTexts label="QUAN"/>
      <inlineType primitiveType="DECIMAL" length="31" precision="31" scale="14"/>
    </element>
    <element name="COUNT_POS" aggregationBehavior="SUM" engineAggregation="SUM">
      <endUserTexts label="COUNT_POS"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="COUNT_HU" aggregationBehavior="SUM" engineAggregation="SUM">
      <endUserTexts label="COUNT_HU"/>
      <inlineType primitiveType="INTEGER" length="10" precision="10" scale="0"/>
    </element>
    <element name="LGPLA" transparentFilter="false" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="LGPLA"/>
      <inlineType primitiveType="NVARCHAR" length="18" precision="18" scale="0"/>
    </element>
    <element name="LGBER" transparentFilter="false" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="LGBER"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="LGTYP" transparentFilter="false" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="LGTYP"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="HUIDENT_ZERO" hidden="false" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="HUIDENT_ZERO"/>
      <inlineType name="NVARCHAR" primitiveType="NVARCHAR" length="20" semanticType="empty"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>ltrim(&quot;HUIDENT&quot;, '0')</formula>
      </calculationDefinition>
    </element>
    <input>
      <viewNode xsi:type="View:Union">#/0/Union_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CLOSED_DIFF" sourceName="CLOSED_DIFF"/>
      <mapping xsi:type="Type:ElementMapping" targetName="SHIFT" sourceName="SHIFT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NAME_ORG" sourceName="NAME_ORG"/>
      <mapping xsi:type="Type:ElementMapping" targetName="NLTYP" sourceName="NLTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DOCNO" sourceName="DOCNO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="PARTNER" sourceName="PARTNER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="HUIDENT" sourceName="HUIDENT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGPLA" sourceName="LGPLA"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGBER" sourceName="LGBER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGTYP" sourceName="LGTYP"/>
      <mapping xsi:type="Type:ElementMapping" targetName="QUAN" sourceName="QUAN"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_POS" sourceName="COUNT_POS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="COUNT_HU" sourceName="COUNT_HU"/>
    </input>
    <layout xCoordinate="415" yCoordinate="87" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewLayout relativeWidthScenario="58"/>
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
