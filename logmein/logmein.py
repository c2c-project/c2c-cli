import argparse
import helpers
import csvparser

parser = argparse.ArgumentParser(description='Logmein/GotoWebinar cli')
parser.add_argument('--csv', dest='filepath')
parser.add_argument('-R','--refresh', dest='refresh', action='store_true', default=False)

args = parser.parse_args()

if args.refresh:
    helpers.post_refresh_token()

if args.filepath:
    registrants = csvparser.parse(args.filepath)
    (info, fields) = helpers.create_registrant_v1(registrants)
    csvparser.dump(info, fields)