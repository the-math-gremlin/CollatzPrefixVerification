import csv
import math

def collatz_step(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (3 * n + 1) // 2  # Includes immediate halving after odd step

def height(n):
    if n == 0:
        return 0
    return math.floor(math.log(abs(n), 3)) + math.log2((n & -n).bit_length())

def verify_prefix(prefix_decimal, max_steps=500):
    n0 = 3**10 * prefix_decimal
    initial_height = height(n0)
    n = n0
    for step in range(1, max_steps + 1):
        n = collatz_step(n)
        current_height = height(n)
        if current_height < initial_height:
            return step, initial_height, current_height, "Height Drop"
        if n in {1, 2, 4}:
            return step, initial_height, current_height, "Cycle Entry"
    return max_steps, initial_height, current_height, "No Drop Found"

def main():
    with open('prefix_summary.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Prefix (Base-3)", "Decimal r", "Minimal n0", "Steps to Contract", "Initial H(n0)", "Final H", "Contraction Type"])
        
        for prefix_decimal in range(0, 3**10):
            prefix_base3 = format(prefix_decimal, '010b').replace('0', '0').replace('1', '1').replace('2', '2')  # Just pad for now
            steps, h_initial, h_final, contraction_type = verify_prefix(prefix_decimal)
            minimal_n0 = 3**10 * prefix_decimal
            writer.writerow([prefix_base3, prefix_decimal, minimal_n0, steps, h_initial, h_final, contraction_type])

if __name__ == "__main__":
    main()
