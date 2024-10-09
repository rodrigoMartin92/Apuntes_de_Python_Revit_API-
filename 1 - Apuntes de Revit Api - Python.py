        # -------------------------------------------- INDICE --------------------------------------------

    # 1 - Importaciones y selecciones de documento

    # 2 - Nodos de Dynamo iniciales

    # 3 - Metodos de Dynamo en Python Script

    # 4 - Metodos de seleccion

    # 5 - Parametros de elementos

    # 6 - Categorias

    # 7 - Colectores

    # 8 - Filtros

    # 9 - Colectores + Filtros

    # 10 - Formulario Windows Forms

    # 10.1 - Etiquetas

    # 10.2 - Botones

    # 10.3 - Textbox

    # 10.4 - Checkbox

    # 10.5 - Combobox

    # 11 - Clase de creacion de formularios

    # 12 - Transacciones

    # 13 - Instalacion y utilizacion de RevitPythonShell

    # 14 - Utilizacion de pyRevit

    # IMPORTACIONES
        # Plantilla de importaciones

        # Para Python Script - Dynamo

import sys
import clr 
import System

from System import Array
from System.Collections.Generic import *
from System.Collections.Generic import List
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *       # No esta en ultimo codigo de importaciones

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

clr.AddReference('System')
from System.Collections.Generic import *

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.Exceptions import *        

    # No funcionan en Windows Forms de pyRevit

doc =   DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app =   uiapp.Application 
uidoc = uiapp.ActiveUIDocument 

    # Para Revit PYthon Shell

import clr                                      # Si esta en importaciones de Dynamo
clr.AddReference('RevitAPIUI')
import Autodesk                                 # Si esta en importaciones de Dynamo
from Autodesk.Revit.UI import *                 # Si esta en importaciones de Dynamo
from Autodesk.Revit.UI.Selection import *
from Autodesk.Revit.DB import *                 # Si esta en importaciones de Dynamo
from Autodesk.Revit.Exceptions import *        
from Autodesk.Revit.Attributes import *  

clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Windows.Forms import *
from System.Drawing import *

    # Funcionan en Windows Forms de pyRevit

uidoc = __revit__.ActiveUIDocument
doc =   __revit__.ActiveUIDocument.Document

    # Con alias

from Autodesk.Revit.DB import FilteredElementCollector as Fec
from Autodesk.Revit.DB import BuiltInCategory as Bic

    ########################################################

	    #SELECCIONES DE DOCUMENTO

    # Seleccion del documento actual en -RevitPythonShell-

uidoc = __revit__.ActiveUIDocument                                  
doc =   __revit__.ActiveUIDocument.Document                         

    # Seleccion del documento actual en Dynamo - Python Script
    
doc =   DocumentManager.Instance.CurrentDBDocument                  
uiapp = DocumentManager.Instance.CurrentUIApplication               
    # doc = Documento actual - Si realizo las importaciones que en Dynamo, puedo importar esto mismo en RPS

app =   uiapp.Application                                           
uidoc = uiapp.ActiveUIDocument                                      

    # Explicaciones de CHAT GPT de las importaciones

import sys
    # 1. `import sys`: Importa el modulo `sys`, que proporciona funciones y variables que interactuan con el interprete de Python y su entorno. Es una importante libreria de Python - que usamos para cargar las librerias estandar de IronPython.
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib') #Importa las Librerias estandar de IronPython cubriendo desde servidores y encriptacion hasta expresiones regulares.
import clr 
    # 2. `import clr`: Importa el modulo `clr`, que se utiliza para interactuar con Common Language Runtime (CLR), que es el entorno de ejecucion de .NET Framework capaz de ejecutar codigo de distintos lenguajes.
import System
    # 3. `import System`: Importa el modulo `System`, que es parte del espacio de nombres de .NET y proporciona una amplia gama de funcionalidades y tipos basicos.
from System import Array
    # 4. `from System import Array`: Importa la clase `Array` del espacio de nombres `System`, que se usa para trabajar con matrices en .NET.
from System.Collections.Generic import *
    # 5. `from System.Collections.Generic import *`: Importa todas las clases y funciones del espacio de nombres `System.Collections.Generic`, que se utilizan para trabajar con colecciones genericas en .NET.
from System.Collections.Generic import List
    # 6. `from System.Collections.Generic import List`: Importa la clase `List` del espacio de nombres `System.Collections.Generic`, que se utiliza para trabajar con listas genericas en .NET.
clr.AddReference('ProtoGeometry')
    # 7. `clr.AddReference('ProtoGeometry')`: Agrega una referencia al ensamblaje "ProtoGeometry" en .NET. Esto generalmente se usa para acceder a las funcionalidades relacionadas con geometria en Revit.
from Autodesk.DesignScript.Geometry import *
    # 8. `from Autodesk.DesignScript.Geometry import *`: Importa todas las clases y funciones del modulo `Geometry` del espacio de nombres `Autodesk.DesignScript`, que se utiliza para trabajar con geometria en Revit.
clr.AddReference('RevitAPI')
    # 9. `clr.AddReference('RevitAPI')`: Agrega una referencia al ensamblaje "RevitAPI", que proporciona acceso al API de Revit para interactuar con los elementos de un modelo de Revit.
from Autodesk.Revit.DB import *
    # 10. `from Autodesk.Revit.DB import *`: Importa todas las clases y funciones del modulo `DB` del espacio de nombres `Autodesk.Revit`, que proporciona acceso al API de Revit.
from Autodesk.Revit.DB.Structure import *       # No esta en ultimo codigo de importaciones
    # 11. `from Autodesk.Revit.DB.Structure import *`: Importa todas las clases y funciones del modulo `Structure` del espacio de nombres `Autodesk.Revit.DB`, que se utilizan para trabajar con elementos estructurales en Revit.
clr.AddReference('RevitAPIUI')
    # 12. `clr.AddReference('RevitAPIUI')`: Agrega una referencia al ensamblaje "RevitAPIUI", que proporciona acceso al API de interfaz de usuario de Revit.
from Autodesk.Revit.UI import *
    # 13. `from Autodesk.Revit.UI import *`: Importa todas las clases y funciones del modulo `UI` del espacio de nombres `Autodesk.Revit`, que se utilizan para crear interfaces de usuario personalizadas en Revit.
clr.AddReference('System')
    # 14. `clr.AddReference('System')`: Agrega una referencia adicional al ensamblaje "System" en .NET.
from System.Collections.Generic import *
clr.AddReference('RevitNodes')
    # 15. `clr.AddReference('RevitNodes')`: Agrega una referencia al ensamblaje "RevitNodes", que proporciona funcionalidades adicionales para trabajar con Revit dentro del entorno de Dynamo.
import Revit
    # 16. `import Revit`: Importa el modulo `Revit`, que se refiere a las extensiones especificas de Dynamo para trabajar con Revit.
clr.ImportExtensions(Revit.GeometryConversion)
    # 17. `clr.ImportExtensions(Revit.GeometryConversion)`: Importa extensiones especificas para la conversion de geometria entre Dynamo y Revit.
clr.ImportExtensions(Revit.Elements)
    # 18. `clr.ImportExtensions(Revit.Elements)`: Importa extensiones especificas para trabajar con elementos en Revit desde Dynamo.
clr.AddReference('RevitServices')
    # 19. `clr.AddReference('RevitServices')`: Agrega una referencia al ensamblaje "RevitServices", que proporciona funcionalidades para trabajar con la gestion de documentos en Revit.
import RevitServices
    # 20. `import RevitServices`: Importa el modulo `RevitServices`, que se utiliza para interactuar con las funciones de gestion de documentos y transacciones en Revit.
from RevitServices.Persistence import DocumentManager
    # 21. `from RevitServices.Persistence import DocumentManager`: Importa la clase `DocumentManager` del modulo `Persistence` en `RevitServices`, que se utiliza para gestionar documentos de Revit.
from RevitServices.Transactions import TransactionManager
    # 22. `from RevitServices.Transactions import TransactionManager`: Importa la clase `TransactionManager` del modulo `Transactions` en `RevitServices`, que se utiliza para gestionar transacciones en Revit.
clr.AddReference('RevitAPI')
    # 23. `clr.AddReference("RevitAPIUI")`: Agrega otra referencia al ensamblaje "RevitAPIUI" para garantizar que este disponible cuando se trabaje con la interfaz de usuario de Revit.
clr.AddReference('RevitAPIUI')
    # 24. `import Autodesk`: Importa el modulo `Autodesk`, que contiene clases relacionadas con Autodesk y se utiliza para acceder a clases especificas de Revit.

import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
doc =   DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app =   uiapp.Application 
uidoc = uiapp.ActiveUIDocument 

# Finalmente, las ultimas lineas del codigo crean objetos que representan el entorno de trabajo de Revit, como el documento actual (`doc`), la aplicacion Revit (`app`), y el documento de interfaz de usuario activo (`uidoc`). Estos objetos son fundamentales para interactuar con el modelo de Revit y realizar operaciones especificas en el.

        # --------------- Medotos de Dynamo iniciales ---------------

    # Python

for x, y in zip(Colector_de_tipos, Nuevos_nombres):
    x.Name = y

        # --------------------------------------

        ###################### Funciones utiles ######################

def recorrer_lista_anidada(lista):
    for elemento in lista:
        if isinstance(elemento, list):
            # Si el elemento es una lista, llamamos a la funcion recursivamente
            recorrer_lista_anidada(elemento)
        else:
            # Si el elemento no es una lista, puedes realizar alguna operacion
            print(elemento)  # En este caso, simplemente lo imprimimos

    # C#

"""
using System;
using System.Collections;
using System.Collections.Generic;

class Program
{
    static void RecorrerListaAnidada(List<object> lista)
    {
        foreach (var elemento in lista)
        {
            if (elemento is List<object>)
            {
                // Si el elemento es una lista, llamamos a la funcion recursivamente
                RecorrerListaAnidada((List<object>)elemento);
            }
            else
            {
                // Si el elemento no es una lista, puedes realizar alguna operacion
                Console.WriteLine(elemento); // En este caso, simplemente lo imprimimos
            }
        }
    }

    static void Main()
    {
        List<object> miListaAnidada = new List<object> { 1, 2, new List<object> { 3, 4, new List<object> { 5, 6 } }, 7, new List<object> { 8, 9 } };
        RecorrerListaAnidada(miListaAnidada);
    }
}
"""

    # Dynamo - Python Script

dynamo_point = Autodesk.DesignScript.Geometry.Point.ByCoordinates(0,0,0)
Elemento_de_Revit_API = UnwrapElement(IN[0])

element_parameters = UnwrapElement(IN[0]).Parameters
element_parameters_Names = [i.Definition.Name for i in UnwrapElement(IN[0]).Parameters]
family_type = doc.GetElement(UnwrapElement(IN[0]).GetTypeId())

        # --------------------------------------

Poligonos = IN[0]
Tipo_de_pisos = UnwrapElement(IN[1])
Nivel = UnwrapElement(IN[2])

Pisos = []
TransactionManager.Instance.EnsureInTransaction(doc)
try:
    for i in Poligonos:
        contorno = CurveLoop()
        for poligono in i:
            contorno.Append(poligono.ToRevitType())
        Pisos.append(Floor.Create(doc, [contorno], Tipo_de_pisos.Id, Nivel.Id))
except:
    contorno = CurveLoop()
    for poligono in Poligonos:
        contorno.Append(poligono.ToRevitType())
    Pisos.append(Floor.Create(doc, [contorno], Tipo_de_pisos.Id, Nivel.Id))

    TransactionManager.Instance.TransactionTaskDone()

OUT = Pisos

    # Revit API

seleccion_id = uidoc.Selection.GetElementIds()
Lista_seleccion_id = [i for i in uidoc.Selection.GetElementIds()]

Elementos_Seleccionados_PickObjets = [doc.GetElement(x) for x in uidoc.Selection.PickObjects(ObjectType.Element)]

Elementos_Seleccionados_PickObjets = [i.Definition.Name.ToString() for x in uidoc.Selection.PickObjects(ObjectType.Element) for i in doc.GetElement(x).Parameters]

curveloop = CurveLoop()

LookupParameters_PickObjets = [i.LookupParameter(x.Definition.Name) for i in (doc.GetElement(x) for x in uidoc.Selection.PickObjects(ObjectType.Element)) for x in i.Parameters]

Parametros_ValorElectricoes = [x.Definition.BuiltInParameter for i in uidoc.Selection.PickObjects(ObjectType.Element) for x in doc.GetElement(i).Parameters]

Floor.Create() - ViewPlan.Create()

doc.Delete("Id de elemento")

tipoDeMarca = tipo.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_MARK).AsString()

Instancia_del_colector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElementIds()
Instancia_del_colector = FilteredElementCollector(doc).OfClass(FloorType).WhereElementIsNotElementType().ToElementIds()

categorias = List[BuiltInCategory]()

ElementMulticategoryFilter()
collector.WherePasses("filtro").ToElements()
ElementIsElementTypeFilter()

get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_NAME)

class Filtro_de_seleccion_de_categoria_Multiple(ISelectionFilter):
    def __init__(self, *categorias):
        self.categorias = categorias

    def AllowElement(self, element):
        return element.Category.Name in self.categorias

    def AllowReference(self, refer, point):
        return True

Nombres = [doc.GetElement(x).Name for x in uidoc.Selection.PickObjects(ObjectType.Element, Filtro_de_seleccion_de_categoria_Multiple("Walls"))]

# Forma desarmada
elementos_seleccionados = []
FiltroMuros1 = Filtro_de_seleccion_de_categoria_Multiple("Walls")
seleccionFiltroMultiple1 = uidoc.Selection.PickObjects(ObjectType.Element, FiltroMuros1)
for x in seleccionFiltroMultiple1:
    nombre_elemento = doc.GetElement(x).Name
    elementos_seleccionados.append(nombre_elemento)
Nombres = elementos_seleccionados


Ventana_emergente = TaskDialog.Show("Titulo","Instruccion principal")
Ventana_emergente.Show()

    # Windows Forms

Caja_de_mensaje = MessageBox.Show("Mensaje 1", "Mensaje 2")
Caja_de_mensaje.Show()

Formulario = Form()

Formulario.Text = "Titulo"
Formulario.Size = Size(100,100)
Formulario.StarPosition = FormStartPosition.CenterScreen
Formulario.BackColor = Drawing.Color.LightGray
Formulario.MinimumSize = Drawing.Size(200, 200)
Formulario.MaximumSize = Drawing.Size(800, 600)
Formulario.TextAlign = ContentAlignment.MiddleCenter
Formulario.ControlBox = False
Formulario.AutoScroll = True
Formulario.Padding = Drawing.Padding(10)
Formulario.Font = Drawing.Font("Arial", 12, Drawing.FontStyle.Bold)
Formulario.ForeColor = Drawing.Color.Blue

label = Label()
label.Parent = self
label.Text = "Sheet Number:"
label.Location = Point(5,10)
label.Size = Size(100,25)

def MiMetodoClick(sender, event):
    pass

Boton = Button()
Boton.Text = "Texto del boton"
Boton.Location = Point(100,100)
Boton.Size = (50,50)
Boton.BackColor = Color.Red
Boton.ForeColor = Color.White
Boton.Font = Font("Arial", 12)
Boton.Enabled = True
Boton.Visible = True
Boton.TabIndex = 1
Boton.Image = Image.FromFile("ruta_de_la_imagen.png")
Boton.ImageAlign = ContentAlignment.MiddleLeft
imageList = ImageList()
imageList.Images.Add(Image.FromFile("imagen1.png"))
imageList.Images.Add(Image.FromFile("imagen2.png"))
Boton.ImageList = imageList
Boton.ImageIndex = 0

Boton.Click += MiMetodoClick

Formulario.Control.Add(Boton)

textBox = TextBox()
checkBox = CheckBox()
comboBox = ComboBox()

Application.EnableVisualStyles()
Application.Run(Formulario)

    # Transacciones

TransactionManager.Instance.EnsureInTransaction(doc)   
TransactionManager.Instance.TransactionTaskDone()                                            

Transaccion_en_RevitPythonShell = Transaction(doc, "Transaccion en Revit Python Shell")
Transaccion_en_RevitPythonShell.Start()
Transaccion_en_RevitPythonShell.Commit()

    # ---------------------------------------------------

Formulario.Icon = Icon("icono.ico")
Formulario.FormBorderStyle = FormBorderStyle.FixedDialog # Permite impedir el cambiar las dimensiones del formulario
Formulario.BackgroundImage = Bitmap("Imagen.jpg")
    # Permite poner una imagen de fondo
Formulario.BackgroundImageLayout = ImageLayout.Zoom

        # --------------- METODOS DE DYNAMO EN PYTHON SCRIPT ---------------

    # Python Script - Dynamo
dynamo_point = Autodesk.DesignScript.Geometry.Point.ByCoordinates(0,0,0) # Requiere de escribir toda la ruta hasta llegar al metodo
OUT = dynamo_point

        # ---------------- TRASFORMAR DE DYNAMO A REVIT API ----------------

Elemento_de_Revit_API = UnwrapElement(IN[0])
    # Este elemento permite trasformar un objeto de Dynamo a la API de Revit, si ya esta trasnformado, no lo transforma de nuevo.

Element_parameters = UnwrapElement(IN[0]).Parameters
    # Devuelve los parametros del elemento transformado en elemento de la Revit API, pero sin nombres visibles

Nombres_de_parametros = [i.Definition.Name for i in UnwrapElement(IN[0]).Parameters]
    # Devuelve los nombres de los parametros de manera legible

family_type = doc.GetElement(UnwrapElement(IN[0]).GetTypeId())
    # Busca acceder a los parametros del "FamilyType" desde un "FamilyInstance"

        ###################### Funciones utiles ######################
def Extraer_Parametros(elemento):
    Nombres_de_parametros = [i.Definition.Name for i in elemento.Parameters]
    return Nombres_de_parametros




























        # --------------------------- METODOS DE SELECCION ---------------------------

seleccion = uidoc.Selection                                             
    # Selecciona el elemnto actual seleccionado en el modelo

seleccion_id = uidoc.Selection.GetElementIds()
    # Esto se usa para obtener una lista con los Ids de los elementos seleccionados en el documento

for i in uidoc.Selection.GetElementIds():
	print(i)
    # Imprime la lista de Ids

selection               # Por alguna extrana razon que no comprendo "selection" tambien selecciona cosas
                        # Quizas sea un metodo unicamente de -RevitPythonShell-
print(selection)        # "selection" parece que solo funciona en -RevitPythonShell-
for i in selection:     
	print(i.Name)       # Imprime el nombre del elemento
	print(i.Id)         # Imprime el id del elemento

        # Metodos de seleccion en el modelo
    # REQUIEREN LAS IMPORTACIONES DE -RevitPythonShell- para funcionar
Seleccion_por_rectangulo =  uidoc.Selection.PickElementsByRectangle()
    # Permite seleccionar elementos por un rectangulo
    # Devuelve una "List[Element]()"

Elemento_seleccionado =   uidoc.Selection.PickObject(ObjectType.Element,"Seleccionar elemento")
    # Permite seleccionar un elemento
Elementos_seleccionados = uidoc.Selection.PickObjects(ObjectType.Element,"Seleccionar elementos")                                           
    # Permite seleccionar varios elementos con clics
    # Devuelve una "List[Reference]()"

names = []
for x in Elementos_seleccionados:
	element = doc.GetElement(x)
	names.append(element)
print(names)
    # Para obtener los elementos de la List[Reference]() necesitamos usar el metodo ".GetElement()" en los elementos de la lista, pero no en la lista

names = [doc.GetElement(x) for x in uidoc.Selection.PickObjects(ObjectType.Element,"Seleccionar elementos")]
print(names)
    # Metodo completo con compresion de listas 

        ###################### Funciones utiles ######################

# Funcion para obtener elementos seleccionados
def get_selected_elements():
    selection = uidoc.Selection
    return selection

# Funcion para obtener IDs de elementos seleccionados
def get_selected_element_ids():
    element_ids = [x for x in uidoc.Selection.GetElementIds()]
    return element_ids

# Funcion para seleccionar elementos mediante un rectangulo
def select_elements_by_rectangle():
    selected_elements = uidoc.Selection.PickElementsByRectangle()
    return selected_elements

# Funcion para seleccionar elementos mediante clic
def select_elements_by_pick():
    selected_elements = uidoc.Selection.PickObjects(ObjectType.Element, "Seleccionar elementos")
    elements = [doc.GetElement(x) for x in selected_elements]
    return elements


        # --------------------------- CURVE LOOPS ---------------------------

curveloop = CurveLoop()                       
    # Crea un curveloop vacio al cual se le pueden agregar cosas, es una clase de la API de Revit
    # Es similar a escribir "lista = []", pero es necesario para algunos metodos

        # -------------------- PARAMETROS DE ELEMENTOS ---------------------

# elemento.Id 
# elemento.Name
# elemento.Category
# elemento.Geometry
# elemento.Document 
# elemento.DesignOption 
# elemento.Parameters

# Se pueden buscar en la pagina de https://www.revitapidocs.com/

        # EJEMPLOS DE SINTAXIS CORRECTAS/UTILES ------------------------
input = UnwrapElement(IN[0])
OUT =   [
        input.Id,
        input.Name,
        input.Category,
        input.Category.Name,
        input.Category.Id,
        input.Category.Material,
        input.Category.BuiltInCategory,
        input.Category.CategoryType,
        input.Category.Parent,
        #input.Geometry,
        input.Document,
        #input.DesignOptions,
        ]

    # Busqueda de Parametros de elementos seleccionados - ByRectangle - Menos comodo
Seleccion_por_rectangulo =  uidoc.Selection.PickElementsByRectangle()
Nombres_Parametros = []
for i in Seleccion_por_rectangulo:
    for x in i.Parameters:
        Nombres_Parametros.append(x.Definition.Name)
print(Nombres_Parametros)

    # Con compresion de listas
Nombres_Parametros = [x.Definition.Name for i in uidoc.Selection.PickElementsByRectangle() for x in i.Parameters]
print(Nombres_Parametros)

        ###################### Funciones utiles ######################
# Funcion para obtener nombres de parametros de elementos
def get_parameter_names(elements):
    parameter_names = [x.Definition.Name for element in elements for x in element.Parameters]
    return parameter_names

# Funcion para obtener nombres de parametros de elementos seleccionados
def get_selected_parameter_names():
    parameter_names = [x.Definition.Name for element in uidoc.Selection.PickElementsByRectangle() for x in element.Parameters]
    return parameter_names

    # -----------------------

    # Busqueda de Parametros de elementos seleccionados - PickObjetcs - Mas comodo
Seleccion_por_rectangulo =  [doc.GetElement(x) for x in uidoc.Selection.PickObjects(ObjectType.Element,"Seleccionar elementos")]
Nombres_Parametros = []
for i in Seleccion_por_rectangulo:
    for x in i.Parameters:
        Nombres_Parametros.append(x.Definition.Name)
print(Nombres_Parametros)

    # Con compresion de listas
Nombres_Parametros = [x.Definition.Name for i in [doc.GetElement(x) for x in uidoc.Selection.PickObjects(ObjectType.Element,"Seleccionar elementos")] for x in i.Parameters]
print(Nombres_Parametros)

    # -----------------------

Seleccion_por_rectangulo =  [doc.GetElement(x) for x in uidoc.Selection.PickObjects(ObjectType.Element,"Seleccionar elementos")]
print("--------------")
for i in Seleccion_por_rectangulo:
    print("Elemento")
    print(i)
    print("Name")
    print(i.Name)
    for x in i.Parameters:
        Definition_Name =   x.Definition.Name
        HasValue =          x.HasValue
        Id =                x.Id
        Storage_Type =      x.StorageType
        User_Modifiable =   x.UserModifiable
        print(f"Definition_Name =  {Definition_Name}; HasValue =  {HasValue}; Id =  {Id}; StorageType =  {Storage_Type}; UserModifiable = {User_Modifiable};")

    # -----------------------

    # Sintaxis para Python Script de Dynamo - No es muy comoda la salida
    # Requiere agregar algunas importaciones de -RevitPythonShell-
Seleccion_por_rectangulo =  UnwrapElement(IN[0])
for i in Seleccion_por_rectangulo:
    for x in i.Parameters:
        Definition_Name =   x.Definition.Name
        HasValue =          x.HasValue
        Id =                x.Id
        Storage_Type =      x.StorageType
        User_Modifiable =   x.UserModifiable

OUT =   (f"Definition_Name =  {Definition_Name}; HasValue =  {HasValue}; Id =  {Id}; StorageType =  {Storage_Type}; UserModifiable = {User_Modifiable};")

        ###################### Funciones utiles ######################

# Funcion para obtener nombres de Parameters Definition de elementos
def get_parameters_definition_names(elements):
    parameter_names = []
    for element in elements:
        for x in element.Parameters:
            parameter_names.append(x.Definition.Name)
    return parameter_names

# Funcion para obtener informacion detallada de elementos
def get_element_info(elements):
    info = []
    for element in elements:
        element_info = []
        for parameter in element.Parameters:
            definition_name =   parameter.Definition.Name
            has_value =         parameter.HasValue
            parameter_id =      parameter.Id
            storage_type =      parameter.StorageType
            user_modifiable =   parameter.UserModifiable
            param_info = f"Definition_Name = {definition_name}; HasValue = {has_value}; Id = {parameter_id}; StorageType = {storage_type}; UserModifiable = {user_modifiable};"
            element_info.append(param_info)
        info.append(element_info)
    return info

# Funcion para imprimir informacion detallada de un parametro
def print_parameter_info(parameter):
    definition_name =   parameter.Definition.Name
    has_value =         parameter.HasValue
    parameter_id =      parameter.Id
    storage_type =      parameter.StorageType
    user_modifiable =   parameter.UserModifiable
    print(f"Definition Name: {definition_name}")
    print(f"Has Value: {has_value}")
    print(f"Parameter ID: {parameter_id}")
    print(f"Storage Type: {storage_type}")
    print(f"User Modifiable: {user_modifiable}")
    print("-" * 20)

# Funcion principal
def main():
    selected_elements = [doc.GetElement(x) for x in uidoc.Selection.PickObjects(ObjectType.Element, "Seleccionar elementos")]
    print("-" * 20)
    for element in selected_elements:
        print("Element:")
        print(element)
        print("Name:")
        print(element.Name)
        for parameter in element.Parameters:
            print_parameter_info(parameter)

if __name__ == "__main__":
    main()

        # ------------------------ OBTENER ValorElectricoES ------------------------
        
seleccion = UnwrapElement(IN[0])

Parametros_ValorElectricoes = []
for i in seleccion:
	for x in i.Parameters:
		Parametros_ValorElectricoes.append(i.LookupParameter(x.Definition.Name).AsDouble())
OUT = Parametros_ValorElectricoes

        # --------------------------------------

seleccion =  uidoc.Selection.PickElementsByRectangle()

seleccion =  [doc.GetElement(x) for x in uidoc.Selection.PickObjects(ObjectType.Element,"Seleccionar elementos")]
print(seleccion)

Parametros_ValorElectricoes = []
for i in seleccion:
	print(i)
	for x in i.Parameters:
		Parametros_ValorElectricoes.append(i.LookupParameter(x.Definition.Name).AsDouble())
print("------")
print(Parametros_ValorElectricoes)

        # --------------------------------------

Elementos_seleccionados = uidoc.Selection.PickObjects(ObjectType.Element)
print(Elementos_seleccionados)

names = []
for x in Elementos_seleccionados:
    element = doc.GetElement(x)
    names.append(element)

Parametros_ValorElectricoes = []
for i in names:
    print(i)
    print("------ Elemento ------")
    for x in i.Parameters:
        print(" - " + x.Definition.Name)
        print(x.Definition.BuiltInParameter)
        print(i.LookupParameter(x.Definition.Name).AsDouble())
            
        # --------------------------------------

Elementos_seleccionados = uidoc.Selection.PickObjects(ObjectType.Element)
print(Elementos_seleccionados)

names = []
for x in Elementos_seleccionados:
    element = doc.GetElement(x)
    names.append(element)

Parametros_ValorElectricoes = []
for i in names:
    print(i)
    print("------ Elemento ------")
    for x in i.Parameters:
        print(" - " + x.Definition.Name)
        if x.StorageType == StorageType.Double:
            print("Numero fraccionario")
            print(i.LookupParameter(x.Definition.Name).AsDouble())
        elif x.StorageType == StorageType.String:
            print("Texto")
            print(i.LookupParameter(x.Definition.Name).AsString())
        elif x.StorageType == StorageType.Integer:
            print("Numero redondo")
            print(i.LookupParameter(x.Definition.Name).AsInteger())
#        elif x.StorageType == StorageType.Boolean:
#            print("Boolean")
#            print(i.LookupParameter(x.Definition.Name).AsBoolean())    
        # Pense que funcionaria un metodo "AsBoolean()"
        else:
            print("Tipo de parametro no admitido")

        # --------------------------------------

names = [doc.GetElement(x) for x in uidoc.Selection.PickObjects(ObjectType.Element)]

Parametros_ValorElectricoes = []
for i in names:
    print(i)
    for x in i.Parameters:
        print("------ Elemento ------")
        print(" - Definition.Name")
        print(x.Definition.Name)
        print(" - StorageType")
        print(x.StorageType)
        print(" - Definition.BuiltInParameter")
        print(x.Definition.BuiltInParameter)
        if x.StorageType == StorageType.Double:
            print(" - LookupParameter(x.Definition.Name).AsDouble()")
            print(i.LookupParameter(x.Definition.Name).AsDouble())
        elif x.StorageType == StorageType.String:
            print(" - LookupParameter(x.Definition.Name).AsString()")
            print(i.LookupParameter(x.Definition.Name).AsString())
        elif x.StorageType == StorageType.Integer:
            print(" - LookupParameter(x.Definition.Name).AsInteger()")
            print(i.LookupParameter(x.Definition.Name).AsInteger())
        else:
            print("Tipo de parametro no admitido")

        ###################### Funciones utiles ######################

def Devolver_LookupParameters(elemento):
    Parametros_ValorElectricoes = []
    for i in elemento:
        for x in i.Parameters:
            Parametros_ValorElectricoes.append(i.LookupParameter(x.Definition.Name).AsDouble())
    return Parametros_ValorElectricoes

# Funcion para obtener ValorElectricoes de parametros usando LookupParameter
def get_lookup_parameter_values(elements):
    parameter_values = []
    for element in elements:
        for parameter in element.Parameters:
            param_name = parameter.Definition.Name
            lookup_param = element.LookupParameter(param_name)
            if lookup_param is not None:
                if parameter.StorageType == StorageType.Double:
                    parameter_values.append(lookup_param.AsDouble())
                elif parameter.StorageType == StorageType.String:
                    parameter_values.append(lookup_param.AsString())
                elif parameter.StorageType == StorageType.Integer:
                    parameter_values.append(lookup_param.AsInteger())
    return parameter_values

# Funcion para obtener informacion detallada de elementos usando LookupParameter
def get_lookup_parameter_info(elements):
    info = []
    for element in elements:
        element_info = []
        for parameter in element.Parameters:
            param_name = parameter.Definition.Name
            lookup_param = element.LookupParameter(param_name)
            if lookup_param is not None:
                definition_name = parameter.Definition.Name
                has_value = parameter.HasValue
                parameter_id = parameter.Id
                storage_type = parameter.StorageType
                user_modifiable = parameter.UserModifiable
                param_info = f"Definition_Name = {definition_name}; HasValue = {has_value}; Id = {parameter_id}; StorageType = {storage_type}; UserModifiable = {user_modifiable};"
                element_info.append(param_info)
        info.append(element_info)
    return info

        # --------------------------------------

def obtener_elementos_seleccionados(uidoc):
    Elementos_seleccionados = uidoc.Selection.PickObjects(ObjectType.Element)
    return Elementos_seleccionados

def obtener_ValorElectricoes_parametros(elemento):
    parametros_ValorElectricoes = []
    for parametro in elemento.Parameters:
        definicion = parametro.Definition
        tipo_almacenamiento = parametro.StorageType

        print("------ Elemento ------")
        print(" - Definition.Name:", definicion.Name)
        print(" - StorageType:", tipo_almacenamiento)
        print(" - Definition.BuiltInParameter:", definicion.BuiltInParameter)

        ValorElectrico = obtener_ValorElectrico_parametro(elemento, definicion, tipo_almacenamiento)
        parametros_ValorElectricoes.append((definicion.Name, ValorElectrico))

    return parametros_ValorElectricoes

def obtener_ValorElectrico_parametro(elemento, definicion, tipo_almacenamiento):
    if tipo_almacenamiento == StorageType.Double:
        return elemento.LookupParameter(definicion.Name).AsDouble()
    elif tipo_almacenamiento == StorageType.String:
        return elemento.LookupParameter(definicion.Name).AsString()
    elif tipo_almacenamiento == StorageType.Integer:
        return elemento.LookupParameter(definicion.Name).AsInteger()
    else:
        print("Tipo de parametro no admitido")
        return None

def imprimir_informacion_elemento(elemento):
    print("Elemento seleccionado:", elemento.Name, elemento.Category.Name)
    print("Categoria del elemento:", elemento.Category.Name)
    print("Id de la categoria del elemento:", elemento.Category.Id)
    print("BuiltInCategory:", elemento.Category.BuiltInCategory)

if __name__ == "__main__":
    uidoc = __revit__.ActiveUIDocument
    doc = __revit__.ActiveUIDocument.Document
    elementos_seleccionados = obtener_elementos_seleccionados(uidoc)

    for elemento_id in elementos_seleccionados:
        elemento = doc.GetElement(elemento_id)
        informacion_elementos = imprimir_informacion_elemento(elemento)
        parametros_ValorElectricoes = obtener_ValorElectricoes_parametros(elemento)

        # EJEMPLOS DE SINTAXIS CORRECTAS/UTILES ------------------------

    # Codigo para Revit Script - Dynamo
volumen = UnwrapElement(IN[0]).LookupParameter("Volume")    # Devuelve "Autodesk.Revit.DB.Parameter" como resultado
volumen_name = volumen.Definition.Name                      # Devuelve "Volume" como resultado
volumen_ValorElectrico = volumen.AsDouble()                          # Devuelve el volumen del elemento

    # Sin compresion de listas
Parametros_input1 = []
for i in UnwrapElement(IN[0]).Parameters:
    Parametros_input1.append(i.Definition.Name)

    # Con compresion de listas
Parametros_input1 = [i.Definition.Name for i in UnwrapElement(IN[0]).Parameters]

OUT =   [
        volumen,
        volumen_name,
        volumen_ValorElectrico,
        Parametros_input1,
        ]

        # --------------------------------------

    # Codigo para -RevitPythonShell-
volumen = names.LookupParameter("Volume")    # Devuelve "Autodesk.Revit.DB.Parameter" como resultado
volumen_name = volumen.Definition.Name                      # Devuelve "Volume" como resultado
volumen_ValorElectrico = volumen.AsDouble()                          # Devuelve el volumen del elemento

    # Sin compresion de listas
selected_elements = uidoc.Selection.PickObjects(ObjectType.Element, "Seleccionar elementos")
Parametros_Nombres = []
for obj in selected_elements:
    element = doc.GetElement(obj)
    for parameter in element.Parameters:
        Parametros_Nombres.append(parameter.Definition.Name)
print(Parametros_Nombres)

    # Con compresion de listas
Parametros_Nombres = [x.Definition.Name for i in [doc.GetElement(x) for x in uidoc.Selection.PickObjects(ObjectType.Element, "Seleccionar elementos")] for x in i.Parameters]
print(Parametros_Nombres)

        ###################### Funciones utiles ######################

def Seleccionar_y_obtener_ParametersDefinitionName():
    Elementos_Seleccionados = uidoc.Selection.PickObjects(ObjectType.Element, "Seleccionar elementos")
    Parametros_Nombres = []
    for obj in Elementos_Seleccionados:
        element = doc.GetElement(obj)
        for parameter in element.Parameters:
            Parametros_Nombres.append(parameter.Definition.Name)
    return Parametros_Nombres

def Seleccionar_y_obtener_LookupParameters():
    elementos_seleccionados = uidoc.Selection.PickObjects(ObjectType.Element)
    lookup_parameters = []

    for elemento_seleccionado in elementos_seleccionados:
        elemento = doc.GetElement(elemento_seleccionado)

        for parametro in elemento.Parameters:
            nombre_parametro = parametro.Definition.Name
            lookup_parametro = elemento.LookupParameter(nombre_parametro)
            lookup_parameters.append(lookup_parametro)
    return lookup_parameters

def Obtener_LookupParameters_ValorElectricoes(elemento):
    Parametros_ValorElectricoes = []
    for x in elemento.Parameters:
        if x.StorageType == StorageType.Double:
            print(" - LookupParameter(x.Definition.Name).AsDouble()")
            print(elemento.LookupParameter(x.Definition.Name).AsDouble())
        elif x.StorageType == StorageType.String:
            print(" - LookupParameter(x.Definition.Name).AsString()")
            print(elemento.LookupParameter(x.Definition.Name).AsString())
        elif x.StorageType == StorageType.Integer:
            print(" - LookupParameter(x.Definition.Name).AsInteger()")
            print(elemento.LookupParameter(x.Definition.Name).AsInteger())
        else:
            print("Tipo de parametro no admitido")
    return Parametros_ValorElectricoes

def Seleccionar_y_obtener_LookupParameters_ValorElectricoes():
    Parametros_ValorElectricoes = []
    for i in [doc.GetElement(x) for x in uidoc.Selection.PickObjects(ObjectType.Element)]:
        for x in i.Parameters:
            if x.StorageType == StorageType.Double:
                print(" - LookupParameter(x.Definition.Name).AsDouble()")
                print(i.LookupParameter(x.Definition.Name).AsDouble())
            elif x.StorageType == StorageType.String:
                print(" - LookupParameter(x.Definition.Name).AsString()")
                print(i.LookupParameter(x.Definition.Name).AsString())
            elif x.StorageType == StorageType.Integer:
                print(" - LookupParameter(x.Definition.Name).AsInteger()")
                print(i.LookupParameter(x.Definition.Name).AsInteger())
            else:
                print("Tipo de parametro no admitido")
    return Parametros_ValorElectricoes

# Funcion para obtener nombres de parametros usando LookupParameter
def get_lookup_parameter_names(elements):
    parameter_names = []
    for element in elements:
        for parameter in element.Parameters:
            param_name = parameter.Definition.Name
            lookup_param = element.LookupParameter(param_name)
            if lookup_param is not None:
                parameter_names.append(param_name)
    return parameter_names

        # --------------------------------------

    # Esta funcion extrae la BuiltInCategory del elemento

elementos_seleccionados = uidoc.Selection.PickObjects(ObjectType.Element)

for elemento_id in elementos_seleccionados:
    elemento = doc.GetElement(elemento_id)
    BuiltInCategory_del_elemento = elemento.Category.BuiltInCategory
    
    print(elemento.Name)
    print(BuiltInCategory_del_elemento)

        # --------------------------- CATEGORIAS ---------------------------

# ViewFamily - FloorPlan - 

for i in doc.Settings.Categories:
	print(i.Name)
     
categorias = []
for i in doc.Settings.Categories:
	categorias.append(i.Name)
categorias.sort()

for i in categorias:
	print(i)

        ###################### Funciones utiles ######################

# Funcion para obtener categorias en el modelo
def get_categories():
    categories = [i.Name for i in doc.Settings.Categories]
    categories.sort()
    return categories

        # --------------- CREACION DE ELEMENTOS EN REVIT API ---------------

Floor.Create() - ViewPlan.Create()            
    #Crea un elemento de la categoria

        # ------------------------ FUNCIONES RAPIDAS ------------------------

doc.Delete("Id de elemento") # No logro que funcione
    # Borra un elemento por Id

input = UnwrapElement(IN[0])                                         
tipo = doc.GetElement(input.GetTypeId())
OUT = tipo
    # Extrae del documento activo el tipo de todos los elementos desde el Id del tipo

tipoDeMarca = tipo.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_MARK).AsString()            
    # Extrae el parametro especificado de un elemento y lo transforma a cadena de texto

        ###################### Funciones utiles ######################

# Funcion para borrar elementos
def delete_elements(element):
    transaction = Transaction(doc, "Borrar Elemento")
    transaction.Start()
    doc.Delete(element.GetTypeId())
    transaction.Commit()

        # ------------------------ FUNCIONES PYTHON ------------------------

Nuevos_nombres.append(i.replace("Exterior","E_").replace("Interior","I_").replace("Generic","G_"))
for x, y in zip(Colector_de_tipos, Nuevos_nombres):
    x.Name = y                                
    # Reemplaza un grupo de Strings por otro

        # ---------------------------- COLECTORES ----------------------------
Instancia_del_colector = FilteredElementCollector(doc)                               
    # Colector sin categoria, no permite ver los elementos si no tiene seleccionada una "BuiltInCategory"
    # Tampoco se pueden sacar elementos en un bucle para agregarlos a una lista
    # En RevitPythonShell devuelve que es un colector

Instancia_del_colector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls)                                        
    # Instancia_del_colector = FilteredElementCollector(doc).OfCategory(BuiltInCateInstancia del colector que tiene una lista con todas las instancias de muros y todos los tipos de muros

Instancia_del_colector_por_vistas = FilteredElementCollector(doc,doc.ActiveView.Id).OfCategory(BuiltInCategory.OST_Walls)                   
    # Instancia del colector que tiene una lista con todas las instancias de muros y todos los tipos de muros, en la vista actual

Elementos_del_colector = Instancia_del_colector.ToElements()                                 
    # Devuelve el elemento extraido por la instancia del colector usado
    # .ToStrings() no funciona

Ids_de_elementos_del_colector = Instancia_del_colector.ToElementIds()                        
    # Devuelve el ID  del elemento extraido por la instancia del colector usado
    # .Id() no funciona
    # .GetElementIds() no funciona

Instancia_del_colector.WhereElementIsElementType().ToElements()                              
    # Devuelve las familias

Instancia_del_colector.WhereElementIsNotElementType().ToElements()                           
    # Devuelve las instancias

        # EJEMPLOS DE SINTAXIS CORRECTAS/UTILES ------------------------
Instancia_del_colector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls)
Instancia_del_colector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).ToElements()
    # Devuelve los elementos de forma no entendible, familias e instancias

Instancia_del_colector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).ToElementIds()
    # Devuelve los Ids de los elementos existentes, familias e instancias

Instancia_del_colector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsElementType()
    # Quita las instancias

Instancia_del_colector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType()
    # Quita las familias

Instancia_del_colector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsElementType().ToElementIds()
    # Quita los ids de las instancias 

Instancia_del_colector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElementIds()
    # Quita los ids de las familias 

        ###################### Funciones utiles ######################

# Funcion para obtener instancias de una categoria
def get_instances(ost_category):
    category = BuiltInCategory[ost_category]
    instance_collector = FilteredElementCollector(doc).OfCategory(category).WhereElementIsNotElementType().ToElements()
    return instance_collector

# Funcion para obtener IDs de instancias de una categoria
def get_instance_ids(ost_category):
    category = BuiltInCategory[ost_category]
    instance_ids = FilteredElementCollector(doc).OfCategory(category).WhereElementIsNotElementType().ToElementIds()
    return instance_ids

# Funcion para obtener familias de una categoria
def get_families(ost_category):
    category = BuiltInCategory[ost_category]
    family_collector = FilteredElementCollector(doc).OfCategory(category).WhereElementIsElementType().ToElements()
    return family_collector

# Funcion para obtener IDs de familias de una categoria
def get_family_ids(ost_category):
    category = BuiltInCategory[ost_category]
    family_ids = FilteredElementCollector(doc).OfCategory(category).WhereElementIsElementType().ToElementIds()
    return family_ids

    # AGREGAR FUNCIONES CON "OfClass()" ################### -----------------------

Filtro_de_tipos_de_Vistas = FilteredElementCollector(doc).OfClass(FloorType)  

        # ---------------------------- FILTROS ----------------------------

        # ElementQuickFilter Class - Filtros rapidos
filtro_simple_por_tipo = ElementIsElementTypeFilter()                                        
    # Filtro rapido, filtra los tipos de los elementos cargados en el archivo de Revit
    # No se pueden sacar elementos en un bucle para agregarlos a una lista

Tipos_de_elementos = Instancia_del_colector.WherePasses(filtro_simple_por_tipo)              
    # Quita de "Instancia_del_colector" todos los elementos que son instancias
    # Pide un "elementfilter" dentro de los parentesis, osea un quickfilter, slowfilter...

Tipos_de_elementos = Instancia_del_colector.WherePasses(filtro_simple_por_tipo)              
    # Quita de "Instancia_del_colector" todos los elementos que son instancias

Tipos_de_elementos.ToElements()               
    # Devuelve el elemento extraido por la instancia del colector usado

Tipos_de_elementos.ToElementIds()             
    # Devuelve el ID  del elemento extraido por la instancia del colector usado

filtro_simple_por_instancias = ElementIsElementTypeFilter(True)                              
    # Filtro rapido, filtra las instancias de los elementos cargados en el archivo de Revit
    # True if the filter should match all elements which are not ElementTypes.

Instancias_de_elementos = Instancia_del_colector.WherePasses(filtro_simple_por_instancias)   
    # Quita de "Instancia_del_colector" todos los elementos que son tipos

Instancias_de_elementos.ToElements()          
    # Devuelve el elemento extraido por la instancia del colector usado

Instancias_de_elementos.ToElementIds()        
    # Devuelve el ID  del elemento extraido por la instancia del colector usado


Filtro_de_tipos_de_Vistas = FilteredElementCollector(doc).OfClass(ViewFamilyType)            
    # Devuelve las instancias de tipos de Niveles existentes
    # El metodo "OfClass()" pide un "Autodesk.Revit.DB.ElementType", osea un "ElementType"

Nombres_de_tipos_de_vistas = Filtro_de_tipos_de_Vistas.ToElements()                          
    # Devuelve los nombres de los tipos de niveles

        # CREACION DE UN FILTRO MULTI-CATEGORIA
categorias = List[BuiltInCategory]()
    # List[]() Parece solo funcionar en Dynamo - Python Script
    # Especifica que la lista va a contener solamente elementos "BuiltInCategory"
    # Es una "IColection"
    # List es una clase en Python que representa una lista vacia 

categorias.Add(BuiltInCategory.OST_Walls)     
categorias.Add(BuiltInCategory.OST_Floors)    
categorias.Add(BuiltInCategory.OST_Ceilings)  
    # Agregamos las "BuiltInCategory" que necesitemos
    
Filtro_multiple = ElementMulticategoryFilter(categorias)
    # Es un filtro rapido
#colectorMultiple1 = FilteredElementCollector(doc,doc.ActiveView.Id) # Es un colector por vistas, ¿Que hace esto aca?

Elementos_del_filtro = Filtro_multiple.ToElements()                                          
    # Devuelve los elementos del filtro

Ids_del_filtro = Filtro_multiple.ToElementsIds()                                             
    # Devuelve los IDs del filtro
OUT = collector.WherePasses(filtro).ToElements()


        # EJEMPLOS DE SINTAXIS CORRECTAS/UTILES ------------------------
filtro_simple_por_tipo = ElementIsElementTypeFilter()
Instancia_del_colector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls)
Instancias_de_elementos = Instancia_del_colector.WherePasses(filtro_simple_por_tipo).ToElementIds()
    # Devuelve los Ids de las familias

filtro_simple_por_tipo = ElementIsElementTypeFilter()
Instancia_del_colector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WherePasses(filtro_simple_por_tipo).ToElementIds()
    # Devuelve los Ids de las familias

Instancia_del_colector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsElementType().ToElementIds()
    # Devuelve los Ids de las familias

Filtro_de_tipos_de_Vistas = FilteredElementCollector(doc).OfClass(FloorType)  
Nombres_de_tipos_de_vistas = Filtro_de_tipos_de_Vistas.ToElementIds() 
    # Devuelve los Ids de las familias

    # Cualquiera de las 4 anteriores hace lo mismo

Instancia_del_colector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls)
filtro_simple_por_tipo = ElementIsElementTypeFilter(True)
Instancias_de_elementos = Instancia_del_colector.WherePasses(filtro_simple_por_tipo).ToElementIds()
    # Devuelve los Ids de las instancias

        ###################### Funciones utiles ######################

# Funcion para filtrar elementos por BuiltInCategory
def filter_by_category(ost_category):
    category = BuiltInCategory[ost_category]
    instance_ids = FilteredElementCollector(doc).OfCategory(category).WherePasses(ElementIsElementTypeFilter()).ToElementIds()
    return instance_ids

        # ----------------------- FILTRO + COLECTOR -----------------------

Todos_los_niveles = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType()                        
    # Filtro + colector que devuelve todos los niveles existentes

Todos_los_niveles = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()        
    # Filtro + colector que devuelve todos los nombres de niveles existentes

Todos_los_niveles = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsElementType()                        

    # Filtro + colector que devuelve todos los niveles existentes

colector1 = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsElementType()#.ToElement()
wallInstancesIds = []
for i in colector1:
	wallInstancesIds.append(i.Id.ToString())     
    # Devuelve los Id de las instancias

colector2 = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsElementType()#.ToElement()
wallTypes = []
for i in colector2:
	wallTypes.append(i.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_NAME).AsString())          
	# Devuelve los tipos de las instancias del elemento especificado

        ###################### Funciones utiles ######################

# Funcion para obtener IDs de instancias de una categoria
def get_instance_ids(ost_category):
    category = BuiltInCategory[ost_category]
    instance_ids = [i.Id.ToString() for i in FilteredElementCollector(doc).OfCategory(category).WhereElementIsElementType().ToElement()]
    return instance_ids

# Funcion para obtener tipos de instancias de una categoria
def get_instance_types(ost_category):
    category = BuiltInCategory[ost_category]
    instance_types = [i.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_NAME).AsString() for i in FilteredElementCollector(doc).OfCategory(category).WhereElementIsElementType().ToElement()]
    return instance_types

        # -----------------------  VENTANAS EMERGENTES -----------------------

Ventana_emergente = TaskDialog.Show("Titulo","Instruccion principal", TaskDialogCommonButtons.Ok, TaskDialogResult.Ok)                      
    # Crea una ventana emergente 

Ventana_emergente.Show()                      
    # Muestra la ventana emergente ya creada

        # EJEMPLOS DE SINTAXIS CORRECTAS/UTILES ------------------------

Ventana_emergente = TaskDialog.Show("Titulo","Instruccion principal")
Ventana_emergente = TaskDialog.Show("Titulo","Instruccion principal", TaskDialogCommonButtons.Ok, TaskDialogResult.Ok)

Ventana_emergente = TaskDialog("Ventana emergente", "Contenido de ventana emergente")
Ventana_emergente.Show()

Caja_de_mensaje = MessageBox.Show("Mensaje 1", "Mensaje 2", MessageBoxButtons.OK)
    #Parece que MessageBox no tiene un contructor como TaskDialog, y siempre se necesita usar con ".Show()"

resultado = MessageBox.Show("Mensaje 1", "Mensaje 2", MessageBoxButtons.YesNo)
if resultado == DialogResult.Yes:
	pass # Hacer algo si el usuario hizo clic en "Si"
else:
	pass # Hacer algo si el usuario hizo clic en "No"

        # Tipos de MessageBoxButtons:

# MessageBoxButtons.OKCancel:         # Muestra dos botones, "Aceptar" y "Cancelar".
# MessageBoxButtons.AbortRetryIgnore: # Muestra tres botones, "Abortar", "Reintentar" e "Ignorar".
# MessageBoxButtons.YesNoCancel:      # Muestra tres botones, "Si", "No" y "Cancelar".
# MessageBoxButtons.YesNo:            # Muestra dos botones, "Si" y "No".
# MessageBoxButtons.RetryCancel:      # Muestra dos botones, "Reintentar" y "Cancelar".
# MessageBoxButtons.Custom:           # Permite personalizar los botones mostrados en el cuadro de dialogo MessageBox

        # --------- METODOS PARA COLECTORES Y ELEMENTOS DE COLECTORES ---------

colector1 = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
    # ".ToElements()" no es necesario en Python, por que ese lenguaje de programacion hace una conversion automatica de tipos; pero en C# si va a hacer falta

colector1 = FilteredElementCollector(doc)
colector1.OfCategory(BuiltInCategory.OST_Walls)

colector1.WhereElementIsElementType()       # METODO de la clase "FilteredElementCollector()"
colector1.WhereElementIsNotElementType()    # METODO de la clase "FilteredElementCollector()"

colector1.ToElements()      # Esto es un METODO de la clase "FilteredElementCollector()"
colector1.ToElementIds()    # Esto es un METODO de la clase "FilteredElementCollector()"

for i in colector1:
	print(i)
      
len(list(colector1))        # Muestra la cantidad de elementos en el colector
	
for i in colector1:
	print(i.Id)             # Esto es una PROPIEDAD de la clase "Element", igual que .Name

for i in colector1:
	print(i.ToString())     # ¿Esto es un METODO de muchas clases?


doors = Fec(doc).OfCategory(Bic.OST_Doors).\
        WhereElementIsNotElementType().ToElements()

doors = FilteredElementCollector(doc).\
        OfCategory(BuiltInCategory.OST_Doors).\
        WhereElementIsNotElementType().ToElements()

all_furniture = FilteredElementCollector(doc)           # This code starts by creating a new FilteredElementCollector instance, which takes the Revit document as the argument in its constructor
all_furniture.OfCategory(BuiltInCategory.OST_Furniture) # The collector is then furniture-refined by specifying a filter - in our example, we only want to return elements of the Furniture category. This is specified as an option in the BuiltInCategory enumeration.
all_furniture.WhereElementIsNotElementType()            # Line 3 adds in a further filter - we don't want to include Furniture Family Types in our returned elements, only instances.
all_furniture.ToElements()                              # In Line 4 we specify we want the FilteredElementCollector to return us the actual Revit elements (instead of their ElementIds).
OUT = all_furniture                                     # Finally, Line 5 uses OUT to output the collected elements from the node.

all_furniture = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Furniture).WhereElementIsNotElementType().ToElements() # It's also possible to condense the above script down to a single line
OUT = all_furniture

Objetos_seleccionados = selection   # DEBERIA AMPLIAR ESTO - metodo que permite capturar los elementos seleccionados


        # ----------------------- HERENCIAS DE REVIT -----------------------

class FiltroDeUnaCategoria(ISelectionFilter): # Herencia de User Interface de Revit
    pass

        # ----------------- SELECCION DE ELEMENTOS PRE-FILTRADOS -----------------

class Filtro_de_seleccion_de_categoria_simple(ISelectionFilter): # Herencia de User Interface de Revit API, creacion de la clase del filtro                                     
	def __init__(self, Nombre_de_categoria):
		self.Nombre_de_categoria = Nombre_de_categoria
	def AllowElement(self, element):                            # AllowElement() y AllowReference() son los unicos metodos de ISelectionFilter
		if element.Category.Name == self.Nombre_de_categoria:   
			return True
		else:
			return False
	def AllowReference(self, refer, point):
		return False

Filtro_de_seleccion_de_pisos = Filtro_de_seleccion_de_categoria_simple("Floors")    # Esto es un ISelectionFilter, por el hecho de heredar la interfaz ISelectionFilter durante la creacion de la clase

    # Seleccion puntual
Seleccion_de_objetos_puntual = uidoc.Selection.PickObjects(ObjectType.Element, Filtro_de_seleccion_de_pisos)    # PickObject Method (ObjectType, ISelectionFilter)

Nombres = []
for x in Seleccion_de_objetos_puntual:
	elemento = doc.GetElement(x)
	Nombres.append(elemento.Name)
	
print(Nombres)

    # Seleccion por rectangulo
Seleccion_por_rectangulo = uidoc.Selection.PickElementsByRectangle(Filtro_de_seleccion_de_pisos)                # PickElementsByRectangle(ISelectionFilter)

Nombres = []
for x in Seleccion_por_rectangulo:
	Nombres.append(x.Name)
	
print(Nombres)

    # La diferencia (Revit 2023) entre seleccion puntual y por rectangulo es que seleccion puntual tiene las opciones de "finish" o "cancel"

        # SELECCION CON FILTRO DOBLE-CATEGORIA

class Filtro_de_seleccion_de_categoria_Doble(ISelectionFilter): # Herencia de User Interface de Revit API, creacion de la clase del filtro                                     
	def __init__(self, Nombre_de_categoria_1, Nombre_de_categoria_2):
		self.Nombre_de_categoria1 = Nombre_de_categoria_1
		self.Nombre_de_categoria2 = Nombre_de_categoria_2
	def AllowElement(self, element):                            # AllowElement() y AllowReference() son los unicos metodos de ISelectionFilter
		if element.Category.Name == self.Nombre_de_categoria1 or element.Category.Name == self.Nombre_de_categoria2:
			return True
		else:
			return False
	def AllowReference(self, refer, point):
		return True
	
Filtro_de_seleccion_de_pisos = Filtro_de_seleccion_de_categoria_Doble("Walls","Floors")

Seleccion_por_rectangulo = uidoc.Selection.PickElementsByRectangle(Filtro_de_seleccion_de_pisos)                # PickElementsByRectangle(ISelectionFilter)

Nombres = []
for x in Seleccion_por_rectangulo:
	Nombres.append(x.Name)
	
print(Nombres)

        # SELECCION CON FILTRO MULTI-CATEGORIA CON ARGUMENTOS INDEFINIDOS

class Filtro_de_seleccion_de_categoria_Multiple(ISelectionFilter):
    def __init__(self, *categorias):
        self.categorias = categorias

    def AllowElement(self, element):
        return element.Category.Name in self.categorias

    def AllowReference(self, refer, point):
        return True

# Ejemplo de uso
categorias_seleccionadas = ["Walls", "Floors", "Doors"]
filtro_multiple = Filtro_de_seleccion_de_categoria_Multiple(*categorias_seleccionadas)
seleccion_por_rectangulo = uidoc.Selection.PickElementsByRectangle(filtro_multiple)

#nombres = [element.Name for element in seleccion_por_rectangulo] # Esta linea se desarma en la siguiente
nombres = []
for element in seleccion_por_rectangulo:
    nombres.append(element.Name)

        ###################### Funciones utiles ######################

# Clase para filtrar la seleccion por multiples categorias
class MultipleCategorySelectionFilter(ISelectionFilter):
    def __init__(self, *categories):
        self.categories = categories

    def AllowElement(self, element):
        return element.Category.Name in self.categories

    def AllowReference(self, reference, point):
        return True

# Funcion para seleccionar elementos de multiples categorias
def select_elements_by_multiple_categories(*categories):
    filter = MultipleCategorySelectionFilter(*categories)
    selected_elements = uidoc.Selection.PickElementsByRectangle(filter)
    element_names = [element.Name for element in selected_elements]
    return element_names

categorias_a_seleccionar = ["Walls", "Doors"]
seleccion = Filtro_multi_categoria(*categorias_a_seleccionar)


        # SELECCION CON FILTRO MULTI-CATEGORIA CON ARGUMENTOS INDEFINIDOS - SELECCION PICKOBJECTS

class Filtro_de_seleccion_de_categoria_Multiple(ISelectionFilter):
    def __init__(self, *categorias):
        self.categorias = categorias

    def AllowElement(self, element):
        return element.Category.Name in self.categorias

    def AllowReference(self, refer, point):
        return True

categorias_seleccionadas = ["Walls", "Floors", "Doors"]

Nombres = []
for x in uidoc.Selection.PickObjects(ObjectType.Element, Filtro_de_seleccion_de_categoria_Multiple(*categorias_seleccionadas)):
	elemento = doc.GetElement(x)
	Nombres.append(elemento)
     

# SELECCION CON FILTRO MULTI-CATEGORIA CON ARGUMENTOS INDEFINIDOS Y FILTROS ADICIONALES
    # Este filtro permite seleccionar muros solo si son muros con alturas conectadas a niveles

class FiltroDeSeleccionDeCategoriaMultiple(ISelectionFilter):
    def __init__(self, *categorias):
        self.categorias = categorias

    def AllowElement(self, element):
        if element.Category.Name == "Walls":

            altura_elemento_param = element.get_Parameter(BuiltInParameter.WALL_USER_HEIGHT_PARAM)

            # Permite seleccionar solo muros que tienen alturas que estan conectadas a un nivel
            if altura_elemento_param.IsReadOnly:
                return True
            else:
                return False

        if element.Category.Name in self.categorias:
            return True
        
        return False

    def AllowReference(self, refer, point):
        return True
     
        ###################### Funciones utiles ######################

class Filtro_de_seleccion_de_categoria_Multiple(ISelectionFilter):
    def __init__(self, *categorias):
        self.categorias = categorias

    def AllowElement(self, element):
        return element.Category.Name in self.categorias

    def AllowReference(self, refer, point):
        return True

categorias_seleccionadas = ["Walls", "Floors", "Doors"]

Nombres = [doc.GetElement(x) for x in uidoc.Selection.PickObjects(ObjectType.Element, Filtro_de_seleccion_de_categoria_Multiple(*categorias_seleccionadas))]




        # --------------------- FORMULARIO WINDOWS FORMS ---------------------

Formulario = Form()                           
    # Crea el formulario

Application.EnableVisualStyles()              
    # Activa/Habilita los estilos visuales
Application.Run(Formulario)                   
    # Ejecuta el formulario creado
    # La ejecucion del formulario debe estar al final de todo el contenido que va a tener el formulario

        # EJEMPLO BASICO DE FORMULARIO
        
    #crear la instancia Form
form = Form()

    #propiedades de texto e icono
form.Text = "Mi WinForm"

    #establecer dimensiones
form.Size = Size(400,200)
form.FormBorderStyle = FormBorderStyle.FixedDialog

    #agregar boton
button = Button()
button.Text = "Rename"
button.Location = Point(0,0)
button.Size = Size(60,25)
form.Controls.Add(button)
button.Click += lambda *args: MessageBox.Show("Elementos renombrados","Operacion exitosa")

    #iniciar el formulario al centro de la pantalla
form.StartPosition = FormStartPosition.CenterScreen

    #ejecutar la aplicacion
Application.EnableVisualStyles()
Application.Run(form)




    # PROPIEDADES DEL FORMULARIO              
Formulario.Text = "Titulo del formulario"
Formulario.Size = Size(100,100) # Permite darle dimensiones al formulario en pixeles

Formulario.StarPosition = FormStartPosition.CenterScreen
    # Permite iniciar el formulario en el centro de la pantalla

# Configuracion de color de fondo
Formulario.BackColor = Drawing.Color.LightGray

# Configuracion de tamano minimo y maximo
Formulario.MinimumSize = Drawing.Size(200, 200)
Formulario.MaximumSize = Drawing.Size(800, 600)

    # ---------------------------------------------------


Formulario.Icon = Icon("icono.ico")
Formulario.FormBorderStyle = FormBorderStyle.FixedDialog # Permite impedir el cambiar las dimensiones del formulario
Formulario.BackgroundImage = Bitmap("Imagen.jpg")
    # Permite poner una imagen de fondo
Formulario.BackgroundImageLayout = ImageLayout.Zoom
    # Permite agrandar la imagen de fondo

    # ---------------------------------------------------

# Alineacion de texto (para controles de texto en el formulario)
# Formulario.TextAlign = ContentAlignment.MiddleCenter

# Control de botones de cierre
# Formulario.ControlBox = False

# Barra de desplazamiento
# Formulario.AutoScroll = True

# Margenes internos
# Formulario.Padding = Drawing.Padding(10)

# Fuentes y colores personalizados
# Formulario.Font = Drawing.Font("Arial", 12, Drawing.FontStyle.Bold)
# Formulario.ForeColor = Drawing.Color.Blue

# Ejecucion del formulario
Forms.Application.Run(Formulario)

        # ------------------ ETIQUETAS - FORMULARIO WINDOWS FORMS ------------------

    # Creamos una etiqueta (Label)
label1 = Label()
label1.Parent = self
label1.Text = "Sheet Number:"
label1.Location = Point(5,10)
label1.Size = Size(100,25)

        # ------------------ BOTONES - FORMULARIO WINDOWS FORMS ------------------

def MiMetodoClick(sender, event):   # Asociar un metodo al evento Click del boton
    # Tu codigo para manejar el evento Click aqui
    pass

    # BOTONES                                 
Boton = Button()                    # Crea un boton
Boton.Text = "Texto del boton"      # Texto del boton
Boton.Location = Point(100,100)     # Permite ubicar el boton en algun sitio
Boton.Size = (50,50)                # Medidas del boton
Boton.BackColor = Color.Red         # Cambiar el color de fondo del boton
Boton.ForeColor = Color.White       # Cambiar el color del texto en el boton
Boton.Font = Font("Arial", 12)      # Cambiar la fuente y el tamano del texto en el boton
Boton.Enabled = True                # Habilitar el boton
Boton.Visible = True                # Hacer el boton visible
Formulario.Control.Add(Boton)       # Agrega el boton al formulario

Boton.TabIndex = 1                  # Cambiar el orden en que se selecciona el boton al presionar Tab
Boton.Image = Image.FromFile("ruta_de_la_imagen.png")   # Asignar una imagen al boton en lugar de texto
Boton.ImageAlign = ContentAlignment.MiddleLeft          # Controlar la alineacion de la imagen dentro del boton

imageList = ImageList()
imageList.Images.Add(Image.FromFile("imagen1.png"))     # Puedes usar una lista de imagenes y asignar indices a las imagenes
imageList.Images.Add(Image.FromFile("imagen2.png"))
Boton.ImageList = imageList
Boton.ImageIndex = 0                # indice de la imagen en la lista

    # Funcionalidad del boton

Boton.Click += MiMetodoClick        # Acciona la funcion definida

        # ------------------ TEXTBOX - FORMULARIO WINDOWS FORMS ------------------

def CrearCuadroTexto(
    form,
    textoInicial="",
    origenCuadroTexto=Point(5, 60),
    tamanoCuadroTexto=Size(200, 20)
):
    textBox = TextBox()
    textBox.Parent = form
    textBox.Text = textoInicial
    textBox.Location = origenCuadroTexto
    textBox.Size = tamanoCuadroTexto
    return textBox  # Devolvemos el cuadro de texto para poder referenciarlo mas adelante

        # ------------------ CHECKBOX - FORMULARIO WINDOWS FORMS ------------------

def CrearCasillaVerificacion(
    form,
    textoCasilla="Casilla",
    estadoInicial=False,
    origenCasilla=Point(5, 90)
):
    checkBox = CheckBox()
    checkBox.Parent = form
    checkBox.Text = textoCasilla
    checkBox.Checked = estadoInicial
    checkBox.Location = origenCasilla
    #checkBox.CheckedChanged += FuncionCheckBox  # Asociamos la funcion al evento CheckedChanged
    #return checkBox  # Devolvemos la casilla de verificacion para poder referenciarla mas adelante

        # ------------------ COMBOBOX - FORMULARIO WINDOWS FORMS ------------------

def CrearComboBox(
    form,
    items=[],
    seleccionInicial="Texto sin editar ---",
    origenComboBox=Point(5, 120),
    tamanoComboBox=Size(200, 20)
):
    comboBox = ComboBox()
    comboBox.Parent = form
    comboBox.Location = origenComboBox
    comboBox.Size = tamanoComboBox
    comboBox.DropDownStyle = ComboBoxStyle.DropDownList  # Establece el estilo para que el usuario no pueda escribir
#    comboBox.Items.AddRange(items)  # Agrega los elementos al ComboBox
    comboBox.SelectedItem = seleccionInicial  # Establece la seleccion inicial
    return comboBox  # Devolvemos el ComboBox para poder referenciarlo mas adelante

        # ----------- FUNCIONALIDADES Botones - FORMULARIO WINDOWS FORMS -----------

    # Sin funcion lamda

def button_click(sender, args):
    try:
        MessageBox.Show("Elementos", "Operacion exitosa")
    except Exception as ex:
        MessageBox.Show(str(ex), "Error")
    # La excepcion capturada se almacena en la variable "ex"
Boton.Click += button_click

    # Con funcion lamda

Boton.Click += lambda *args: MessageBox.Show("Elementos","Operacion exitosa")
    # Crea un evento al boton click - Crea un mensaje



        # ----------------- CLASES DE CREACION DE FORMULARIOS -----------------

#----------------------

        ###################### Funciones utiles ######################

            # AUTOMATIZACION DEL FORMULARIO ----------------

        # Etiqueta Automatica ----------------
def create_label    (
                    form,
                    text="Texto de etiqueta",
                    location=Point(5, 10),
                    size=Size(100, 45),
                    bg_color=Color.White,
                    text_color=Color.Black,
                    font=Font("Arial", 10)
                    ):
    label = Label()
    label.Parent = form
    label.Text = text
    label.Location = location
    label.Size = size
    label.BackColor = bg_color
    label.ForeColor = text_color
    label.Font = font
    return label

        # Boton Automatico ----------------
    # Funcionalidad del boton

def Function_Click(sender, eventArgs):
    TaskDialog.Show("Elementos", "Operacion exitosa")   # Ventana de Revit API
    #MessageBox.Show("Elementos", "Operacion exitosa")  # Ventana de Windows Forms
    # Se puede elegir entre ambas opciones,

def create_button   (  
                    form,
                    text="Boton",
                    location=Point(150, 10),
                    size=Size(100, 30),
                    bg_color=Color.White,
                    text_color=Color.Black,
                    font=Font("Arial", 10)
                    ):
    button = Button()
    button.Parent = form
    button.Text = text
    button.Location = location
    button.Size = size
    button.BackColor = bg_color
    button.ForeColor = text_color
    button.Font = font
    button.Click += Function_Click  # Asociamos la funcion al evento Click del boton
    return button  # Devolvemos el boton para poder referenciarlo mas adelante

        # No tiene argumentos porque esta destinada a ser utilizada como un manejador de eventos para un boton en una interfaz de usuario
        # Cuando se utiliza como manejador de eventos, esta funcion se invocara automaticamente cuando se haga clic en el boton, sin necesidad de pasarle argumentos explicitos.

        # Cuadro de Texto Automatico ----------------
def create_text_box (
                    form,
                    text="Texto sin modificar",
                    location=Point(5, 60),
                    size=Size(200, 20)
                    ):
    text_box = TextBox()
    text_box.Parent = form
    text_box.Text = text
    text_box.Location = location
    text_box.Size = size
    return text_box

        # Casilla de Verificacion Automatica ----------------

"""
        # Funcion para manejar el evento de la casilla de verificacion
def FuncionCheckBox(sender, eventArgs):
    if checkBox.Checked:
        TaskDialog.Show("Check box tildada","---------")
    else:
        TaskDialog.Show("Check box destildada","---------")

# ------- Arroja error este metodo -----
"""

def create_check_box(
                    form,
                    text="Casilla",
                    checked=False,
                    location=Point(5, 90)
                    ):
    check_box = CheckBox()
    check_box.Parent = form
    check_box.Text = text
    check_box.Checked = checked
    check_box.Location = location
    #checkBox.CheckedChanged += FuncionCheckBox  # Asociamos la funcion al evento CheckedChanged
    return check_box  # Devolvemos la casilla de verificacion para poder referenciarla mas adelante

        # Combobox Automatico ----------------
def create_combo_box(
                    form,
                    items=[],
                    selected_item="Texto sin editar",
                    location=Point(5, 120),
                    size=Size(200, 20)
                    ):
    combo_box = ComboBox()
    combo_box.Parent = form
    combo_box.Location = location
    combo_box.Size = size
    combo_box.DropDownStyle = ComboBoxStyle.DropDownList # Establece el estilo para que el usuario no pueda escribir
    combo_box.Items.AddRange(items) # Agrega los elementos al ComboBox
    combo_box.SelectedItem = selected_item # Establece la seleccion inicial
    return combo_box


        # Formulario Automatico ----------------
class CustomForm(Form):
    def __init__(self):
        self.Text = "Formulario"
        self.Size = Size(300, 300)
        self.CenterToScreen()
        self.label = create_label(self)
        self.button = create_button(self)
        self.text_box = create_text_box(self)
        self.check_box = create_check_box(self)
        self.combo_box = create_combo_box(self, items=["Opcion 1", "Opcion 2", "Opcion 3"], selected_item="Opcion 1")

# Crear una instancia del formulario personalizado
Formulario = CustomForm()

# Ejecutar la aplicacion
Application.EnableVisualStyles()
Application.Run(Formulario)
#Formulario.ShowDialog() # Este es un sustituto del metodo de arriba

# -----------

        ###################### Funciones utiles ######################

def ButtonClickCreate(self, sender, args):
    titleBlockCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_TitleBlocks)
    titleBlockId = titleBlockCollector.FirstElementId()
    if sender.Click:
        self.sheetNumber = self.textBox1.Text
        self.sheetName = self.textBox2.Text
        if self.sheetNumber == "" or self.sheetName == "":
            tD = TaskDialog.Show("Values is missing", "Sheet Number or Sheet Name is missing")
        else:
            tSheet = Transaction(doc, "Create Sheets")
            tSheet.Start()
            
            newSheet = ViewSheet.Create(doc, titleBlockId)
            newSheet.SheetNumber = self.sheetNumber
            newSheet.Name = self.sheetName
            
            tSheet.Commit()
            
        self.DialogResult = DialogResult.OK
        self.Close()

# Definimos la funcionalidad de los botones
def ButtonClickDelete(self, sender, args):
    categories = []
    for x in doc.Settings.Categories:
        categories.append(x)
    selectedCategory = self.comboBox1.SelectedItem
    categoryId = None

    for cat in categories:
        if cat.Name == selectedCategory:
            categoryId = cat.Id

    # Crear un colector de elementos de la categoria seleccionada
    collector = FilteredElementCollector(doc).OfCategoryId(categoryId).WhereElementIsNotElementType()

    t = Transaction(doc, "Delete Elements")
    t.Start()
    for e in collector.ToElementIds():
        doc.Delete(e)
    t.Commit()

    tD = TaskDialog.Show("Ok", "Successful Operation")
    self.DialogResult = DialogResult.OK
    self.Close()

def ButtonClickCancel(self, sender, args):
    self.DialogResult = DialogResult.Cancel
    self.Close()

form.ShowDialog() # Este es un sustituto del metodo de arriba, pero que no permite interactuar hasta no cerrar la ventana


# --------------------------------------

        # -------------------------- TRANSACCIONES --------------------------

TransactionManager.Instance.EnsureInTransaction(doc)                                         
    # Acciones
TransactionManager.Instance.TransactionTaskDone()                                            

    # Crea una transaccion en un nodo de Python Script de  Dynamo

Transaccion_en_RevitPythonShell = Transaction(doc, "Transaccion en Revit Python Shell")

Transaccion_en_RevitPythonShell.Start()
    # Acciones
Transaccion_en_RevitPythonShell.Commit()

    # Crea una instancia de transaccion con un nombre en particular - Se usa en RevitPYthonShell pero tambien en Python Script de Dynamo

        # -------------------------- ACOMODAR --------------------------



        # REVIT PYTHON SHELL

p = el.LookupParameter("Volume")

p # Imprime "[autodesk.Revit.DB.Parameter]"

p.Definition.Name # Imprime "Volume"

p.StorageType # Imprime "Autodesk.Revit.DB.StorageType.Double"

    # Suma de todos los volumenes

Colector_muros = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType()

Volumen_Total = 0.0

for muro in Colector_muros:
    param_volumen = muro.LookupParameter("Volume")
    if param_volumen:
        Volumen_Total = Volumen_Total + param_volumen.AsDouble()
print("Volumen total es: {}".format(Volumen_Total))

####################### Dudas ###########################



        ###################### Funciones utiles ######################

def Crear_pisos(Poligonos, Tipo_de_piso=None, Nivel=None):
    if Tipo_de_piso is None:
        Tipo_de_piso = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsElementType().ToElements()[0]
    if Nivel is None:
        Nivel = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsElementType().ToElements()[0]

    Pisos = []
    contorno = CurveArray()
    for poligono in Poligonos:
        contorno.Append(poligono.ToRevitType())
    
    Pisos.append(Floor.Create(doc, contorno, Tipo_de_piso.Id, Nivel.Id))
    return Pisos

        # --------------------------------------

# -*- coding: utf-8 -*-
"""Print all sheets with a specified revision date. 

NOTE: 
Name of the files will be sheet number, name and appended revision.
Existing files will be overwritten."""
__title__ = 'Print by\nRev Date'
__author__ = "nWn"

# Import commom language runtime
import clr

# Import Revit DB
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, \
                            Transaction, TransactionGroup, ElementId, PrintManager, \
							PrintSetting, ViewSet

# Import libraries to enable Windows forms
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Drawing import Point, Size
from System.Windows.Forms import Application, Button, Form, Label, TextBox, FolderBrowserDialog, DialogResult

# Import os, shutil to move files
import os, shutil

# Import sleep for moving files after printing
from time import sleep

# Create a class form
class CreateWindow(Form):
	def __init__(self, title, author):
		# Create the form
		self.Name = "Create Window"
		self.Text = title
		self.Size = Size(500, 150)
		self.CenterToScreen()
		
		self.value = ""
		
		# Create label for input title
		labelDiv = Label(Text = author + ":")
		labelDiv.Parent = self
		labelDiv.Size = Size(100, 150)
		labelDiv.Location = Point(30, 20)
		
		# Create TextBox for input
		self.textboxDiv = TextBox()
		self.textboxDiv.Parent = self
		self.textboxDiv.Text = "01/22/2019"
		self.textboxDiv.Location = Point(300, 20)
	
		# Create button
		button = Button()
		button.Parent = self
		button.Text = "Ok"
		button.Location = Point(300, 60)
		
		# Register event
		button.Click += self.ButtonClicked
		
	def ButtonClicked(self, sender, args):
		if sender.Click:
			# Handle non numeric cases
			try:
				self.value = self.textboxDiv.Text
				self.Close()
			except:
				self.Close()

# Path to save the pdfs by default
directory = "C:\Users\Snoopy\Desktop"

# Function to create Windows folder browser
def windBrowser():
    # Create folder browser window 
    dialog = FolderBrowserDialog()
    # Record for user action and store selected path
    if (dialog.ShowDialog() == DialogResult.OK):
        return dialog.SelectedPath

# Call windBrowser to select folder with backup files and store path to var
finalDirectory = windBrowser()

# Call the CreateWindow class and create the input for Revision Date
formRevision = CreateWindow("Revision Date on Sheets to Print", "Input Revision Date")
Application.Run(formRevision)

# Assign the input to variable
revDate = formRevision.value

# Store current document to variable
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

# Collects all sheets in current document
sheetsCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets)

# Variable to store sheets with revisions
sheets = []

# Get curent revision on sheets and collect sheets
for s in sheetsCollector:
	if s.GetCurrentRevision() != ElementId.InvalidElementId and doc.GetElement(s.GetCurrentRevision()).RevisionDate == revDate:
		rev = doc.GetElement(s.GetCurrentRevision())
		sheets.append(s)

# Retrieve sheets number, name and revision
outName = []
finalName = []
for s in sheets:
	number = s.SheetNumber
	name = s.Name
	revision = s.GetRevisionNumberOnSheet(doc.GetElement(s.GetCurrentRevision()).Id)
	pdfName = directory + "\\" + number + " - " + name + "[" + revision + "]" + ".pdf"
	finalPdfName = finalDirectory + "\\" + number + " - " + name + "[" + revision + "]" + ".pdf"
	outName.append(pdfName)
	finalName.append(finalPdfName)

# Check if there are files with same name and clean them
for file in outName:
	if os.path.exists(file):
		os.remove(file)

# Collect all print settings from document
printSettingCollector = FilteredElementCollector(doc).OfClass(PrintSetting)

# Function to pick printSetting by Name
def pickPrintSetting(name):
	for p in printSettingCollector:
		if p.Name == name:
			return p

# Function to print
def printSheet(sheet, printerName, combined, filePath, printSettingName):

	# Set print range
	printManager = doc.PrintManager
	printManager.PrintRange = printManager.PrintRange.Select
	printManager.Apply()

	# Define current view set as current
	viewSet = ViewSet()
	viewSet.Insert(sheet)
	viewSheetSetting = printManager.ViewSheetSetting
	viewSheetSetting.CurrentViewSheetSet.Views = viewSet
	viewSheetSetting.SaveAs("Current Print")

	# Set printer
	printManager.SelectNewPrintDriver(printerName)
	printManager.Apply()

	# Print to file
	printManager.CombinedFile = combined
	printManager.Apply()
	printManager.PrintToFile = True
	printManager.Apply()

	# Set destination filepath
	printManager.PrintToFileName = filePath
	printManager.Apply()

	# Set print setting
	printSetup = printManager.PrintSetup
	printSetup.CurrentPrintSetting = pickPrintSetting(printSettingName)
	printManager.Apply()

	# Submit to printer
	printManager.SubmitPrint()

	# Delete Current viewSheetSettings to allow new setting to be stored
	viewSheetSetting.Delete()

# Create a individual transaction
t = Transaction(doc, "Batch Print")
# Start transaction
t.Start()

# Print sheets
printedSheets = []
failedSheets = []
for sheet, fileName in zip(sheets, outName):
	try:
		printSheet(sheet, "PDF24", True, fileName, "A3")
		printedSheets.append(sheet.SheetNumber)
	except:
		failedSheets.append(fileName)

# Commit transaction
t.Commit()

# Function to Move Files
def moveFiles(origin, destination):
	for fileName, finalDestination in zip(outName, finalName):
		shutil.move(fileName, finalDestination)

# Set timer to call function and Move files to final destination
timeToPrint = 4
sleep(len(outName) * timeToPrint)
moveFiles(outName, finalName)

# Function to display result to user
def printMessage(resultList, message, messageWarning):
    if len(resultList) != 0:
        print(message)
        print("\n".join(resultList))
    else:
        print(messageWarning)

# Print message
printMessage(printedSheets, "The following sheets have been printed:", "No file has been printed.") 

        # --------------------------------------

def pick_elements_by_rectangle():
    # Seleccionar elementos en un rectangulo
    uidoc = __revit__.ActiveUIDocument
    Seleccion = uidoc.Selection.PickElementsByRectangle()
    return Seleccion

def get_parameter_values(elements):
    Parametros_ValorElectricoes = []
    for element in elements:
        for parameter in element.Parameters:
            parameter_value = element.LookupParameter(parameter.Definition.Name)
            if parameter_value is not None and parameter_value.HasValue:
                Parametros_ValorElectricoes.append(parameter_value.AsDouble())
    return Parametros_ValorElectricoes

def main():
    Seleccion = pick_elements_by_rectangle()
    print("Elementos seleccionados:")
    for element in Seleccion:
        print(element)
    
    Parametros_ValorElectricoes = get_parameter_values(Seleccion)
    print("ValorElectricoes de los parametros:")
    print(Parametros_ValorElectricoes)

if __name__ == "__main__":
    main()

    # ---------------------------------- 

def Seleccionar_Elementos():
    Referencias_elementos = uidoc.Selection.PickObjects(ObjectType.Element)
    Elementos_Seleccionados = []
    for i in Referencias_elementos:
        elemento = doc.GetElement(i)
        Elementos_Seleccionados.append(elemento)
    return Elementos_Seleccionados

        ###################################
        # COMPILACION DE FUNCIONES UTILES #
        ###################################

# Funcion para obtener elementos seleccionados
def get_selected_elements():
    selection = uidoc.Selection
    return selection

# Funcion para obtener IDs de elementos seleccionados
def get_selected_element_ids():
    element_ids = [x for x in uidoc.Selection.GetElementIds()]
    return element_ids

# Funcion para seleccionar elementos mediante un rectangulo
def select_elements_by_rectangle():
    selected_elements = uidoc.Selection.PickElementsByRectangle()
    return selected_elements

# Funcion para seleccionar elementos mediante clic
def select_elements_by_pick():
    selected_elements = uidoc.Selection.PickObjects(ObjectType.Element, "Seleccionar elementos")
    elements = [doc.GetElement(x) for x in selected_elements]
    return elements

# Funcion para obtener nombres de parametros de elementos
def get_parameter_names(elements):
    parameter_names = [x.Definition.Name for element in elements for x in element.Parameters]
    return parameter_names

# Funcion para obtener nombres de parametros de elementos seleccionados
def get_selected_parameter_names():
    parameter_names = [x.Definition.Name for element in uidoc.Selection.PickElementsByRectangle() for x in element.Parameters]
    return parameter_names

# Funcion para obtener nombres de Parameters Definition de elementos
def get_parameters_definition_names(elements):
    parameter_names = []
    for element in elements:
        for x in element.Parameters:
            parameter_names.append(x.Definition.Name)
    return parameter_names

# Funcion para obtener informacion detallada de elementos
def get_element_info(elements):
    info = []
    for element in elements:
        element_info = []
        for parameter in element.Parameters:
            definition_name =   parameter.Definition.Name
            has_value =         parameter.HasValue
            parameter_id =      parameter.Id
            storage_type =      parameter.StorageType
            user_modifiable =   parameter.UserModifiable
            param_info = f"Definition_Name = {definition_name}; HasValue = {has_value}; Id = {parameter_id}; StorageType = {storage_type}; UserModifiable = {user_modifiable};"
            element_info.append(param_info)
        info.append(element_info)
    return info

# Funcion para imprimir informacion detallada de un parametro
def print_parameter_info(parameter):
    definition_name =   parameter.Definition.Name
    has_value =         parameter.HasValue
    parameter_id =      parameter.Id
    storage_type =      parameter.StorageType
    user_modifiable =   parameter.UserModifiable
    print(f"Definition Name: {definition_name}")
    print(f"Has Value: {has_value}")
    print(f"Parameter ID: {parameter_id}")
    print(f"Storage Type: {storage_type}")
    print(f"User Modifiable: {user_modifiable}")
    print("-" * 20)

# Funcion principal
def main():
    selected_elements = [doc.GetElement(x) for x in uidoc.Selection.PickObjects(ObjectType.Element, "Seleccionar elementos")]
    print("-" * 20)
    for element in selected_elements:
        print("Element:")
        print(element)
        print("Name:")
        print(element.Name)
        for parameter in element.Parameters:
            print_parameter_info(parameter)

if __name__ == "__main__":
    main()

def Devolver_LookupParameters(elemento):
    Parametros_ValorElectricoes = []
    for i in elemento:
        for x in i.Parameters:
            Parametros_ValorElectricoes.append(i.LookupParameter(x.Definition.Name).AsDouble())
    return Parametros_ValorElectricoes

# Funcion para obtener ValorElectricoes de parametros usando LookupParameter
def get_lookup_parameter_values(elements):
    parameter_values = []
    for element in elements:
        for parameter in element.Parameters:
            param_name = parameter.Definition.Name
            lookup_param = element.LookupParameter(param_name)
            if lookup_param is not None:
                if parameter.StorageType == StorageType.Double:
                    parameter_values.append(lookup_param.AsDouble())
                elif parameter.StorageType == StorageType.String:
                    parameter_values.append(lookup_param.AsString())
                elif parameter.StorageType == StorageType.Integer:
                    parameter_values.append(lookup_param.AsInteger())
    return parameter_values

# Funcion para obtener informacion detallada de elementos usando LookupParameter
def get_lookup_parameter_info(elements):
    info = []
    for element in elements:
        element_info = []
        for parameter in element.Parameters:
            param_name = parameter.Definition.Name
            lookup_param = element.LookupParameter(param_name)
            if lookup_param is not None:
                definition_name = parameter.Definition.Name
                has_value = parameter.HasValue
                parameter_id = parameter.Id
                storage_type = parameter.StorageType
                user_modifiable = parameter.UserModifiable
                param_info = f"Definition_Name = {definition_name}; HasValue = {has_value}; Id = {parameter_id}; StorageType = {storage_type}; UserModifiable = {user_modifiable};"
                element_info.append(param_info)
        info.append(element_info)
    return info

        # --------------------------------------

def obtener_elementos_seleccionados(uidoc):
    Elementos_seleccionados = uidoc.Selection.PickObjects(ObjectType.Element)
    return Elementos_seleccionados

def obtener_ValorElectricoes_parametros(elemento):
    parametros_ValorElectricoes = []
    for parametro in elemento.Parameters:
        definicion = parametro.Definition
        tipo_almacenamiento = parametro.StorageType

        print("------ Elemento ------")
        print(" - Definition.Name:", definicion.Name)
        print(" - StorageType:", tipo_almacenamiento)
        print(" - Definition.BuiltInParameter:", definicion.BuiltInParameter)

        ValorElectrico = obtener_ValorElectrico_parametro(elemento, definicion, tipo_almacenamiento)
        parametros_ValorElectricoes.append((definicion.Name, ValorElectrico))

    return parametros_ValorElectricoes

def obtener_ValorElectrico_parametro(elemento, definicion, tipo_almacenamiento):
    if tipo_almacenamiento == StorageType.Double:
        return elemento.LookupParameter(definicion.Name).AsDouble()
    elif tipo_almacenamiento == StorageType.String:
        return elemento.LookupParameter(definicion.Name).AsString()
    elif tipo_almacenamiento == StorageType.Integer:
        return elemento.LookupParameter(definicion.Name).AsInteger()
    else:
        print("Tipo de parametro no admitido")
        return None

def imprimir_informacion_elemento(elemento):
    print("Elemento seleccionado:", elemento.Name, elemento.Category.Name)
    print("Categoria del elemento:", elemento.Category.Name)
    print("Id de la categoria del elemento:", elemento.Category.Id)
    print("BuiltInCategory:", elemento.Category.BuiltInCategory)

if __name__ == "__main__":
    uidoc = __revit__.ActiveUIDocument
    doc = __revit__.ActiveUIDocument.Document
    elementos_seleccionados = obtener_elementos_seleccionados(uidoc)

    for elemento_id in elementos_seleccionados:
        elemento = doc.GetElement(elemento_id)
        informacion_elementos = imprimir_informacion_elemento(elemento)
        parametros_ValorElectricoes = obtener_ValorElectricoes_parametros(elemento)

def Seleccionar_y_obtener_ParametersDefinitionName():
    Elementos_Seleccionados = uidoc.Selection.PickObjects(ObjectType.Element, "Seleccionar elementos")
    Parametros_Nombres = []
    for obj in Elementos_Seleccionados:
        element = doc.GetElement(obj)
        for parameter in element.Parameters:
            Parametros_Nombres.append(parameter.Definition.Name)
    return Parametros_Nombres

def Seleccionar_y_obtener_LookupParameters():
    elementos_seleccionados = uidoc.Selection.PickObjects(ObjectType.Element)
    lookup_parameters = []

    for elemento_seleccionado in elementos_seleccionados:
        elemento = doc.GetElement(elemento_seleccionado)

        for parametro in elemento.Parameters:
            nombre_parametro = parametro.Definition.Name
            lookup_parametro = elemento.LookupParameter(nombre_parametro)
            lookup_parameters.append(lookup_parametro)
    return lookup_parameters

def Obtener_LookupParameters_ValorElectricoes(elemento):
    Parametros_ValorElectricoes = []
    for x in elemento.Parameters:
        if x.StorageType == StorageType.Double:
            print(" - LookupParameter(x.Definition.Name).AsDouble()")
            print(elemento.LookupParameter(x.Definition.Name).AsDouble())
        elif x.StorageType == StorageType.String:
            print(" - LookupParameter(x.Definition.Name).AsString()")
            print(elemento.LookupParameter(x.Definition.Name).AsString())
        elif x.StorageType == StorageType.Integer:
            print(" - LookupParameter(x.Definition.Name).AsInteger()")
            print(elemento.LookupParameter(x.Definition.Name).AsInteger())
        else:
            print("Tipo de parametro no admitido")
    return Parametros_ValorElectricoes

def Seleccionar_y_obtener_LookupParameters_ValorElectricoes():
    Parametros_ValorElectricoes = []
    for i in [doc.GetElement(x) for x in uidoc.Selection.PickObjects(ObjectType.Element)]:
        for x in i.Parameters:
            if x.StorageType == StorageType.Double:
                print(" - LookupParameter(x.Definition.Name).AsDouble()")
                print(i.LookupParameter(x.Definition.Name).AsDouble())
            elif x.StorageType == StorageType.String:
                print(" - LookupParameter(x.Definition.Name).AsString()")
                print(i.LookupParameter(x.Definition.Name).AsString())
            elif x.StorageType == StorageType.Integer:
                print(" - LookupParameter(x.Definition.Name).AsInteger()")
                print(i.LookupParameter(x.Definition.Name).AsInteger())
            else:
                print("Tipo de parametro no admitido")
    return Parametros_ValorElectricoes

# Funcion para obtener nombres de parametros usando LookupParameter
def get_lookup_parameter_names(elements):
    parameter_names = []
    for element in elements:
        for parameter in element.Parameters:
            param_name = parameter.Definition.Name
            lookup_param = element.LookupParameter(param_name)
            if lookup_param is not None:
                parameter_names.append(param_name)
    return parameter_names

# Funcion para obtener categorias en el modelo
def get_categories():
    categories = [i.Name for i in doc.Settings.Categories]
    categories.sort()
    return categories

# Funcion para borrar elementos
def delete_elements(element):
    transaction = Transaction(doc, "Borrar Elemento")
    transaction.Start()
    doc.Delete(element.GetTypeId())
    transaction.Commit() 

# Funcion para obtener instancias de una categoria
def get_instances(ost_category):
    category = BuiltInCategory[ost_category]
    instance_collector = FilteredElementCollector(doc).OfCategory(category).WhereElementIsNotElementType().ToElements()
    return instance_collector

# Funcion para obtener IDs de instancias de una categoria
def get_instance_ids(ost_category):
    category = BuiltInCategory[ost_category]
    instance_ids = FilteredElementCollector(doc).OfCategory(category).WhereElementIsNotElementType().ToElementIds()
    return instance_ids

# Funcion para obtener familias de una categoria
def get_families(ost_category):
    category = BuiltInCategory[ost_category]
    family_collector = FilteredElementCollector(doc).OfCategory(category).WhereElementIsElementType().ToElements()
    return family_collector

# Funcion para obtener IDs de familias de una categoria
def get_family_ids(ost_category):
    category = BuiltInCategory[ost_category]
    family_ids = FilteredElementCollector(doc).OfCategory(category).WhereElementIsElementType().ToElementIds()
    return family_ids

# Funcion para filtrar elementos por BuiltInCategory
def filter_by_category(ost_category):
    category = BuiltInCategory[ost_category]
    instance_ids = FilteredElementCollector(doc).OfCategory(category).WherePasses(ElementIsElementTypeFilter()).ToElementIds()
    return instance_ids

# Funcion para obtener IDs de instancias de una categoria
def get_instance_ids(ost_category):
    category = BuiltInCategory[ost_category]
    instance_ids = [i.Id.ToString() for i in FilteredElementCollector(doc).OfCategory(category).WhereElementIsElementType().ToElement()]
    return instance_ids

# Funcion para obtener tipos de instancias de una categoria
def get_instance_types(ost_category):
    category = BuiltInCategory[ost_category]
    instance_types = [i.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_NAME).AsString() for i in FilteredElementCollector(doc).OfCategory(category).WhereElementIsElementType().ToElement()]
    return instance_types

# Clase para filtrar la seleccion por multiples categorias
class MultipleCategorySelectionFilter(ISelectionFilter):
    def __init__(self, *categories):
        self.categories = categories

    def AllowElement(self, element):
        return element.Category.Name in self.categories

    def AllowReference(self, reference, point):
        return True

# Funcion para seleccionar elementos de multiples categorias
def select_elements_by_multiple_categories(*categories):
    filter = MultipleCategorySelectionFilter(*categories)
    selected_elements = uidoc.Selection.PickElementsByRectangle(filter)
    element_names = [element.Name for element in selected_elements]
    return element_names

categorias_a_seleccionar = ["Walls", "Doors"]
seleccion = Filtro_multi_categoria(*categorias_a_seleccionar)

# Funcion para crear una etiqueta
def create_label    (
                    form,
                    text="Texto de etiqueta",
                    location=Point(5, 10),
                    size=Size(100, 45),
                    bg_color=Color.White,
                    text_color=Color.Black,
                    font=Font("Arial", 10)
                    ):
    label = Label()
    label.Parent = form
    label.Text = text
    label.Location = location
    label.Size = size
    label.BackColor = bg_color
    label.ForeColor = text_color
    label.Font = font
    return label

        # Boton Automatico ----------------
    # Funcionalidad del boton

def Function_Click(sender, eventArgs):
    TaskDialog.Show("Elementos", "Operacion exitosa")   # Ventana de Revit API
    #MessageBox.Show("Elementos", "Operacion exitosa")  # Ventana de Windows Forms
    # Se puede elegir entre ambas opciones,

# Funcion para crear un boton
def create_button   (  
                    form,
                    text="Boton",
                    location=Point(150, 10),
                    size=Size(100, 30),
                    bg_color=Color.White,
                    text_color=Color.Black,
                    font=Font("Arial", 10)
                    ):
    button = Button()
    button.Parent = form
    button.Text = text
    button.Location = location
    button.Size = size
    button.BackColor = bg_color
    button.ForeColor = text_color
    button.Font = font
    button.Click += Function_Click  # Asociamos la funcion al evento Click del boton
    return button  # Devolvemos el boton para poder referenciarlo mas adelante

        # No tiene argumentos porque esta destinada a ser utilizada como un manejador de eventos para un boton en una interfaz de usuario
        # Cuando se utiliza como manejador de eventos, esta funcion se invocara automaticamente cuando se haga clic en el boton, sin necesidad de pasarle argumentos explicitos.

        # Cuadro de Texto Automatico ----------------
# Funcion para crear un cuadro de texto
def create_text_box (
                    form,
                    text="Texto sin modificar",
                    location=Point(5, 60),
                    size=Size(200, 20)
                    ):
    text_box = TextBox()
    text_box.Parent = form
    text_box.Text = text
    text_box.Location = location
    text_box.Size = size
    return text_box

"""
        # Funcion para manejar el evento de la casilla de verificacion
def FuncionCheckBox(sender, eventArgs):
    if checkBox.Checked:
        TaskDialog.Show("Check box tildada","---------")
    else:
        TaskDialog.Show("Check box destildada","---------")

# ------- Arroja error este metodo -----
"""

# Funcion para crear una casilla de verificacion
def create_check_box(
                    form,
                    text="Casilla",
                    checked=False,
                    location=Point(5, 90)
                    ):
    check_box = CheckBox()
    check_box.Parent = form
    check_box.Text = text
    check_box.Checked = checked
    check_box.Location = location
    #checkBox.CheckedChanged += FuncionCheckBox  # Asociamos la funcion al evento CheckedChanged
    return check_box  # Devolvemos la casilla de verificacion para poder referenciarla mas adelante

        # Combobox Automatico ----------------
# Funcion para crear un ComboBox
def create_combo_box(
                    form,
                    items=[],
                    selected_item="Texto sin editar",
                    location=Point(5, 120),
                    size=Size(200, 20)
                    ):
    combo_box = ComboBox()
    combo_box.Parent = form
    combo_box.Location = location
    combo_box.Size = size
    combo_box.DropDownStyle = ComboBoxStyle.DropDownList # Establece el estilo para que el usuario no pueda escribir
    combo_box.Items.AddRange(items) # Agrega los elementos al ComboBox
    combo_box.SelectedItem = selected_item # Establece la seleccion inicial
    return combo_box


        # Formulario Automatico ----------------
# Clase para un formulario personalizado
class CustomForm(Form):
    def __init__(self):
        self.Text = "Formulario"
        self.Size = Size(300, 300)
        self.CenterToScreen()
        self.label = create_label(self)
        self.button = create_button(self)
        self.text_box = create_text_box(self)
        self.check_box = create_check_box(self)
        self.combo_box = create_combo_box(self, items=["Opcion 1", "Opcion 2", "Opcion 3"], selected_item="Opcion 1")

# Crear una instancia del formulario personalizado
Formulario = CustomForm()

# Ejecutar la aplicacion
Application.EnableVisualStyles()
Application.Run(Formulario)
#Formulario.ShowDialog() # Este es un sustituto del metodo de arriba

    # ------------------------------ ACOMODAR ------------------------------

def ButtonClickCreate(self, sender, args):
    titleBlockCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_TitleBlocks)
    titleBlockId = titleBlockCollector.FirstElementId()
    if sender.Click:
        self.sheetNumber = self.textBox1.Text
        self.sheetName = self.textBox2.Text
        if self.sheetNumber == "" or self.sheetName == "":
            tD = TaskDialog.Show("Values is missing", "Sheet Number or Sheet Name is missing")
        else:
            tSheet = Transaction(doc, "Create Sheets")
            tSheet.Start()
            
            newSheet = ViewSheet.Create(doc, titleBlockId)
            newSheet.SheetNumber = self.sheetNumber
            newSheet.Name = self.sheetName
            
            tSheet.Commit()
            
        self.DialogResult = DialogResult.OK
        self.Close()

# Definimos la funcionalidad de los botones
def ButtonClickDelete(self, sender, args):
    categories = []
    for x in doc.Settings.Categories:
        categories.append(x)
    selectedCategory = self.comboBox1.SelectedItem
    categoryId = None

    for cat in categories:
        if cat.Name == selectedCategory:
            categoryId = cat.Id

    # Crear un colector de elementos de la categoria seleccionada
    collector = FilteredElementCollector(doc).OfCategoryId(categoryId).WhereElementIsNotElementType()

    t = Transaction(doc, "Delete Elements")
    t.Start()
    for e in collector.ToElementIds():
        doc.Delete(e)
    t.Commit()

    tD = TaskDialog.Show("Ok", "Successful Operation")
    self.DialogResult = DialogResult.OK
    self.Close()

def ButtonClickCancel(self, sender, args):
    self.DialogResult = DialogResult.Cancel
    self.Close()

def Crear_pisos(Poligonos, Tipo_de_piso=None, Nivel=None):
    if Tipo_de_piso is None:
        Tipo_de_piso = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsElementType().ToElements()[0]
    if Nivel is None:
        Nivel = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsElementType().ToElements()[0]

    Pisos = []
    contorno = CurveArray()
    for poligono in Poligonos:
        contorno.Append(poligono.ToRevitType())
    
    Pisos.append(Floor.Create(doc, contorno, Tipo_de_piso.Id, Nivel.Id))
    return Pisos

def pick_elements_by_rectangle():
    # Seleccionar elementos en un rectangulo
    uidoc = __revit__.ActiveUIDocument
    Seleccion = uidoc.Selection.PickElementsByRectangle()
    return Seleccion

def get_parameter_values(elements):
    Parametros_ValorElectricoes = []
    for element in elements:
        for parameter in element.Parameters:
            parameter_value = element.LookupParameter(parameter.Definition.Name)
            if parameter_value is not None and parameter_value.HasValue:
                Parametros_ValorElectricoes.append(parameter_value.AsDouble())
    return Parametros_ValorElectricoes

def main():
    Seleccion = pick_elements_by_rectangle()
    print("Elementos seleccionados:")
    for element in Seleccion:
        print(element)
    
    Parametros_ValorElectricoes = get_parameter_values(Seleccion)
    print("ValorElectricoes de los parametros:")
    print(Parametros_ValorElectricoes)

if __name__ == "__main__":
    main()

    # ---------------------------------- 

def Seleccionar_Elementos():
    Referencias_elementos = uidoc.Selection.PickObjects(ObjectType.Element)
    Elementos_Seleccionados = []
    for i in Referencias_elementos:
        elemento = doc.GetElement(i)
        Elementos_Seleccionados.append(elemento)
    return Elementos_Seleccionados


    # ---------------------------------- ACOMODAR

collector = FilteredElementCollector(doc).OfClass(Viewport).ToElements()

scope_box_name = []
for sc in collector:
    scope_box_parameter = sc.get_Parameter(BuiltInParameter.VIEWER_VOLUME_OF_INTEREST_CROP)
    if scope_box_parameter:
        name = scope_box_parameter.AsValueString()
        scope_box_name.append(name)
    else:
        scope_box_name.append("N/A")
mensaje = "Lista de nombres de scope box \n"
for name in scope_box_name:
    mensaje += " - " + name + "\n"
TascDialog.Show("RESULTADO", mensaje)



    # ---------------------------------- BUSCAR CONTENIDO DE LA FUNCION "ElementId()"

# Public method	ElementId(Int32)	
# Create an ElementId handle with the given integer id.
# Public method	ElementId(BuiltInCategory)	
# Create an ElementId handle with the given BuiltInCategory id.
# Public method	ElementId(BuiltInParameter)	
# Create an ElementId handle with the given BuiltInParameter id.


    # 13 - Instalacion y utilizacion de RevitPythonShell


    # ...........................





    # 14 - Utilizacion de pyRevit

        # Instalacion

    #

        # Uso de pyRevit

    # Crear una carpeta "MyExtensions"
    # Dentro otra carpeta " .extensions"
    # Dentro otra carpeta " .tab", esta va a ser el menu de herramientas
    # Dentro crear otra carpeta " .panel"





            ### COSAS QUE FALTAN
            
    # Funcion para pbtener el BuiltInCategory desde una categoria



"""
        ESTO ES PARA HABILITAR LA SELECCION MULTIPLE EN EL LISTBOX

// Establecer la propiedad SelectionMode en MultiSimple o MultiExtended
listBox1.SelectionMode = SelectionMode.MultiSimple;

// Anadir elementos al ListBox
listBox1.Items.Add("Elemento 1");
listBox1.Items.Add("Elemento 2");
listBox1.Items.Add("Elemento 3");


"""



        #################################################
        ## ORDENAR - UTIL
        #################################################



Diccionario_Categorias = {"Walls": BuiltInCategory.OST_Walls, "Floors":BuiltInCategory.OST_Floors, "Ceilings":BuiltInCategory.OST_Ceilings}
Lista_de_categorias_Seleccionables = list(Diccionario_Categorias.keys())

def Obtener_todos_las_Categorias():
    try:
        categories = [i.Name for i in doc.Settings.Categories]
        categories.sort()
        return categories
    except:
        MessageBox.Show("error al obtener todas las categorias", "button5_Click")

def Obtener_todos_las_BuiltInCategory():
    # Obtener todos los BuiltInCategories en el documento
    BuiltInCategories = []
    Category = System.Enum.GetValues(BuiltInCategory)
    for i in Category:
        BuiltInCategories.append(i)
    BuiltInCategories.sort()
    return BuiltInCategories

def Funcion_Categoria_seleccionada(Categoria_seleccionada):
        collector = FilteredElementCollector(doc).OfClass(Categoria_seleccionada).WhereElementIsNotElementType()
        return collector

    # No funciona
def Obtener_BuiltInCategory_desde_Category(Categoria):

    collector = FilteredElementCollector(doc).OfCategory(Categoria_seleccionada).WhereElementIsElementType().ToString()

    BuiltInCategory = []
    for i in collector:
        if Categoria.Name in i.Name:
            BuiltInCategory.append(i)
    return BuiltInCategory

def get_instances(ost_category):
    instance_collector = FilteredElementCollector(doc).OfCategory(ost_category).WhereElementIsNotElementType().ToElements()
    instancias = []
    for i in instance_collector:
        instancias.append(i)
    return instancias


Categorias = ["Walls", "Floors", "Doors"]
Minimo = 1
Maximo = 8

    # Variables a rellenar por el filtro

Parametros = []
ValorElectricoes_Parametros = []
Parametros_Numerados = []
Parametros_Textuales = []
Parametros_Decimales = []


class FiltroDeSeleccionDeCategoriaMultiple(ISelectionFilter):
    def __init__(self, *categorias):
        self.categorias = categorias

    def AllowElement(self, element):
        if element.Category.Name in self.categorias:
            if element.Category.Name == "Walls":
                altura_elemento = element.get_Parameter(BuiltInParameter.WALL_USER_HEIGHT_PARAM).AsDouble()
                altura_en_metros = UnitUtils.ConvertFromInternalUnits(altura_elemento, UnitTypeId.Meters)
                return Minimo <= altura_en_metros <= Maximo
            return True
        return False

    def AllowReference(self, refer, point):
        return True


seleccionados = uidoc.Selection.PickObjects(ObjectType.Element, FiltroDeSeleccionDeCategoriaMultiple(*Categorias))



for x in seleccionados:
    elemento = doc.GetElement(x)
    for j in elemento.Parameters:
        Parametros.append(j.Definition.Name)
        Parametros.append(j.HasValue)
        Parametros.append(j.Id)
        Parametros.append(j.StorageType)
        Parametros.append(j.UserModifiable)

        if j.StorageType == StorageType.Double:
            ValorElectricoes_Parametros.append(  [
                                        j.Definition.Name,
                                        "Numero fraccionario",
                                        elemento.LookupParameter(j.Definition.Name).AsDouble()
                                        ])
            Parametros_Decimales.append([
                                        j.Definition.Name,
                                        elemento.LookupParameter(j.Definition.Name).AsDouble()
                                        ])
            
        elif j.StorageType == StorageType.String:
            ValorElectricoes_Parametros.append(  [
                                        j.Definition.Name,
                                        "Texto",
                                        elemento.LookupParameter(j.Definition.Name).AsString()
                                        ])
            Parametros_Textuales.append([
                                        j.Definition.Name,
                                        elemento.LookupParameter(j.Definition.Name).AsString()
                                        ])
            
        elif j.StorageType == StorageType.Integer:
            ValorElectricoes_Parametros.append(  [
                                        j.Definition.Name,
                                        "Numero redondo",
                                        elemento.LookupParameter(j.Definition.Name).AsInteger()
                                        ])
            Parametros_Numerados.append([
                                        j.Definition.Name,
                                        elemento.LookupParameter(j.Definition.Name).AsInteger()])
            
        else:
            ValorElectricoes_Parametros.append(  [
                                        j.Definition.Name,
                                        "Tipo de parametro no admitido"
                                        ])

"""
for a in ValorElectricoes_Parametros:
    print(" ---- ")
    for b in a:
        print(b)
"""


def Obtener_Category_desde_String(String):
    categories = [i for i in doc.Settings.Categories]
    category = []
    for categoria in categories:
        if categoria.Name == String:
            category.append(categoria)
    return category[0]

        ############################################################################

    # Quiero que esto permita seleccionar la forma en la que voy a trasladar y copiar los elementos seleccionados

def pick_point(message):
    reference = uidoc.Selection.PickObject(ObjectType.PointOnElement, message)
    return reference.GlobalPoint

def create_distance_xyz(point1, point2):
    return XYZ(point1.X - point2.X, point1.Y - point2.Y, point1.Z - point2.Z)

def Crear_distancia_XYZ():
    try:
        point1 = pick_point("Select the first point in the view")
        point2 = pick_point("Select the second point in the view")

        with Transaction(doc, "Distances XYZ") as transaction:
            transaction.Start()
            distance_xyz = create_distance_xyz(point1, point2)
            transaction.Commit()

    except Exception as ex:
        MessageBox.Show(ex, "button5_Click")

        ############################################################################

"""

def Crear_distancia_XYZ():
        try:
            Clic_Referencia_1 = uidoc.Selection.PickObject(ObjectType.PointOnElement, "Selecciona un punto en la vista")
            pointXYZ_1 = Clic_Referencia_1.GlobalPoint

            Clic_Referencia_2 = uidoc.Selection.PickObject(ObjectType.PointOnElement, "Selecciona un punto en la vista")
            pointXYZ_2 = Clic_Referencia_2.GlobalPoint

            transaction_Obtener_Distancias_XYZ = Transaction(doc, "Distancias XYZ")
            transaction_Obtener_Distancias_XYZ.Start()

            Distancia_XYZ_1 = XYZ((pointXYZ_1.X)-(pointXYZ_2.X), (pointXYZ_1.Y)-(pointXYZ_2.Y), (pointXYZ_1.Z)-(pointXYZ_2.Z))

            FamilyInstance pointInstance = doc.Create.NewFamilyInstance(newPoint, new FilteredElementCollector(doc).OfClass(typeof(FamilySymbol)).FirstElementId, StructuralType.NonStructural);
            
            transaction_Obtener_Distancias_XYZ.Commit()

            print(Clic_Referencia_1, Clic_Referencia_2, pointXYZ_1, pointXYZ_2, Distancia_XYZ_1)

        except:
            MessageBox.Show("Error al crear punto XYZ", "button5_Click")

"""

def delete_elements(element):
    Transaccion_Borrar_Elemento_Seleccionado = Transaction(doc, "Borrar elemento seleccionado")
    Transaccion_Borrar_Elemento_Seleccionado.Start()
    doc.Delete(element.Id)
    Transaccion_Borrar_Elemento_Seleccionado.Commit()


def copiar_con_punto_base(doc, elemento, punto_base):
    # Inicia una transaccion
    transaction_copiar_con_punto_base = Transaction(doc, "Copiar con Punto Base")
    transaction_copiar_con_punto_base.Start()
    ElementTransformUtils.CopyElement(doc, elemento.Id, punto_base)
    transaction_copiar_con_punto_base.Commit()

def mover_con_punto_base(doc, elemento, punto_base):
    Transaccion_mover_con_punto_base = Transaction(doc, "Trasladar elemento seleccionado")
    Transaccion_mover_con_punto_base.Start()
    ElementTransformUtils.MoveElement(doc, elemento.Id, punto_base)
    Transaccion_mover_con_punto_base.Commit()

    # Filtro con tamices

class FiltroDeSeleccionDeCategoriaMultiple(ISelectionFilter):
    def __init__(self, *categorias):
        self.categorias = categorias

    def AllowElement(self, element):
        if element.Category.Name in self.categorias:
            for j in element.Parameters:
                if j.Definition.Name == listBox1.SelectedItem.ToString():
                    Medida_del_elemento = element.LookupParameter(j.Definition.Name).AsDouble()
                    Medida_del_elemento_en_metros = UnitUtils.ConvertFromInternalUnits(Medida_del_elemento, UnitTypeId.Meters)
                    if Minimo <= Medida_del_elemento_en_metros <= Maximo:
                        return True 
        return False
    
    def AllowReference(self, refer, point):
        return True

        ######################################
        # FUNCIONALIDADES DE ELEMENTOS DE WF #
        ######################################

def button1_Click (sender, args):
        # Seleccionar elementos por categoria y filtro por tamanos numericos
    try:
        Instancia_del_colector = uidoc.Selection.PickObjects(ObjectType.Element, FiltroDeSeleccionDeCategoriaMultiple(Categoria_Seleccionada_Desde_Diccionario))
        global Elementos_seleccionados_filtrados
        global Elementos_seleccionados_filtrados_Id
        for elem in Instancia_del_colector:
            elemento = doc.GetElement(elem)
            Elementos_seleccionados_filtrados.append(elemento)
        for a in Elementos_seleccionados_filtrados:
            listBox4.Items.Add(a.Name)
            Elementos_seleccionados_filtrados_Id.append(a.Id)
        Formulario_entrega_python_III.BringToFront()
    except:
        MessageBox.Show("Error al seleccionar", "button1_Click")

def button1_Click_1 (sender, args):
        # Borrar elementos seleccionados
    try:
        for elem in Elementos_seleccionados_filtrados:
            delete_elements(elem)
    except:
        MessageBox.Show("Hubo algun error", "button1_Click")

def button2_Click (sender, args):
        # Duplicar elementos seleccionados
    punto_base = XYZ(100, 100, 0)
    try:
        for elemento in Elementos_seleccionados_filtrados:
            copiar_con_punto_base(doc, elemento, punto_base)
    except Exception as e:
        MessageBox.Show("Error al copiar", "button2_Click")

def button3_Click(sender, args):
        # Trasladar elementos seleccionados
    punto_base = XYZ(100, 100, 0)
    try:
        for elemento in Elementos_seleccionados_filtrados:
            mover_con_punto_base(doc, elemento, punto_base)
    except Exception as e:
        MessageBox.Show("Error al trasladar", "button3_Click")

def button4_Click(sender, args):
    # Ocultar elementos seleccionados
    try:
        vista_Actual = doc.ActiveView
        ICollection_1 = List[ElementId]()
        for Id in Elementos_seleccionados_filtrados_Id:
            ICollection_1.Add(Id)
        Transaccion_Ocultar_Elemento_Seleccionado = Transaction(doc, "Ocultar elemento seleccionado")
        Transaccion_Ocultar_Elemento_Seleccionado.Start()
        vista_Actual.HideElements(ICollection_1)
        Transaccion_Ocultar_Elemento_Seleccionado.Commit()

    except Exception as e:
        MessageBox.Show("Error al ocultar", "button4_Click")

def button5_Click (sender, args):
        # Cerrar Formulario
    Formulario_entrega_python_III.Close()

def textBox2_TextChanged (sender, e):
        # ValorElectrico minimo para filtrar
    global Minimo
    try:
        nuevo_ValorElectrico = int(textBox2.Text)
        Minimo = nuevo_ValorElectrico
    except ValueError:
        MessageBox.Show("Introduce un numero valido", "Error")

def textBox3_TextChanged(sender, e):
        # ValorElectrico maximo para filtrar
    global Maximo
    try:
        nuevo_ValorElectrico = int(textBox3.Text)
        Maximo = nuevo_ValorElectrico
    except ValueError:
        MessageBox.Show("Introduce un numero valido", "Error")

def comboBox1_SelectedIndexChanged (sender, e):
        # Filtrar por
    MessageBox.Show("ComboBox1 cambiado", "comboBox1_SelectedIndexChanged")

def ListBox3_SelectedIndexChanged (sender, e):
        # Filtrar por
    Categoria_seleccionada = []

    if  listBox3.SelectedItem != None:
        Categoria_seleccionada = Obtener_Category_desde_String(listBox3.SelectedItem)

        Categorias = Categoria_seleccionada.Name

        global Categoria_Seleccionada_Desde_Diccionario
        Categoria_Seleccionada_Desde_Diccionario = Categorias

        Instancia_del_colector_para_obtener_categorias = FilteredElementCollector(doc).OfCategory(Diccionario_Categorias[Categoria_Seleccionada_Desde_Diccionario]).WhereElementIsNotElementType().ToElements()

        Primera_instancia = Instancia_del_colector_para_obtener_categorias[0]
        Parametros_decimales_elemento_analizado = []

        for j in Primera_instancia.Parameters:

            if j.StorageType == StorageType.Double:
                _Nombre = Primera_instancia.Name
                _Parametro = j.Definition.Name
                _ValorElectrico_Numerico = UnitUtils.ConvertFromInternalUnits(Primera_instancia.LookupParameter(j.Definition.Name).AsDouble(), UnitTypeId.Meters) 
                Parametros_decimales_elemento_analizado.append( [
                                                                _Nombre,
                                                                _Parametro,
                                                                _ValorElectrico_Numerico
                                                                ])

        comboBox1.Items.Clear()
        for a in Parametros_decimales_elemento_analizado:
            comboBox1.Items.Add(a[1])

        listBox1.Items.Clear()
        for a in Parametros_decimales_elemento_analizado:
            listBox1.Items.Add(a[1])

        listBox2.Items.Clear()
        for a in Instancia_del_colector_para_obtener_categorias:
            listBox2.Items.Add(a.Name)

    else:
        MessageBox.Show("Error al buscar las propiedades de la categoria", "comboBox1_SelectedIndexChanged")


for a in Parametros_Numerados:
    print(" ---- ")
    for b in a:
        print(b)









# ------------------------

Instancia_del_colector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType()

Lista_Muros = []
Nombres_Muros = []

for i in Instancia_del_colector:
    Lista_Muros.append(i)
    Nombres_Muros.append(i.Name)

Primer_Muro = Lista_Muros[0]
Parametro_Muro = []
Parametros_Decimales_Muro = []


for j in Primer_Muro.Parameters:
    Parametro_Muro.append(j.Definition.Name)
    Parametro_Muro.append(j.HasValue)
    Parametro_Muro.append(j.Id)
    Parametro_Muro.append(j.StorageType)
    Parametro_Muro.append(j.UserModifiable)
    if j.StorageType == StorageType.Double:
        _Nombre = Primer_Muro.Name
        _Parametro = j.Definition.Name
        _ValorElectrico_Numerico = UnitUtils.ConvertFromInternalUnits(Primer_Muro.LookupParameter(j.Definition.Name).AsDouble(), UnitTypeId.Meters) 
        Parametros_Decimales_Muro.append(   [
                                            _Nombre,
                                            _Parametro,
                                            _ValorElectrico_Numerico
                                            ])


for a in Parametros_Decimales_Muro:
    print(" -------- ")
    print(a)



