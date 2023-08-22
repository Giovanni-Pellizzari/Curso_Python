#diferencia en porcentaje entre el curso actual y el mas rapido de los otros cursos

curso_actual = 1.5
curso_mas_rapido = 2.5
curso_mas_lento = 7 
curso_promedio = 4
crudo_cursos = 5
crudo_este_curso = 3.5


porcentaje = 100 - curso_actual / curso_mas_rapido * 100
porcentaje2 = 100 - curso_actual * 1000 // curso_mas_lento /10 
porcentaje3 = 100 - curso_actual / curso_promedio * 100

print (f" - Este curso dura un  {porcentaje} % menos que el curso más rapido")
print(f" - Este curso dura un {porcentaje2}% menos que el curso más lento")
print(f" - Este curso dura un {porcentaje3}% menos que el promedio de los cursos")
print(" ")


porcentaje_crudo_este_curso = 100 - curso_actual * 1000 // crudo_este_curso / 10
porcentaje_crudo_otros_cursos = 100 - curso_promedio *1000 // crudo_cursos / 10

print(f" - Este curso eliminia el {porcentaje_crudo_este_curso}% del crudo")
print(f" - El promedio de los cursos eliminan el {porcentaje_crudo_otros_cursos}% del crudo")
print(" ")


horas_curso_actual = curso_promedio *100 // curso_actual / 10

print(f" - Ver 10 horas de este curso equivale a ver {horas_curso_actual} horas de otro cuso")

