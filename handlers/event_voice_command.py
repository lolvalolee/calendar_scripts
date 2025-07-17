def start_event(match):
    event_name = match.group('event_name').lower()
    print(':)')
    print(event_name)

def end_event(match):
    pass