import datetime


agora = datetime.datetime.now()
fmt = agora.strftime("%d/%m/%Y %H:%M")

print(fmt)


"""
data_string = "2020-17-12 07:00"
data_format = "%Y-%d-%m %H:%M"

datafmt = dt.datetime.strptime(data_string, data_format)

print(datafmt)
"""
""""
agora = dt.datetime.now()
daqui_um_minuto = agora + dt.timedelta(minutes = 45)

print(agora)

data_inicial = ""
"""
"""
cont = 0
for i in range(10):
    cont += 60
    #daqui_um_minuto = agora + dt.timedelta(minutes = cont)
    #dat = daqui_um_minuto.strftime("%d/%m/%Y %H:%M")
    #print(dat)

    mint = datafmt + dt.timedelta(minutes=cont)
    dat = mint.strftime("%d/%m/%Y %H:%M")
    print(dat)

"""