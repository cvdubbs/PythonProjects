S = 'ABCDEFGHI'
print(S[2:7])	# CDEFG

S = 'ABCDEFGHI'
print(S[-7:-2])	# CDEFG

S = 'ABCDEFGHI'
print(S[2:-5])	# CD

# Return every 2nd item between position 2 to 7
S = 'ABCDEFGHI'
print(S[2:7:2])	# CEG

# Returns every 2nd item between position 6 to 1 in reverse order
S = 'ABCDEFGHI'
print(S[6:1:-2])    # GEC

# Slice first three characters from the string
S = 'ABCDEFGHI'
print(S[:3])    # ABC

# Slice last three characters from the string
S = 'ABCDEFGHI'
print(S[6:])    # GHI

S = 'ABCDEFGHI'
print(S[::-1])    # IHGFEDCBA