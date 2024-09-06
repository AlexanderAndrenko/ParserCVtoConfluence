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
<View:ColumnView xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:Param="http://www.sap.com/ndb/ViewModelParameter.ecore" xmlns:Type="http://www.sap.com/ndb/DataModelType.ecore" xmlns:View="http://www.sap.com/ndb/ViewModelView.ecore" schemaVersion="2.3" name="CV_INVENT_09" dataCategory="CUBE" hierarchiesSQLEnabled="false" defaultNode="#/0/Aggregation" clientDependent="false" applyPrivilegeType="ANALYTIC_PRIVILEGE" translationRelevant="true">
  <endUserTexts label="CV_INVENT_TIME"/>
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
  <viewNode xsi:type="View:Projection" name="Projection_1">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="WHO">
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="STARTED_AT">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="CONFIRMED_AT">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="STATUS">
      <inlineType primitiveType="NVARCHAR" length="1" precision="1" scale="0"/>
    </element>
    <element name="WCR">
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="MANDT">
      <inlineType primitiveType="NVARCHAR" length="3" precision="3" scale="0"/>
    </element>
    <element name="STARTED" aggregationBehavior="NONE">
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="15"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;STARTED_AT&quot;</formula>
      </calculationDefinition>
    </element>
    <element name="CONFIRMED" aggregationBehavior="NONE">
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="15"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;CONFIRMED_AT&quot;</formula>
      </calculationDefinition>
    </element>
    <element name="DATE_UTC" aggregationBehavior="NONE">
      <endUserTexts label="DATE_UTC"/>
      <inlineType name="DATE" primitiveType="DATE"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;TIMESTAMP&quot;</formula>
      </calculationDefinition>
    </element>
    <element name="TIMESTAMP" aggregationBehavior="NONE">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;STARTED_AT&quot;</formula>
      </calculationDefinition>
    </element>
    <filterExpression language="COLUMN_ENGINE">
      <formula>(&quot;STARTED_AT&quot;>0) &#xD;
AND (&quot;CONFIRMED_AT&quot;>0)&#xD;
AND(&quot;STATUS&quot;='C')&#xD;
AND(&quot;WCR&quot;='INVE')&#xD;
and (&quot;MANDT&quot;='$$IP_MANDT$$')</formula>
    </filterExpression>
    <input>
      <entity>#/0/"SAPHANADB"./SCWM/WHO</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="WHO" sourceName="WHO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STARTED_AT" sourceName="STARTED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STATUS" sourceName="STATUS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="WCR" sourceName="WCR"/>
      <mapping xsi:type="Type:ElementMapping" targetName="MANDT" sourceName="MANDT"/>
    </input>
    <layout xCoordinate="330" yCoordinate="531" width="-1" height="-1" expanded="true"/>
  </viewNode>
  
  <viewNode xsi:type="View:Projection" name="Projection_2">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="VARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="ORDER">
      <inlineType primitiveType="VARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="GUID_DOC">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <input>
      <entity>#/0/REPORTING.INVENT::CV_INVENT_09_ORDERS</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ORDER" sourceName="ORDER"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
    </input>
    <layout xCoordinate="22" yCoordinate="531" width="-1" height="-1" expanded="true"/>
  </viewNode>
    <viewNode xsi:type="View:Projection" name="Projection_3">
    <endUserTexts label=" "/>
    <element name="GUID_DOC">
      <inlineType primitiveType="VARBINARY" length="16" precision="16" scale="0"/>
    </element>
    <element name="ITEM_NO">
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <input>
      <entity>#/0/REPORTING.INVENT::CV_INVENT_COUNT_DOC</entity>
      <mapping xsi:type="Type:ElementMapping" targetName="GUID_DOC" sourceName="GUID_DOC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ITEM_NO" sourceName="ITEM_NO"/>
    </input>
    <layout xCoordinate="176" yCoordinate="531" width="-1" height="-1" expanded="true"/>
  </viewNode>
  
  <viewNode xsi:type="View:JoinNode" name="Join_2" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="VARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="ORDER">
      <inlineType primitiveType="VARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ORDER" sourceName="ORDER"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_3</viewNode>
    </input>
    <layout xCoordinate="176" yCoordinate="435" width="0" height="0" expanded="true"/>
    <join leftInput="#/0/Join_2/Projection_2" rightInput="#/0/Join_2/Projection_3" joinType="inner">
      <leftElementName>GUID_DOC</leftElementName>
      <leftElementName>ITEM_NO</leftElementName>
      <rightElementName>GUID_DOC</rightElementName>
      <rightElementName>ITEM_NO</rightElementName>
    </join>
  </viewNode>
  
  <viewNode xsi:type="View:Aggregation" name="Aggregation_2">
    <endUserTexts label=" "/>
    <element name="DATE_UTC">
      <endUserTexts label="DATE_UTC"/>
      <inlineType name="DATE" primitiveType="DATE" length="0" precision="0" scale="0"/>
    </element>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="NVARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="WHO">
      <inlineType primitiveType="NVARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="STARTED_AT">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="CONFIRMED_AT">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="DATE_UTC" sourceName="DATE_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="WHO" sourceName="WHO"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STARTED_AT" sourceName="STARTED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
    </input>
    <layout xCoordinate="330" yCoordinate="435" width="0" height="0" expanded="true"/>
  </viewNode>
  
  
  <viewNode xsi:type="View:JoinNode" name="Join_1" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="VARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="ORDER">
      <inlineType primitiveType="VARCHAR" length="10" precision="10" scale="0"/>
    </element>
    <element name="DATE_UTC">
      <endUserTexts label="DATE_UTC"/>
      <inlineType name="DATE" primitiveType="DATE" length="0" precision="0" scale="0"/>
    </element>
    <element name="STARTED_AT">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="CONFIRMED_AT">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="STARTED_TS" aggregationBehavior="NONE">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;STARTED_AT&quot;</formula>
      </calculationDefinition>
    </element>
    <element name="CONFIRMED_TS" aggregationBehavior="NONE">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;CONFIRMED_AT&quot;</formula>
      </calculationDefinition>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="ORDER" sourceName="ORDER"/>
    </input>
    <input>
      <viewNode xsi:type="View:Aggregation">#/0/Aggregation_2</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="DATE_UTC" sourceName="DATE_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STARTED_AT" sourceName="STARTED_AT"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_AT" sourceName="CONFIRMED_AT"/>
    </input>
    <layout xCoordinate="252" yCoordinate="339" width="-1" height="-1" expanded="true"/>
    <join leftInput="#/0/Join_1/Join_2" rightInput="#/0/Join_1/Aggregation_2" joinType="inner">
      <leftElementName>LGNUM</leftElementName>
      <leftElementName>ORDER</leftElementName>
      <rightElementName>LGNUM</rightElementName>
      <rightElementName>WHO</rightElementName>
    </join>
  </viewNode>
  
  
  <viewNode xsi:type="View:Projection" name="Projection_4">
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
    <layout xCoordinate="98" yCoordinate="339" width="-1" height="-1" expanded="true"/>
  </viewNode>
  
  
  
  <viewNode xsi:type="View:JoinNode" name="Join_3" joinOrder="OUTSIDE_IN">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="VARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DATE_UTC">
      <endUserTexts label="DATE_UTC"/>
      <inlineType name="DATE" primitiveType="DATE" length="0" precision="0" scale="0"/>
    </element>
    <element name="STARTED_TS">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_TS">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="TZONE">
      <inlineType primitiveType="NVARCHAR" length="6" precision="6" scale="0"/>
    </element>
    <element name="STARTED_AT">
      <inlineType primitiveType="DECIMAL" length="15" precision="15" scale="0"/>
    </element>
    <element name="DATE" aggregationBehavior="NONE">
      <endUserTexts label="DATE"/>
      <inlineType name="DATE" primitiveType="DATE"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>utctolocal(&quot;TIMESTAMP&quot;,&quot;TZONE&quot;)</formula>
      </calculationDefinition>
    </element>
    <element name="TIMESTAMP" aggregationBehavior="NONE">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>&quot;STARTED_AT&quot;</formula>
      </calculationDefinition>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DATE_UTC" sourceName="DATE_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STARTED_TS" sourceName="STARTED_TS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_TS" sourceName="CONFIRMED_TS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STARTED_AT" sourceName="STARTED_AT"/>
    </input>
    <input>
      <viewNode xsi:type="View:Projection">#/0/Projection_4</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="TZONE" sourceName="TZONE"/>
    </input>
    <layout xCoordinate="175" yCoordinate="243" width="0" height="0" expanded="true"/>
    <join leftInput="#/0/Join_3/Join_1" rightInput="#/0/Join_3/Projection_4" joinType="leftOuter">
      <leftElementName>LGNUM</leftElementName>
      <rightElementName>LGNUM</rightElementName>
    </join>
  </viewNode>
  
  <viewNode xsi:type="View:Aggregation" name="Aggregation_1">
    <endUserTexts label=" "/>
    <element name="LGNUM">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="VARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DATE_UTC">
      <endUserTexts label="DATE_UTC"/>
      <inlineType name="DATE" primitiveType="DATE" length="0" precision="0" scale="0"/>
    </element>
    <element name="STARTED_TS" aggregationBehavior="MIN">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="CONFIRMED_TS" aggregationBehavior="MAX">
      <inlineType name="TIMESTAMP" primitiveType="TIMESTAMP" length="0" precision="0" scale="0"/>
    </element>
    <element name="DATE">
      <endUserTexts label="DATE"/>
      <inlineType name="DATE" primitiveType="DATE" length="0" precision="0" scale="0"/>
    </element>
    <element name="BETWEEN" aggregationBehavior="NONE">
      <inlineType name="INTEGER" primitiveType="INTEGER"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>secondsbetween(&quot;STARTED_TS&quot;,&quot;CONFIRMED_TS&quot;)</formula>
      </calculationDefinition>
    </element>
    <element name="DIFF_HOURS" aggregationBehavior="NONE">
      <endUserTexts label="DIFF_HOURS"/>
      <inlineType name="DECIMAL" primitiveType="DECIMAL" length="15" scale="2"/>
      <calculationDefinition language="COLUMN_ENGINE">
        <formula>(&quot;BETWEEN&quot;/3600)</formula>
      </calculationDefinition>
    </element>
    <input>
      <viewNode xsi:type="View:JoinNode">#/0/Join_3</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DATE_UTC" sourceName="DATE_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="STARTED_TS" sourceName="STARTED_TS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="CONFIRMED_TS" sourceName="CONFIRMED_TS"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DATE" sourceName="DATE"/>
    </input>
    <layout xCoordinate="175" yCoordinate="165" width="-1" height="-1" expanded="true"/>
  </viewNode>
  <viewNode xsi:type="View:Aggregation" name="Aggregation">
    <element name="LGNUM" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="LGNUM"/>
      <inlineType primitiveType="VARCHAR" length="4" precision="4" scale="0"/>
    </element>
    <element name="DATE_UTC" hidden="true" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="DATE_UTC"/>
      <inlineType name="DATE" primitiveType="DATE" length="0" precision="0" scale="0"/>
    </element>
    <element name="DIFF_HOURS" aggregationBehavior="SUM" engineAggregation="SUM">
      <endUserTexts label="DIFF_HOURS"/>
      <inlineType primitiveType="DECIMAL" length="15" precision="0" scale="2"/>
    </element>
    <element name="DATE" aggregationBehavior="NONE" drillDownEnablement="DRILL_DOWN">
      <endUserTexts label="DATE"/>
      <inlineType name="DATE" primitiveType="DATE" length="0" precision="0" scale="0"/>
    </element>
    <input>
      <viewNode xsi:type="View:Aggregation">#/0/Aggregation_1</viewNode>
      <mapping xsi:type="Type:ElementMapping" targetName="LGNUM" sourceName="LGNUM"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DATE_UTC" sourceName="DATE_UTC"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DATE" sourceName="DATE"/>
      <mapping xsi:type="Type:ElementMapping" targetName="DIFF_HOURS" sourceName="DIFF_HOURS"/>
    </input>
    <layout xCoordinate="175" yCoordinate="87" width="0" height="0" expanded="true"/>
  </viewNode>
  <viewLayout relativeWidthScenario="43"/>
</View:ColumnView>'''

editorInput = Text(wrap="word")
editorInput.pack(fill="both")
InsertTextToOutput(editorInput, cv)

btnConvertion = ttk.Button(text="Конвертировать", command=ClickbtnConvertion)
btnConvertion.pack()

editorOutput = Text(wrap="word")
editorOutput.pack(fill="both")


root.mainloop()
