def gen_seconds(limit):
    current = 0

    while current <= limit:
        yield current

        current += 1

def gen_ticks(limit, tick_rate):
    current = 0

    while current <= limit:
        yield current

        current = current + tick_rate