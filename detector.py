# delta is an object here, python returns delta as "seconds" and
# .total_seconds gets os how you return it
def detector(failedAttempts, threshold=5, window=60):
    flagged = set()
    for ip, timestamps in failedAttempts.items():
        for i in range(len(timestamps)):
            for j in range(i + 1, len(timestamps)):
                delta = timestamps[j] - timestamps[i]
                if delta.total_seconds() > window:
                    break
                if (j - i + 1) >= threshold:
                    flagged.add(ip)
                    break
    return flagged