from collections import defaultdict
import re
from datetime import datetime

def parser(filepath):
    failedAtempts = defaultdict(list)
    pattern = r"(\w{3}\s+\d+\s+\d+:\d+:\d+).*Failed password.*from\s+(\d+\.\d+\.\d+\.\d+)"
    

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip() #This strips \n out of the line
            if "Failed password" in line:
                match = re.search(pattern, line)
                if match:
                    timestampStr = match.group(1)
                    ip = match.group(2)
                    dateParsed = datetime.strptime(timestampStr, "%b %d %H:%M:%S")
                    failedAtempts[ip].append(dateParsed)

    return failedAtempts
                    