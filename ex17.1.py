class Time:
    def _init_(self, hour=0, minute=0, second=0):
        self.seconds = hour * 3600 + minute * 60 + second

def print_time(time):
    hours = time.seconds // 3600
    minutes = (time.seconds % 3600) // 60
    seconds = time.seconds % 60
    print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')

def time_to_int(time):
    return time.seconds

def int_to_time(seconds):
    return Time(0, 0, seconds)

def add_time(t1, t2):
    total = t1.seconds + t2.seconds
    return int_to_time(total)

def is_after(t1, t2):
    return t1.seconds > t2.seconds

def increment(time, seconds):
    total = time.seconds + seconds
    return int_to_time(total)

# Código de teste (não deve ser alterado)
if __name__ == '_main_':
    start = Time(9, 45, 0)
    duration = Time(1, 35, 0)
    print_time(start)
    end = add_time(start, duration)
    print_time(end)
    print(is_after(end, start))