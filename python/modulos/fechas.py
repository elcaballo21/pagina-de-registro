from datetime import date

def obtenerfecha():
    fecha = date.today()
    d1 = fecha.strftime("%d/%m/%Y")
    return d1
