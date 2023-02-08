from tkinter import *
from tkinter import ttk
import hashlib
from tkinter import messagebox
import Consulta_Triaje

class Usuario(object):
	def __init__(self):
		self.obj_Triaje=Consulta_Triaje.queryTriaje()		
	def Top_Agregar(self):
		font_text=('Candara',12,'bold')
		self.ventana_usuario=Toplevel()
		self.ventana_usuario.geometry('450x300')
		self.ventana_usuario.attributes('-topmost',True)
		self.ventana_usuario.iconbitmap('img/usuario.ico')
		self.ventana_usuario.title('Registro de Usuario')
		etiqueta_nombre=Label(self.ventana_usuario,text='DNI',font=font_text,fg='#105B79')
		etiqueta_nombre.grid(row=1,column=0,pady=10)
		self.Entry_DNI=ttk.Entry(self.ventana_usuario,width=30)
		self.Entry_DNI.bind('<Return>',self.buscar_persona)
		self.Entry_DNI.bind('<Button-1>',self.borrado_widget)
		self.Entry_DNI.grid(row=1,column=1,pady=10)

		etiqueta_apellidoP=Label(self.ventana_usuario,text='NOMBRE',font=font_text,fg='#105B79')
		etiqueta_apellidoP.grid(row=2,column=0)
		self.Entry_nombre=ttk.Entry(self.ventana_usuario,width=30,state='readonly')
		self.Entry_nombre.grid(row=2,column=1,pady=6)

		etiqueta_apellidoM=Label(self.ventana_usuario,text='APE. PATERNO',font=font_text,fg='#105B79')
		etiqueta_apellidoM.grid(row=3,column=0)
		self.Entry_apellidoP=ttk.Entry(self.ventana_usuario,width=30,state='readonly')
		self.Entry_apellidoP.grid(row=3,column=1,pady=6)

		etiqueta_apellidoM=Label(self.ventana_usuario,text='APE. MATERNO',font=font_text,fg='#105B79')
		etiqueta_apellidoM.grid(row=4,column=0)
		self.Entry_apellidoM=ttk.Entry(self.ventana_usuario,width=30,state='readonly')
		self.Entry_apellidoM.grid(row=4,column=1,pady=6)

		etiqueta_usuario=Label(self.ventana_usuario,text='USUARIO',font=font_text,fg='#105B79')
		etiqueta_usuario.grid(row=5,column=0,pady=6)
		self.Entry_usuario=ttk.Entry(self.ventana_usuario,width=30)
		self.Entry_usuario.grid(row=5,column=1,pady=6)

		etiqueta_contra=Label(self.ventana_usuario,text='CONTRASEÑA',font=font_text,fg='#105B79')
		etiqueta_contra.grid(row=6,column=0,pady=6)
		self.Entry_contra=ttk.Entry(self.ventana_usuario,width=30,show='*')
		self.Entry_contra.grid(row=6,column=1,pady=6)

		etiqueta_repeat_contra=Label(self.ventana_usuario,text='REP. CONTRASEÑA',font=font_text,fg='#105B79')
		etiqueta_repeat_contra.grid(row=7,column=0)
		self.Entry_repeat_contra=ttk.Entry(self.ventana_usuario,width=30,show='*')
		self.Entry_repeat_contra.grid(row=7,column=1,pady=6)
		self.Entry_repeat_contra.bind('<KeyRelease>',self.validate_password)

		self.etiqueta_validate=Label(self.ventana_usuario,text='.',font=font_text)
		self.etiqueta_validate.grid(row=7,column=2)

		self.btn_Guardar=ttk.Button(self.ventana_usuario,text='GUARDAR')
		self.btn_Guardar['command']=self.save_User
		self.btn_Guardar.grid(row=8,column=0)

		self.btn_Limpiar=ttk.Button(self.ventana_usuario,text='LIMPIAR')
		self.btn_Limpiar.grid(row=8,column=1)

		self.btn_Cancelar=ttk.Button(self.ventana_usuario,text='CANCELAR')
		self.btn_Cancelar['command']=self.ventana_usuario.destroy
		self.btn_Cancelar.grid(row=8,column=2)
		self.ventana_usuario.mainloop()
	def setter_attributes(self,datos):
		self.Nombre=datos['nombre']
		self.Dni=''
		self.Apellido_Paterno=datos['apellidoP']
		self.Apellido_Materno=datos['apellidoM']
		self.Usuario=datos['usuario']
		self.Contrasenia=self.set_Password(datos['contrasenia'])
	def set_Password(self,contra):
		codificar=hashlib.md5()
		codificar.update(b'%a'%contra)
		self.Contrasenia=codificar.hexdigest()

	def insertar_Usuario(self):
		messagebox.showinfo('Alerta','mensaje')

	def buscar_persona(self,event):
		dni=self.Entry_DNI.get()
		rows=self.obj_Triaje.Consulta_ExistUsuario(dni)
		if len(rows)==0:
			rows_datos=self.obj_Triaje.consulta_DatosPaciente(dni)
			if len(rows_datos)!=0:
				for val in rows_datos:
					self.active_entry()
					self.Entry_nombre.insert(0,val.Nombre)
					self.Entry_apellidoP.insert(0,val.Apellido_Paterno)
					self.Entry_apellidoM.insert(0,val.Apellido_Materno)
					self.disable_entry()
			else:
				messagebox.showinfo('Alerta','Registre los Datos del usuario en \n el apartado de PACIENTES')

		else:
			messagebox.showinfo('Alerta','Existe Un usuario para este Paciente')
	def active_entry(self):
		self.Entry_nombre.config(state='NORMAL')
		self.Entry_apellidoP.config(state='NORMAL')
		self.Entry_apellidoM.config(state='NORMAL')
	def disable_entry(self):
		self.Entry_nombre.config(state='readonly')
		self.Entry_apellidoP.config(state='readonly')
		self.Entry_apellidoM.config(state='readonly')
	def borrado_widget(self,event):
		self.active_entry()
		self.Entry_DNI.delete(0,'end')
		self.Entry_nombre.delete(0,'end')
		self.Entry_apellidoP.delete(0,'end')
		self.Entry_apellidoM.delete(0,'end')
		self.Entry_contra.delete(0,'end')
		self.Entry_repeat_contra.delete(0,'end')
		self.disable_entry()
		#self.Entry_DNI.delete(0,'end')
	def borrado_Entrys(self):
		self.active_entry()
		self.Entry_DNI.delete(0,'end')
		self.Entry_nombre.delete(0,'end')
		self.Entry_apellidoP.delete(0,'end')
		self.Entry_apellidoM.delete(0,'end')
		self.Entry_contra.delete(0,'end')
		self.Entry_repeat_contra.delete(0,'end')
		self.Entry_usuario.delete(0,'end')
		self.disable_entry()
		#self.Entry_DNI.delete(0,'end')

	def validate_password(self,event):
		passs=self.Entry_repeat_contra.get()
		if len(passs)!=0:
			if passs==self.Entry_contra.get():
				self.etiqueta_validate.config(bg='green')
				self.etiqueta_validate.config(text='Correcto')
			else:
				self.etiqueta_validate.config(background='red')
				self.etiqueta_validate.config(text='Incorrecto')
		else:
			messagebox.showinfo('Alerta','Llene los campos de Contraseña')
	def save_User(self):
		usuario=self.Entry_usuario.get()
		rows_Users=self.obj_Triaje.Consulta_UserExists(usuario)		
		if len(rows_Users)==0:
			#recuperar valores
			self.active_entry()
			dni=self.Entry_DNI.get()
			persona_Usuario=self.obj_Triaje.Consulta_ExistUsuario(dni)
			if len(persona_Usuario)==0:
				
				passs1=self.Entry_repeat_contra.get()
				passs2=self.Entry_contra.get()
				if passs1==passs2 and len(dni)!=0 and len(usuario)!=0:
					self.set_Password(passs1)
					try:
						self.obj_Triaje.Insert_User(dni,usuario,self.Contrasenia,2)
						messagebox.showinfo('Alerta','Se insertó correctamente')
						self.ventana_usuario.destroy()						
					except Exception as e:
						raise e	
			else:
				messagebox.showinfo('Informacion','El DNI ya está vinculado con un Usuario')

		else:
			messagebox.showerror('Alerta','El nombre de usuario no está disponible!')
			self.borrado_Entrys()
	def top_ListaUsuario(self):
		rows=self.obj_Triaje.Consulta_Usuarios()
		font_text=('Candara',12,'bold')
		self.ventana_UserReport=Toplevel()
		self.ventana_UserReport.iconbitmap('img/usuario.ico')
		self.ventana_UserReport.geometry('500x500')
		self.ventana_UserReport.attributes('-topmost',True)
		self.ventana_UserReport.title('Reporte de Usuarios')
		self.ventana_UserReport.grab_set()

		self.table_General=ttk.Treeview(self.ventana_UserReport,columns=('#1','#2','#3','#4'),show='headings')		
		self.table_General.heading("#1",text="DNI")
		self.table_General.column("#1",width=200,anchor="center")
		self.table_General.heading("#2",text="USUARIO")
		self.table_General.column("#2",width=100,anchor="center")
		self.table_General.heading("#3",text="ESTADO")
		self.table_General.column("#3",width=100,anchor="center")								
		self.table_General.place(x=10,y=70,width=400,height=290)	
	
		for valores in rows:
			self.table_General.insert('','end',values=(valores.dni,valores.Usuario,valores.estado))

		self.btn_Restaurar=ttk.Button(self.ventana_UserReport,text='REESTABLECER PASSWORD')
		self.btn_Restaurar.place(x=10,y=400)
		self.btn_Restaurar['command']=self.top_changePassword
		self.btn_Activar=ttk.Button(self.ventana_UserReport,text='ACTIVAR')
		self.btn_Activar.place(x=200,y=400)
		self.btn_Activar['command']=lambda:self.eventos_('ESTADOACTIVO') 
		self.btn_Inactivar=ttk.Button(self.ventana_UserReport,text='INACTIVAR')
		self.btn_Inactivar.place(x=300,y=400)
		self.btn_Inactivar['command']=lambda:self.eventos_('ESTADOINACTIVO')		

	def eventos_(self,identificador):
		if len(self.table_General.focus())!=0:
			dni=self.table_General.item(self.table_General.selection()[0],option='values')[0]
			if identificador=='CAMBIARPASS':
				self.set_Password(self.Entry_pass.get())
				#passs=self.Contrasenia
				self.obj_Triaje.change_password(self.Contrasenia,dni)
				messagebox.showinfo('Alerta','Se cambio correctamente')
				self.ventana_ChangePass.destroy()
				
			if identificador=='ESTADOINACTIVO':
				self.obj_Triaje.update_State('INACTIVO',dni)
				messagebox.showinfo('Alerta','Actualizacion exitosa!!')
				self.ventana_UserReport.destroy()
			if identificador=='ESTADOACTIVO':
				self.obj_Triaje.update_State('ACTIVO',dni)
				messagebox.showinfo('Alerta','Actualizacion exitosa!!')
				self.ventana_UserReport.destroy()
		else:
			messagebox.showinfo('Alerta','Seleccione un valor')
	def top_changePassword(self):		
		self.ventana_ChangePass=Toplevel()
		self.ventana_ChangePass.geometry('300x100')
		self.ventana_ChangePass.iconbitmap('img/pass.ico')
		self.ventana_ChangePass.attributes('-topmost',True)
		self.ventana_ChangePass.title('Reporte de Usuarios')
		self.ventana_ChangePass.grab_set()

		etiqueta=Label(self.ventana_ChangePass,text='Contraseña:')
		etiqueta.place(x=10,y=10)
		self.Entry_pass=ttk.Entry(self.ventana_ChangePass,show='*')
		self.Entry_pass.place(x=120,y=10)

		btn_Aceptar=ttk.Button(self.ventana_ChangePass,text='Aceptar')
		btn_Aceptar.place(x=10,y=60)
		btn_Aceptar['command']=lambda:self.eventos_('CAMBIARPASS')	

		btn_Cancelar=ttk.Button(self.ventana_ChangePass,text='Cancelar')
		btn_Cancelar.place(x=120,y=60)
		btn_Cancelar['command']=self.ventana_ChangePass.destroy
		
		




			
