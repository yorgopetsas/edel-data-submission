import csv
import os
import streamlit as st
from reportlab.pdfgen import canvas
from datetime import datetime
from variables import *

with st.container(border=True):
	st.write(f"**{general_cointainer_label}**")
	st.write(f"{client_l}: **{st.session_state.client}**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{form_type_l}: **{st.session_state.form_type}**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{stage_l}: **{st.session_state.stage}**")
	st.write(f"{man_type_l}: **{st.session_state.man_type}**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{stops_l}: **{st.session_state.stops}**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{reference_l}: **{st.session_state.reference}**")
	st.write(f"{date_l}: **{st.session_state.date}**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{delivery_date_l}: **{st.session_state.delivery_date}**")

temp_stops = int(st.session_state.stops)

previous_button = st.button(label="Haga click aquí para editar la información general", use_container_width=True)
if previous_button:
      st.switch_page("fnl.py")

with st.container(border=True):
	st.markdown(f"**{motor_l}**")
	col5, col6 = st.columns(2)
	with col5:
		central_current = st.selectbox(label=central_current_l, options=central_currents)
		potencia_central_cv = st.text_input(label=potencia_central_cv_l)
		potencia_central_kw = st.text_input(label=potencia_central_kw_l)
		consumo_central = st.text_input(label=consumo_central_l)
		starter_type = st.selectbox(label=start_type_l, options=starter_types)
	with col6:
		fabricante_central = st.text_input(label=fabricante_central_l)
		central_model = st.text_input(label=central_model_l)
		col7, col8 = st.columns(2)
		with col7:
				central_valves_type = st.text_input(label=central_valves_type_l)
				valve_pressure_fast = st.text_input(label=valve_pressure_fast_l)
				valve_pressure_climb = st.text_input(label=valve_pressure_climb_l)
		with col8:
				central_valves_type_model = st.text_input(label=central_valves_type_model_l)
				valve_pressure_downhill = st.text_input(label=valve_pressure_downhill_l)
				valve_pressure_emergency = st.text_input(label=valve_pressure_emergency_l)
	
	st.divider()
	st.markdown(maniobra)
	man1, man2 = st.columns(2)
	with man1:
		wardrobe = st.selectbox(label=wardrobe_l, options=wardrobes)
		renivelation  = st.selectbox(label=renivelation_l, options=renivelations)
	with man2:
		if starter_type == "Directo" or starter_type == "Estrella Triangulo":
				starter = st.text_input(label=starter_l, value=starter_type)
		else:
				starter = st.text_input(label=starter_l, value="Seleccionar...")
		starterz = st.selectbox(label=starterz_l, options=starterzs)
motor_finished = 1

if motor_finished:
	with st.container(border=True):
		st.markdown(installation_title)

		ins1, ins2, ins3 = st.columns(3)
		with ins1:
			installation = st.selectbox(label=installation_l, options=installations)
			line_current = st.selectbox(label=line_current_l, options=line_currents)
		with ins2:
			standart = st.selectbox(label=standart_l, options=standarts)
			stops = st.number_input(label=stops_l, value=temp_stops)
		with ins3:
			standart_additional = st.selectbox(label=standart_additional_l, options=standarts_additional)
			sec_stop = st.text_input(label=sec_stop_l, value="!!! DUDAS REPETICIÓN !!!")

		ins4, ins5 = st.columns(2)
		with ins4:
			installation_type = st.selectbox(label=installation_type_l, options=installation_types)
			positions_1 = st.selectbox(label=positions_1_l, options=positions_1s)
		with ins5:
			calls_type = st.selectbox(label=calls_type_l, options=calls_types)
			positions_2 = st.selectbox(label=positions_2_l, options=positions_2s)
installation_finished = 1

if installation_finished:
	with st.container(border=True):
		st.markdown(puertas_title) 

		puerta1, puerta2 = st.columns(2)
		with puerta1:
			tipo_puerta = st.selectbox(label=tipo_puertas_l, options=tipo_puertas)
			leva = st.selectbox(label=leva_l, options=levas)
			puertas_model = st.text_input(label=puertas_model_l)
		with puerta2:
			
			operator = st.selectbox(label=operator_l, options=operators)
			leva_current = st.text_input(label=leva_current_l)
			st.markdown(emergency_exit_kit)
			kit_apertura = st.checkbox(kit_apertura_l)

		st.markdown(fotocell_title_l)
		fotos1, fotos2, fotos3 = st.columns(3)
		with fotos1:
			fotocell = st.selectbox(label=fotocell_l, options=fotocells)
		with fotos2:
			provide = st.selectbox(label=provide_l, options=provides)
		with fotos3:
			foto_current = st.text_input(label=foto_current_l)

		puertas1, puertas2, puertas3 = st.columns(3)
		with puertas1:
			embarque = st.radio(embarque_l, embarques, index=None)
		with puertas2:
			if embarque == embarques[0]:
				operator1 = st.text_input(label=operator1_l)
				operator2 = st.text_input(label=operator2_l)
			elif embarque == embarques[1]:
				apreture = st.radio(apreture_l,	apretures, index=None)
		with puertas3:
			if embarque == embarques[1]:
				if apreture == apretures[0]:
					floors_1door = st.text_input(label=floors_1door_l)
					floors_2door = st.text_input(label=floors_2door_l)
cabin_finished = 1

if cabin_finished:
	with st.container(border=True):
		st.markdown(rellano_title)

		shaft1, shaft2 = st.columns(2)
		with shaft1:
			door_type = st.selectbox(label=door_type_l, options=door_types)
		with shaft2:
			if door_type == door_types[3]:
				automatic_doors = st.text_input(label=automatic_doors_l)
				semiautomatic_doors = st.text_input(label=semiautomatic_doors_l)
door_finished = 1

if door_finished:
	with st.container(border=True):
		st.markdown(otros_title)

		datos1, datos2, datos3 = st.columns(3)
		with datos1:
			limitador = st.selectbox(label=limitador_l, options=limitadors)
			light_path = st.selectbox(label=light_paths_l, options=light_paths)
		with datos2:
			limitador_current = st.text_input(label=limitador_current_l)
			fire_security = st.selectbox(label=fire_security_l, options=fire_securitys)
		with datos3:
			a3_standart = st.selectbox(label=a3_standart_hidraulic_l, options=a3_standarts_hidraulic)
			weighing = st.selectbox(label=weighing_l, options=weighings)
		datos21, datos22, datos23 = st.columns(3)
		with datos21:
			light_alert = st.selectbox(label=light_alert_l, options=light_alerts)
			extras = st.text_input(label=extras_l)
		with datos22:
			cables_amount = st.text_input(label=cables_amount_l)
		with datos23:
			section = st.text_input(label=section_l)
other_finished = 1

if other_finished:
	with st.container(border=True):
		st.markdown(situation_container_l)

		situation1, situation2, situation3 = st.columns(3)
		with situation1:
			situation = st.selectbox(label=situation_l, options=situations)
			lower_fase = st.selectbox(label=lower_fase_l, options=lower_fases)
			lower_escape = st.selectbox(label=lower_escape_l, options=lower_escapes)
			motor_distance = st.text_input(label=motor_distance_l)
		with situation2:
			flat_indication = st.text_input(label=flat_indication_l)
			mecanic = st.text_input(label=mecanic_l)
			service_room = st.selectbox(label=service_room_l, options=service_rooms)
			frame_distance = st.text_input(label=frame_distance_l)
		with situation3:
			distance = st.text_input(label=distance_l)
			wardrobe_flat = st.text_input(label=wardrobe_flat_l)
situation_finished = 1

if situation_finished:
	with st.container(border=True):

		st.markdown(heights_title)
		stops = st.text_input(floor_number_l, value=stops)
		num_fields = int(stops)
		if 'dynamic_fields' not in st.session_state:
			st.session_state.dynamic_fields = {'distances': [''] * num_fields, 'names': [''] * num_fields}
		else:
			for key in ['distances', 'names']:
				current_len = len(st.session_state.dynamic_fields[key])
				if num_fields > current_len:
					st.session_state.dynamic_fields[key].extend([''] * (num_fields - current_len))
				elif num_fields < current_len:
					st.session_state.dynamic_fields[key] = st.session_state.dynamic_fields[key][:num_fields]

		with st.container():
			huida = st.text_input(huida_l, key='huida_distance')

			floors1, floors2 = st.columns(2)
			for i in reversed(range(num_fields)):
				with floors1:
					st.session_state.dynamic_fields['distances'][i] = st.text_input(f"Altura {i+1} Distancia", value=st.session_state.dynamic_fields ['distances'][i],  key=f"distance_{i}")
				with floors2:
					st.session_state.dynamic_fields['names'][i] = st.text_input(f"Altura {i+1} Nombre de Piso", value=st.session_state.dynamic_fields['names'][i], key=f"name_{i}")
			with st.container():
				foso = st.text_input(foso_l, key='foso_distance')
			comments = st.text_area(comments_heights_l, key='comments')
height_finished = 1

if height_finished:
	with st.container(border=True):
		st.markdown(botonera_cabina_title)
		botonera_cabina_toggle = st.toggle(botonera_cabina_toggle_l)
		if botonera_cabina_toggle:
			buttons1, buttons2 = st.columns(2)
			with buttons1:
				panel_floor = st.text_input(panel_floor_l, value=stops)
				panel_type = st.selectbox(label=panel_type_l, options=panel_types)
			with buttons2:
				floors_sequence = st.text_input(floors_sequence_l)
				back_box = st.selectbox(label=back_box_l, options=back_boxes)
			edel_standart = st.toggle(edel_standart_l)
			panel1, panel2 = st.columns(2)
			if edel_standart == False:   
				with panel1:
						column_height = st.text_input(column_height_l)
						column_width = st.text_input(column_width_l)
						column_fixture_top = st.text_input(column_fixture_top_l)
						middle_fixture = st.text_input(middle_fixture_l)
				with panel2:
						bottom_mesurement = st.text_input(bottom_mesurement_l)
						clued_mesurement = st.text_input(clued_mesurement_l)
						column_fixture_bottom = st.text_input(column_fixture_bottom_l)
						middle_fixture_distance = st.text_input(middle_fixture_distance_l)
			with panel1:
				emergency_light = st.selectbox(label=emergency_light_l, options=emergency_lights)
				display_type = st.selectbox(label=display_type_l, options=display_types)
				double_contact_alarm = st.checkbox(double_contact_alarm_l)
				door_closer = st.checkbox(door_closer_l)
				stop_button = st.checkbox(stop_button_l)
			with panel2:
				emergency_light_color = st.selectbox(label=emergency_light_color_l, options=emergency_light_colors)
				button_type = st.selectbox(label=button_type_l, options=button_types)
				braille_button = st.checkbox(braille_button_l)
				button_phone = st.checkbox(button_phone_l)

			st.markdown(grabados_title)
			engraving = st.selectbox(label=engraving_l, options=engravings)
			engravings1, engravings2 = st.columns(2)
			with engravings1:
				anagram_logo = st.checkbox(anagram_logo_l)
				anagram_retro = st.checkbox(anagram_retro_l)
				engravings_kg = st.text_input(engravings_kg_l)
				engravings_persons = st.text_input(engravings_persons_l)
				engravings_other = st.text_input(engravings_other_l)
			with engravings2:
				forbiden_smoke = st.checkbox(forbiden_smoke_l)
				emergency_phone_text = st.checkbox(emergency_phone_text_l)
				engraving_rae = st.text_input(engraving_rae_l)
				engravings_phone_number = st.text_input(engravings_phone_number_l)

			st.markdown(telefono_title)
			phone1, phone2 = st.columns(2)
			with phone1:
				phone_select = st.selectbox(label=phone_select_l, options=phone_selects)
				voice_simulation = st.selectbox(label=voice_simulation_l, options=voice_simulations)
				edel_connect = st.selectbox(label=edel_connect_l, options=edel_connects)
				function = st.selectbox(label=function_l, options=functions)
				functions_other = st.text_input(functions_other_l)
			with phone2:
				other_band_model = st.text_input(other_band_model_l)
				voice_simulation_language = st.text_input(voice_simulation_language_l)
				key = st.selectbox(label=key_l, options=keys)
				functions_floors = st.text_input(functions_floors_l)
plate_finished = 1

if plate_finished:
	with st.container(border=True):
		st.markdown(botonera_external_title)
		botonera_external_toggle = st.toggle(botonera_external_toggle_l)
		if 	botonera_external_toggle:
			options1, options2 = st.columns(2)
			with options1:
				option_1 = st.selectbox(label=option_1_l, options=options_1)
				options_1_width = st.text_input(options_1_width_l)
				option_2 = st.selectbox(label=option_2_l, options=options_2)
				options_2_width = st.text_input(options_2_width_l)
				option_3 = st.selectbox(label=option_3_l, options=options_3)
				options_3_width = st.text_input(options_3_width_l)
				options_other = st.text_input(options_other_l)
				options_other_width = st.text_input(options_other_width_l)
			with options2:
				options_1_height = st.text_input(options_1_height_l)
				options_1_quantity = st.text_input(options_1_quantity_l)
				options_2_height = st.text_input(options_2_height_l)
				options_2_quantity = st.text_input(options_2_quantity_l)
				options_3_height = st.text_input(options_3_height_l)
				options_3_quantity = st.text_input(options_3_quantity_l)
				options_other_height = st.text_input(options_other_height_l)
				options_other_quantity = st.text_input(options_other_quantity_l)
ext_plate_finished = 1			

if ext_plate_finished:
	with st.container(border=True):
		st.markdown(standart_title)

		norm1, norm2, norm3 = st.columns(3)
		with norm1:
			beep_button = st.checkbox(beep_button_l)
			green_arrow = st.checkbox(green_arrow_l)
			location = st.text_input(location_l)
		with norm2:
			button_braille = st.checkbox(button_braille_l)
			arrow_next = st.checkbox(arrow_next_l)
		with norm3:
			exterior_gong = st.checkbox(exterior_gong_l)
			inductive_loop = st.checkbox(inductive_loop_l)
norm_finished = 1

if norm_finished:
	submit_button = st.button(label=submit_button_l)

if submit_button:
	date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	output_folder = "output"
	csv_filename = os.path.join(output_folder, f"{client}_{date_str}_{st.session_state.man_type}.csv")
	pdf_filename = os.path.join(output_folder, f"{client}_{date_str}_{st.session_state.man_type}.pdf")

	labels_list = initialize_labels_list_hidraulic()

	# CSV File Generation
	with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:

		writer = csv.writer(file)
		writer.writerow(labels_list)

		var_list = [st.session_state.client, st.session_state.reference, st.session_state.date, st.session_state.delivery_date, st.session_state.man_type, central_current, potencia_central_cv, potencia_central_kw, consumo_central, starter_type, fabricante_central, central_model, central_valves_type, valve_pressure_fast, valve_pressure_climb, central_valves_type_model, valve_pressure_downhill, valve_pressure_emergency, wardrobe, renivelation, starter, starterz, motor_type, motor_current, potencia_motor_cv, potencia_motor_kw, consumo, break_tension, mabra, mot_second, restate, installation, line_current, standart, st.session_state.stops, standart_additional, sec_stop, installation_type, calls_type, positions_1, positions_2, tipo_puerta, leva, puertas_model, operator, leva_current, kit_apertura, fotocell, provide, foto_current, embarque, apreture, floors_1door, floors_2door, door_type, automatic_doors, semiautomatic_doors, limitador, light_path, limitador_current, fire_security, a3_standart, weighing, light_alert, extras, cables_amount, section, situation,frame_distance, motor_distance, flat_indication, lower_fase, lower_escape, mecanic, service_room, distance, wardrobe_flat, huida, foso, comments, panel_floor, panel_type, floors_sequence, back_box, edel_standart, column_height, column_width, column_fixture_top, middle_fixture, bottom_mesurement, clued_mesurement, column_fixture_bottom, middle_fixture_distance, emergency_light, display_type, emergency_light_color, button_type, braille_button, double_contact_alarm, door_closer, button_phone, stop_button, anagram_logo, anagram_retro, engraving, engravings_kg, engravings_persons, forbiden_smoke, emergency_phone_text, engravings_rae, engravings_phone_number, engravings_other, phone_select, voice_simulation, edel_connect, function, other_band_model, voice_simulation_language, key, functions_floors, functions_other, option_1, options_1_width, options_1_height, options_1_quantity, option_2, options_2_width, options_2_height, options_2_quantity, option_3, options_3_width, options_3_height, options_3_quantity, options_other, options_other_width, options_other_height, options_other_quantity, beep_button, green_arrow, location, button_braille, arrow_next, exterior_gong, inductive_loop] 
	
		writer.writerow(var_list)

	# PDF File Creation
	c = canvas.Canvas(pdf_filename)
	y_position = 820
	line_height = 20
	counter = 0
	for n, k in enumerate(var_list):
		if counter == 119:
			y_position = 820
			counter += 1
		elif counter == 79:
			c.showPage()
			y_position = 820
			counter += 1
		elif counter == 39:
			y_position = 820
			counter += 1
		elif counter < 39:
			y_position -= line_height 
			c.drawString(30, y_position, f"{labels_list[n]}: {var_list[n]}")
			counter += 1
		elif counter > 39 and counter < 79:
			y_position -= line_height
			c.drawString(335, y_position, f"{labels_list[n]}: {var_list[n]}")
			counter += 1
		elif counter > 79 and counter < 119:
			y_position -= line_height 
			c.drawString(30, y_position, f"{labels_list[n]}: {var_list[n]}")
			counter += 1
		elif counter > 119 and counter < 158:
			y_position -= line_height
			c.drawString(335, y_position, f"{labels_list[n]}: {var_list[n]}")
			counter += 1
	c.save()
	for n, k in enumerate(var_list):
		st.write(f"{labels_list[n]}: **{var_list[n]}**")
	st.success(submittion_confirmation)