import argparse

def get_parser():

    parser = argparse.ArgumentParser(
            description='timescales is a benchmark generator for metric temporal logic properties',
            formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('property',
                            help='''Supported properties are below:
        absence_after_q                   UBOUND
        absence_before_r                  UBOUND
        absence_between_q_and_r    LBOUND UBOUND

        always_after_q                    UBOUND
        always_before_r                   UBOUND
        always_between_q_and_r     LBOUND UBOUND

        recurrence_globally               UBOUND
        recurrence_between_q_and_r        UBOUND MIN_RECUR MAX_RECUR

        response_globally          LBOUND UBOUND
        response_between_q_and_r   LBOUND UBOUND MIN_RECUR MAX_RECUR''')

    parser.add_argument('--interval',
                        help='''select the message publishing interval (in seconds)''',
                        default=0.1,
                        type=float)

    parser.add_argument('-d', '--duration',
                        help='''define the approximate duration for the trace (default:1000)''',
                        default=1000,
                        type=int,
                        metavar='N')
    parser.add_argument('-l', '--lbound',
                        help='''define the lower bound for the property if available for the property (default:0)''',
                        default=0,
                        type=int,
                        metavar='N')
    parser.add_argument('-u', '--ubound',
                        help='''define the upper bound for the property if available for the property (default:100)''',
                        default=100,
                        type=int,
                        metavar='N')
    parser.add_argument('-p', '--persistent',
                        help='''enable persistent (delta-encoded) trace generation''',
                        action="store_true",
                        default=False)
    parser.add_argument('--min-recur',
                        help='''define the minimum number of recurrence in the trace if available for the property (default:1)''',
                        default=1,
                        type=int,
                        metavar='N')
    parser.add_argument('--max-recur',
                        help='''define the maximum number of recurrence in the trace if available for the property (default:7)''',
                        default=7,
                        type=int,
                        metavar='N')
    parser.add_argument('--name',
                        help='''define the name of specification (default: spec)''',
                        default="spec",
                        metavar='STRING')
    parser.add_argument('--condense',
                        help='''define the maximum amount of condensation in the generated trace (default: 0)''',
                        default=0,
                        type=int,
                        metavar='N')
    parser.add_argument('--failing-end',
                        help='''disable appending a sequence to the trace to make the spec fail (default: false)''',
                        action="store_true",
                        default=False)
    parser.add_argument('--future',
                        help='''generate a future MTL formula (default: past)''',
                        action="store_true",
                        default=False)
    parser.add_argument('--output-dir',
                        help='''use existing DIR as the directory to write output files in (default: current)''',
                        default='',
                        metavar='DIR')
    parser.add_argument('--format',
                        help='''select the output format in {csv, json, protobuf, flatbuf} (default: csv)''',
                        default='string',
                        metavar='FORMAT')
    
    return parser

