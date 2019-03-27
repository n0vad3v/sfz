from sfz import *

# Example ID number from 95nw
example_number = "432503197505028819"

# Import the Sfz number
s = Sfz(example_number)

# Test for Location
loc = s.loc()
assert "湖南" in loc

# Test for Gender
gender = s.gender()
assert "男" in gender
