import rpw
from rpw import revit, db, ui, DB, UI

import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

doc = revit.doc
uidoc = revit.uidoc


getselection = uidoc.Selection.GetElementIds()

t = Transaction(doc, "Rotation axe x")
t.Start()
point2 = XYZ(0,0,1)
for e in getselection():
	o = doc.GetElement(e).Location.Point
	z = XYZ(o.X, o.Y + 1, o.Z)
	axis = Line.CreateBound(o, z)
	ElementTransformUtils.RotateElement(doc,e,axis,pi/2)
