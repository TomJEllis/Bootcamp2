def initialise_call_count():
    global  global_call_count
    global_call_count = 0

def get_call_count():
    return global_call_count

def increment_call_count():
    global global_call_count
    global_call_count += 1