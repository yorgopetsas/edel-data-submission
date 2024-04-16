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

roof_url = "img/roof-wide.png"

building_active_url = "building-active.png"

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

