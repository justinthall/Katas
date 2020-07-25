def weather_info(temp):
    c = convertToCelsius(temp)
    if (c > 0):
        return "{} is above freezing temperature".format(c)
    else:
        return "{} is freezing temperature".format(c)


def convertToCelsius(temperature):
    celsius = (temperature - 32) * (5 / 9)
    return celsius
