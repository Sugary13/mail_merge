# 📬 Carta personalizada con Python

Este proyecto automatiza la creación de cartas personalizadas utilizando Python. A partir de una plantilla con un marcador (`[name],`) y una lista de nombres, el programa genera una carta individual para cada persona, lista para enviar.

---

## 📁 Estructura del proyecto

project-root/
├── Input/
│ ├── Letters/
│ │ └── starting_letter.txt
│ └── Names/
│ └── invited_names.txt
├── Output/
│ └── ReadyToSend/
│ └── letter_for_<name>.txt
├── main.py
└── README.md


---

## 🧠 ¿Qué hace el script?

1. Lee una **plantilla de carta** (`starting_letter.txt`) con el marcador `[name],`.
2. Lee una **lista de nombres** (`invited_names.txt`), uno por línea.
3. Para cada nombre:
   - Elimina saltos de línea y espacios extra.
   - Reemplaza `[name],` por el nombre real.
   - Guarda la carta personalizada como `letter_for_<name>.txt`.

---

## 📝 Ejemplo

### Entrada (plantilla):

Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Carlos


### Entrada (nombres):

Maria
Jose
Eduardo


### Salidas generadas:
- `letter_for_Maria.txt`
- `letter_for_Jose.txt`
- `letter_for_Eduardo.txt`

---

## 🚀 Cómo ejecutar

1. Asegúrate de tener Python 3 instalado.
2. Organiza los archivos como se muestra arriba.
3. Ejecuta el script:

```bash
python main.py

4. Las cartas aparecerán en ./Output/ReadyToSend/.

🏁 Autor
Carlos Esquerra Martínez
