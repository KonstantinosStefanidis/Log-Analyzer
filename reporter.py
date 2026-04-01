import json

def report(flagged, failedAttempts, exportPath=None):
    for ip in flagged:
        print(f"[ALERT] {ip} - {len(failedAttempts[ip])} attempts in window")
    if len(flagged) == 0:
        print("[OK] No IPs Flagged.")
    if exportPath:
        data = {}
        for ip in flagged:
            data[ip] = [timestamp.strftime("%b %d %H:%M:%S") for timestamp in failedAttempts[ip]]
        with open(exportPath, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"[+] Report exported to {exportPath}")
