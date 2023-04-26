
"""Programme pour calcluer la moyenne de chaque élèves, calculer la moyenne de la classe.
   Et afficher un classement.
"""

students = {
    "Bobby Green": [12, 15, 18],
    "Baxter Black": [10, 19, 15],
    "Rachel Brown": [14, 16, 19],
    "Jason Red": [9, 10, 14],
    "Kelly Blue": [10, 14, 18]
}

# Défini les fonctions pour les options du menu.
def display_students():
    for student, notes in students.items():
        # Sépare le nom et prénom de l'élève.
        name_surname_split = student.split()
        name = name_surname_split[1]
        surname = name_surname_split[0]
        print(f"Notes de {(surname)} {(name)} : {str(notes)}")

def calculate_average_student():
    student_input = input("Choisissez l'élève dont vous souhaitez calculer la moyenne \n> ")
    # Vérifie si l'élève existe
    if student_input not in students:
        
        return print(f"{(student_input)} n'est pas dans la liste")

    notes = students[student_input]
    average = sum(notes) / len(notes)

    # Sépare le nom et le prénom.
    name_surname_split = student_input.split()
    name = name_surname_split[1]
    surname = name_surname_split[0]
    print(f"Moyenne de {(surname)} {(name)} : {str(average)}")

def calculate_average_class():
    notes = []
    for student in students.values():
        notes.extend(student)

    average = sum(notes) / len(notes)
    print(f"La moyenne de la classe est de {(average)}")

def display_ranking():
    averages = {}

    for student, notes in students.items():
        average = sum(notes) / len(notes)
        averages[student] = average

    ranking = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    print(f"classement des élèves")

    for i, (student, average) in enumerate(ranking):
        name_surname_split = student.split()
        name = name_surname_split[1]
        surname = name_surname_split[0]
        print(f"{str(i+1)} {(surname)} {(name)} a une moyenne de {(round(average), 2)}")

# Boucle principal du programme.
while True:
	# Afficher le menu.
	print("\nMenu principal")
	print("1. Afficher les élèves et leurs notes")
	print("2. Calculer la moyenne d'un élève")
	print("3. Calculer la moyenne de la classe")
	print("4. Afficher le classement des élèves")
	print("5. Quitter le programme\n")

	choice_menu = input("Choisissez le numéro de votre choix :\n> ")

	if choice_menu == "1":
		display_students()
	elif choice_menu == "2":
		calculate_average_student()
	elif choice_menu == "3":
		calculate_average_class()
	elif choice_menu == "4":
		display_ranking()
	elif choice_menu == "5":
		print("Merci d'avoir utiliser se programme !")
		break
	else:
		print("Choix invalide, saisir un nombre entre 1 et 5.")




