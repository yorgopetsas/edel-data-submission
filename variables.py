###########################################
# other_l = "Otra"
# central_l = "**CENTRAL HIDRÁULICA**"
### Hidraulic Motor
###########################################
## General
form_types = ["Elegir:", "Pedido", "Oferta"]
stages = ["Elegir:", "I.E.P. Completa", "Media I.E.P. Cabina", "Solo Maniobra"]
header_url = "img/header-k2-advanced-es.png"
submittion_confirmation = 'Form submitted! Data has been saved as CSV and PDF.'

### General Labels
client_l="Cliente"
client_lo="Cliente 🚩"
date_l="Fecha"
reference_l="Referencia"
delivery_date_l="Fecha Entrega"
submit_button_l = "Enviar"
form_type_l = "Tipo de Solicitud"
form_type_lo = "Tipo de Solicitud 🚩"
stage_l = "Se Solicita"
stage_lo = "Se Solicita 🚩"
general_cointainer_label = "Información General"
edit_general_info_l = "Haga click aquí para editar la información general"

## Button Lables
next_button_l = "Siguiente Paso"
previous_button_l = "Paso Anterior"

### Mensajes
# warning = "**Rellene todos los campos para poder enviar la solicitus.**"
comments_l = "Comentarios"

## Maniobra Type
man_types = ["Elegir:", "Eléctrica", "Hidráulica"]

### Maniobra Type Labels
man_type_l = "Tipo de Maniobra"
man_type_lo = "Tipo de Maniobra 🚩"

## Motor
motor_types = ["Elegir:", "Gearless", "Geared"]
motor_currents = ["Elegir:", "230V", "400V"]

### Motor Labels
motor_l = "MOTOR"
motor_type_l = "Tipo de Motor"
motor_type_lo = "Tipo de Motor 🚩"
motor_current_l = "Tensión de Motor"
consumo_l = "Consumo A"
potencia_motor_cv_l = "Potencia Motor CV"
break_tension_l = "Tensión Freno V"
potencia_motor_kw_l = "Potencia Motor KW"

### Gearless Motor Labels
rpm_l = "R.P.M."
vel_l = "Vel. m/s"
enconder_type_l = "Tipo encoder"
encoder_model_l = "Modelo encoder"

## Central
starter_types = ["Elegir:", "Directo", "Estrella Triangulo"]
central_currents = ["Elegir:", "230V", "400V"]

### Central Labels
central_current_l = "Tensión Central"
fabricante_central_l = "Fabricante de la Central"
potencia_central_cv_l = "Potencia Central CV"
central_model_l = "Modelo"
potencia_central_kw_l = "Potencia Central KW"
central_valves_type_l = "Tipo de Valvula"
central_valves_type_model_l = "Modelo de valvula"
consumo_central_l = "Consumo Central A"
valve_pressure_fast_l = "Rápida"
valve_pressure_downhill_l = "Bajada"
start_type_l = "Tipo de Arranque"
valve_pressure_climb_l = "Subida"
valve_pressure_emergency_l = "Emergencia"

## Maniobra
wardrobes_el = ["Elegir:", "CCM", "SCM", "SCM INOX", "MDP", "MDP Armario"]
maniobras = ["Elegir:", "2 Velocidades", "VF"]
restates = ["Elegir:", "Manual", "Palanca Freno", "Automatico", "Por SAI"]

### Maniobra Labels
maniobra = "**MANIOBRA**"
wardrobe_l = "Armario"
wardrobe_el_l = "Armario Tipo"
maniobra_motor_l = "Motor"
mabra_l = "Maniobra"
restate_l = "Rescate"

### Maniobra Hidraulic 
wardrobes = ["Elegir:", "CCM", "SCM Dentro Central"]
renivelations = ["Elegir:", "Puerta Abierta", "Puerta Cerrada"]
starterzs = ["Elegir:", "Suministrar", "Existente"]

### EXTRAS EN MANIOBRA MISSING ###

### Maniobra Hidraulic Labels
starter_l = "Arranque"
renivelation_l  = "Renivelación"
starterz_l = "Arrancador"

## Electric Installation
installations = ["Elegir:", "Obra Nueva", "Reforma", "Reforma Integral"]
standarts = ["Elegir:", "EN 81.16", "EN 81.20/50" ]
standarts_additional = ["Elegir:", "En 81.71 CAT. 1", "En 81.71 CAT. 2", "En 81.72", "En 81.73"]
line_currents = ["Elegir:", "230V", "400V"]
installation_types = ["Elegir:", "Hilo a Hilo", "CAN-BUS MIXTA (cabina hilo a hilo exteriores)", "CAN-BUS TOTAL (cabina y exteriores)"]
calls_types = ["Elegir:", "Universal", "Selectivo Bajada", "Subida / Bajada" ]
positions_1s = ["Elegir:", "Kit de Imanes", "Kit Fotorruptor", "Kit encoder Hueco"]
positions_2s = ["Elegir:", "Kit Biestables", "Paradores FC"]
                 
### Electric Installation Labels
installation_title = "**INSTALACIÓN ELÉCTRICA**"
installation_l = "Instalación"
standart_l = "Nomrativa"
standart_additional_l = "Otras Normas"
line_current_l = "Tensión Linea"
stops_l = "Numero de Paradas"
stops_lo = "Numero de Paradas 🚩"
sec_stop_l = "Sec Pisos"
installation_type_l = "Tipo de Instalación"
calls_type_l = "Tipo de llamadas"
positions_1_l = "Posicionamiento 1"
positions_2_l = "Posicionamiento 2"

## Puertas de Cabina
tipo_puertas = ["Elegir:", "Automáticas", "Manuales", "Sin Puertas"]
operators = ["Elegir:", "Monofásico", "VF (Libre Tensión)", "Trifásico"]
levas = ["Elegir:", "Leva Monofásica", "Leva Trifásica", "Leva Mecánica"]
fotocells = ["Elegir:", "Barrera", "Boton (tipo Telco)"]
provides = ["Elegir:", "Sí", "No", "Existente"]
embarques = ["**Simple**", "**Mixto**"]
apretures = ["**SELECTIVA**", "**SIMULTÁNEA**"]

### Puertas de Cabina Labels
puertas_title = "**PUERTAS DE CABINA**"
tipo_puertas_l = "Tipo de Puertas"
operator_l = "Operador"
leva_l  = "Leva"
leva_current_l = "Tensión Leva"
puertas_model_l = "Modelo de Puertas"
emergency_exit_kit = "KIT ABREPUERTAS DE EMERGENCIA"
kit_apertura_l = 'Sí (no incluye el KIT)'
fotocell_title_l = "**Fotocélula**"
fotocell_l = "Fotocélula"
provide_l = "Suministrar"
foto_current_l = "Tensión Fotocélula"
operator1_l = "OPERADOR 1 ACTÚA EN PISOS"
operator2_l = "OPERADOR 2 ACTÚA EN PISOS"
floors_1door_l = "PLANTAS CON 1 PUERTA"
floors_2door_l = "PLANTAS CON 2 PUERTAS"
embarque_l = "Tipo de DOBLE EMBARQUE"
apreture_l = "Apertura"

## PUERTAS DE RELLANO
door_types = ["Elegir:", "Automática", "Semiautomática", "Mixtas"]

### PUERTAS DE RELLANO Labels
rellano_title = "**PUERTAS DE RELLANO**"
door_type_l = "Tipo de Puerta"
automatic_doors_l = "Plantas con Puerta manuales/semiautomáticas"
semiautomatic_doors_l = "Plantas con Puerta automáticas"

## Otros Datos
limitadors = ["Elegir:", "Viajando en cabina", "En el hueco", "En el cuarto de Máquinas"]
a3_standarts_electric = ["Elegir:", "Micros Friend", "Limitador"]
a3_standarts_hidraulic= ["Elegir:", "Válvulas NGV", "Doble válvula mecánica"]
light_paths = ["Elegir:", "Solo Preparación", "Bombillas", "Flourescente LED", "Tira LED"]
fire_securitys = ["Elegir:", "Solo Señal", "Llavín en cabina y Relleno", "Llavín solo en Relleno"]
weighings = ["Elegir:", "Solo Preparación", "De cables", "Bajo cabina", "De bancada"]
light_alerts = ["Elegir:", "Por contacto en cerraduras", "Por señal en maniobra"]

### Otros Datos Labels
otros_title = "**OTROS DATOS**"
limitador_l = "Limitador"
limitador_current_l = "Tensión del Limitador"
a3_standart_electric_l = "Norma A3 Eléctrico"
a3_standart_hidraulic_l = "Norma A3 Hidráulico"
weighing_l = "PESACARGAS"
light_paths_l = "ROSARIO DE LUCES"
fire_security_l = "Bomberos"
light_alert_l = "Luminoso de está"
cables_amount_l = "Numero de Cables"
section_l = "Sección"
extras_l = "Extras"

## SITUACIÓN CUARTO MÁQUINAS Y DISTANCIAS
situations = ["Elegir:", "Superior", "Intermedia", "Inferior"]
service_rooms = ["Elegir:", "Solo Stop", "Bot. Completa"]
lower_fases = ["Elegir:", "Estandar", "EN 81.21"]
lower_escapes = ["Elegir:", "Estandar", "EN 81.21"]

### SITUACIÓN CUARTO MÁQUINAS Y DISTANCIAS Labels
situation_container_l = "**Situación Cuarto Máquinas y Distancias**"
situation_l = "Situación"
flat_indication_l = "Intermedia Indicar Piso"
service_room_l = "Cuarto de Poleas"
frame_distance_l = "Distancia entre el cuadro y el suelo de la última o primera parada"
lower_fase_l = "Foso Menor"
distance_l = "Distancia"
motor_distance_l = "Distancia entre el cuadro y el motor o central hidráulica."
lower_escape_l = "Huida Menor"
wardrobe_flat_l = "Situación del Armario de Maniobra"
mecanic_l = "Mecánica de:"

## Heights Labels
floor_number_l = "Número de Pisos"
heights_title = "**ALTURAS**"
huida_distanca_l = "Huida Distancia"
foso_distance_l = "Foso Distancia"
huida_l = "Huida Distancia"
foso_l = "Foso Distancia"
comments_heights_l = 'Observaciones'

## Botoner de Cabina
panel_types = ["Elegir:", "De Columna (baquetón toda la cabina)", "De Placa (Semicolumna Enrasada)", "De Superficie (Sobresale de la pared)"]
back_boxes = ["Elegir:", "Sí", "No", "Existente"]
emergency_lights = ["Elegir:", "Sí Estandar", "Sí cumpliendo EN 81.20", "No", "Existente"]
emergency_light_colors = ["Elegir:", "Rojo", "Azul"]
display_types = ["Elegir:", "Rotativo Rojo", "Rotativo Azul", "TFT Raffaello 2,8 pulgadas", "Mini LCD 3 Pulgadas", "LCD Azul Edel 5,7 Pulgadas", "TFT Color Edel 5,7 Pulgadas", "TFT DMG 5,7 Pulgadas", "TFT MK-800 7 Pulgadas", "TFT DMG 10 Pulgadas"]
button_types = ["Elegir:", "Edel (Aro Cromado)", "Edel White (Aro Cromado)", "Edel Black (Aro Black)", "DMG BLX (Cuadrado)", "DMG BM (Redondo)", "DMG Dardo"]
engravings = ["Elegir:", "En place Inox", "En Chapa Botonera"]
phone_selects = ["Elegir:", "Sí", "No", "Existente", "Teléfono + GSM"]
voice_simulations = ["Elegir:", "Sí", "No", "Existente"]
edel_connects = ["Elegir:", "GSM EdelConnect 875 + Modulo Tlf 791", "GSM Liftcom Nettel con cable Advanced", "Kit TFT Color Mk-800 7 Pulgadas + GSM 875 + Tlf 791"]
keys = ["Elegir:", "Sí", "No", "Existente"]
functions = ["Elegir:", "Llamada a Piso", "Prioridad cabina", "Parar Ascensor", "Bomberos cabina y exteriores", "Bomberos solo exteriores"]

### Botoner de Cabina Labels
botonera_cabina_title = "**Botonera Cabina**"
botonera_cabina_toggle_l = "Quiero Botonera de Cabina"
panel_floor_l = "Número de paradas"
floors_sequence_l = "Secuencia de pisoso"
panel_type_l = "Tipo de botonera"
back_box_l = "Cajetín trasero"
edel_standart_l = "MEDIDAS ESTANDAR EDEL (PONER MEDIDAS)"
column_height_l = "Alto MEDIDA"
bottom_mesurement_l = "Fondo MEDIDA"
column_width_l = "Ancho MEDIDA"
clued_mesurement_l = "Plegado MEDIDA"
column_fixture_top_l = "Fijación Superior"
column_fixture_bottom_l = "Fijación Inferior"
middle_fixture_l = "Fijación intermedia"
middle_fixture_distance_l = "Distancia fijación intermedia"
emergency_light_l = "Luz de Emergencia"
emergency_light_color_l = "Iluminación"
display_type_l = "Tipo de Display"
button_type_l = "Tipo de Pulsador"
braille_button_l = "Braille"
double_contact_alarm_l = "Alarma Doble Contacto"
door_closer_l = "Cierrapuertas"
button_phone_l = "Pulsador Teléfono"
stop_button_l = "STOP"
grabados_title = "**Grabados**"
engraving_l = "Grabados"
anagram_logo_l = "Anagrama (Logo Cliente)"
forbiden_smoke_l = "Prohibido Fumar"
anagram_retro_l = "Anagrama Retroiluminado"
emergency_phone_text_l = "Texto Teléfono de Emergencia"
engravings_kg_l = "KG"
engraving_rae_l = "RAE"
engravings_persons_l = "Personas"
engravings_phone_number_l = "Número de teléfono"
engravings_other_l = "Otros Grabados"
telefono_title = "**Teléfono**"
phone_select_l = "Teléfono"
other_band_model_l = "Otro Marca/Modelo"
voice_simulation_l = "Sintesis de Voz"
voice_simulation_language_l = "Idioma"
edel_connect_l = "Telecontrol EdelConnect"
key_l = "Llavines"
function_l = "Función"
functions_floors_l = "En pisos"
functions_other_l = "Otra Función"

## Botoner de Exteriores
options_1 = ["Elegir:", "Solo Pulsador llamada", "Llamada + Torquel Display", "Llamada + Flechas", "Llamada + Puerta Abierta", "Llamada + Piloto Está"]
options_2 = ["Elegir:", "Solo Pulsador llamada", "Llamada + Torquel Display", "Llamada + Flechas", "Llamada + Puerta Abierta", "Llamada + Piloto Está"]
options_3 = ["Elegir:", "Solo Pulsador llamada", "Llamada + Torquel Display", "Llamada + Flechas", "Llamada + Puerta Abierta", "Llamada + Piloto Está"]

### Botoner de Exteriores Labels
botonera_external_title = "**Botonera de Exteriores**"
botonera_external_toggle_l = "Quiero Botonera de Exteriores"
option_1_l = "Opción 1"
options_1_height_l = "Opción 1 Alto MEDIDA"
options_1_width_l = "Opción 1 Ancho MEDIDA"
options_1_quantity_l = "Opción 1 Cantidad"
option_2_l = "Opción 2"
options_2_height_l = "Opción 2 Alto MEDIDA"
options_2_width_l = "Opción 2 Ancho MEDIDA"
options_2_quantity_l = "Opción 2 Cantidad"
option_3_l = "Opción 3"
options_3_height_l = "Opción 3 Alto MEDIDA"
options_3_width_l = "Opción 3 Ancho MEDIDA"
options_3_quantity_l = "Opción 3 Cantidad"
options_other_l = "Otras Opciones"
options_other_height_l = "Otras Opciones Alto MEDIDA"
options_other_width_l = "Otras Opciones Ancho MEDIDA"
options_other_quantity_l = "Otras Opciones Cantidad"

## NORMA EN 81.70 Label
standart_title = "**NORMA EN 81.70**"
beep_button_l = "Zumbador (BIP Pulsador)"
button_braille_l = "Otras Braille Pulsadores"
exterior_gong_l = "Gong de exteriores"
green_arrow_l = "Aro Verde Planta Salida"
arrow_next_l = "Flechas de próxima partida"
inductive_loop_l = "Bucle inductivo"
location_l = "Ubicación"

# Initiations
stage = ""
form_type = ""
motor_finished = 0
installation_finished = 0
cabin_finished = 0
door_finished = 0
other_finished = 0
door_finished = 0
situation_finished = 0
height_finished = 0
plate_finished = 0
ext_plate_finished = 0
norm_finished = 0
submit_button = 0
client = ""
central_current = 0 
motor_current = 0
reference = ""
date = ""
delivery_date = ""
man_type = ""
central_current = 0 
potencia_central_cv = 0 
potencia_central_kw = 0 
consumo_central = 0 
starter_type = 0 
fabricante_central = 0 
central_model = 0 
central_valves_type = 0 
valve_pressure_fast = 0 
valve_pressure_climb = 0 
central_valves_type_model = 0 
valve_pressure_downhill = 0 
valve_pressure_emergency = 0 
wardrobe = 0 
renivelation = 0 
starter = 0 
starterz = 0
motor_type = "" 
potencia_motor_cv = 0 
potencia_motor_kw = 0 
consumo = 0 
break_tension = 0 
rpm = 0 
vel = 0 
enconder_type = 0 
encoder_model = 0 
wardrobe_el = 0 
mabra = 0 
mot_second = 0 
restate = 0 
installation = 0 
line_current = 0 
standart = 0 
stops = ""
installation_type = 0
calls_type = 0
positions_1 = 0
positions_2 = 0
standart_additional = 0 
sec_stop = 0 
tipo_puerta = 0 
leva = 0 
puertas_model = 0 
operator = 0 
leva_current = 0 
kit_apertura = 0 
fotocell = 0 
provide = 0 
foto_current = 0 
embarque = 0 
apreture = 0 
floors_1door = 0 
floors_2door = 0 
door_type = 0 
automatic_doors = 0 
semiautomatic_doors = 0 
limitador = 0 
light_path = 0 
limitador_current = 0 
fire_security = 0 
a3_standart = 0 
weighing = 0 
light_alert = 0 
extras = 0 
cables_amount = 0 
section = 0 
situation = 0 
frame_distance = 0 
motor_distance = 0 
flat_indication = 0 
lower_fase = 0 
lower_escape = 0 
mecanic = 0 
service_room = 0 
distance = 0 
wardrobe_flat = 0 
huida = 0 
foso = 0 
comments = 0 
panel_floor = 0 
panel_type = 0 
floors_sequence = 0 
back_box = 0 
edel_standart = 0 
column_height = 0 
column_width = 0 
column_fixture_top = 0 
middle_fixture = 0 
bottom_mesurement = 0 
clued_mesurement = 0 
column_fixture_bottom = 0 
middle_fixture_distance = 0 
emergency_light = 0 
display_type = 0 
double_contact_alarm = 0
door_closer = 0
button_phone = 0
stop_button = 0
emergency_light_color = 0 
button_type = 0 
braille_button = 0
anagram_logo = 0 
anagram_retro = 0
engraving = 0
engravings_kg = 0 
engravings_persons = 0 
engraving = 0 
forbiden_smoke = 0 
emergency_phone_text = 0 
engravings_rae = 0 
engravings_phone_number = 0 
engravings_other = 0 
phone_select = 0 
voice_simulation = 0 
edel_connect = 0 
function = 0 
other_band_model = 0
voice_simulation_language = 0 
key = 0 
functions_floors = 0
functions_other = 0
option_1 = 0 
options_1_width = 0 
options_1_height = 0 
options_1_quantity = 0 
option_2 = 0 
options_2_width = 0 
options_2_height = 0 
options_2_quantity = 0 
option_3 = 0 
options_3_width = 0 
options_3_height = 0 
options_3_quantity = 0 
options_other = 0 
options_other_width = 0 
options_other_height = 0 
options_other_quantity = 0 
beep_button = 0 
green_arrow = 0 
location = 0 
button_braille = 0 
arrow_next = 0 
exterior_gong = 0 
inductive_loop = 0

var_list_gearless = ["client", "reference", "date", "delivery_date", "stage", "form_type", "man_type", "central_current", "potencia_central_cv", "potencia_central_kw", "consumo_central", "starter_type", "fabricante_central", "central_model", "central_valves_type", "valve_pressure_fast", "valve_pressure_climb", "central_valves_type_model", "valve_pressure_downhill", "valve_pressure_emergency", "wardrobe", "renivelation", "starter", "starterz", "motor_type", "motor_current", "potencia_motor_cv", "potencia_motor_kw", "consumo", "break_tension", "rpm", "vel", "enconder_type", "encoder_model", "wardrobe_el", "mabra", "mot_second", "restate", "installation", "line_current", "standart", "stops", "standart_additional", "sec_stop", "installation_type", "calls_type", "positions_1", "positions_2", "tipo_puerta", "leva", "puertas_model", "operator", "leva_current", "kit_apertura", "fotocell", "provide", "foto_current", "embarque", "apreture,floors_1door", "floors_2door", "door_type", "automatic_doors", "semiautomatic_doors", "limitador", "light_path", "limitador_current", "fire_security", "a3_standart", "weighing", "light_alert", "extras", "cables_amount", "section", "situation,frame_distance", "motor_distance", "flat_indication", "lower_fase", "lower_escape", "mecanic", "service_room", "distance", "wardrobe_flat", "huida", "foso", "comments", "panel_floor", "panel_type", "floors_sequence", "back_box", "edel_standart", "column_height", "column_width", "column_fixture_top", "middle_fixture", "bottom_mesurement", "clued_mesurement", "column_fixture_bottom", "middle_fixture_distance", "emergency_light", "display_type", "emergency_light_color", "button_type", "braille_button", "double_contact_alarm", "door_closer", "button_phone", "stop_button", "anagram_logo", "anagram_retro", "engraving", "engravings_kg", "engravings_persons", "forbiden_smoke", "emergency_phone_text", "engravings_rae", "engravings_phone_number", "engravings_other", "phone_select", "voice_simulation", "edel_connect", "function", "other_band_model", "voice_simulation_language", "key", "functions_floors", "functions_other", "option_1", "options_1_width", "options_1_height", "options_1_quantity", "option_2", "options_2_width", "options_2_height", "options_2_quantity", "option_3", "options_3_width", "options_3_height", "options_3_quantity", "options_other", "options_other_width", "options_other_height", "options_other_quantity", "beep_button", "green_arrow", "location", "button_braille", "arrow_next", "exterior_gong", "inductive_loop"]

def initialize_labels_list_gearless():
    labels_list = [client_l, reference_l, date_l, delivery_date_l, maniobra, central_current_l ,potencia_central_cv_l, potencia_central_kw_l, consumo_central_l, start_type_l, fabricante_central_l, central_model_l, central_valves_type_l, valve_pressure_fast_l, valve_pressure_climb_l, central_valves_type_model_l, valve_pressure_downhill_l, valve_pressure_emergency_l, wardrobe_l, renivelation_l, starter_l, starterz_l, motor_type_l, motor_current_l, potencia_motor_cv_l, potencia_motor_kw_l, consumo_l, break_tension_l, rpm_l, vel_l, enconder_type_l, encoder_model_l, wardrobe_el_l, mabra_l, maniobra_motor_l, restate_l, installation_l, line_current_l, standart_l, stops_l, standart_additional_l, sec_stop_l, installation_type_l, calls_type_l, positions_1_l, positions_2_l, tipo_puertas_l, leva_l, puertas_model_l, operator_l, leva_current_l, kit_apertura_l, fotocell_l, provide_l, foto_current_l, embarque_l, apreture_l, floors_1door_l, floors_2door_l, door_type_l, automatic_doors_l, semiautomatic_doors_l, limitador_l, light_paths_l, limitador_current_l, fire_security_l, a3_standart_electric_l, weighing_l, light_alert_l, extras_l, cables_amount_l, section_l, situation_l,frame_distance_l, motor_distance_l, flat_indication_l, lower_fase_l, lower_escape_l, mecanic_l , service_room_l, distance_l, wardrobe_flat_l, huida_l, foso_l, comments_l, panel_floor_l, panel_type_l, floors_sequence_l, back_box_l, edel_standart_l, column_height_l, column_width_l, column_fixture_top_l, middle_fixture_l, bottom_mesurement_l, clued_mesurement_l, column_fixture_bottom_l, middle_fixture_distance_l, emergency_light_l, display_type_l, emergency_light_color_l, button_type_l, braille_button_l, double_contact_alarm_l, door_closer_l, button_phone_l, stop_button_l, anagram_logo_l, anagram_retro_l, engraving_l, engravings_kg_l, engravings_persons_l, forbiden_smoke_l, emergency_phone_text_l, engraving_rae_l, engravings_phone_number_l, engravings_other_l, phone_select_l, voice_simulation_l, edel_connect_l, function_l, other_band_model_l, voice_simulation_language_l, key_l, functions_floors_l, functions_other_l, option_1_l, options_1_width_l, options_1_height_l, options_1_quantity_l, option_2_l, options_2_width_l, options_2_height_l, options_2_quantity_l, option_3_l, options_3_width_l, options_3_height_l, options_3_quantity_l, options_other_l, options_other_width_l, options_other_height_l, options_other_quantity_l, beep_button_l, green_arrow_l, location_l, button_braille_l, arrow_next_l, exterior_gong_l, inductive_loop_l]

    return labels_list

def initialize_labels_list_geared():
    labels_list = [client_l, reference_l, date_l, delivery_date_l, maniobra, central_current_l ,potencia_central_cv_l, potencia_central_kw_l, consumo_central_l, start_type_l, fabricante_central_l, central_model_l, central_valves_type_l, valve_pressure_fast_l, valve_pressure_climb_l, central_valves_type_model_l, valve_pressure_downhill_l, valve_pressure_emergency_l, wardrobe_l, renivelation_l, starter_l, starterz_l, motor_type_l, motor_current_l, potencia_motor_cv_l, potencia_motor_kw_l, consumo_l, break_tension_l, wardrobe_el_l, mabra_l, maniobra_motor_l, restate_l, installation_l, line_current_l, standart_l, stops_l, standart_additional_l, sec_stop_l, installation_type_l, calls_type_l, positions_1_l, positions_2_l, tipo_puertas_l, leva_l, puertas_model_l, operator_l, leva_current_l, kit_apertura_l, fotocell_l, provide_l, foto_current_l, embarque_l, apreture_l, floors_1door_l, floors_2door_l, door_type_l, automatic_doors_l, semiautomatic_doors_l, limitador_l, light_paths_l, limitador_current_l, fire_security_l, a3_standart_electric_l, weighing_l, light_alert_l, extras_l, cables_amount_l, section_l, situation_l,frame_distance_l, motor_distance_l, flat_indication_l, lower_fase_l, lower_escape_l, mecanic_l , service_room_l, distance_l, wardrobe_flat_l, huida_l, foso_l, comments_l, panel_floor_l, panel_type_l, floors_sequence_l, back_box_l, edel_standart_l, column_height_l, column_width_l, column_fixture_top_l, middle_fixture_l, bottom_mesurement_l, clued_mesurement_l, column_fixture_bottom_l, middle_fixture_distance_l, emergency_light_l, display_type_l, emergency_light_color_l, button_type_l, braille_button_l, double_contact_alarm_l, door_closer_l, button_phone_l, stop_button_l, anagram_logo_l, anagram_retro_l, engraving_l, engravings_kg_l, engravings_persons_l, forbiden_smoke_l, emergency_phone_text_l, engraving_rae_l, engravings_phone_number_l, engravings_other_l, phone_select_l, voice_simulation_l, edel_connect_l, function_l, other_band_model_l, voice_simulation_language_l, key_l, functions_floors_l, functions_other_l, option_1_l, options_1_width_l, options_1_height_l, options_1_quantity_l, option_2_l, options_2_width_l, options_2_height_l, options_2_quantity_l, option_3_l, options_3_width_l, options_3_height_l, options_3_quantity_l, options_other_l, options_other_width_l, options_other_height_l, options_other_quantity_l, beep_button_l, green_arrow_l, location_l, button_braille_l, arrow_next_l, exterior_gong_l, inductive_loop_l]

    return labels_list

def initialize_labels_list_hidraulic():
    labels_list = [client_l, reference_l, date_l, delivery_date_l, maniobra, central_current_l, potencia_central_cv_l, potencia_central_kw_l, consumo_central_l, start_type_l, fabricante_central_l, central_model_l, central_valves_type_l, valve_pressure_fast_l, valve_pressure_climb_l, central_valves_type_model_l, valve_pressure_downhill_l, valve_pressure_emergency_l, wardrobe_l, renivelation_l, starter_l, starterz_l, motor_type_l, motor_current_l, potencia_motor_cv_l, potencia_motor_kw_l, consumo_l, break_tension_l, mabra_l, maniobra_motor_l, restate_l, installation_l, line_current_l, standart_l, stops_l, standart_additional_l, sec_stop_l, installation_type_l, calls_type_l, positions_1_l, positions_2_l, tipo_puertas_l, leva_l, puertas_model_l, operator_l, leva_current_l, kit_apertura_l, fotocell_l, provide_l, foto_current_l, embarque_l, apreture_l, floors_1door_l, floors_2door_l, door_type_l, automatic_doors_l, semiautomatic_doors_l, limitador_l, light_paths_l, limitador_current_l, fire_security_l, a3_standart_hidraulic_l, weighing_l, light_alert_l, extras_l, cables_amount_l, section_l, situation_l,frame_distance_l, motor_distance_l, flat_indication_l, lower_fase_l, lower_escape_l, mecanic_l , service_room_l, distance_l, wardrobe_flat_l, huida_l, foso_l, comments_l, panel_floor_l, panel_type_l, floors_sequence_l, back_box_l, edel_standart_l, column_height_l, column_width_l, column_fixture_top_l, middle_fixture_l, bottom_mesurement_l, clued_mesurement_l, column_fixture_bottom_l, middle_fixture_distance_l, emergency_light_l, display_type_l, emergency_light_color_l, button_type_l, braille_button_l, double_contact_alarm_l, door_closer_l, button_phone_l, stop_button_l, anagram_logo_l, anagram_retro_l, engraving_l, engravings_kg_l, engravings_persons_l, forbiden_smoke_l, emergency_phone_text_l, engraving_rae_l, engravings_phone_number_l, engravings_other_l, phone_select_l, voice_simulation_l, edel_connect_l, function_l, other_band_model_l, voice_simulation_language_l, key_l, functions_floors_l, functions_other_l, option_1_l, options_1_width_l, options_1_height_l, options_1_quantity_l, option_2_l, options_2_width_l, options_2_height_l, options_2_quantity_l, option_3_l, options_3_width_l, options_3_height_l, options_3_quantity_l, options_other_l, options_other_width_l, options_other_height_l, options_other_quantity_l, beep_button_l, green_arrow_l, location_l, button_braille_l, arrow_next_l, exterior_gong_l, inductive_loop_l]

    return labels_list