import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

#
import sqlite3

# je demande à la bibliotheque sqlite de me donner une connection
# sur ma base de données
conn = sqlite3.connect('students.db')

# ensuite je demande un curseur
# c'est grace au curseur que je peux effectuer des requetes
c = conn.cursor()

# la premire requete: je m'assure que la table existe, autrement je la crée
c.execute('''CREATE TABLE IF NOT EXISTS students
             (name TEXT, age INTEGER, major TEXT)''')
conn.commit()


# Navigation
# je veux un menu dans la marge
st.sidebar.title("Menu")

# je veux un bouton radio dans la marge afin de selectionner la page que je veux
page = st.sidebar.radio("Go to", ["List Students", "Add Student", "Graphic analysis"])


# List Students Page
if page == "List Students":
    # j'affiche la liste des etudiants
    st.title("List of Students")
    st.write("Here you can see the list of students.")

    # je selectionne tous les etudiants depuis la table
    c.execute("SELECT * FROM students")
    # pour dire au système que vous voulez "posséder" les résultat de la requete
    # alors, il faut appeler la méthode fetchall
    students = c.fetchall()
    data = []
    for student in students:    

        # je recupere les elements de chaque occurence sous forme d'un dictionnaire
        dico ={
                "Name": student[0], 
                "Age": student[1], 
                "Major": student[2]
                }
        
        # je fusionne les dictionnaires
        data.append(dico)

        # je convertis en base de donnees
    df = pd.DataFrame(data)

    # et j'affiche
    st.dataframe(df, use_container_width=True)
# add graphic analysis
elif page == "Graphic analysis":
    st.title("Analysis name student and age")
    st.write("Presentation des etudiants en fonction de leurs ages")
    students = c.fetchall()
    data = []
    for student in students:    

        # je recupere les elements de chaque occurence sous forme d'un dictionnaire
        dico ={
                "Name": student[0], 
                "Age": student[1], 
                "Major": student[2]
                }
        
        # je fusionne les dictionnaires
        data.append(dico)

        # je convertis en base de donnees
    df = pd.DataFrame(data)
    #st.bar_chart(df, column=["Name", "Age"])   
    #fig = px.bar(Name=df[0], Age=df[1])
    plt.bar(df[0],df[1], data=df)

# Add Student Page
elif page == "Add Student":
    st.title("Add a New Student")
    st.write("Enter student details below:")

    # formulaire d'ajout
    with st.form(key='add_student_form'):
        # les champs de mon formulaire
        name = st.text_input(label='Name')
        age = st.number_input(label='Age', min_value=1, max_value=100)
        major = st.text_input(label='Major')
        submit = st.form_submit_button(label='Add Student')

        # après soumission
        if submit:
            # j'insere en utilisant une requete SQL d'insertion
            c.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)",
                      (name, age, major))

            # demander un enregistrement effectif de toutes les modif effectuées
            conn.commit()
            # afficher un message de succès
            st.success(f"Added {name} to the database!")

conn.close()
