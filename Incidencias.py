from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class IncidenciasV(object):

	def __init__(self):
		pass
	def Incidencias(self,frame,width,height):
		self.left_Frame=Frame(frame,width=int(width*0.13),height=int(height*0.80),bg='red')
		self.left_Frame.pack(side='left')

		self.main_Frame=Frame(frame,width=int(width*0.85),height=int(height*0.80),bg='green')
		self.main_Frame.pack(side='right',padx=int(width*0.01))

		self.Menu_Button()

	def Menu_Button(self):
		self.btn_Incidencias=ttk.Button(self.left_Frame,text='Insertar')
		self.btn_Incidencias.place(x=5,y=20)		

		self.btn_Reporte=ttk.Button(self.left_Frame,text='Reporte Incidencias')
		self.btn_Reporte.place(x=5,y=80)
	def Animation(self,event,btn):
		pass
		#btn.configure(relief='raised')
		