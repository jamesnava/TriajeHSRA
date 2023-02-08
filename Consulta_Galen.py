import conect_bd

class queryGalen(object):
	def __init__(self):
		obj_conectar=conect_bd.Conexion_Galen()
		obj_conectar.ejecutar_conn()
		self.cursor=obj_conectar.get_cursor()
	def query_Programacion(self,fecha):
		rows=[]
		sql=f"""SELECT Nombre,IdMedico,IdTurno FROM ProgramacionMedica AS P  INNER JOIN Servicios as S ON P.IdServicio=S.IdServicio  AND P.Fecha=CONVERT(date,'{fecha}') ORDER BY Nombre ASC"""						
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()		
		return rows	
	def query_Paciente(self,dni):
		rows=[]
		#sql=f"""SELECT NroDocumento,PrimerNombre,ApellidoPaterno,ApellidoMaterno,NroHistoriaClinica FROM Pacientes WHERE NroDocumento='{dni}'"""
		sql=f"""SELECT * FROM Pacientes INNER JOIN CentrosPoblados ON Pacientes.IdCentroPobladoDomicilio=CentrosPoblados.IdCentroPoblado WHERE NroDocumento='{dni}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def consulta_Medico_Responsable(self,servicio,fecha,idmedico,turno):
		rows=[]
		sql=f"""
			SELECT E.Nombres,E.ApellidoPaterno,E.ApellidoMaterno,TUR.Descripcion FROM ProgramacionMedica AS P  INNER JOIN Servicios as S ON P.IdServicio=S.IdServicio AND P.Fecha=CONVERT(date,'{fecha}') AND
			S.Nombre='{servicio}' AND P.IdMedico='{idmedico}'
 			INNER JOIN Medicos as M ON  P.IdMedico=M.IdMedico INNER JOIN Empleados AS E ON M.IdEmpleado=E.IdEmpleado INNER JOIN Turnos as TUR ON P.IdTurno=TUR.IdTurno AND TUR.IdTurno='{turno}'
			"""						
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()	
		return rows
	def query_Establecimiento(self,digitacion):
		rows=[]
		sql=f"""SELECT EST.Nombre AS Establecimiento,DIST.Nombre AS Distrito,PROV.Nombre AS Provincia FROM Establecimientos AS EST INNER JOIN Distritos as DIST ON DIST.IdDistrito=EST.IdDistrito
		INNER JOIN Provincias AS PROV ON DIST.IdProvincia=PROV.IdProvincia WHERE EST.Nombre LIKE '%{digitacion}%'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def query_DatosPaciente(self,dni):
		rows=[]
		self.cursor.execute(f"""SELECT PrimerNombre,SegundoNombre,ApellidoPaterno,ApellidoMaterno FROM Pacientes WHERE NroDocumento='{dni}'""")
		rows=self.cursor.fetchall()
		return rows
