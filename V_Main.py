from tkinter import *
import datetime
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from ttkthemes import ThemedTk
import GUI_User
import Consulta_Galen
import Consulta_Triaje
import Top_Triaje
import Top_Paciente
import Top_Reporte
import Impresion
import os
import Incidencias

class Ventana_Principal(object):
	"""docstring for Ventana_Principal"""
	def __init__(self,usuario,nivel):
		self.Usuario=usuario
		self.nivel=nivel		
		self.letra_leyenda=('Candara',16,'bold italic')
		##creando punteros a las consultas
		self.obj_QueryGalen=Consulta_Galen.queryGalen()
		self.obj_QueryTriaje=Consulta_Triaje.queryTriaje()
		Objeto_Triaje=Top_Triaje.Triaje()
		self.obj_Impresion=Impresion.Reporte()
		##fin de la creancion de punteros
		height=0
		
		#self.ventana=Tk()
		self.ventana=ThemedTk(theme='arc')
		self.ventana.title('Sistema de citas de Consultorio Externo')
		#self.ventana.attributes('-fullscreen', True) 
		self.ventana.iconbitmap('img/doctor.ico')
		#self.ventana.focus_set()
		#self.ventana.grab_set()
		self.height=self.ventana.winfo_screenheight()
		self.width=self.ventana.winfo_screenwidth()		
		self.ventana.geometry("%dx%d" % (self.width,self.height))
		#self.ventana.protocol('WM_DELETE_WINDOW',self.salir)
		#frame principal
		self.Frame_Principal=Frame(self.ventana,bg='#828682',width=self.width,height=self.height)
		self.Frame_Principal.pack()
		#agregando menu
		self.Barra_Menu=Menu(self.ventana)
		self.ventana['menu']=self.Barra_Menu
		#creando menu
		self.M_Archivo=Menu(self.Barra_Menu,tearoff=False)
		self.M_Archivo.add_command(label='Minimizar',command=self.ventana.iconify)
		self.M_Archivo.add_command(label='Cerrar',command=self.ventana.destroy)
		self.M_Archivo.add_separator()		
		self.Barra_Menu.add_cascade(label='Archivo',menu=self.M_Archivo)

		#menu configuracion
		if self.nivel=='1':			
			self.M_Usuario=Menu(self.Barra_Menu,tearoff=False)
			self.M_Usuario.add_command(label='Agregar Usuario',command=self.Desk_User)
			self.M_Usuario.add_command(label='Reporte Usuario',command=self.Reporte_Usuarios)
			self.Barra_Menu.add_cascade(label='Configuracion',menu=self.M_Usuario)

		#menu triaje
		if self.nivel=='2':
			self.M_Triaje=Menu(self.Barra_Menu,tearoff=False)
			self.M_Triaje.add_command(label='Agendar Cita',command=self.Frame_Triaje)
			self.M_Triaje.add_command(label='Reporte Citas',command=self.Reporte_Cita)
			self.M_Triaje.add_command(label='Buscar Atención',command=Objeto_Triaje.search_Citas)
			self.M_Triaje.add_command(label='Incidencias',command=self.Incidencias)
			self.Barra_Menu.add_cascade(label='Triaje',menu=self.M_Triaje)

		elif self.nivel=='1':
			self.M_Triaje=Menu(self.Barra_Menu,tearoff=False)
			self.M_Triaje.add_command(label='Agendar Cita',command=self.Frame_Triaje)
			self.M_Triaje.add_command(label='Reporte Citas',command=self.Reporte_Cita)
			self.M_Triaje.add_command(label='Buscar Atención',command=Objeto_Triaje.search_Citas)
			self.M_Triaje.add_command(label='Incidencias',command=self.Incidencias)
			self.Barra_Menu.add_cascade(label='Triaje',menu=self.M_Triaje)

		#menu paciente
		self.M_Paciente=Menu(self.Barra_Menu,tearoff=False)
		self.M_Paciente.add_command(label='Insertar',command=self.Agregar_Pacientes)
		self.M_Paciente.add_command(label='Listar pacientes',command=self.Listar_Pacientes)
		self.Barra_Menu.add_cascade(label='Pacientes',menu=self.M_Paciente)	
		
		#menu ayuda
		self.M_Usuario=Menu(self.Barra_Menu,tearoff=False)
		self.M_Usuario.add_command(label='Acerca de...',command=lambda:self.mensaje_Info('INFORMACION'))
		self.M_Usuario.add_command(label='Version',command=lambda:self.mensaje_Info('VERSION'))
		self.Barra_Menu.add_cascade(label='Ayuda',menu=self.M_Usuario)
		#self.ventana.mainloop()
	def mensaje_Info(self,iden):
		if iden=='INFORMACION':
			messagebox.showinfo('Notificación',f"""Sistema de citas de consultorio externo, desarrollado\npor la Unidad de Estadística e Informática, a traves de la oficina\nde Desarrollo y Programacion del HOSPITAL SUB REGIONAL DE ANDAHUAYLAS...\nTodos los derechos resevados© Andahuaylas 2022\nby Jaime Navarro Crúz""")
		elif iden=='VERSION':
			messagebox.showinfo('Notificación',f"""SISTEMA DE CITAS DE CONSULTORIO EXTERNO.\nversion 1.5""")

	
	def Desk_User(self):
		#datos={'nombre':'jaime','apellidoP':'navarro','apellidoM':'cruz','usuario':'user','contrasenia':'123'}
		obj_usuario=GUI_User.Usuario()
		obj_usuario.Top_Agregar()
	def Reporte_Usuarios(self):
		obj_usuario=GUI_User.Usuario()
		obj_usuario.top_ListaUsuario()
	def Incidencias(self):
		self.Frame_incidencias=Frame(self.Frame_Principal,width=self.width,height=self.height,bg="#828682")
		self.Frame_incidencias.place(x=0,y=0)
		self.Frame_incidencias.pack_propagate(False)
		obj_incidencia=Incidencias.IncidenciasV()
		obj_incidencia.Incidencias(self.Frame_incidencias,self.width,self.height)
	def Frame_Triaje(self):
		self.F_Triaje=Frame(self.Frame_Principal,width=self.width,height=self.height,bg='#828682')
		self.F_Triaje.place(x=0,y=0)
		#AGRENDO LA SEPARACION DEL FRAME
		self.Frame_Programacion=Frame(self.F_Triaje,width=int(self.width*0.16),height=int(self.height*0.95),bg='white')
		#self.Frame_Programacion.pack_propagate(False)
		self.Frame_Programacion.place(x=0,y=0)

		date=datetime.datetime.now()
		
		self.calendario=Calendar(self.Frame_Programacion,selectmode='day',year=date.year,month=date.month,day=date.day)
		self.calendario.bind('<<CalendarSelected>>',self.calendar_event)
		self.calendario.grid(row=0,column=1,columnspan=3)
		#Agrego lo programado
		self.Lista_Menu=Listbox(self.Frame_Programacion,height=28,width=40,selectforeground='#ffffff',selectbackground="#00aa00",selectborderwidth=2,cursor='hand2')
		self.llenar_Menu()
		self.Lista_Menu.bind('<<ListboxSelect>>',self.Generate_Cupos)
		self.Lista_Menu.grid(row=1,column=0,columnspan=3)
		scroll_bar=Scrollbar(self.Frame_Programacion)
		scroll_bar.grid(row=1,column=4)
		self.Lista_Menu.configure(yscrollcommand=scroll_bar.set)
		scroll_bar.configure(command=self.Lista_Menu.yview)
		#AGREGO PANEL PRINCIPAL
		self.Frame_TriajeP=Frame(self.F_Triaje,width=int(self.width*0.85),height=int(self.height*0.95),bg='#828682')
		self.Frame_TriajeP.place(x=int(self.width*0.16)+10,y=0)		
		#agrego label
		#label=Label(self.Frame_TriajeP,text='here',width=40,height=40,bg='green')
		#label.bind('<Button-3>',self.evento_clickRight)
		#label.place(x=0,y=0)
		#menu agregar y eliminar
		self.menu_right=Menu(self.Frame_TriajeP,tearoff=0)
		self.menu_right.add_command(label='Agregar',command=self.evento_agregar)


		self.menu_FechaAnterior=Menu(self.Frame_TriajeP,tearoff=0)
		#self.menuFechaAnterior.add_command(label='Eliminar',command=self.evento_EliminarCupo)
		self.menu_FechaAnterior.add_command(label='Consultar',command=self.evento_ConsultaCupo)
		self.menu_FechaAnterior.add_command(label='Imprimir',command=self.evento_ImprimirCupo)

		#:::::::::::::::
		self.menu_Fechaposterior=Menu(self.Frame_TriajeP,tearoff=0)
		self.menu_Fechaposterior.add_command(label='Eliminar',command=self.evento_EliminarCupo)
		self.menu_Fechaposterior.add_command(label='Consultar',command=self.evento_ConsultaCupo)
		self.menu_Fechaposterior.add_command(label='Imprimir',command=self.evento_ImprimirCupo)

		# leyenda::::::::::::::::::::::::::::::
		self.frame_Leyenda=Frame(self.F_Triaje,width=self.width,height=int(self.height*0.1),bg='black')
		#agregando Widgets Leyenda
		etiqueta_Leyenda=Label(self.frame_Leyenda,text='Leyenda',fg='white',bg='black',font=self.letra_leyenda)
		etiqueta_Leyenda.grid(row=0,column=0,padx=5)
		styl = ttk.Style()
		styl.configure('white.TSeparator', background='white')

		etiqueta_Leyenda=Label(self.frame_Leyenda,text='SALUDPOL',fg='#4B418C',bg='black',font=self.letra_leyenda)
		etiqueta_Leyenda.grid(row=1,column=9,padx=5)
		styl = ttk.Style()
		#styl.configure('white.TSeparator', background='white')

		etiqueta_Leyenda=Label(self.frame_Leyenda,text='REFCON',fg='#0D898A',bg='black',font=self.letra_leyenda)
		etiqueta_Leyenda.grid(row=1,column=10,padx=5)
		styl = ttk.Style()
		#styl.configure('white.TSeparator', background='white')

		etiqueta_Leyenda=Label(self.frame_Leyenda,text='TELESALUD',fg='#946F12',bg='black',font=self.letra_leyenda)
		etiqueta_Leyenda.grid(row=1,column=11,padx=5)
		styl = ttk.Style()
		#styl.configure('white.TSeparator', background='white')

		s1=ttk.Separator(self.frame_Leyenda,orient='vertical',style='white.TSeparator',takefocus=1)
		s1.grid(row=0,column=1,rowspan=2,sticky='NS')
		etiqueta_Leyenda=Label(self.frame_Leyenda,text='Agendado',fg='red',bg='black',font=self.letra_leyenda)
		etiqueta_Leyenda.grid(row=0,column=2,padx=5)
		#s1=ttk.Separator(self.frame_Leyenda,orient='vertical',style='white.TSeparator',takefocus=1)
		#s1.grid(row=0,column=4,rowspan=2,sticky='NS')
		etiqueta_Leyenda=Label(self.frame_Leyenda,text='Libre',fg='green',bg='black',font=self.letra_leyenda)
		etiqueta_Leyenda.grid(row=1,column=2,padx=5)
		s1=ttk.Separator(self.frame_Leyenda,orient='vertical',style='white.TSeparator',takefocus=1)
		s1.grid(row=0,column=7,rowspan=2,sticky='NS')		
		self.etiqueta_Medico=Label(self.frame_Leyenda,text='Medico',fg='white',bg='black',font=self.letra_leyenda)
		self.etiqueta_Medico.grid(row=0,column=9,columnspan=4,padx=5)

		s1=ttk.Separator(self.frame_Leyenda,orient='vertical',style='white.TSeparator',takefocus=1)
		s1.grid(row=0,column=17,rowspan=2,sticky='NS')
		self.etiqueta_servicio=Label(self.frame_Leyenda,text='Servicio',fg='white',bg='black',font=self.letra_leyenda)
		self.etiqueta_servicio.grid(row=0,column=18)


		s1=ttk.Separator(self.frame_Leyenda,orient='vertical',style='white.TSeparator',takefocus=1)
		s1.grid(row=0,column=25,rowspan=2,sticky='NS')
		etiqueta_Turno=Label(self.frame_Leyenda,text='Turno :',fg='white',bg='black',font=self.letra_leyenda)
		etiqueta_Turno.grid(row=0,column=26)
		self.etiqueta_Turno1=Label(self.frame_Leyenda,text='',fg='white',bg='black',font=self.letra_leyenda)
		self.etiqueta_Turno1.grid(row=0,column=28)

		#s1=ttk.Separator(self.frame_Leyenda,orient='vertical',style='white.TSeparator',takefocus=1)
		#s1.grid(row=0,column=35,rowspan=2,sticky='NS')
		s1=ttk.Separator(self.frame_Leyenda,orient='vertical',style='white.TSeparator',takefocus=1)
		s1.grid(row=0,column=33,rowspan=2,sticky='NS')
		etiqueta_Usuario=Label(self.frame_Leyenda,text='Usuario :',fg='white',bg='black',font=self.letra_leyenda)
		etiqueta_Usuario.grid(row=0,column=34)
		etiqueta_Usuario=Label(self.frame_Leyenda,text=f'{self.Usuario}',fg='white',bg='black',font=self.letra_leyenda)
		etiqueta_Usuario.grid(row=0,column=35)	

		self.frame_Leyenda.place(x=0,y=int(self.height*0.84))
	def evento_clickRight(self,event):
		try:
			#print(len(self.Lista_Menu.curselection()))
			if len(self.Lista_Menu.curselection())!=0:
				self.cupo_=event.widget.cget('text')			
				consultorio_Total=self.Lista_Menu.get(self.Lista_Menu.curselection()[0])
				consultorio=consultorio_Total[consultorio_Total.find('_')+1:]
				#consultar si el cupo esta agendado			
				rows=self.obj_QueryTriaje.query_CupoNumber(self.calendario.selection_get(),consultorio,self.cupo_,self.turno,self.Medico_Datos)
			
				if len(rows)==1:
					date=datetime.date.today()
					if self.calendario.selection_get()<date:
						self.menu_FechaAnterior.tk_popup(event.x_root,event.y_root)
					else:
						self.menu_Fechaposterior.tk_popup(event.x_root,event.y_root)			

				elif len(rows)==0:
					self.menu_right.tk_popup(event.x_root,event.y_root)
			else:
				messagebox.showinfo('Alerta','Seleccione un consultorio!')

		finally:
			self.menu_right.grab_release()
	def evento_agregar(self):
		date=datetime.date.today()
		obj_TopTriaje=None
		if self.calendario.selection_get()>=date:
			obj_TopTriaje=Top_Triaje.Triaje()
			obj_TopTriaje.Top_Agregar(globals()['self.cupo%s'%self.cupo_],self.servicio,self.Medico_Datos,self.Usuario,self.calendario.selection_get(),self.turno)		
		else:
			messagebox.showinfo('Alerta','No se puede programar para esta fecha!')
		#globals()['self.cupo%s'%self.cupo_].configure(bg='green')	
	def evento_EliminarCupo(self):
		result=messagebox.askquestion('Alerta','Estas seguro que desea Eliminar')
		if result=='yes':
			consultorio_Total=self.Lista_Menu.get(self.Lista_Menu.curselection()[0])
			consultorio=consultorio_Total[consultorio_Total.find('_')+1:]
			if int(self.cupo_)<21:				
				self.obj_QueryTriaje.Eliminar_Cita(self.cupo_,self.calendario.selection_get(),consultorio,self.Medico_Datos,self.turno)
				globals()['self.cupo%s'%self.cupo_].configure(bg='#185522',fg='white')
			else:
				self.obj_QueryTriaje.Eliminar_Cita(self.cupo_,self.calendario.selection_get(),consultorio,self.Medico_Datos,self.turno)
				globals()['self.cupo%s'%self.cupo_].configure(fg='white')
		#self.obj_ConsultaTriaje
	def evento_ImprimirCupo(self):
		consultorio_Total=self.Lista_Menu.get(self.Lista_Menu.curselection()[0])
		consultorio=consultorio_Total[consultorio_Total.find('_')+1:]	
		rows=self.obj_QueryTriaje.query_DataTriaje(self.calendario.selection_get(),consultorio,self.cupo_,self.Medico_Datos,self.turno)
		for val in rows:
			dni=val.dni
			fuente=val.fuente
			cupo=val.Nro_Cupo
			medico=val.Medico
			consultorio=val.Especialidad
			nro_Referencia=val.Nro_Referencia
			establecimiento=val.P_C
			Historia=val.Historia
			fecha_A=val.Fecha_Atencion
			turno=val.Turno
		self.obj_Impresion.imprimir_Cupo(dni,fuente,cupo,medico,consultorio,nro_Referencia,fecha_A,Historia,establecimiento,turno)
		os.startfile('cupo.pdf','print')
	def evento_ConsultaCupo(self):
		consultorio_Total=self.Lista_Menu.get(self.Lista_Menu.curselection()[0])
		consultorio=consultorio_Total[int(consultorio_Total.find('_'))+1:]
		rows=self.obj_QueryTriaje.query_DataTriaje(self.calendario.selection_get(),consultorio,self.cupo_,self.Medico_Datos,self.turno)		
		for val in rows:
			dni=val.dni
			fuente=val.fuente
			cupo=val.Nro_Cupo
			medico=val.Medico
			consultorio=val.Especialidad
			nro_Referencia=val.Nro_Referencia
			establecimiento=val.P_C
			Historia=val.Historia
			fecha_A=val.Fecha_Atencion
			turno=val.Turno
		
		self.obj_Impresion.imprimir_Cupo(dni,fuente,cupo,medico,consultorio,nro_Referencia,fecha_A,Historia,establecimiento,turno)
		obj_TopReporte=Top_Reporte.Reporte()
		obj_TopReporte.top_ConsultaCupo()

	def llenar_Menu(self):
		try:
			self.Lista_Menu.delete(0,'end')
			rows=self.obj_QueryGalen.query_Programacion(self.calendario.selection_get())
			for val in rows:
				self.Lista_Menu.insert(0,str(val.IdTurno)+'-'+str(val.IdMedico)+'_'+val.Nombre)
		except Exceptions as e:
			messagebox.showinfo('Alerta',f'Error {e}')
	def calendar_event(self,event):
		#self.Frame_TriajeP=Frame(self.F_Triaje,width=int(self.width*0.85),height=int(self.height*0.95),bg='#828682')
		#self.Frame_TriajeP.place(x=int(self.width*0.16)+10,y=0)	
		self.llenar_Menu()
	def Generate_Cupos(self,event):
		try:
			data_lista=self.Lista_Menu.get(self.Lista_Menu.curselection()[0])
			self.turno_codi=data_lista[:data_lista.find('-')]
			self.IdMedico=data_lista[data_lista.find('-')+1:data_lista.find('_')]						
			self.servicio=data_lista[data_lista.find('_')+1:]						
			letra=('Arial',18,'bold')			
			medico=self.obj_QueryGalen.consulta_Medico_Responsable(self.servicio,self.calendario.selection_get(),self.IdMedico,self.turno_codi)	
			for val in medico:
				self.Medico_Datos=val.Nombres+" "+val.ApellidoPaterno+" "+val.ApellidoMaterno
				self.turno=val.Descripcion

			rows=self.obj_QueryTriaje.query_Cupo(self.calendario.selection_get(),self.servicio,self.Medico_Datos,self.turno)
			lista_cupos=[]
			for valores in rows:
				lista_cupos.append(valores.Nro_Cupo)		
			Nro_Cupo=1		
			for i in range(4):
				for j in range(9):
					if Nro_Cupo in lista_cupos:
						if Nro_Cupo<=20:
							globals()['self.cupo%s'%Nro_Cupo]=Label(self.Frame_TriajeP,text=Nro_Cupo, width=8,height=5,bg='red',fg='white',borderwidth=2,font=letra)
							globals()['self.cupo%s'%Nro_Cupo].bind('<Button-3>',self.evento_clickRight)
							globals()['self.cupo%s'%Nro_Cupo].grid(row=i,column=j, padx=7,pady=7)
						elif Nro_Cupo>20 and Nro_Cupo<26:
							globals()['self.cupo%s'%Nro_Cupo]=Label(self.Frame_TriajeP,text=Nro_Cupo, width=8,height=5,bg='#4B418C',fg='red',borderwidth=2,font=letra)
							globals()['self.cupo%s'%Nro_Cupo].bind('<Button-3>',self.evento_clickRight)
							globals()['self.cupo%s'%Nro_Cupo].grid(row=i,column=j, padx=7,pady=7)
						elif Nro_Cupo>25 and Nro_Cupo<31:
							globals()['self.cupo%s'%Nro_Cupo]=Label(self.Frame_TriajeP,text=Nro_Cupo, width=8,height=5,bg='#0D898A',fg='red',borderwidth=2,font=letra)
							globals()['self.cupo%s'%Nro_Cupo].bind('<Button-3>',self.evento_clickRight)
							globals()['self.cupo%s'%Nro_Cupo].grid(row=i,column=j, padx=7,pady=7)
						elif Nro_Cupo>30:
							globals()['self.cupo%s'%Nro_Cupo]=Label(self.Frame_TriajeP,text=Nro_Cupo, width=8,height=5,bg='#946F12',fg='red',borderwidth=2,font=letra)
							globals()['self.cupo%s'%Nro_Cupo].bind('<Button-3>',self.evento_clickRight)
							globals()['self.cupo%s'%Nro_Cupo].grid(row=i,column=j, padx=7,pady=7)

					else:
						if Nro_Cupo<=20:
							globals()['self.cupo%s'%Nro_Cupo]=Label(self.Frame_TriajeP,text=Nro_Cupo, width=8,height=5,bg='#185522',fg='white',borderwidth=2,font=letra)
							globals()['self.cupo%s'%Nro_Cupo].bind('<Button-3>',self.evento_clickRight)
							globals()['self.cupo%s'%Nro_Cupo].grid(row=i,column=j, padx=7,pady=7)
						elif Nro_Cupo>20 and Nro_Cupo<26:
							globals()['self.cupo%s'%Nro_Cupo]=Label(self.Frame_TriajeP,text=Nro_Cupo, width=8,height=5,bg='#4B418C',fg='white',borderwidth=2,font=letra)
							globals()['self.cupo%s'%Nro_Cupo].bind('<Button-3>',self.evento_clickRight)
							globals()['self.cupo%s'%Nro_Cupo].grid(row=i,column=j, padx=7,pady=7)
						elif Nro_Cupo>25 and Nro_Cupo<31:
							globals()['self.cupo%s'%Nro_Cupo]=Label(self.Frame_TriajeP,text=Nro_Cupo, width=8,height=5,bg='#0D898A',fg='white',borderwidth=2,font=letra)
							globals()['self.cupo%s'%Nro_Cupo].bind('<Button-3>',self.evento_clickRight)
							globals()['self.cupo%s'%Nro_Cupo].grid(row=i,column=j, padx=7,pady=7)
						elif Nro_Cupo>30:
							globals()['self.cupo%s'%Nro_Cupo]=Label(self.Frame_TriajeP,text=Nro_Cupo, width=8,height=5,bg='#946F12',fg='white',borderwidth=2,font=letra)
							globals()['self.cupo%s'%Nro_Cupo].bind('<Button-3>',self.evento_clickRight)
							globals()['self.cupo%s'%Nro_Cupo].grid(row=i,column=j, padx=7,pady=7)

					Nro_Cupo+=1				

			self.etiqueta_Turno1.configure(text=f'{self.turno}')
			self.etiqueta_Medico.configure(text=f'Medico : {self.Medico_Datos}')
			self.etiqueta_servicio.configure(text=f'Consultorio : {self.servicio}')
		except Exception as e:
			print(e)	

	def Reporte_Cita(self):
		obj_Reporte=Top_Reporte.Reporte()
		#pacientes
		obj_Reporte.Top_Reporte()
	def Agregar_Pacientes(self):
		obj_TopPaciente=Top_Paciente.Paciente()
		obj_TopPaciente.Top_Agregar()
	def Listar_Pacientes(self):
		obj_TopPaciente=Top_Paciente.Paciente()
		obj_TopPaciente.paciente_Visualizacion()
	

#obj=Ventana_Principal('usuario','jaime')
