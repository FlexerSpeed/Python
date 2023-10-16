import sys

print(sys.argv)

if len(sys.argv) < 3:
    raise IOError('You must provide usename & password')

filename, username, password
