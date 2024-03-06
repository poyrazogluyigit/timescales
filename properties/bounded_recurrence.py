import random
from collections import namedtuple

TimedData = namedtuple('TimedData', ["time", 'data'])


class bounded_recurrence_globally:

    @staticmethod
    def generate_trace(upper_bound, duration=1000, failing_end=True):

        Data = namedtuple('Data', ['p'])

        time = 0

        yield [TimedData(time=time, data=Data(p=True))]
        time += 1

        while time < duration:

            # Draws a random number between lower and upper bounds
            k = random.randint(1, upper_bound)

            for j in range(k-1):
                yield [TimedData(time=time, data=Data(p=False))]
                time += 1

            yield [TimedData(time=time, data=Data(p=True))]
            time += 1

        if failing_end:
            for j in range(upper_bound+1):
                yield [TimedData(time=time, data=Data(p=False))]
                time += 1

            # yield [TimedData(time=time, data=Data(p=True))]
            # time += 1


class bounded_recurrence_between_q_and_r:

    @staticmethod
    def generate_trace(upper_bound, duration=1000, min_recur=True, max_recur=7, failing_end=True):

        Data = namedtuple('Data', ['q', 'p', 'r'])

        time = 0

        while time < duration:

            yield [TimedData(time=time, data=Data(q=True, p=False, r=False))]
            time += 1

            for i in range(0, random.randint(min_recur, max_recur)):

                # Draws a random number between 0 and the specified time parameter
                k = random.randint(1, upper_bound)

                for j in range(k-1):
                    yield [TimedData(time=time,
                                       data=Data(q=False, p=False, r=False))]
                    time += 1

                yield [TimedData(time=time,
                                   data=Data(q=False, p=True, r=False))]
                time += 1

            for j in range(k-1):
                yield [TimedData(time=time,
                                   data=Data(q=False, p=False, r=False))]
                time += 1

            yield [TimedData(time=time, data=Data(q=False, p=False, r=True))]
            time += 1

            for j in range(k-1):
                yield [TimedData(time=time,
                                   data=Data(q=False, p=False, r=False))]
                time += 1

        if failing_end:
            yield [TimedData(time=time, data=Data(q=True, p=False, r=False))]
            time += 1
            for j in range(upper_bound+1):
                yield [TimedData(time=time,
                                   data=Data(q=False, p=False, r=False))]
                time += 1
            yield [TimedData(time=time, data=Data(q=False, p=False, r=True))]
            time += 1
