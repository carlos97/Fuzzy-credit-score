
import numpy as np
import skfuzzy as fuzz

x_ingresos = np.arange(0, 20.1, 1)

ingresos_bajo,ingresos_bajo_score = fuzz.trapmf(x_ingresos,[0, 0.5, 1, 2]),0.2
ingresos_medio,ingresos_medio_score  = fuzz.trapmf(x_ingresos,[1.5, 2, 3, 4]),0.3
ingresos_alto,ingresos_alto_score  = fuzz.trapmf(x_ingresos,[3, 4, 20.099, 20.1]),0.5

calificacion_crediticia = np.arange(0, 1000, 1)

calificacion_crediticia_bajo,calificacion_crediticia_bajo_score = fuzz.zmf(calificacion_crediticia,0,400),0.1
calificacion_crediticia_medio,calificacion_crediticia_medio_score = fuzz.gaussmf(calificacion_crediticia,600,150),0.3
calificacion_crediticia_alto,calificacion_crediticia_alto_score = fuzz.smf(calificacion_crediticia,750,1000),0.6

obligaciones_financieras = np.arange(0, 20.6, 1)

obligaciones_financieras_bajo,obligaciones_financieras_bajo_score = fuzz.zmf(obligaciones_financieras,0,1),0.5
obligaciones_financieras_normal,obligaciones_financieras_normal_score = fuzz.gaussmf(obligaciones_financieras,1.250,0.800),0.35
obligaciones_financieras_alta,obligaciones_financieras_alta_score = fuzz.smf(obligaciones_financieras,2.500,20.500),0.15

edad = np.arange(18, 90, 1)

edad_joven,edad_joven_score = fuzz.trapmf(edad,[18, 18.1, 22, 29]),0.1
edad_adulto,edad_adulto_score = fuzz.trapmf(edad,[22, 26, 50, 61]),0.6
edad_anciano,edad_anciano_score = fuzz.trapmf(edad,[50, 58, 89, 90]),0.3

antiguedad = np.arange(0, 54, 1)

antiguedad_Malo,antiguedad_Malo_score = fuzz.zmf(antiguedad, 0, 18),0.1
antiguedad_Normal,antiguedad_Normal_score = fuzz.gaussmf(antiguedad,24,10),0.3
antiguedad_Bueno,antiguedad_Bueno_score = fuzz.smf(antiguedad, 36,54),0.6

personas_cargo = np.arange(0, 8, 1)

personas_cargo_pocas,personas_cargo_pocas_score = fuzz.zmf(personas_cargo,0,3),0.5
personas_cargo_normal,personas_cargo_normal_score = fuzz.gaussmf(personas_cargo,4,1),0.4
personas_cargo_muchas,personas_cargo_muchas_score = fuzz.smf(personas_cargo,3,7),0.1

RRF = np.arange(0, 266, 1)

RRF_bajo,RRF_bajo_score = fuzz.zmf(RRF,0,30),0.2
RRF_medio,RRF_medio_score = fuzz.gaussmf(RRF,40,20),0.25
RRF_alto,RRF_alto_score = fuzz.smf(RRF,30,70),0.55

min_val = 0.28
max_val = 3.50

score = np.arange(0, max_val+0.1, 0.1)

score_bajo = fuzz.trapmf(score,[min_val, 0.98, 0.98, 1.68])
score_medio  = fuzz.trapmf(score,[0.98, 1.68, 1.68, 2.38])
score_alto  = fuzz.trapmf(score,[1.68, 2.38, 2.38, max_val])

contrato_options ={
    'Indefinido': 60,
    'Fijo': 45,
    'Prestación de Servicios': 35,
    'desempleado': 0,
}
"Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a", "Unión Libre"
estado_civil_options = {
    'Soltero/a': 35,
    'Casado/a': 50,
    'Divorciado/a': 45,
    'Viudo/a': 40,
    'Unión Libre': 45,
}
condicion_medica_options = {
    'Ninguna': 80,
    'Crónica': 50,
    'Discapacidad': 20,
}
nivel_estudios_options = {
    'Primaria': 15,
    'Secundaria': 25,
    'Técnico': 35,
    'Tecnólogo': 45,
    'Universitario': 65,
    'Posgrado': 75,
    'Ninguno': 0,
}



def  RRF_def(v_contrato,v_estado_civil,v_condicion_medica,v_nivel_estudios):
    points = 0
    points += contrato_options.get(v_contrato, 0)
    points += estado_civil_options.get(v_estado_civil, 0)
    points += condicion_medica_options.get(v_condicion_medica, 0)
    points += nivel_estudios_options.get(v_nivel_estudios, 0)
    print(points)
    return points

def centroide_pertenencia(var_name, values, memberships):

    valid_memberships = []
    for val_name in values:
        memb_value = memberships.get(f'valor_membresia_{var_name}_{val_name}')
        if memb_value is not None and memb_value > 0:
            valid_memberships.append((val_name, memb_value))

    if not valid_memberships:
        return (None, 0)

    # Encontrar la variable con el valor de membresía más alto
    best_variable = None
    max_membership = -1
    for var, memb in valid_memberships:
        if memb > max_membership:
            max_membership = memb
            best_variable = var

    return (best_variable, max_membership)

    
def membership_functions(v_ingresos,v_calificacion_crediticia,v_obligaciones_financieras,v_edad,v_antiguedad,v_personas_cargo,v_RRF):

    valor_membresia_ingresos_bajo = fuzz.interp_membership(x_ingresos, ingresos_bajo, int(v_ingresos))
    valor_membresia_ingresos_medio = fuzz.interp_membership(x_ingresos, ingresos_medio, int(v_ingresos))
    valor_membresia_ingresos_alto = fuzz.interp_membership(x_ingresos, ingresos_alto, int(v_ingresos))

    valor_membresia_calificacion_crediticia_bajo = fuzz.interp_membership(calificacion_crediticia, calificacion_crediticia_bajo, v_calificacion_crediticia)
    valor_membresia_calificacion_crediticia_medio = fuzz.interp_membership(calificacion_crediticia, calificacion_crediticia_medio, v_calificacion_crediticia)
    valor_membresia_calificacion_crediticia_alto = fuzz.interp_membership(calificacion_crediticia, calificacion_crediticia_alto, v_calificacion_crediticia)

    valor_membresia_obligaciones_financieras_bajo = fuzz.interp_membership(obligaciones_financieras, obligaciones_financieras_bajo, v_obligaciones_financieras)
    valor_membresia_obligaciones_financieras_normal = fuzz.interp_membership(obligaciones_financieras, obligaciones_financieras_normal, v_obligaciones_financieras)
    valor_membresia_obligaciones_financieras_alta = fuzz.interp_membership(obligaciones_financieras, obligaciones_financieras_alta, v_obligaciones_financieras)
    print(v_edad)
    valor_membresia_edad_joven = fuzz.interp_membership(edad, edad_joven, v_edad)
    valor_membresia_edad_adulto = fuzz.interp_membership(edad, edad_adulto, v_edad)
    valor_membresia_edad_anciano = fuzz.interp_membership(edad, edad_anciano, v_edad)

    valor_membresia_antiguedad_Malo = fuzz.interp_membership(antiguedad, antiguedad_Malo, v_antiguedad)
    valor_membresia_antiguedad_Normal = fuzz.interp_membership(antiguedad, antiguedad_Normal, v_antiguedad)
    valor_membresia_antiguedad_Bueno = fuzz.interp_membership(antiguedad, antiguedad_Bueno, v_antiguedad)

    valor_membresia_personas_cargo_pocas = fuzz.interp_membership(personas_cargo, personas_cargo_pocas, v_personas_cargo)
    valor_membresia_personas_cargo_normal = fuzz.interp_membership(personas_cargo, personas_cargo_normal, v_personas_cargo)
    valor_membresia_personas_cargo_muchas = fuzz.interp_membership(personas_cargo, personas_cargo_muchas, v_personas_cargo)

    valor_membresia_RRF_bajo = fuzz.interp_membership(RRF, RRF_bajo, v_RRF)
    valor_membresia_RRF_medio = fuzz.interp_membership(RRF, RRF_medio, v_RRF)
    valor_membresia_RRF_alto = fuzz.interp_membership(RRF, RRF_alto, v_RRF)
    
    all_memberships = {
        'valor_membresia_ingresos_bajo': valor_membresia_ingresos_bajo,
        'valor_membresia_ingresos_medio': valor_membresia_ingresos_medio,
        'valor_membresia_ingresos_alto': valor_membresia_ingresos_alto,
        'valor_membresia_calificacion_crediticia_bajo': valor_membresia_calificacion_crediticia_bajo,
        'valor_membresia_calificacion_crediticia_medio': valor_membresia_calificacion_crediticia_medio,
        'valor_membresia_calificacion_crediticia_alto': valor_membresia_calificacion_crediticia_alto,
        'valor_membresia_obligaciones_financieras_bajo': valor_membresia_obligaciones_financieras_bajo,
        'valor_membresia_obligaciones_financieras_normal': valor_membresia_obligaciones_financieras_normal,
        'valor_membresia_obligaciones_financieras_alta': valor_membresia_obligaciones_financieras_alta,
        'valor_membresia_edad_joven': valor_membresia_edad_joven,
        'valor_membresia_edad_adulto': valor_membresia_edad_adulto,
        'valor_membresia_edad_anciano': valor_membresia_edad_anciano,
        'valor_membresia_antiguedad_Malo': valor_membresia_antiguedad_Malo,
        'valor_membresia_antiguedad_Normal': valor_membresia_antiguedad_Normal,
        'valor_membresia_antiguedad_Bueno': valor_membresia_antiguedad_Bueno,
        'valor_membresia_personas_cargo_pocas': valor_membresia_personas_cargo_pocas,
        'valor_membresia_personas_cargo_normal': valor_membresia_personas_cargo_normal,
        'valor_membresia_personas_cargo_muchas': valor_membresia_personas_cargo_muchas,
        'valor_membresia_RRF_bajo': valor_membresia_RRF_bajo,
        'valor_membresia_RRF_medio': valor_membresia_RRF_medio,
        'valor_membresia_RRF_alto': valor_membresia_RRF_alto,
    }

# Definir los grupos de variables y sus posibles valores
    grupos_variables = {
        'ingresos': ['bajo', 'medio', 'alto'],
        'calificacion_crediticia': ['bajo', 'medio', 'alto'],
        'obligaciones_financieras': ['bajo', 'normal', 'alta'],
        'edad': ['joven', 'adulto', 'anciano'],
        'antiguedad': ['Malo', 'Normal', 'Bueno'],
        'personas_cargo': ['pocas', 'normal', 'muchas'],
        'RRF': ['bajo', 'medio', 'alto'],
    }

    # Calcular la pertenencia definitiva para cada grupo
    resultados_centroide = {}
    for var, valores in grupos_variables.items():
        mejor_var, mejor_membresia = centroide_pertenencia(var, valores, all_memberships)
        resultados_centroide[var] = (mejor_var, mejor_membresia)
    return resultados_centroide

def calculateScore(edad,calificacion_crediticia,obligaciones_financieras,ingresos,antiguedad,personas_cargo,RRF):
  d1 = calificacion_crediticia+obligaciones_financieras+ingresos
  d2 = antiguedad+personas_cargo+RRF
  d3 = edad
  return (d1*d2)+d3

def eval_score(vingresos,vcalificacion_crediticia,vobligaciones_financieras,vedad,vantiguedad,vpersonas_cargo,vRRF):
    resultados_centroide = membership_functions(vingresos,vcalificacion_crediticia,vobligaciones_financieras,vedad,vantiguedad,vpersonas_cargo,vRRF)
    vedad = eval(f"edad_{resultados_centroide['edad'][0]}_score")
    vingresos = eval(f"ingresos_{resultados_centroide['ingresos'][0]}_score")
    vcalificacion_crediticia = eval(f"calificacion_crediticia_{resultados_centroide['calificacion_crediticia'][0]}_score")
    vobligaciones_financieras =  eval(f"obligaciones_financieras_{resultados_centroide['obligaciones_financieras'][0]}_score")
    vantiguedad = eval(f"antiguedad_{resultados_centroide['antiguedad'][0]}_score")
    vpersonas_cargo = eval(f"personas_cargo_{resultados_centroide['personas_cargo'][0]}_score")
    vRRF = eval(f"RRF_{resultados_centroide['RRF'][0]}_score")

    result = calculateScore(vedad,vcalificacion_crediticia,vobligaciones_financieras,vingresos,vantiguedad,vpersonas_cargo,vRRF)
    return result

def get_score(vingresos,vcalificacion_crediticia,vobligaciones_financieras,vedad,vantiguedad,vpersonas_cargo,vRRF):

    min_val = 0.28
    max_val = 3.50

    score = np.arange(0, max_val+0.1, 0.1)

    score_bajo = fuzz.trapmf(score,[min_val, 0.98, 0.98, 1.68])
    score_medio  = fuzz.trapmf(score,[0.98, 1.68, 1.68, 2.38])
    score_alto  = fuzz.trapmf(score,[1.68, 2.38, 2.38, max_val])

    result = eval_score(vingresos,vcalificacion_crediticia,vobligaciones_financieras,vedad,vantiguedad,vpersonas_cargo,vRRF)

    valor_membresia_score_bajo = fuzz.interp_membership(score, score_bajo, result)
    valor_membresia_score_medio = fuzz.interp_membership(score, score_medio, result)
    valor_membresia_score_alto = fuzz.interp_membership(score, score_alto, result)
    all_memberships = {
        'valor_membresia_score_bajo': valor_membresia_score_bajo,
        'valor_membresia_score_medio': valor_membresia_score_medio,
        'valor_membresia_score_alto': valor_membresia_score_alto,
    }
    # Definir los grupos de variables y sus posibles valores
    grupos_variables = {
        'score': ['bajo', 'medio', 'alto'],
    }

    # Calcular la pertenencia definitiva para cada grupo
    resultados_centroide = {}
    for var, valores in grupos_variables.items():
        mejor_var, mejor_membresia = centroide_pertenencia(var, valores, all_memberships)
        resultados_centroide[var] = (mejor_var, mejor_membresia)
    
    return (resultados_centroide)

