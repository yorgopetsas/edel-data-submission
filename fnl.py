import streamlit as st
from variables import *
from variables import var_list_gearless

for n, el in enumerate(var_list_gearless):
	if var_list_gearless[n] not in st.session_state:
		if var_list_gearless[n] == "form_type":
			st.session_state[var_list_gearless[n]] = form_types[0]
		elif var_list_gearless[n] == "stage":
			st.session_state[var_list_gearless[n]] = stages[0]
		elif var_list_gearless[n] == "man_type":
			st.session_state[var_list_gearless[n]] = man_types[0]
		elif var_list_gearless[n] == "motor_type":
			st.session_state[var_list_gearless[n]] = motor_types[0]
		else:
			st.session_state[var_list_gearless[n]] = ''

def render_selectbox(field_options, field_value, field_label):
	selected_value = st.selectbox(label=f"**{field_label}**", options=field_options, index=field_options.index(st.session_state.get(field_value, field_options[0])))
	st.session_state[field_value] = selected_value

with st.container(border=False):
	st.image(f'{header_url}', width=700)
	
with st.container(border=True):
	st.write(f"**{general_cointainer_label}**")
	col1, col2 = st.columns(2)

	with col1:
		st.session_state.client = st.text_input(label=client_l, value=st.session_state.client)
		st.session_state.reference = st.text_input(label=reference_l, value=st.session_state.reference)
		render_selectbox(form_types, "form_type", form_type_l)
		render_selectbox(man_types, "man_type", man_type_l)

	with col2:
		col3, col4 = st.columns(2)
		with col3:
			st.session_state.date = st.date_input(label=date_l)
		with col4:
			st.session_state.delivery_date = st.date_input(label=delivery_date_l)
		render_selectbox(stages, "stage", stage_l)
		st.session_state.stops = st.text_input(label=stops_l, value=st.session_state.stops)
		if st.session_state.man_type == "Eléctrica":
			render_selectbox(motor_types, "motor_type", motor_type_l)

next_button = st.button(label=next_button_l, use_container_width=True)
if next_button:
	if st.session_state.man_type == man_types[1]:
		st.switch_page("pages/electric.py")
	elif st.session_state.man_type == man_types[2]:
		st.switch_page("pages/hidraulic.py")


