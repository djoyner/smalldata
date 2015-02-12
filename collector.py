#!/usr/bin/env python

from __future__ import print_function
from datetime import datetime, timedelta
from select import select
import sys, termios, traceback

if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "<dev>", file=sys.stderr)
    sys.exit(1)

# Open the modem device
with open(sys.argv[1], 'rU') as f:

    print("Opened", sys.argv[1], file=sys.stderr)

    # Set the modem baud rate
    tc = termios.tcgetattr(f.fileno())
    tc[4] = tc[5] = 38400
    termios.tcsetattr(f.fileno(), termios.TCSANOW, tc)

    # Outer loop runs until EOF is reached or a fatal error occurs
    done = False
    while not done:

        # Inner loop runs until the top of the next minute
        accum = 0
        now = datetime.now()
        deadline = now + timedelta(0, 60 - now.second - (now.microsecond / 1e6))
        while not done:

            # Wait for input from the modem
            timeout = (deadline - datetime.now()).total_seconds()
            if timeout < 0:
                break  # deadline already passed
            try:
                fds = select([f], [], [], timeout)
                if not fds[0]:
                    break  # deadline reached w/o input
                line = f.readline()
                if line:
                    line = line.strip()
                    print(line, file=sys.stderr)
                    if line == '+':
                        accum += 1  # count a revolution
                else:
                    done = True
            except KeyboardInterrupt:
                done = True
            except:
                traceback.print_exc(file=sys.stderr)
                sys.exit(1)

        # Print the number of revolutions accumulated in the last minute
        print("%02d%02d" % (now.hour, now.minute), accum, sep=',')
        sys.stdout.flush()
