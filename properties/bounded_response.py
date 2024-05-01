import random

from collections import namedtuple

TimedData = namedtuple('TimedData', ["time", 'data'])


class bounded_response_globally:

    @staticmethod
    def generate_trace(lower_bound, upper_bound):

        Data = namedtuple('Data', ['p', 's'])

        time = 0

        while True:

            yield [TimedData(time=time, data=Data(p=True, s=False))]
            time += 1

            # Draws a random number between lower and upper bounds
            k = random.randint(lower_bound+1, upper_bound)

            for j in range(k-1):
                yield [TimedData(time=time, data=Data(p=False, s=False))]
                time += 1

            yield [TimedData(time=time, data=Data(p=False, s=True))]
            time += 1



class bounded_response_between_q_and_r:

    @staticmethod
    def generate_trace(lower_bound, upper_bound, min_recur=True, max_recur=7):

        Data = namedtuple('Data', ['q', 'p', 's', 'r'])

        time = 0

        while True:

            yield [TimedData(time=time, data=Data(q=True,
                                                    p=False, s=False, r=False))]
            time += 1

            yield [TimedData(time=time,
                                data=Data(q=False, p=False, s=False, r=False))]
            time += 1

            for i in range(0, random.randint(min_recur, max_recur)):

                yield [TimedData(time=time,
                                    data=Data(q=False, p=True, s=False, r=False))]
                time += 1

                # Draws a random number between lower and upper bounds
                k = random.randint(lower_bound+1, upper_bound)

                for j in range(k-1):
                    yield [TimedData(time=time,
                                        data=Data(q=False, p=False, s=False, r=False))]
                    time += 1

                yield [TimedData(time=time,
                                    data=Data(q=False, p=False, s=True, r=False))]
                time += 1

                yield [TimedData(time=time,
                                    data=Data(q=False, p=False, s=False, r=False))]
                time += 1

            yield [TimedData(time=time,
                                data=Data(q=False, p=False, s=False, r=True))]
            time += 1

        