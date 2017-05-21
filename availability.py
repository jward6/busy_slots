import datetime

tests = [[
        {'start': '2017-06-01T09:00',
            'stop': '2017-06-01T17:00'},
        {'start': '2017-06-02T10:00',
            'stop': '2017-06-02T12:00'},
        {'start': '2017-06-02T15:00',
            'stop': '2017-06-02T18:00'},
        {'start': '2017-06-03T08:00',
            'stop': '2017-06-03T14:00'},
        {'start': '2017-06-04T11:00',
            'stop': '2017-06-04T19:00'},
        {'start': '2017-06-05T09:00',
            'stop': '2017-06-05T14:00'},
        {'start': '2017-06-05T17:00',
            'stop': '2017-06-05T20:00'},
        {'start': '2017-06-07T12:00',
            'stop': '2017-06-07T16:00'},
        ],
        [
        {'start': '2017-06-01T09:30',
            'stop': '2017-06-01T20:00'},
        {'start': '2017-06-02T10:15',
            'stop': '2017-06-02T13:00'},
        {'start': '2017-06-02T15:00',
            'stop': '2017-06-02T18:45'},
        {'start': '2017-06-03T08:00',
            'stop': '2017-06-03T14:30'},
        {'start': '2017-06-04T11:30',
            'stop': '2017-06-04T19:15'},
        {'start': '2017-06-05T09:00',
            'stop': '2017-06-05T14:00'},
        {'start': '2017-06-06T07:30',
            'stop': '2017-06-06T14:30'},
        {'start': '2017-06-07T12:00',
            'stop': '2017-06-07T16:00'},
        ],
        ]

solutions = [105, 118]

def parse_dtstr(i):
    return datetime.datetime.strptime(i, '%Y-%m-%dT%H:%M')

def get_hours(d):
    return d.seconds / 3600

def floor_dt(dt):
    return datetime.datetime(dt.year, dt.month, dt.day)

def calculate_busy_slots(availability):
    ''' Add Code Here '''

    result = 0

    prev = None
    for a in availability:
        start = parse_dtstr(a['start'])
        stop = parse_dtstr(a['stop'])

        if prev is None:
            result += get_hours(start - floor_dt(start))
        else:
            result += get_hours(start - prev)

        prev = stop

    next_day = prev + datetime.timedelta(days = 1)
    result += get_hours(floor_dt(next_day) - prev)
       
    return result

#print(calculate_busy_slots(tests[1]))

results = []
for i, test in enumerate(tests):
    r = calculate_busy_slots(test)
    print('{} >> {}'.format(r, 'PASS' if r == solutions[i] else 'FAIL'))
    results.append(r)

print('{}'.format('PASS' if [results[i] == solutions[i] for i in range(len(results))].count(False) == 0 else 'FAIL'))

