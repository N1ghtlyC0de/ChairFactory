from businessLogic.controller import Controller
from businessLogic.catalogoSillas import CatalogoSillas
from userInterface.ui import UI

catalogo = CatalogoSillas('.//resources//sillas.txt')
catalogo.crearSillas()
ui = UI()
ctrl = Controller(ui, catalogo)
ctrl.loop()
