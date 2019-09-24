# This document will contain all of the functions in the bridgeup module

# Add a comment at the bottom of the file explaining what your function does 
# and then add your function below

import pandas as pd

df = pd.read_csv("internship_bootcamp_data.csv")

def student_season(student_name):
	season = df["Fav season"].loc[df["First Name"]== student_name]
	return season

print(student_season("Stephanie"))