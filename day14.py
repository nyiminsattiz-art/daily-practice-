def was_package_received_yesterday(tz_from, tz_to, start, duration):
    received_hour = start + duration + (tz_to - tz_from)
    if received_hour < 0:
        return True
    else:
        return False
        
