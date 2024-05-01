from properties.bounded_absence import *
from properties.bounded_recurrence import *
from properties.bounded_universality import *
from properties.bounded_response import *

class Generator:

    
    functions = {"absence_after_q": [bounded_absence_after_q.generate_trace, [1]],
                 "absence_before_r": [bounded_absence_before_r.generate_trace, [1]],
                 "absence_between_q_and_r": [bounded_absence_between_q_and_r.generate_trace, [0, 1]],
                 "always_after_q": [bounded_universality_after_q.generate_trace, [1]],
                 "always_before_r": [bounded_universality_before_r.generate_trace, 1],
                 "always_between_q_and_r": [bounded_universality_between_q_and_r.generate_trace, [0, 1]],
                 "recurrence_globally": [bounded_recurrence_globally.generate_trace, [1]],
                 "recurrence_between_q_and_r": [bounded_recurrence_between_q_and_r.generate_trace, [1, 2, 3]],
                 "response_globally": [bounded_response_globally.generate_trace, [0, 1]],
                 "response_between_q_and_r": [bounded_response_between_q_and_r.generate_trace, [0, 1, 2, 3]]}

    @staticmethod
    def generate(property, lower_bound, upper_bound, min_recur, max_recur):
        params = [lower_bound, upper_bound, min_recur, max_recur]
        try:
            generator, args = Generator.functions.get(property)
            try:
                argv = [params[i] for i in args]
                return generator(*argv)
            except:
                raise ValueError("Invalid arguments. Please see -h or --help for supported arguments.")
            
        except:
            raise KeyError("Invalid property. Please see -h or --help for supported properties.")

