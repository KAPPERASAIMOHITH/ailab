def hanoi(n, source, target, auxiliary):
    if n > 0:
        # Move n-1 discs from source to auxiliary peg
        hanoi(n - 1, source, auxiliary, target)
        
        # Move the nth disc from source to target peg
        print(f"Move disc {n} from {source} to {target}")
        
        # Move the n-1 discs from auxiliary peg to target peg
        hanoi(n - 1, auxiliary, target, source)

# Example usage
if __name__ == "__main__":
    num_discs = 3
    hanoi(num_discs, 'A', 'C', 'B')
