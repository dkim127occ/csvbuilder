# CSVBuilder
An automated CSV builder built using something that does not resemble Python at all.

##Usage
    python csvbuilder.py inputfile outputcsv.csv

##Input file format
    <latitude1> <longitude1> <latitude2> <longitude2> <type> <direction> <count>

    <latitude> <longitude>: starting and ending coordinates of the row
                    <type>: [normal], [staff], [ev], [handicap], [coin]
               <direction>: [H]orizontal, [V]ertical
                   <count>: number of spaces in this row

 
##Example input file 
        # single row
        33.670467 -117.908397 33.670192 -117.908001 normal v 21
        
        # multiple rows
        33.670467 -117.908397 33.670192 -117.908001 normal v 21
        35.670467 -117.908397 33.670192 -117.908001 normal h 10


        
