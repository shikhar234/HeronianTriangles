from math import isqrt

MAX_LENGTH = 120

results = []

for a in range(1, MAX_LENGTH + 1):
    for b in range(a, MAX_LENGTH + 1):
        # c must satisfy b <= c < a + b  (triangle inequality)
        cmax = min(MAX_LENGTH, a + b - 1)
        for c in range(b, cmax + 1):
            s1 = a + b + c
            s2 = -a + b + c
            s3 = a - b + c
            s4 = a + b - c
            T = s1 * s2 * s3 * s4

            if T <= 0:
                continue

            sqrtT = isqrt(T)
            if sqrtT * sqrtT != T:
                continue

            if sqrtT % 4 != 0:
                continue

            area = sqrtT // 4
            results.append(((a, b, c), area))

results.sort(key=lambda kv: (kv[1], kv[0][0], kv[0][1], kv[0][2]))

for (a, b, c), area in results:
    print((a, b, c), ":", area)

print("COMPLETED")
