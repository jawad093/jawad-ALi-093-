import math

def simple_minimax(depth, index, is_max_turn, scores, max_depth):
    
    if depth == max_depth:
        return scores[index]

  
    if is_max_turn:
        return max(
            simple_minimax(depth + 1, index * 2, False, scores, max_depth),
            simple_minimax(depth + 1, index * 2 + 1, False, scores, max_depth)
        )
    else:
        
        return min(
            simple_minimax(depth + 1, index * 2, True, scores, max_depth),
            simple_minimax(depth + 1, index * 2 + 1, True, scores, max_depth)
        )

scores = [3, 5, 6, 9, 1, 2, 0, -1]


max_depth = math.log2(len(scores))  


result = simple_minimax(0, 0, True, scores, int(max_depth))

print("The final score is:", result)
