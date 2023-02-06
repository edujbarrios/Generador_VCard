import qrcode
import os

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def main():
    print("Generador de Código QR de Contacto")
    print("Opciones:")
    print("1. Pulsa '1' para crear una VCARD")
    opcion = int(input("Elije una opción: "))
    data = ""
    if opcion == 1:
        nombre = input("Introduzca el nombre: ")
        movil = input("Introduzca el número de móvil: ")
        trabajo = input("Introduzca el número de trabajo: ")
        email = input("Introduzca la dirección de email: ")
        direccion = input("Introduzca la dirección completa: ")
        sitio_web = input("Introduzca la URL del sitio web: ")
        trabajo = input("Introduzca la información laboral: ")
        data = "BEGIN:VCARD\n" + "VERSION:3.0\n" + "N:" + nombre + "\n" + "TEL;TYPE=WORK,VOICE:" + trabajo + "\n" + "TEL;TYPE=CELL,VOICE:" + movil + "\n" + "ADR;TYPE=WORK:" + direccion + "\n" + "EMAIL;TYPE=PREF,INTERNET:" + email + "\n" + "URL:" + sitio_web + "\n" + "ROLE:" + trabajo + "\n" + "END:VCARD"
        img = generate_qr_code(data)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        img.save(current_dir + "\contacto_qr.png")
        print("El archivo se ha guardado en el mismo directorio en el que se encuentra el script.")
        exit()
    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()
	