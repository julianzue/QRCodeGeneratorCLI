def generator():
    import qrcode
    import pyfiglet
    from colorama import Fore, init
    import os

    init()

    yellow = Fore.LIGHTYELLOW_EX
    green = Fore.LIGHTGREEN_EX
    reset = Fore.RESET

    f = pyfiglet.Figlet(width=100)
    print(f.renderText("QR Code Generator"))

    url = input(yellow + "[+] Enter URL: " + reset)

    name = url.split(".")
    
    img = qrcode.make(url)

    save_as = input(yellow + "[+] Save as: " + reset + "'QR_-_" + name[1] + ".jpg'" + yellow + "? [y|n] [default: y]: " + reset)

    if save_as == "" or save_as == "y":
        name = "QR_-_" + name[1] + ".jpg"
    else:
        name = input(yellow + "[+] Enter name: " + reset)

    if not os.path.exists("./Pictures"):
        os.system("mkdir Pictures")

    img.save("Pictures/" + name)
    
    print(green + "[*] Successfully saved!" + reset)

    again = input("[+] Again? [y|n] [default: n]: ")

    if again == "" or again == "n":
        quit()
    else:
        generator()

try:
    generator()

except ModuleNotFoundError:

    print("[*] Installing Modules")
    print("")
    
    import os

    os.system("pip install colorama")
    os.system("pip install qrcode")
    os.system("pip install pyfiglet")

    print("")

    print("[*] All required modules installed!")

    print("")

    generator()