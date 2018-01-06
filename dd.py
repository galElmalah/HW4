
# def old_apply(operator, obj1, obj2):
#     if operator == 'add':  
#         if isinstance(obj1, Meters):
#             if not isinstance(obj2, dict):
#                 return Meters(obj1.value + inches_to_meters(obj2.value)) if isinstance(obj2, Inches) else Meters(obj1.value + obj2.value)
#             if type_of(obj2)=='Miles':
#                 return Meters(obj1.value + miles_to_meters(obj2['get']('value')))
#             if type_of(obj2)=='Feets':
#                 return Meters(obj1.value + feets_to_meters(obj2['get']('value')))
#         # Inches is obj1
#         elif isinstance(obj1, Inches):
#             if not isinstance(obj2, dict):
#                 return Inches(obj1.value + meters_to_inches(obj2.value)) if isinstance(obj2, Meters) else Inches(obj1.value + obj2.value)
#             if type_of(obj2)=='Miles':
#                 return Inches(obj1.value + miles_to_inches(obj2['get']('value')))
#             if type_of(obj2)=='Feets':
#                 return Inches(obj1.value + feets_to_inches(obj2['get']('value')))
#         # Miles is obj1
#         elif type_of(obj1) == 'Miles':
#             if isinstance(obj2, dict):
#                 return Miles['new'](obj1['get']('value') + feets_to_miles(obj2['get']('value'))) if type_of(obj2)=='Feets' else Miles['new'](obj1['get']('value') + obj2['get']('value'))
#             if isinstance(obj2, Meters):
#                 return Miles['new'](obj1['get']('value') + meters_to_miles(obj2.value))
#             if isinstance(obj2, Inches):
#                 return Miles['new'](obj1['get']('value') + inches_to_miles(obj2.value))
#         # Feets is obj1
#         elif type_of(obj1) == 'Feets':
#             if isinstance(obj2, dict):
#                 return Feets['new'](obj1['get']('value') + miles_to_feets(obj2['get']('value'))) if type_of(obj2)=='Miles' else Feets['new'](obj1['get']('value') + obj2['get']('value'))
#             if isinstance(obj2, Meters):
#                 return Feets['new'](obj1['get']('value') + meters_to_feets(obj2.value))
#             if isinstance(obj2, Inches):
#                 return Feets['new'](obj1['get']('value') + inches_to_feets(obj2.value))
#     elif operator=='sub':

#         # Miles is obj1
#         elif type_of(obj1) == 'Miles':
#             if isinstance(obj2, dict):
#                 return Miles['new'](obj1['get']('value') - feets_to_miles(obj2['get']('value'))) if type_of(obj2)=='Feets' else Miles['new'](obj1['get']('value') - obj2['get']('value'))
#             if isinstance(obj2, Meters):
#                 return Miles['new'](obj1['get']('value') - meters_to_miles(obj2.value))
#             if isinstance(obj2, Inches):
#                 return Miles['new'](obj1['get']('value') - inches_to_miles(obj2.value))
#         # Feets is obj1
#         elif type_of(obj1) == 'Feets':
#             if isinstance(obj2, dict):
#                 return Feets['new'](obj1['get']('value') - miles_to_feets(obj2['get']('value'))) if type_of(obj2)=='Miles' else Feets['new'](obj1['get']('value') - obj2['get']('value'))
#             if isinstance(obj2, Meters):
#                 return Feets['new'](obj1['get']('value') - meters_to_feets(obj2.value))
#             if isinstance(obj2, Inches):
#                 return Feets['new'](obj1['get']('value') - inches_to_feets(obj2.value))
#     if operator =='>' or operator=='gt':
#         # Meters is obj1
#         if isinstance(obj1, Meters):
#             if not isinstance(obj2, dict):
#                 return obj1.value > inches_to_meters(obj2.value) if isinstance(obj2, Inches) else obj1.value > obj2.value
#             if type_of(obj2)=='Miles':
#                 return obj1.value > miles_to_meters(obj2['get']('value'))
#             if type_of(obj2)=='Feets':
#                 return obj1.value > feets_to_meters(obj2['get']('value'))
#         # Inches is obj1
#         elif isinstance(obj1, Inches):
#             if not isinstance(obj2, dict):
#                 return obj1.value > meters_to_inches(obj2.value) if isinstance(obj2, Meters) else obj1.value > obj2.value
#             if type_of(obj2)=='Miles':
#                 return obj1.value > miles_to_inches(obj2['get']('value'))
#             if type_of(obj2)=='Feets':
#                 return obj1.value > feets_to_inches(obj2['get']('value'))
#         # Miles is obj1
#         elif type_of(obj1) == 'Miles':
#             if isinstance(obj2, dict):
#                 return obj1['get']('value') > feets_to_miles(obj2['get']('value')) if type_of(obj2)=='Feets' else obj1['get']('value') > obj2['get']('value')
#             if isinstance(obj2, Meters):
#                 return obj1['get']('value') > meters_to_miles(obj2.value)
#             if isinstance(obj2, Inches):
#                 return obj1['get']('value') > inches_to_miles(obj2.value)
#         # Feets is obj1
#         elif type_of(obj1) == 'Feets':
#             if isinstance(obj2, dict):
#                 return obj1['get']('value') > miles_to_feets(obj2['get']('value')) if type_of(obj2)=='Miles' else obj1['get']('value') > obj2['get']('value')
#             if isinstance(obj2, Meters):
#                 return obj1['get']('value') > meters_to_feets(obj2.value)
#             if isinstance(obj2, Inches):
#                 return obj1['get']('value') > inches_to_feets(obj2.value)
#     ## equality operator ##
#     elif operator =='==' or operator=='eq':
#         # Meters is obj1
#         if isinstance(obj1, Meters):
#             if not isinstance(obj2, dict):
#                 return obj1.value == inches_to_meters(obj2.value) if isinstance(obj2, Inches) else obj1.value == obj2.value
#             if type_of(obj2)=='Miles':
#                 return obj1.value == miles_to_meters(obj2['get']('value'))
#             if type_of(obj2)=='Feets':
#                 return obj1.value == feets_to_meters(obj2['get']('value'))
#         # Inches is obj1
#         elif isinstance(obj1, Inches):
#             if not isinstance(obj2, dict):
#                 return obj1.value == meters_to_inches(obj2.value) if isinstance(obj2, Meters) else obj1.value == obj2.value
#             if type_of(obj2)=='Miles':
#                 return obj1.value == miles_to_inches(obj2['get']('value'))
#             if type_of(obj2)=='Feets':
#                 return obj1.value == feets_to_inches(obj2['get']('value'))
#         # Miles is obj1
#         elif type_of(obj1) == 'Miles':
#             if isinstance(obj2, dict):
#                 return obj1['get']('value') == feets_to_miles(obj2['get']('value')) if type_of(obj2)=='Feets' else obj1['get']('value') == obj2['get']('value')
#             if isinstance(obj2, Meters):
#                 return obj1['get']('value') == meters_to_miles(obj2.value)
#             if isinstance(obj2, Inches):
#                 return obj1['get']('value') == inches_to_miles(obj2.value)
#         # Feets is obj1
#         elif type_of(obj1) == 'Feets':
#             if isinstance(obj2, dict):
#                 return obj1['get']('value') == miles_to_feets(obj2['get']('value')) if type_of(obj2)=='Miles' else obj1['get']('value') == obj2['get']('value')
#             if isinstance(obj2, Meters):
#                 return obj1['get']('value') == meters_to_feets(obj2.value)
#             if isinstance(obj2, Inches):
#                 return obj1['get']('value') == inches_to_feets(obj2.value)
