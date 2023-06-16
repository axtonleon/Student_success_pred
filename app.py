import streamlit as st
import pickle as pk
from sklearn.preprocessing import StandardScaler
import time
import os
cwd = os.getcwd()

# save the model to disk
filename = 'logreg_model.sav'
import pandas as pd
# Mapping of output options to numbers
education_level_mapping = {
    "none": 0,
    "primary education": 1,
    "secondary education": 2,
    "higher education": 3
}

failure_mapping = {
    "very low": 1,
    "low": 2,
    "moderate": 3,
    "high": 4,
    "very high": 5
}

goout_mapping = {
    "very low": 1,
    "low": 2,
    "moderate": 3,
    "high": 4,
    "very high": 5
}

sex_mapping = {
    "Male": 0,
    "Female": 1
}

support_mapping = {
    "Yes": 1,
    "No": 0
}

course_mapping = {
    "Yes": 1,
    "No": 0
}

st.title("STUDENT SUCCESS PEDICTOR")
col1, col2, col3 = st.columns(3)
with col1:
	age = st.text_input('Enter your age: ')
	Medu = st.selectbox('Enter your mothers education level: ', ("none", "primary education", "secondary education", "higher education"))
	Fedu = st.selectbox('Enter your fathers education level: ', ("none", "primary education", "secondary education", "higher education"))
	Medu = education_level_mapping[Medu]
	Fedu = education_level_mapping[Fedu]
with col2:
	failures = st.selectbox('how often do you fail?: ', ("very low", "low","moderate", "high", "very high"))
	goout = st.selectbox('how often do you go outing: ', ("very low", "low","moderate", "high", "very high"))
	sex_M = st.selectbox('Enter your sex: ', ("Male", "Female"))
	failures = failure_mapping[failures]
	goout = goout_mapping[goout]
	sex_M = sex_mapping[sex_M]
with col3:
	schoolsup_yes = st.selectbox('do you recieve extra educational support: ', ("Yes", "No"))
	higher_yes = st.selectbox('do you like your course of study : ', ("Yes", "No"))
	schoolsup_yes = support_mapping[schoolsup_yes]
	higher_yes = course_mapping[higher_yes]

if st.button('Predict'):

	# dictionary with list object in values
	dets = {
	    'age' : [age],
	    'Medu' : [Medu],
	    'Fedu' : [Fedu],
	    'failures' : [failures],
	    'goout' : [goout],
	    'sex_M' : [sex_M],
	    'schoolsup_yes' : [schoolsup_yes],
	    'higher_yes' : [higher_yes],

	}
	  
	# creating a Dataframe object 
	df = pd.DataFrame(dets)
	  
	scaler = StandardScaler()
	df_scaled = scaler.fit_transform(df)
	loaded_model = pk.load(open(filename, 'rb'))
	y_pred = loaded_model.predict(df_scaled)
	if y_pred == 1:
		st.write("""
			we predict you going to PASS

			you on your way to SUCCESS, Keep up the good work
			""")
	else:
		st.write("""
			we predict you going to FAIL

			Does't look so good, please sit up and seek advice from you lecturers""")
