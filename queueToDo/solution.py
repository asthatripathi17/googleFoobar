def xor_seq(start, end):
    repeated_xor = []
    if start % 2 == 0:
        repeated_xor = [end, 1, end + 1, 0]
    else:
        repeated_xor = [start, start ^ end, start - 1, (start - 1) ^ end]
    ans = repeated_xor[(end - start) % 4]
    return ans

def solution(start, length):
    checksum = 0
    temp = length
    current_start = start

    while temp > 0:
        checksum ^= xor_seq(current_start, current_start + temp - 1)
        current_start = current_start + length
        temp -= 1

    return checksum
