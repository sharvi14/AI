import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if curDepth == targetDepth or nodeIndex >= len(scores):
        return scores[nodeIndex] if nodeIndex < len(scores) else 0  # Return 0 for non-existing nodes
    
    if maxTurn:
        # Maximizing player's turn
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        # Minimizing player's turn
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))

# take input from the user
def main():
    # Taking input from the user
    scores = list(map(int, input("Enter the leaf node scores separated by space: ").split()))
    
    treeDepth = math.ceil(math.log2(len(scores)))
    
    print("The optimal value is:", minimax(0, 0, True, scores, treeDepth))

# Run the program
if __name__ == "__main__":
    main()