
import pyttsx3
import os


class AplicacionVoz:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("volume", 1.0)
        self.engine.setProperty("rate", 150)

        self.voices = self.engine.getProperty("voices")

    # --------------------------------------
    # MOSTRAR MENU
    # --------------------------------------

    def mostrar_menu(self):
        print("\n" + "=" * 45)
        print("          SISTEMA DE SÍNTESIS DE VOZ")
        print("=" * 45)
        print("1. Convertir texto a voz")
        print("2. Configurar velocidad")
        print("3. Configurar volumen")
        print("4. Cambiar voz")
        print("5. Guardar audio")
        print("6. Salir")
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

        # Evitar nombres de archivo no válidos
        if any(c in nombre for c in '<>:"/\\|?*'):
            print("Error: El nombre contiene caracteres no permitidos.")
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
                print("\nCerrando aplicación...")
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
