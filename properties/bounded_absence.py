import random
from collections import namedtuple

TimedData = namedtuple('TimedData', ["time", 'data'])


class bounded_absence_after_q:

    @staticmethod
    def generate_trace(upper_bound):

        Data = namedtuple('Data', ['q', 'p'])

        time = 0

        while True:

            yield [TimedData(time=time, data=Data(q=True, p=False))]
            time += 1

            for j in range(upper_bound):
                yield [TimedData(time=time, data=Data(q=False, p=False))]
                time += 1

            for j in range(upper_bound):
                yield [TimedData(time=time, data=Data(q=False,
                                                        p=bool(random.randint(0, 1))))]
                time += 1


class bounded_absence_before_r:

    @staticmethod
    def generate_trace(upper_bound):

        Data = namedtuple('Data', ['p', 'r'])

        time = 0

        while True:

            for j in range(upper_bound):
                yield [TimedData(time=time,
                                    data=Data(p=bool(random.randint(0, 1)), r=False))]
                time += 1

            for j in range(upper_bound):
                yield [TimedData(time=time, data=Data(p=False, r=False))]
                time += 1

            yield [TimedData(time=time, data=Data(p=False, r=True))]
            time += 1


class bounded_absence_between_q_and_r:

    @staticmethod
    def generate_trace(lower_bound, upper_bound):

        Data = namedtuple('Data', ['q', 'p', 'r'])

        time = 0

        while True:

            yield [TimedData(time=time, data=Data(q=True, p=False, r=False))]
            time += 1

            # Draws a random number between 0 and the specified time parameter
            k = random.randint(lower_bound, upper_bound-1)

            for j in range(k):
                yield [TimedData(time=time,
                                    data=Data(q=False, p=False, r=False))]
                time += 1

            yield [TimedData(time=time, data=Data(q=False, p=False, r=True))]
            time += 1

            yield [TimedData(time=time, data=Data(q=False,
                                                    p=bool(random.randint(0, 1)), r=False))]
            time += 1
