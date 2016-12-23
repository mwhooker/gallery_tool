"""
gallery.py helps you calculate where to place your hanger

All units in inches
"""

from fractions import Fraction

# we hang frames at 57" on center
CENTER = Fraction(57)

def parse_input(s):
    """
    >>> parse_input("5")
    Fraction(5, 1)
    >>> parse_input("5 7/8")
    Fraction(47, 8)

    """
    parts = s.split(' ')
    if len(parts) == 1:
        return Fraction(parts[0])
    elif len(parts) == 2:
        return Fraction(parts[0]) + Fraction(parts[1])
    else:
        raise ValueError("Can't parse %s" % s)

def repr_fraction(f):
    """
    >>> x = "5 7/8"
    >>> repr_fraction(parse_input(x)) == x
    True

    """
    whole = int(f)
    part = f - whole
    return "%s %s/%s" % (whole, part.numerator, part.denominator)

def main():
    height = parse_input(raw_input("Frame height:\n\t"))
    hang_pt = parse_input(raw_input("Distance from top to mount point:\n\t"))
    print "Install hook at %s" % repr_fraction(CENTER + (height / 2) - hang_pt)

if __name__ == '__main__':
    main()
