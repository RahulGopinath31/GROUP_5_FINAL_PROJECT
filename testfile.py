import database as db



db_obj = db.DBHelper()
dt = {
    "mob_no" :987654345,
    "age" : 33,
    "name" : "Aswini",
    "gender" :  "F",
    "vaccine_dose" : 1,
    "covid_rel_diseases" : "cold",
    "covid_symptoms":"high fever",
    "days_showing_symptoms" : 5,
    "contact_history" : 5,
    "family_member" : "True",
    "public_place_visit" : "Marriage",
    "covid_test" : "y",
    "test_mode" : "kit",
    "test_result" : "Positive",
    "doctor_consulted" : "y",
    "allergetic_drugs" : "no", 
    "ongoing_medication" : "Nil",
    "covid_prediction" : "No"
}


#db_obj.update(**dt)
#db_obj.create(**dt)
db_obj.update("age", 36, 987654333)



