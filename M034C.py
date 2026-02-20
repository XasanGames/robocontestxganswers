import math
import sys

for line in sys.stdin:
    if not line.strip():
        break
    
    # Har bir qatordagi X va Y ni ajratib olamiz
    x, y = map(int, line.split())
    
    # Masala formulasi
    d = math.gcd(x, y)
    result = 2 * (x + y) // d
    
    print(result)