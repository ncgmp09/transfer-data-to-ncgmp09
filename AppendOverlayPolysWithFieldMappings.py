import arcpy, shutil
from arcpy import env

# List all file geodatabases in the current workspace 
# 
workspaces = arcpy.ListWorkspaces("*", "")
for workspace in workspaces:
    name = arcpy.Describe(workspace).name
    namepart = name.split(".")
    newname = namepart[0]
    # Set local variables 
    #
    featureclassin = "OverlayPolys"
    featureclassout = "OtherPolys"
    inFC = "C:\\Documents\\azgs\\mixed\\" + name + "\\GeologicMap\\" + featureclassin
    outFC = "C:\\Documents\\ncgmp\\mixed\\"+newname+".gdb\\GeologicMap\\" + featureclassout
    schemaType = "NO_TEST"
    subtype = ""

    # Set input field variables
    #
    infield1 = "OverlayPolys_ID"
    infield2 = "MapUnit"
    infield3 = "Label"
    infield4 = "DataSourceID"
    infield5 = "Notes"

    # Set output field variables
    #
    outfield1 = "OtherPolys_ID"
    outfield2 = "Type"
    outfield3 = "Label"
    outfield4 = "DataSourceID"
    outfield5 = "Notes"
   
    print "Adding " + featureclassin + " field map to. . ." + workspace
    # Create a fieldmappings object and two fieldmap objects
    #
    input1 = arcpy.FieldMap()
    input2 = arcpy.FieldMap()
    input3 = arcpy.FieldMap()
    input4 = arcpy.FieldMap()
    input5 = arcpy.FieldMap()

    fieldmappings = arcpy.FieldMappings()

    # Add input fields
    #   to fieldmap object.
    #
    input1.addInputField(inFC,infield1)
    input2.addInputField(inFC,infield2)
    input3.addInputField(inFC,infield3)
    input4.addInputField(inFC,infield4)    
    input5.addInputField(inFC,infield5)

    # Set the Name of the Field output from this field map.
    #
    output1 = input1.outputField
    output1.name = (outfield1)
    input1.outputField = output1
    # Set the Name of the Field output from this field map.
    #
    output2 = input2.outputField
    output2.name = (outfield2)
    input2.outputField = output2
    # Set the Name of the Field output from this field map.
    #
    output3 = input3.outputField
    output3.name = (outfield3)
    input3.outputField = output3
    # Set the Name of the Field output from this field map.
    #
    output4 = input4.outputField
    output4.name = (outfield4)
    input4.outputField = output4
    # Set the Name of the Field output from this field map.
    #
    output5 = input5.outputField
    output5.name = (outfield5)
    input5.outputField = output5
    
    # Add the custom fieldmaps into the fieldmappings object.
    #
    fieldmappings.addFieldMap(input1)
    fieldmappings.addFieldMap(input2)
    fieldmappings.addFieldMap(input3)
    fieldmappings.addFieldMap(input4)
    fieldmappings.addFieldMap(input5)

    try:
        print "Appending data. . ."
        # Process: Append the feature classes into the empty feature class
        arcpy.Append_management(inFC, outFC, schemaType, fieldmappings, subtype)

    except:
        # If an error occurred while running a tool print the messages
        print arcpy.GetMessages()

    print "Append data to " + featureclassout + " " + newname + " complete. . ."

