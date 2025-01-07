#!/usr/local/bin/python

import csv
import sys
import os
import argparse
import mercantile

def process_csv(reader, bbox):
    #Process CSV data row by row within the given bounding box.
    xmin, ymin, xmax, ymax = bbox if bbox else (None, None, None, None)


    for row in reader:
        if(row[2] == "GEOGRAPHY"):
            print("AGG_DAY_PERIOD,ACTIVITY_INDEX_TOTAL,GEOGRAPHY")
        else:
            try:
                tile = mercantile.quadkey_to_tile(row[2])
                tile = mercantile.bounds(tile)

                contained = tile.west >= xmin and tile.east <= xmax
                contained = tile.south >= ymin and tile.north <= ymax and contained

                #use mercantile for that
                if(contained):
                    print(row[0] + "," + row[1] + "," + row[2])
            except ValueError:
                # Handle or skip rows with invalid data
                continue

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="filter HAD CSV within specified bounding box. \n This just assumes the following file structure: col 1: date, col 2: HAD index, col3: quadkey index")
    parser.add_argument('-bbox', '--bounding_box', nargs=4, type=float, metavar=('XMIN', 'YMIN', 'XMAX', 'YMAX'),
                        help='Specify the bounding box with xmin, ymin, xmax, ymax.')
    parser.add_argument('file', nargs='?', help='Path to the CSV file (optional if piping).')

    args = parser.parse_args()
    bbox = args.bounding_box
    file_path = args.file

    if not bbox:
        print("please enter a bounding box using the -bbox variable. like so -bbox 10 10 100 100")
    elif file_path:
        # Read from the file
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            process_csv(reader, bbox)
    else:
        # Read from standard input, process line-by-line
        reader = csv.reader(sys.stdin)
        process_csv(reader, bbox)
