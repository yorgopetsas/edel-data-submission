import streamlit as st
from dictionary import *

def render_selectbox(field_options, field_value, field_label):
	selected_value = st.selectbox(label=f"**{field_label}**", options=field_options, index=field_options.index(st.session_state.get(field_value, field_options[0])))

with st.container(border=False):
	st.image(f'{header_url}', width=700)

# Informacion General
with st.container(border=True):
	st.write(f"**{general_cointainer_label}**")

	col1, col2 = st.columns(2)
	with col1:
		reference = st.text_input(label=reference_l, value=reference)

	with col2:
		col3, col4 = st.columns(2)
		with col3:
			delivery_date = st.date_input(label=delivery_date_l)
		with col4:
			date = st.date_input(label=date_l)

	comments = st.text_area(comments_l, key='comments')	

#Datos Generales
with st.container(border=True):
	st.write(f"**{data_l}**")
	col1, col2, col3, col4 = st.columns(4)
	min_floors = 1
	with col1:
		quantity = st.number_input(label=quantity_l, min_value=1, value=min_floors)
		stops = st.number_input(label=stops_l, min_value=2, max_value=32, value=stops)
	with col2:
		type = st.selectbox(label=type_l, options=types)
		boarding = st.number_input(label=boarding_l, min_value=1, max_value=3, value=1)
	with col3:
		man_type = st.selectbox(label=man_type_l, options=man_types)
		secuencia = st.text_input(label=secuencia_l)
	with col4:
		connection = st.selectbox(label=connection_l, options=connections)
	
	norm = st.selectbox(label=norm_l, options=norms)

	#Aqui puedo mejorar haciendo que pida / proponga secuencia segun el numero de paradas
	

with st.container(border=True):
	st.write(f"**{central_l}**")
	col1, col2 = st.columns(2)
	with col1:
		if man_type == man_types[1] or man_type == man_types[2]:
			machine_type = st.selectbox(label=machine_type_l, options=machine_types_a)
		elif man_type == man_types[3]:
			machine_type = st.selectbox(label=machine_type_l, options=machine_types_h)
	with col2:
		if machine_type == machine_types_a[2]:
			encoder_type = st.selectbox(label=encoder_type_l, options=encoder_types)
	cols1, cols2 = st.columns(2)
	with cols1:
		valves_type = st.selectbox(label=valves_type_l, options=valves_types)
	with cols2:
		if valves_type == valves_types[2]:
			model = st.selectbox(label=valve_models_l, options=valve_models)
	colz1, colz2, colz3, colz4 = st.columns(4)
	with colz1:
		situation = st.selectbox(label=situation_l, options=situations)
		consumo = st.text_input(label=consumo_l)
	with colz2:
		wardrobe_side = st.selectbox(label=wardrobe_side_l, options=wardrobe_sides)
		vbreak = st.text_input(label=vbreak_l)
	with colz3:
		speed = st.text_input(label=speed_l)
		power = st.text_input(label=power_l)
	with colz4:
		current = st.text_input(label=current_l)
		neutral = st.selectbox(label=neutral_l, options=neutrals)

with st.container(border=True):
	st.write(f"**{cabin_door_l}**")
	col1, col2, col3 = st.columns(3)
	with col1:
		operator_type = st.selectbox(label=operator_type_l, options=operator_types)
		manufacturer = st.text_input(label=manufacturer_l)
		door_model = st.selectbox(label=door_model_l, options=door_models)
		consumo_door_motor = st.text_input(label=consumo_door_motor_l)
		coz1, coz2 = st.columns(2)
		with coz1:
			leva = st.selectbox(label=leva_l, options=levas)
		with coz2:
			current_door = st.text_input(label=current_door_l)

		with st.container(border=True):
			floor_door = st.selectbox(label=floor_door_l, options=floor_doors)
	if boarding > 1:
		with col2:
			operator_type2 = st.selectbox(label=operator_type_l2, options=operator_types)
			manufacturer2 = st.text_input(label=manufacturer_l2)
			door_model2 = st.selectbox(label=door_model_l2, options=door_models)
			consumo_door_motor2 = st.text_input(label=consumo_door_motor_l2)
			coz1, coz2 = st.columns(2)
			with coz1:
				leva2 = st.selectbox(label=leva_l2, options=levas)
			with coz2:
				current_door2 = st.text_input(label=current_door_l2)

			with st.container(border=True):
				floor_door2 = st.selectbox(label=floor_door_l2, options=floor_doors)
	if boarding > 2:
		with col3:
			operator_type3 = st.selectbox(label=operator_type_l3, options=operator_types)
			manufacturer3 = st.text_input(label=manufacturer_l3)
			door_model3 = st.selectbox(label=door_model_l3, options=door_models)
			consumo_door_motor3 = st.text_input(label=consumo_door_motor_l3)
			coz1, coz2 = st.columns(2)
			with coz1:
				leva3 = st.selectbox(label=leva_l3, options=levas)
			with coz2:
				current_door3 = st.text_input(label=current_door_l3)

			with st.container(border=True):
				floor_door3 = st.selectbox(label=floor_door_l3, options=floor_doors)

with st.container(border=True):
	st.write(f"**{cabin_l}**")
	with st.container(border=True):
			zcol1, zcol2, zcol3 = st.columns(3)
			with zcol1:
				fotocell = st.selectbox(label=fotocell_l, options=fotocells)
			with zcol2:
				fotocell_current_acdc = st.selectbox(label=fotocell_current_acdc_l, options=fotocell_current_acdcs)
			with zcol3:
				fotocell_current = st.text_input(label=fotocell_current_l)
	col1, col2 = st.columns(2)
	with col1:
		apreture = st.checkbox(apreture_l)
		a3 = st.checkbox(a3_l)
		gong_2 = st.checkbox(gong_2_l)
		line = st.text_input(label=line_l)
	with col2:
		contact = st.checkbox(contact_l)
		gong_1 = st.checkbox(gong_1_l)
		flechas = st.checkbox(flechas_l)
		weight = st.selectbox(label=weight_l, options=weights)

	st.divider()
	limitator = st.selectbox(label=limitator_l, options=limitators)
	xol1, xol2 = st.columns(2)
	with xol1:
		limitator_current = st.text_input(label=limitator_current_l)
	with xol2:
		bobina_count = st.number_input(label=bobina_count_l, min_value=0, max_value=5, value=1)
	st.divider()
	zol1, zol2 = st.columns(2)
	with zol1:
		foso = st.checkbox(label=foso_l)
	with zol2:
		huida = st.checkbox(label=huida_l)


with st.container(border=True):

	num_fields = int(stops)
	if 'dynamic_fields' not in st.session_state:
		st.session_state.dynamic_fields = {'distances': [''] * num_fields, 'names': [''] * num_fields, 'a': [''] * num_fields,'b': [''] * num_fields,'c': [''] * num_fields}
	else:
		for key in ['distances', 'names']:
			current_len = len(st.session_state.dynamic_fields[key])
			if num_fields > current_len:
				st.session_state.dynamic_fields[key].extend([''] * (num_fields - current_len))
			elif num_fields < current_len:
				st.session_state.dynamic_fields[key] = st.session_state.dynamic_fields[key][:num_fields]

	st.markdown(heights_title_l)
	stops = st.number_input(label="PARADAS", min_value=0, max_value=32, value=stops)

	num_fields = int(stops)
	if 'dynamic_fields' not in st.session_state:
		st.session_state.dynamic_fields = {'distances': [''] * num_fields, 'names': [''] * num_fields, 'a': [0] * num_fields, 'b': [0] * num_fields, 'c': [0] * num_fields}
	else:
		for key in ['distances', 'names', 'a', 'b', 'c']:
			current_len = len(st.session_state.dynamic_fields[key])
			if num_fields > current_len:
				st.session_state.dynamic_fields[key].extend([''] * (num_fields - current_len))
			elif num_fields < current_len:
				st.session_state.dynamic_fields[key] = st.session_state.dynamic_fields[key][:num_fields]
	
	if boarding == 1:
		huida1, huida2, huida3, = st.columns([1,1,1])
		with huida1:
			huida_height = st.text_input(huida_distance_l, key='huida_distance')
		with huida2:
			pass
		with huida3:
			st.image(f'{roof_url}', width=159)
			
	elif boarding == 2:
		huida1, huida2, huida3, huida4, huida5  = st.columns([1,1,0.3,0.3,1])
		with huida1:
			huida_height = st.text_input(huida_distance_l, key='huida_distance')
		with huida2:
			pass
		with huida3:
			pass
		with huida4:
			pass
		with huida5:
			st.image(f'{roof_url}', width=159)

	elif boarding == 3:

		huida1, huida2, huida3, huida4, huida5, huida6  = st.columns([1,1,0.3,0.3,0.3,1])
		with huida1:
			huida_height = st.text_input(huida_distance_l, key='huida_distance')
		with huida2:
			pass
		with huida3:
			pass
		with huida4:
			pass
		with huida5:
			pass
		with huida6:
			st.image(f'{roof_url}', width=159)

	for i in reversed(range(num_fields)):
		if boarding == 1:
			floors1, floors2, floors3 = st.columns([1,1,1])
			with floors1:
				st.session_state.dynamic_fields['names'][i] = st.text_input(f"NIVEL {i+1}", placeholder="NIVEL", value=st.session_state.dynamic_fields['names'][i], key=f"name_{i}")
			with floors2:
				st.session_state.dynamic_fields['distances'][i] = st.text_input(f"DISTANCIA {i+1}", value=st.session_state.dynamic_fields ['distances'][i],  placeholder="DISTANCIA", key=f"distance_{i}", label_visibility="hidden")
			with floors3:
				st.image(f'{building_url}', width=159)
		
		elif boarding == 2:
			floors1, floors2, floors3, floors4, floors5 = st.columns([1,1,0.3,0.3,1])
			with floors1:
				st.session_state.dynamic_fields['names'][i] = st.text_input(f"NIVEL {i+1}", placeholder="NIVEL", value=st.session_state.dynamic_fields['names'][i], key=f"name_{i}")
			with floors2:
				st.session_state.dynamic_fields['distances'][i] = st.text_input(f"DISTANCIA {i+1}", value=st.session_state.dynamic_fields ['distances'][i],  placeholder="DISTANCIA", key=f"distance_{i}", label_visibility="hidden")
			with floors3:
				st.write("")
				st.write("")
				st.session_state.dynamic_fields['a'][i] = st.checkbox("A", key=f"a_{i}", value=st.session_state.dynamic_fields['a'][i])
			with floors4:
				st.write("")
				st.write("")
				st.session_state.dynamic_fields['b'][i] = st.checkbox("B", key=f"b_{i}", value=st.session_state.dynamic_fields['b'][i])
			with floors5:
				if st.session_state.dynamic_fields['a'][i] == 1 and st.session_state.dynamic_fields['b'][i] == 1:
					st.image(f'{building_aa_bb_url}', width=159)
				elif st.session_state.dynamic_fields['a'][i] == 0 and st.session_state.dynamic_fields['b'][i] == 1:
					st.image(f'{building_a_bb_url}', width=159)
				elif st.session_state.dynamic_fields['a'][i] == 1 and st.session_state.dynamic_fields['b'][i] == 0:
					st.image(f'{building_aa_b_url}', width=159)
				else:
					st.image(f'{building_a_b_url}', width=159)

		elif boarding == 3:
			floors1, floors2, floors3, floors4, floors5, floors6 = st.columns([1,1,0.3,0.3,0.3,1])
			with floors1:
				st.session_state.dynamic_fields['names'][i] = st.text_input(f"NIVEL {i+1}", placeholder="DENOMINACIÓN", value=st.session_state.dynamic_fields['names'][i], key=f"name_{i}")
			with floors2:
				st.session_state.dynamic_fields['distances'][i] = st.text_input(f"DISTANCIA {i+1}", value=st.session_state.dynamic_fields ['distances'][i],  placeholder="DISTANCIA", key=f"distance_{i}", label_visibility="hidden")
			with floors3:
				st.write("")
				st.write("")
				st.session_state.dynamic_fields['a'][i] = st.checkbox("A", key=f"a_{i}", value=st.session_state.dynamic_fields['a'][i])
			with floors4:
				st.write("")
				st.write("")
				st.session_state.dynamic_fields['b'][i] = st.checkbox("B", key=f"b_{i}", value=st.session_state.dynamic_fields['b'][i])
			with floors5:
				st.write("")
				st.write("")
				st.session_state.dynamic_fields['c'][i] = st.checkbox("C", key=f"c_{i}", value=st.session_state.dynamic_fields['c'][i])

			with floors6:

				if st.session_state.dynamic_fields['a'][i] == 1 and st.session_state.dynamic_fields['b'][i] == 1 and st.session_state.dynamic_fields['c'][i] == 1:
					st.image(f'{building_aa_bb_cc_url}', width=159)

				elif st.session_state.dynamic_fields['a'][i] == 0 and st.session_state.dynamic_fields['b'][i] == 1 and st.session_state.dynamic_fields['c'][i] == 1:
					st.image(f'{building_a_bb_cc_url}', width=159)

				elif st.session_state.dynamic_fields['a'][i] == 0 and st.session_state.dynamic_fields['b'][i] == 0 and st.session_state.dynamic_fields['c'][i] == 1:
					st.image(f'{building_a_b_cc_url}', width=159)	

				elif st.session_state.dynamic_fields['a'][i] == 1 and st.session_state.dynamic_fields['b'][i] == 0 and st.session_state.dynamic_fields['c'][i] == 1:
					st.image(f'{building_aa_b_cc_url}', width=159)

				elif st.session_state.dynamic_fields['a'][i] == 1 and st.session_state.dynamic_fields['b'][i] == 1 and st.session_state.dynamic_fields['c'][i] == 0:
					st.image(f'{building_aa_bb_c_url}', width=159)
				elif st.session_state.dynamic_fields['a'][i] == 0 and st.session_state.dynamic_fields['b'][i] == 1 and st.session_state.dynamic_fields['c'][i] == 0:
					st.image(f'{building_a_bb_c_url}', width=159)
				elif st.session_state.dynamic_fields['a'][i] == 1 and st.session_state.dynamic_fields['b'][i] == 0 and st.session_state.dynamic_fields['c'][i] == 0:
					st.image(f'{building_aa_b_c_url}', width=159)
				else:
					st.image(f'{building_a_b_c_url}', width=159)

	if boarding == 1:
		huida1, huida2, huida3, = st.columns([1,1,1])
		with huida1:
			foso_height = st.text_input(foso_distance_l, key='foso_distance')
		with huida2:
			pass
		with huida3:
			st.image(f'{foso_url}', width=159)
			
	elif boarding == 2:
		huida1, huida2, huida3, huida4, huida5  = st.columns([1,1,0.3,0.3,1])
		with huida1:
			foso_height = st.text_input(foso_distance_l, key='foso_distance')
		with huida2:
			pass
		with huida3:
			pass
		with huida4:
			pass
		with huida5:
			st.image(f'{foso_url}', width=159)

	elif boarding == 3:

		huida1, huida2, huida3, huida4, huida5, huida6  = st.columns([1,1,0.3,0.3,0.3,1])
		with huida1:
			foso_height = st.text_input(foso_distance_l, key='foso_distance')
		with huida2:
			pass
		with huida3:
			pass
		with huida4:
			pass
		with huida5:
			pass
		with huida6:
			st.image(f'{foso_url}', width=159)
		
	# 		comments_h = st.text_area(comments_heights_l, key='comments_h')

# import pandas as pd
# from io import StringIO

# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#     # To read file as bytes:
#     bytes_data = uploaded_file.getvalue()
#     st.write(bytes_data)

#     # To convert to a string based IO:
#     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     st.write(stringio)

#     # To read file as string:
#     string_data = stringio.read()
#     st.write(string_data)

#     # Can be used wherever a "file-like" object is accepted:
#     dataframe = pd.read_csv(uploaded_file)
#     st.write(dataframe)

# uploaded2_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
# for uploaded_file in uploaded2_files:
#     bytes_data = uploaded2_file.read()
#     st.write("filename:", uploaded_file.name)
#     st.write(bytes_data)