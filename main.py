import argparse
from logParser import parser
from detector import detector
from reporter import report

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-l", "--log", help="The path of the log file you want to read", required=True)
    arg_parser.add_argument("-t", "--threshold", help="The amount of failed login attempts within the window by default 5", default=5, type=int)
    arg_parser.add_argument("-w", "--window", help="The time of which the thershold is hit within (in seconds) by default 60s" ,default=60, type=int)
    arg_parser.add_argument("-e", "--export", help="Optional export of the report in json format.")
    args = arg_parser.parse_args()

    logPath = args.log
    threshold = args.threshold
    window = args.window
    exportPath = args.export

    failedAttempts = parser(logPath)
    flagged = detector(failedAttempts, threshold, window)

    report(flagged, failedAttempts, exportPath)

if __name__ == "__main__":
    main()