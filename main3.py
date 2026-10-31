
import pyttsx3
import os
import random

# ==========================================
#       APLICACION PROFESIONAL DE VOZ
# ==========================================

class AplicacionVoz:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("volume", 1.0)
        self.engine.setProperty("rate", 150)

        self.voices = self.engine.getProperty("voices")

        self.nombre_usuario = ""

        # Bromas aleatorias
        self.bromas = [
            "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
            "¿Qué le dice un techo a otro? Techo de menos.",
            "¿Por qué el libro de matemáticas estaba triste? Porque tenía muchos problemas.",
            "¿Qué hace una computadora cuando tiene frío? Cierra Windows.",
            "¿Cuál es el colmo de un jardinero? Que siempre lo dejen plantado."
        ]

        # Mensajes motivacionales
        self.motivacion = [
            "Nunca te rindas. Cada pequeño esfuerzo te acerca a tus metas.",
            "Confía en tus capacidades. Eres capaz de aprender cosas nuevas.",
            "Los errores son parte del aprendizaje. Sigue intentando.",
            "No importa qué tan lento avances, lo importante es no detenerte.",
            "Hoy es una nueva oportunidad para mejorar."
        ]

    # --------------------------------------
    # SALUDO AL USUARIO
    # --------------------------------------

    def saludar_usuario(self):

        print("\n¡Bienvenido a nuestra aplicación de voz!")

        self.nombre_usuario = input("¿Cómo te llamas? ").strip()

        if not self.nombre_usuario:
            self.nombre_usuario = "usuario"

        saludo = f"Hola {self.nombre_usuario}, bienvenido a tu aplicación de voz. ¿Cómo estás hoy?"

        print("\n" + saludo)

        self.engine.say(saludo)
        self.engine.runAndWait()

    # --------------------------------------
    # CONTAR BROMAS
    # --------------------------------------

    def contar_broma(self):

        broma = random.choice(self.bromas)

        print("\n¡Aquí tienes una broma!")
        print(broma)

        self.engine.say(broma)
        self.engine.runAndWait()

    # --------------------------------------
    # MENSAJES DE MOTIVACION
    # --------------------------------------

    def dar_animo(self):

        mensaje = random.choice(self.motivacion)

        print("\nMensaje de motivación:")
        print(mensaje)

        self.engine.say(mensaje)
        self.engine.runAndWait()

    # --------------------------------------
    # MOSTRAR MENU
    # --------------------------------------

    def mostrar_menu(self):

        print("\n" + "=" * 45)
        print("          SISTEMA DE SINTESIS DE VOZ")
        print("=" * 45)
        print("1. Convertir texto a voz")
        print("2. Configurar velocidad")
        print("3. Configurar volumen")
        print("4. Cambiar voz")
        print("5. Guardar audio")
        print("6. Saludar al usuario")
        print("7. Contar una broma")
        print("8. Dar un mensaje de ánimo")
        print("9. Salir")
        print("=" * 45)

    # --------------------------------------
    # CONVERTIR TEXTO A VOZ
    # --------------------------------------

    def convertir_texto(self):

        texto = input("\nIntroduce el texto que deseas escuchar: ")

        if not texto.strip():
            print("Error: No has introducido ningún texto.")
            return

        self.engine.say(texto)
        self.engine.runAndWait()

        print("\nTexto reproducido correctamente.")

    # --------------------------------------
    # CONFIGURAR VELOCIDAD
    # --------------------------------------

    def configurar_velocidad(self):

        try:
            velocidad = int(input("\nIntroduce la velocidad (100-250): "))

            if 100 <= velocidad <= 250:
                self.engine.setProperty("rate", velocidad)
                print("Velocidad actualizada correctamente.")
            else:
                print("Introduce un valor entre 100 y 250.")

        except ValueError:
            print("Error: Introduce un número válido.")

    # --------------------------------------
    # CONFIGURAR VOLUMEN
    # --------------------------------------

    def configurar_volumen(self):

        try:
            volumen = float(input("\nIntroduce el volumen (0.0-1.0): "))

            if 0.0 <= volumen <= 1.0:
                self.engine.setProperty("volume", volumen)
                print("Volumen actualizado correctamente.")
            else:
                print("El volumen debe estar entre 0.0 y 1.0.")

        except ValueError:
            print("Error: Introduce un número válido.")

    # --------------------------------------
    # CAMBIAR VOZ
    # --------------------------------------

    def cambiar_voz(self):

        print("\nVOCES DISPONIBLES")

        for i, voz in enumerate(self.voices):
            print(f"{i}. {voz.name}")

        try:
            seleccion = int(input("\nSelecciona una voz: "))

            if 0 <= seleccion < len(self.voices):
                self.engine.setProperty(
                    "voice", self.voices[seleccion].id
                )
                print("Voz cambiada correctamente.")
            else:
                print("Selección no válida.")

        except ValueError:
            print("Introduce un número válido.")

    # --------------------------------------
    # GUARDAR AUDIO
    # --------------------------------------

    def guardar_audio(self):

        texto = input("\nIntroduce el texto que deseas guardar: ")

        if not texto.strip():
            print("Error: El texto no puede estar vacío.")
            return

        nombre = input("Nombre del archivo (sin extensión): ").strip()

        if not nombre:
            print("Error: Debes introducir un nombre.")
            return

        if any(c in nombre for c in '<>:"/\\|?*'):
            print("Error: Nombre de archivo no válido.")
            return

        carpeta = "audios"
        os.makedirs(carpeta, exist_ok=True)

        ruta = os.path.join(carpeta, nombre + ".wav")

        self.engine.save_to_file(texto, ruta)
        self.engine.runAndWait()

        print(f"\nAudio guardado en: {ruta}")

    # --------------------------------------
    # EJECUTAR APLICACION
    # --------------------------------------

    def ejecutar(self):

        self.saludar_usuario()

        while True:

            self.mostrar_menu()

            opcion = input("\nSelecciona una opción: ").strip()

            if opcion == "1":
                self.convertir_texto()

            elif opcion == "2":
                self.configurar_velocidad()

            elif opcion == "3":
                self.configurar_volumen()

            elif opcion == "4":
                self.cambiar_voz()

            elif opcion == "5":
                self.guardar_audio()

            elif opcion == "6":
                self.saludar_usuario()

            elif opcion == "7":
                self.contar_broma()

            elif opcion == "8":
                self.dar_animo()

            elif opcion == "9":
                despedida = f"Hasta pronto {self.nombre_usuario}. Gracias por utilizar nuestra aplicación."

                print("\n" + despedida)

                self.engine.say(despedida)
                self.engine.runAndWait()

                self.engine.stop()
                break

            else:
                print("\nOpción no válida. Intenta nuevamente.")


# ==========================================
# INICIAR PROGRAMA
# ==========================================

if __name__ == "__main__":

    app = AplicacionVoz()
    app.ejecutar()
