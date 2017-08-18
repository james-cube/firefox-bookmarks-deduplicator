import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()    
    parser.add_argument('--file', dest='file', help='File to process', required=True)
    parser.add_argument('--output', dest='output', help='Output file', required=True)
    return parser.parse_args()
