def find_index(types, type):
				for i, item in enumerate(types):
					if item == type:
						position = i
						return position
					
general_cointainer_label = "Información General"

# URLs
header_url = "img/header-k2-advanced-es.png"
building_url = "img/building-a.png"
building_a_b_url = "img/building-a-b.png"

building_aa_b_url = "img/building-aa-b.png"
building_a_bb_url = "img/building-a-bb.png"     
building_aa_bb_url = "img/building-aa-bb.png"

building_a_b_c_url = "img/building-a-b-c.png"
building_aa_b_c_url = "img/building-aa-b-c.png"
building_a_bb_c_url = "img/building-a-bb-c.png"
building_a_b_cc_url = "img/building-a-b-cc.png"
building_aa_bb_c_url = "img/building-aa-bb-c.png"
building_aa_b_cc_url = "img/building-aa-b-cc.png"
building_a_bb_cc_url = "img/building-a-bb-cc.png"
building_aa_bb_cc_url = "img/building-aa-bb-cc.png"

building_url = "img/building-a.png"

foso_url = "img/foso.png"
foso_2_url = "img/foso-2.png"
foso_wide_url = "img/foso-wide.png"
foso_cmi_url = "img/foso-cmi.png"
urgente_url = "img/urgente.png"

roof_url = "img/roof-wide.png"
roof_cp_url = "img/roof-cp.png"

building_active_url = "building-active.png"

delivery_l = "LUGAR DE ENREGA"
deliveries = ["Elegir", "Madrid", "Barcelona", "Otro..."]
other_address_l = "INTRODUCIR DIRECCIÓN COMPLETA:"

cv_l = "SV"
cvs = ["Elegir", "R00", "R02", "R02", "R03", "R05", "R06", "R07", "R11", "R14", "R15", "R17", "R22", "R31", "R33", "R39", "R40", "R43", "R52", "R54", "R59", "R59", "R68", "R70", "R71", "R76", "R79", "R80", "R81", "R83", "R86", "R87", "R89", "R90", "R94", "R95", "R97", "R98", "R99", "RA2", "RA4", "RA6", "RA7", "RA9", "RB1", "RB2", "RB3", "RB3", "RB3", "RB3", "RB3", "RB3", "RB4", "RB6", "RB8", "RB9", "RC1", "RC2", "RC3", "RC4", "RC6", "RC5", "RC7", "RC8", "RC9", "RD1", "RD2", "RD3", "RD5", "RD6", "RD7", "RD8", "RD9", "RE1", "RE2", "RE3", "RE4", "RE5", "RE6", "RE7", "RE8", "RE9", "RF1", "RF2", "RF3", "RF4", "RF5", "RF6", "RF7", "RF8", "RF9", "RG1", "RG2", "RG3", "RG4", "RG5", "RG6", "RG7", "RG8", "RG9", "RH1", "RH2", "RH3", "RH4", "RH5", "RH6", "RH7", "RH8", "RH9", "RI0", "RI1", "RI2", "RI3", "RI3", "RI3", "RI6", "RI5", "RI9", "RI8", "RJ2", "RJ3", "RJ6", "RJ4", "BE01", "FA06", "IR01"]

other_valve_l = "OTRO MODELO"

reference_l="NUMERO DE ORDEN (SAP)"
date_l="FECHA PEDIDO"
delivery_date_l="ENTREGA EN:"
comments_l = 'Texto o explicaciones:'
man_types = ["Elegir:", "Gearless", "VVVF", "Hidráulica"]
man_type_l = "MODELO"
type_l = "TIPO"
stops_l = "PARADAS"
quantity_l = "CANTIDAD"
types = ["Elegir:", "Universal", "Selectiva Bajada", "Selectiva Subida/Bajada"]
connections = ["Elegir:","SIMPLEX", "DUPLEX", "TRIPLEX", "CUADRUPLEX", "QUINTUPLEX", "SEXTUPLEX"] 
connection_l = "CONEXIÓN"
boarding_l = "EMBARQUES"
boardings = ["Elegir:", "1", "2", "3"]
boardings = ["Elegir:", "1", "2", "3"]
norm_l = "NORMAS"
norms = ["Elegir:", "EN81-1/2 Ascensores eléctricos", "EN81-20/50 Reglas de diseño, cálculos, exámenes y ensayos de componentes de ascensor", "EN81-21 Ascensores nuevos de pasajeros y de pasajeros y cargas en edificios existentes", "EN81-28 Alarmas a distancia en ascensores de pasajeros y pasajeros y cargas", "EN81-70 Accesibilidad a los ascensores de personas, incluyendo personas con discapacidad", "EN81-71 Ascensores resistentes al vandalismo", "EN81-72 Ascensores contra incendios", "EN81-73 Comportamiento de los ascensores en caso de incendio", "U36 No parada ascensor en planta siniestrada"]
secuencia_l = "SECUENCIA"
central_l = "DATOS DE LA MAQUINA/CENTRAL"
data_l = "DATOS GENERALES"
cabin_l = "ELEMENTOS CABINA Y EXTERIORES"
valves_type_l = "TIPO VÁLVULAS"
valves_types = ["Elegir:", "CONVENCIONALE", "ELECTRÓNICAS"]
machine_type_l = "TIPO MAQUINA"
machine_types_h = ["Elegir:", "HIDRAULICO DIRECTO", "HIDRAULICO_ESTR.TRIANG"]
machine_types_a = ["Elegir:", "ELECT._VVVF_SIN_ENCODER", "ELECT._VVVF_CON_ENCODER", "GEARLESS_"]
encoder_types = ["Elegir:", "SSI", "ENDAT", "INCREMENTAL", "SINCOS", "OTRO"]
encoder_type_l = "ENCODER MOD."
valve_models = ["Elegir:", "GMV", "BUCHER", "OTRO"]
valve_models_l = "MODELO VÁLVULA"
situations = ["Elegir:", "SUPERIOR CCM", "INTERMEDIO CCM", "INFERIOR CCM", "SCM (SUP.HUECO)"]
situation_l = "SITUACIÓN MAQUINA"
wardrobe_side_l = "APERTURA ARMARIO"
wardrobe_sides = ["Elegir:", "IZQUIERDA", "DERECHA", "INDISTINTA"]
speed_l = "VELOCIDAD (M/S)"
current_l = "POTENCIA (CV)"
consumo_l = "INT NOM (A)"
vbreak_l = "T. FRENO/VALV. (V)"
power_l = "FUERZA (V)"
neutral_l = "NEUTRO"
neutrals = ["Elegir:", "SÍ", "NO"]
cabin_door_l = "PUERTAS DE CABINA"
operator_type_l = "TIPO OPERADOR"
operator_types = ["Elegir:", "VVVF", "MONOF. 220V", "TRIFAS. 220V", "TRIFAS. 380V", "BUS - AUTON.", "BUS - C/C", "MANUAL"]
manufacturer_l = "FABRICANTE"
door_model_l = 'MODELO PUERTA'
door_models = ["Elegir:", "2 H CENTRAL", "2 H LATERAL", "3 H LATERAL", "4H CENTRAL", "6H CENTRAL", "BUS", "CON CORTINA"]
consumo_door_motor_l = 'CONSUMO MOTOR (A)'
current_door_l = 'TENS.V'
levas = ["Elegir:", "SÍ", "NO"]
leva_l = "LEVA"
floor_door_l = "PUERTAS EMBARQUE 1"
floor_doors = ["Elegir:", "AUTOMÁTICA", "SEMIAUTOMÁTICA"]
heights_title_l = "**ALTURAS**"
####
operator_type_l2 = "TIPO OPERADOR 2"
manufacturer_l2 = "FABRICANTE 2"
door_model_l2 = 'MODELO PUERTA 2'
consumo_door_motor_l2 = 'CONSUMO MOTOR (A) 2'
current_door_l2 = 'TENS.V 2'
leva_l2 = "LEVA 2"
floor_door_l2 = "PUERTAS EMBARQUE 2"
####

####
operator_type_l3 = "TIPO OPERADOR 3"
manufacturer_l3 = "FABRICANTE 3"
door_model_l3 = 'MODELO PUERTA 3'
consumo_door_motor_l3 = 'CONSUMO MOTOR (A) 3'
current_door_l3 = 'TENS.V 3'
leva_l3 = "LEVA 3"
floor_door_l3 = "PUERTAS EMBARQUE 3"
####

submit_button_l = "Enviar"


fotocells = ["Elegir:", "DE BOTON", "CORTINA"]
fotocell_l = "FOTOCÉLULA"
fotocell_current_l = "TENSIÓN FOTOCÉLULA"
fotocell_current_acdc_l = "V"
fotocell_current_acdcs = ["Elegir:", "AC", "CC"]
apreture_l = "APERTURA ANTICIPADA PUERTAS"
contact_l = "CONTACTO TRAMPILLA"
weight_l = "PESACARGAS"
weights = ["Elegir:", "ELECTRÓNICO", "MECÁNICO"]
a3_l = "CUMPLIR A3 - FABRICANTE DEL EQUIPO"
gong_1_l = "GONG DE LLEGADA"
gong_2_l = "GONG EN PISOS"
flechas_l = "FLECHAS DIR.EMB. CABINA"
line_l = "LINEA DE BOTONERAS"
limitator_l = "LIMITADOR VELOCIDAD CON REARME A DISTANCIA"
limitators = ["Elegir:", "CABIN", "PARTE SUPERIOR DEL HUECO"]
foso_l = "FOSO REDUCIDO"
huida_l = "HUIDA REDUCIDA"
bobina_count_l = "NUM.BOBINAS"
limitator_current_l = "TENSIÓN"

## Heights Labels
foso_distance_l = "FOSO DISTANCIA"
huida_distance_l = "HUIDA DISTANCIA"
floor_number_l = "Número de Pisos"
comments_heights_l = "Número de Pisos"

reference = ''
comments = ''
man_type = ''
quantity = ''
man_type = ''
type = ''
connection = ''
boarding = ''
norm = ''
secuencia = ''
machine_type = ''
encoder_type = ''
valves_type = ''
valve_model = ''
situation = ''
wardrobe_side = ''
speed = ''
current = ''
consumo = ''
vbreak = ''
power = ''
neutral = ''
operator_type = ''
manufacturer = ''
door_model = ''
consumo_door_motor = ''
current_door = ''
leva = ''
floor_door = ''
operator_type2 = ''
manufacturer2 = ''
door_model2 = ''
consumo_door_motor2 = ''
current_door2 = ''
leva2 = ''
floor_door2 = ''
operator_type3 = ''
manufacturer3 = ''
door_model3 = ''
consumo_door_motor3 = ''
current_door3 = ''
leva3 = ''
floor_door3 = ''

fotocell = ''
fotocell_current = ''
fotocell_current_acdc = ''
apreture = ''
weight = ''
a3 = ''
gong_1 = ''
gong_2 = ''
flechas = ''
line = ''
limitator = ''
bobina_count = 0
limitator_current = ''
foso = ''
huida = ''
comments_h = ''

stops = 2
dca = 0 
dcl = 0
dcfh = 0
dcb = 0
dcm = 0
recorrido = 0
distancia_foso = 0
distancia_huida = 0

