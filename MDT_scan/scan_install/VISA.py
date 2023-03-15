import pyvisa

rm = pyvisa.ResourceManager()
print(rm.list_resources())
resources = rm.list_resources()

for resource in resources:
    if "6500" in resource:
        my_device = rm.open_resource(resource)
        print(my_device.query("*IDN?"))

def measure_dcv():
    my_device.write("CONFigure:VOLTage:DC")
    result = str(my_device.query("MEASure:VOLTage:DC?"))
    voltage = result[0:5]
    return voltage





