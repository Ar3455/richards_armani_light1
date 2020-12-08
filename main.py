while True:
    print("Light level:"+input.light_level())
    if input.light_level():
        light.set_all(light.rgb(0, 0, 255))
else:
    light.set_all(light.rgb(0, 0, 255 ))