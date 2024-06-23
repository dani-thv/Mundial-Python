import tkinter as tk
from tkinter import ttk, messagebox

class FootballApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Football App")

        self.equipos = {
            'España': {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0},
            'Francia': {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0},
            'Alemania': {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0},
            'Holanda': {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0},
        }

        self.jugadores = {
            'España': [
                {"Nombre": "David", "Apellido": "De Gea", "Edad": 33, "Posición": "Portero"},
                {"Nombre": "Sergio", "Apellido": "Ramos", "Edad": 38, "Posición": "Defensa"},
                {"Nombre": "Jordi", "Apellido": "Alba", "Edad": 35, "Posición": "Defensa"},
                {"Nombre": "Sergio", "Apellido": "Busquets", "Edad": 35, "Posición": "Centrocampista"},
                {"Nombre": "Thiago", "Apellido": "Alcántara", "Edad": 33, "Posición": "Centrocampista"},
                {"Nombre": "Isco", "Apellido": "Alarcón", "Edad": 32, "Posición": "Centrocampista"},
                {"Nombre": "Álvaro", "Apellido": "Morata", "Edad": 31, "Posición": "Delantero"},
                {"Nombre": "Gerard", "Apellido": "Moreno", "Edad": 32, "Posición": "Delantero"},
                {"Nombre": "Rodrigo", "Apellido": "Moreno", "Edad": 33, "Posición": "Delantero"},
            ],
            'Francia': [
                {"Nombre": "Hugo", "Apellido": "Lloris", "Edad": 37, "Posición": "Portero"},
                {"Nombre": "Benjamin", "Apellido": "Pavard", "Edad": 28, "Posición": "Defensa"},
                {"Nombre": "Raphael", "Apellido": "Varane", "Edad": 31, "Posición": "Defensa"},
                {"Nombre": "Lucas", "Apellido": "Hernandez", "Edad": 28, "Posición": "Defensa"},
                {"Nombre": "N'Golo", "Apellido": "Kante", "Edad": 33, "Posición": "Centrocampista"},
                {"Nombre": "Paul", "Apellido": "Pogba", "Edad": 31, "Posición": "Centrocampista"},
                {"Nombre": "Kylian", "Apellido": "Mbappe", "Edad": 25, "Posición": "Delantero"},
                {"Nombre": "Antoine", "Apellido": "Griezmann", "Edad": 33, "Posición": "Delantero"},
                {"Nombre": "Ousmane", "Apellido": "Dembele", "Edad": 27, "Posición": "Delantero"},
            ],
            'Alemania': [
                {"Nombre": "Manuel", "Apellido": "Neuer", "Edad": 38, "Posición": "Portero"},
                {"Nombre": "Joshua", "Apellido": "Kimmich", "Edad": 29, "Posición": "Defensa"},
                {"Nombre": "Antonio", "Apellido": "Rüdiger", "Edad": 31, "Posición": "Defensa"},
                {"Nombre": "Niklas", "Apellido": "Süle", "Edad": 28, "Posición": "Defensa"},
                {"Nombre": "Ilkay", "Apellido": "Gündogan", "Edad": 33, "Posición": "Centrocampista"},
                {"Nombre": "Leon", "Apellido": "Goretzka", "Edad": 29, "Posición": "Centrocampista"},
                {"Nombre": "Thomas", "Apellido": "Müller", "Edad": 34, "Posición": "Delantero"},
                {"Nombre": "Timo", "Apellido": "Werner", "Edad": 28, "Posición": "Delantero"},
                {"Nombre": "Kai", "Apellido": "Havertz", "Edad": 25, "Posición": "Delantero"},
            ],
            'Holanda': [
                {"Nombre": "Jasper", "Apellido": "Cillessen", "Edad": 35, "Posición": "Portero"},
                {"Nombre": "Denzel", "Apellido": "Dumfries", "Edad": 28, "Posición": "Defensa"},
                {"Nombre": "Matthijs", "Apellido": "de Ligt", "Edad": 24, "Posición": "Defensa"},
                {"Nombre": "Virgil", "Apellido": "van Dijk", "Edad": 32, "Posición": "Defensa"},
                {"Nombre": "Nathan", "Apellido": "Aké", "Edad": 29, "Posición": "Defensa"},
                {"Nombre": "Marten", "Apellido": "de Roon", "Edad": 33, "Posición": "Centrocampista"},
                {"Nombre": "Frenkie", "Apellido": "de Jong", "Edad": 27, "Posición": "Centrocampista"},
                {"Nombre": "Georginio", "Apellido": "Wijnaldum", "Edad": 33, "Posición": "Centrocampista"},
                {"Nombre": "Memphis", "Apellido": "Depay", "Edad": 30, "Posición": "Delantero"},
                {"Nombre": "Cody", "Apellido": "Gakpo", "Edad": 25, "Posición": "Delantero"},
                {"Nombre": "Steven", "Apellido": "Bergwijn", "Edad": 26, "Posición": "Delantero"},
            ],
        }

        self.setup_ui()

    def setup_ui(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=1, fill="both")

        # Pestaña para equipos
        frame_equipos = ttk.Frame(notebook)
        notebook.add(frame_equipos, text="Equipos")

        self.tree_equipos = ttk.Treeview(frame_equipos, columns=("Equipo", "PJ", "G", "E", "P", "GF", "GC", "Pts"), show="headings")
        self.tree_equipos.heading("Equipo", text="Equipo")
        self.tree_equipos.heading("PJ", text="PJ")
        self.tree_equipos.heading("G", text="G")
        self.tree_equipos.heading("E", text="E")
        self.tree_equipos.heading("P", text="P")
        self.tree_equipos.heading("GF", text="GF")
        self.tree_equipos.heading("GC", text="GC")
        self.tree_equipos.heading("Pts", text="Pts")
        self.tree_equipos.pack(fill=tk.BOTH, expand=True)

        self.tree_equipos.column("Equipo", width=100)
        self.tree_equipos.column("PJ", width=30)
        self.tree_equipos.column("G", width=30)
        self.tree_equipos.column("E", width=30)
        self.tree_equipos.column("P", width=30)
        self.tree_equipos.column("GF", width=30)
        self.tree_equipos.column("GC", width=30)
        self.tree_equipos.column("Pts", width=30)

        for equipo, stats in self.equipos.items():
            self.tree_equipos.insert("", "end", values=(equipo, stats["PJ"], stats["G"], stats["E"], stats["P"], stats["GF"], stats["GC"], stats["Pts"]))

        frame_agregar_equipo = ttk.Frame(notebook)
        notebook.add(frame_agregar_equipo, text="Agregar Equipo")

        ttk.Label(frame_agregar_equipo, text="Nombre del Equipo:").grid(row=0, column=0)
        self.entry_equipo_nuevo = ttk.Entry(frame_agregar_equipo)
        self.entry_equipo_nuevo.grid(row=0, column=1)
        self.button_agregar_equipo = ttk.Button(frame_agregar_equipo, text="Agregar", command=self.agregar_equipo)
        self.button_agregar_equipo.grid(row=0, column=2)

        # Pestaña para jugadores
        frame_jugadores = ttk.Frame(notebook)
        notebook.add(frame_jugadores, text="Jugadores")

        ttk.Label(frame_jugadores, text="Equipo:").grid(row=0, column=0)
        self.combo_equipos = ttk.Combobox(frame_jugadores, values=list(self.jugadores.keys()))
        self.combo_equipos.grid(row=0, column=1)
        self.combo_equipos.bind("<<ComboboxSelected>>", self.mostrar_jugadores)

        self.tree_jugadores = ttk.Treeview(frame_jugadores, columns=("Nombre", "Apellido", "Edad", "Posición"), show="headings")
        self.tree_jugadores.heading("Nombre", text="Nombre")
        self.tree_jugadores.heading("Apellido", text="Apellido")
        self.tree_jugadores.heading("Edad", text="Edad")
        self.tree_jugadores.heading("Posición", text="Posición")
        self.tree_jugadores.grid(row=1, column=0, columnspan=2, sticky="nsew")

        frame_jugadores.grid_rowconfigure(1, weight=1)
        frame_jugadores.grid_columnconfigure(1, weight=1)

        frame_agregar_jugador = ttk.Frame(notebook)
        notebook.add(frame_agregar_jugador, text="Agregar Jugador")

        ttk.Label(frame_agregar_jugador, text="Equipo:").grid(row=0, column=0)
        self.combo_equipo_jugador = ttk.Combobox(frame_agregar_jugador, values=list(self.jugadores.keys()))
        self.combo_equipo_jugador.grid(row=0, column=1)

        ttk.Label(frame_agregar_jugador, text="Nombre:").grid(row=1, column=0)
        self.entry_nombre_jugador = ttk.Entry(frame_agregar_jugador)
        self.entry_nombre_jugador.grid(row=1, column=1)

        ttk.Label(frame_agregar_jugador, text="Apellido:").grid(row=2, column=0)
        self.entry_apellido_jugador = ttk.Entry(frame_agregar_jugador)
        self.entry_apellido_jugador.grid(row=2, column=1)

        ttk.Label(frame_agregar_jugador, text="Edad:").grid(row=3, column=0)
        self.entry_edad_jugador = ttk.Entry(frame_agregar_jugador)
        self.entry_edad_jugador.grid(row=3, column=1)

        ttk.Label(frame_agregar_jugador, text="Posición:").grid(row=4, column=0)
        self.entry_posicion_jugador = ttk.Entry(frame_agregar_jugador)
        self.entry_posicion_jugador.grid(row=4, column=1)

        self.button_agregar_jugador = ttk.Button(frame_agregar_jugador, text="Agregar", command=self.agregar_jugador)
        self.button_agregar_jugador.grid(row=5, column=1)

        # Pestaña para gestionar partidos
        frame_partidos = ttk.Frame(notebook)
        notebook.add(frame_partidos, text="Gestionar Partidos")

        ttk.Label(frame_partidos, text="Equipo Local:").grid(row=0, column=0)
        self.combo_equipo_local = ttk.Combobox(frame_partidos, values=list(self.equipos.keys()))
        self.combo_equipo_local.grid(row=0, column=1)

        ttk.Label(frame_partidos, text="Equipo Visitante:").grid(row=1, column=0)
        self.combo_equipo_visitante = ttk.Combobox(frame_partidos, values=list(self.equipos.keys()))
        self.combo_equipo_visitante.grid(row=1, column=1)

        ttk.Label(frame_partidos, text="Goles Local:").grid(row=2, column=0)
        self.entry_goles_local = ttk.Entry(frame_partidos)
        self.entry_goles_local.grid(row=2, column=1)

        ttk.Label(frame_partidos, text="Goles Visitante:").grid(row=3, column=0)
        self.entry_goles_visitante = ttk.Entry(frame_partidos)
        self.entry_goles_visitante.grid(row=3, column=1)

        self.button_gestionar_partido = ttk.Button(frame_partidos, text="Registrar Partido", command=self.registrar_partido)
        self.button_gestionar_partido.grid(row=4, column=1)

    def agregar_equipo(self):
        nuevo_equipo = self.entry_equipo_nuevo.get()
        if nuevo_equipo and nuevo_equipo not in self.equipos:
            self.equipos[nuevo_equipo] = {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0}
            self.tree_equipos.insert("", "end", values=(nuevo_equipo, 0, 0, 0, 0, 0, 0, 0))
            self.jugadores[nuevo_equipo] = []
            self.combo_equipos["values"] = list(self.jugadores.keys())
            self.combo_equipo_jugador["values"] = list(self.jugadores.keys())
            self.combo_equipo_local["values"] = list(self.equipos.keys())
            self.combo_equipo_visitante["values"] = list(self.equipos.keys())
            messagebox.showinfo("Éxito", "Equipo agregado exitosamente.")
        else:
            messagebox.showerror("Error", "El equipo ya existe o el nombre es inválido.")

    def mostrar_jugadores(self, event):
        equipo_seleccionado = self.combo_equipos.get()
        if equipo_seleccionado in self.jugadores:
            for item in self.tree_jugadores.get_children():
                self.tree_jugadores.delete(item)
            for jugador in self.jugadores[equipo_seleccionado]:
                self.tree_jugadores.insert("", "end", values=(jugador["Nombre"], jugador["Apellido"], jugador["Edad"], jugador["Posición"]))

    def agregar_jugador(self):
        equipo_seleccionado = self.combo_equipo_jugador.get()
        nombre = self.entry_nombre_jugador.get()
        apellido = self.entry_apellido_jugador.get()
        edad = self.entry_edad_jugador.get()
        posicion = self.entry_posicion_jugador.get()

        if equipo_seleccionado and nombre and apellido and edad and posicion:
            nuevo_jugador = {"Nombre": nombre, "Apellido": apellido, "Edad": edad, "Posición": posicion}
            self.jugadores[equipo_seleccionado].append(nuevo_jugador)
            messagebox.showinfo("Éxito", "Jugador agregado exitosamente.")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    def registrar_partido(self):
        equipo_local = self.combo_equipo_local.get()
        equipo_visitante = self.combo_equipo_visitante.get()
        goles_local = self.entry_goles_local.get()
        goles_visitante = self.entry_goles_visitante.get()

        if equipo_local and equipo_visitante and goles_local.isdigit() and goles_visitante.isdigit() and equipo_local != equipo_visitante:
            goles_local = int(goles_local)
            goles_visitante = int(goles_visitante)

            self.equipos[equipo_local]["PJ"] += 1
            self.equipos[equipo_visitante]["PJ"] += 1

            self.equipos[equipo_local]["GF"] += goles_local
            self.equipos[equipo_visitante]["GF"] += goles_visitante

            self.equipos[equipo_local]["GC"] += goles_visitante
            self.equipos[equipo_visitante]["GC"] += goles_local

            if goles_local > goles_visitante:
                self.equipos[equipo_local]["G"] += 1
                self.equipos[equipo_visitante]["P"] += 1
                self.equipos[equipo_local]["Pts"] += 3
            elif goles_local < goles_visitante:
                self.equipos[equipo_visitante]["G"] += 1
                self.equipos[equipo_local]["P"] += 1
                self.equipos[equipo_visitante]["Pts"] += 3
            else:
                self.equipos[equipo_local]["E"] += 1
                self.equipos[equipo_visitante]["E"] += 1
                self.equipos[equipo_local]["Pts"] += 1
                self.equipos[equipo_visitante]["Pts"] += 1

            self.actualizar_estadisticas()

            messagebox.showinfo("Éxito", "Partido registrado exitosamente.")
        else:
            messagebox.showerror("Error", "Datos del partido inválidos o incompletos.")

    def actualizar_estadisticas(self):
        for item in self.tree_equipos.get_children():
            self.tree_equipos.delete(item)
        for equipo, stats in self.equipos.items():
            self.tree_equipos.insert("", "end", values=(equipo, stats["PJ"], stats["G"], stats["E"], stats["P"], stats["GF"], stats["GC"], stats["Pts"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = FootballApp(root)
    root.mainloop()
