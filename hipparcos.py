limit_magnitude = 6.0

hip = open('hip_main.dat')
lines = hip.readlines()

ralist = []
declist = []
maglist = []


def separate(line):
    sep_line = []
    line = line.rsplit('|')
    for item in line:
        sep_line.append(item.strip())
    return sep_line


def querryHip():
    for line in lines:
        sep_line = separate(line)
        try:
            # mag, ra, dec
            star = (float(sep_line[5]),
                    float(sep_line[8]),
                    float(sep_line[9]))
            if star[0] < limit_magnitude:
                ralist.append(star[1])
                declist.append(star[2])
                maglist.append(10 * 3 ** -star[0])
        except ValueError:
            pass
