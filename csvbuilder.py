from sys import argv
from os.path import exists

"""    
Input format:
    <latitude1> <longitude1> <latitude2> <longitude2> <type> <direction> <count>

 <latitude> <longitude>: starting and ending coordinates of the row
                 <type>: [normal], [staff], [ev], [handicap], [coin]
            <direction>: [H]orizontal, [V]ertical
                <count>: number of spaces in this row
 
Example: 
    33.670467 -117.908397 33.670192 -117.908001 normal v 21
"""

def get_delta(x, y, lots):
    return (y - x) / lots

script, from_file, to_file = argv

if not exists(to_file):
    print "%s not found! Creating a new copy..." % (to_file)
    out_file = open(to_file, 'w')
else:
    print "Appending to %s..." % (to_file)
    out_file = open(to_file, 'a')

with open(from_file) as f:
    lines = f.readlines()
#line = raw_input(">").split(' ')
line = lines[0].split(' ')
linenum = 1
idx = 1
while (line[0] != 'q' or len(line) == 7) and linenum < len(lines):
    lat1, long1, lat2, long2, lot_type, direction, lots = line
    lat1, long1, lat2, long2 = float(lat1), float(long1), float(lat2), float(long2)
    lots = int(lots)
    if direction.upper() == 'H':
        if lat1 > lat2:
            lat1, lat2 = lat2, lat1
        delta = get_delta(lat1, lat2, lots)    
        lat = delta + lat1
        while lat <= lat2:
            out_file.write(str(idx) + ',' + lot_type + ',' + str(lat) + ',' + str(long1) + ',' + str(idx % 2) + '\n')
            lat = lat + delta
            idx = idx + 1
    else:
        if long1 > long2:
            long1, long2 = long2, long1
        delta = get_delta(long1, long2, lots)
        lon = delta + long1
        while lon <= long2:
            out_file.write(str(idx) + ',' + lot_type + ',' + str(lat1) + ',' + str(lon) + ',' + str(idx % 2) + '\n')
            lon = lon + delta
            idx = idx + 1
    #line = raw_input(">").split(' ')
    line = lines[linenum].split(' ')
    linenum = linenum + 1
    

out_file.close()


