#!/usr/local/bin/python

import csv
import sys
import os
import argparse
import mercantile

def process_csv(reader, bbox):
    #Process CSV data row by row within the given bounding box.
    xmin, ymin, xmax, ymax = bbox if bbox else (None, None, None, None)

    # there is probably a quicker way to do this by considering containing quads
    tiles = mercantile.tiles(xmin, ymin, xmax, ymax, 18)
    quadkeys = [mercantile.quadkey(tile) for tile in tiles]

    print("AGG_DAY_PERIOD,ACTIVITY_INDEX_TOTAL,GEOGRAPHY")
    for row in reader:
        try:
            #filter only tiles within bounding box
            #use mercantile for that
            if(row[2] in quadkeys):
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
