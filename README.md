# description
use in command line with mapbox human activity data
this doesn't write to a file by default, so use the > operator to write the stdout to a file (examples below).
It can read a csv file, but you can also use cat and pipe it through the program to generate the file on the fly.
can take 10 or 20 minutes

# examples
`cat had.csv | ./subset.py -bbox 12.23666 51.23809 12.542491 51.448032 > HAD_leipzig.csv`
`cat had.csv | ./subset.py -bbox 7.529068 51.904036 7.713776 52.017008 > HAD_muenster.csv`
`cat had.csv | ./subset.py -bbox 7.3023870 51.4155255 7.6381570 51.6000415 > HAD_dortmund.csv`
`cat had.csv | ./subset.py -bbox 6.4779483 51.2857809 6.7062122 51.4054910 > HAD_krefeld.csv`
`cat had.csv | ./subset.py -bbox 11.8552541 51.4021008 12.0892171 51.5435116 > HAD_halle.csv`
`cat had.csv | ./subset.py -bbox 13.5793237 50.9749370 13.9660626 51.1777202 > HAD_dresden`
`cat had.csv | ./subset.py -bbox 6.6256311 51.3333827 6.8302507 51.5600691 > HAD_duisburg`
