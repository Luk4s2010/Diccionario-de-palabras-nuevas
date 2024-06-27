meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "FOMO": "Miedo a perderse algo",
    "GHOSTEAR": "Desaparecer de la vida de alguien sin dar explicaciones",
    "LIT": "Una abreviatura de literal o literalmente.",
    "CHALLENGE": "consisten en hacer desafíos insólitos y publicarlos en las redes sociales.",
    "CRUSH": "estar enamorado/a de alguien.",
    "HATER": "Personas que utilizan internet y las redes sociales para atacar o burlarse.",
    "MOOD": "Estado emocional, estado anímico o humor.",
    "RANDOM": "Algo aleatorio o algo cualquiera.",
}
print("Hola, soy Lucas y te ayudaré a encontrar el significado de palabras que no entiendas")

for i in range(5):

    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict:
        print("El significado de", word, "es:", meme_dict[word])
    else:
        print("Lo siento, esa palabra no está en el diccionario.")
