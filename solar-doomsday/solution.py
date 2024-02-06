def solution(area):
    result = []
    
    while area > 0:
        largest_square = int(area ** 0.5) ** 2
        result.append(largest_square)
        area -= largest_square
    
    result result
