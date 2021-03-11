minmag = 6.0

hip = open('hip_main.dat')
lines = hip.readlines()

stars = []

ralist = []
declist = []
maglist = []


def chop(line):
    choppedline = []
    list_with_space = line.rsplit('|')
    for item in list_with_space:
        choppedline.append(item.strip())
    return choppedline


def querryHip():
    for line in lines:
        chopdline = chop(line)
        try:
            newstar = {}
            newstar['mag'] = float(chopdline[5])
            newstar['ra'] = float(chopdline[8])
            newstar['de'] = float(chopdline[9])
            stars.append(newstar)
        except ValueError:
            pass

    for star in stars:
        if star['mag'] < minmag:
            ralist.append(star['ra'])
            declist.append(star['de'])
            maglist.append(10 * 3 ** -star['mag'])
