from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import Consulta_Triaje
import Consulta_Galen

class Reporte(object):
	def __init__(self):
		self.obj_Triaje=Consulta_Triaje.queryTriaje()
		self.obj_Galen=Consulta_Galen.queryGalen()
		pdfmetrics.registerFont(TTFont('Vera','Vera.ttf'))		
	def Reporte_Consultorio(self,table,consultorio,medico,fecha,turno):
		libro=canvas.Canvas('consultorio.pdf',landscape(letter))
		w,h=landscape(letter)		
		libro.drawString(20,h-20,f'REPORTE DE CONSULTORIO EXTERNO {consultorio}')
		libro.drawString(20,h-35,f'MEDICO RESPONSABLE: {medico}')
		libro.drawString(20,h-50,f'FECHA: {fecha}')
		nombre_turn=''
		if int(turno)==4:
			nombre_turn='Mañana'
		elif int(turno)==33:
			nombre_turn='Tarde'
		elif int(turno)==1:
			nombre_turn='Mañana y Tarde'

		libro.drawString(400,h-50,f'TURNO: {nombre_turn}')		
		ylist=[]		
		xlist=[10,60,140,270,320,370,435,505,525,550,590,680,780]			

		alto_Celda=70
		for i in range(len(table.get_children())+2):
			ylist.append(h-alto_Celda)
			alto_Celda+=15
		libro.setFont('Times-Roman',10)
		libro.drawString(15,h-82,'DNI')
		libro.drawString(65,h-82,'NOMBRES')
		libro.drawString(145,h-82,'APELLIDOS')
		libro.drawString(275,h-82,'TELEF.')
		libro.drawString(322,h-82,'CUPO')
		libro.drawString(375,h-82,'NRO REF.')
		libro.drawString(437,h-82,'ESTABLECIM.')
		libro.drawString(505,h-82,'CT.')
		libro.drawString(526,h-82,'FUA')
		libro.drawString(552,h-82,'HIST.')
		libro.drawString(591,h-82,'CONSULT.')
		libro.drawString(681,h-82,'MEDICO')
		lista_Datos=[]

		for i in table.get_children():
			lista_Datos.append(table.item(i)['values'])

		letra_distancia=95
		cantidad=len(lista_Datos)
		libro.setFont('Times-Roman',7)
		contador=0
		for i in range(cantidad):
			#print(lista_Datos[i][1])			
			libro.drawString(20,h-letra_distancia,f"""{lista_Datos[i][0]}""")
			libro.drawString(72,h-letra_distancia,f'{lista_Datos[i][1]}')
			libro.drawString(148,h-letra_distancia,f'{lista_Datos[i][2]}')
			libro.drawString(282,h-letra_distancia,f'{lista_Datos[i][3]}')
			libro.drawString(322,h-letra_distancia,f'{lista_Datos[i][5]}')
			libro.drawString(375,h-letra_distancia,f'{lista_Datos[i][6]}')
			libro.drawString(439,h-letra_distancia,f'{lista_Datos[i][7]}')
			libro.drawString(507,h-letra_distancia,f'{lista_Datos[i][10]}')
			libro.drawString(527,h-letra_distancia,f'{lista_Datos[i][11]}')
			libro.drawString(553,h-letra_distancia,f'{lista_Datos[i][12]}')
			
			if len(lista_Datos[i][8])>27:
				libro.drawString(592,h-letra_distancia,f'{lista_Datos[i][8][0:27]}')
			else:
				libro.drawString(592,h-letra_distancia,f'{lista_Datos[i][8]}')
			if len(lista_Datos[i][9])>22:
				libro.drawString(682,h-letra_distancia,f'{lista_Datos[i][9][0:22]}')
			else:
				libro.drawString(682,h-letra_distancia,f'{lista_Datos[i][9]}')
			letra_distancia=letra_distancia+15
			if i==25:
				libro.showPage()
				w,h=landscape(letter)
				letra_distancia=95
				libro.setFont('Times-Roman',7)

		
		#libro.grid(xlist,ylist)

		libro.save()
	def imprimir_Cupo(self,dni,id_fuente,cupo,medico,consultorio,nro_Referencia,fecha_A,historia,establecimiento,Turno):
		nomb_apelle=''
		procedencia=''
		rows=self.obj_Triaje.consulta_DatosPaciente(dni)
		if len(rows)!=0:
			for val in rows:
				nomb_apelle=str(val.Nombre)+' '+str(val.Apellido_Paterno)+' '+str(val.Apellido_Materno)
				procedencia=val.Procedencia
		else:
			rows_galen=self.obj_Galen.query_Paciente(dni)
			for val in rows_galen:
				nomb_apelle=str(val.PrimerNombre)+' '+str(val.SegundoNombre)+' '+str(val.ApellidoPaterno)+' '+str(val.ApellidoMaterno)
				procedencia=val.Nombre
		libro=canvas.Canvas('cupo.pdf')
		w,h=2.9*inch,10*inch
		libro.setPageSize((w,h))
		libro.setFont('Vera',20)
		libro.drawString(40,h-15,'CONSULTA')
		libro.drawString(40,h-40,'EXTERNA')
		libro.drawString(0,h-45,f'_________________________________________')	
		libro.setFont('Helvetica-Bold',14)
		libro.drawString(10,h-70,f'DATOS DEL PACIENTE')
		libro.setFont('Times-Roman',14)
		libro.drawString(10,h-85,f'{nomb_apelle}')
		libro.drawString(10,h-101,f'DNI: {dni}')
		libro.setFont('Helvetica-Bold',14)
		libro.drawString(10,h-123,f'PROCEDENCIA')
		libro.setFont('Times-Roman',14)
		libro.drawString(10,h-140,f'{procedencia}')
		libro.setFont('Times-Roman',15)
		libro.drawString(0,h-155,f'__________________________________________')		
		libro.drawString(0,h-175,f'DETALLE DE LA ATENCIÓN')
		libro.drawString(0,h-190,'____________________________________________')
		
		libro.setFont('Helvetica-Bold',14)
		libro.drawString(10,h-210,f'CONSULTORIO')
		libro.setFont('Times-Roman',14)
		libro.drawString(10,h-230,f'{consultorio}')
		libro.setFont('Helvetica-Bold',14)
		libro.drawString(10,h-260,f'MEDICO')
		libro.setFont('Times-Roman',14)
		libro.drawString(10,h-280,f'{medico}')
		libro.setFont('Helvetica-Bold',14)		
		libro.drawString(10,h-310,f'ESTABLECIMIENTO')
		libro.setFont('Times-Roman',14)
		libro.drawString(10,h-330,f'{establecimiento}')
		libro.setFont('Helvetica-Bold',14)		
		libro.drawString(10,h-360,f'FUENTE')
		libro.setFont('Times-Roman',14)
		libro.drawString(10,h-380,f'{id_fuente}')
		libro.setFont('Helvetica-Bold',14)
		libro.drawString(10,h-410,f'NRO REFERENCIA')
		libro.setFont('Times-Roman',14)
		libro.drawString(20,h-430,f'{nro_Referencia}')

		libro.setFont('Helvetica-Bold',14)
		libro.drawString(10,h-460,f'Turno')
		libro.setFont('Times-Roman',14)
		libro.drawString(20,h-480,f'{Turno}')

		libro.setFont('Helvetica-Bold',14)
		libro.drawString(10,h-510,f'NRO CUPO')
		libro.setFont('Times-Roman',14)
		libro.drawString(20,h-530,f'{cupo}')
		libro.setFont('Helvetica-Bold',14)
		libro.drawString(10,h-560,f'Historia Cl.')
		libro.setFont('Times-Roman',14)
		libro.drawString(20,h-580,f'{historia}')
		libro.setFont('Helvetica-Bold',14)
		libro.drawString(10,h-610,f'FECHA DE ATENCION')
		libro.setFont('Times-Roman',14)
		libro.drawString(20,h-630,f'{fecha_A} ')			
		libro.showPage()
		libro.save()
