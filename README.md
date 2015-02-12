# Science Fair Fun

## Background

This is a small (literally and figuratively) data gathering project that
I built for my 10 year-old daughter's science fair project.

The hypothesis is:

    If I leave my hamster (Leia) in a dark room overnight she will run farther
    than if I leave her in a lighted room.

That's Leia, as in Princess Leia.  We like Star Wars.

We wired a simple optical emitter / detector pair with a pull-up to an
Arduino's digital input.  A small piece of Lego was epoxied onto the
hamster wheel so that once per revolution the optical beam is broken.
When the beam is intact, the Arduino digital input reads as a 1.  When
the beam is broken, it reads as a 0.  The Arduino's code sits in a
tight loop watching for 1->0 transitions and echoing a `+` character
for each one seen.

The Python-based collector runs on a neighboring Mac Mini.  It counts
revolutions and once a minute spits out a data record into a CSV file.

We're currently collecting data...
