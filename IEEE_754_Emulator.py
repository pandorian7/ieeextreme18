import sys
import struct

def hex_to_float(hex_str):
    """Convert a hexadecimal string to a floating-point number."""
    return struct.unpack('!f', bytes.fromhex(hex_str))[0]

def float_to_hex(float_num):
    """Convert a floating-point number to a hexadecimal string."""
    return hex(struct.unpack('<I', struct.pack('<f', float_num))[0])[2:].zfill(8)

def nand_operation(a, b):
    """Perform NAND operation on two integers."""
    a = int(float_to_hex(a), 16)
    b = int(float_to_hex(b), 16)
    ret = ~(a & b) & 0xFFFFFFFF
    return hex_to_float(hex(ret)[2:].zfill(8))

def fused_multiply_add(a, b, c):
    """Perform fused multiply-add operation: (a * b) + c."""
    return a * b + c

def read_input():
    """Read input from standard input."""
    return sys.stdin.read().splitlines()

def process_commands(data):
    """Process the commands and return results."""
    index = 0
    test_cases = int(data[index])  # Number of test cases
    index += 1
    output_results = []
    
    for _ in range(test_cases):
        initial_hex = data[index].strip()
        computations = [hex_to_float(initial_hex)]  # Initialize computations list
        index += 1
        
        lut_count = int(data[index])  # Number of LUTs
        index += 1
        
        look_up_tables = []
        for __ in range(lut_count):
            lut_info = data[index].strip().split()
            lut_values = [hex_to_float(v) for v in lut_info[1:]]  # Convert LUT hex values to floats
            look_up_tables.append(lut_values)
            index += 1
        
        query_count = int(data[index])  # Number of queries
        index += 1
        
        for __ in range(query_count):
            command = data[index].strip().split()
            if command[0] == 'L':
                i, j, b = int(command[1]), int(command[2]), int(command[3])
                mask = (int(initial_hex, 16) >> j) & ((1 << b) - 1)
                computations.append(look_up_tables[i][mask])  # Append result from LUT
            elif command[0] == 'N':
                i, j = int(command[1]), int(command[2])
                result = nand_operation(computations[i], computations[j])
                computations.append(result)  # Append NAND result
            elif command[0] == 'F':
                i, j, k = int(command[1]), int(command[2]), int(command[3])
                result = fused_multiply_add(computations[i], computations[j], computations[k])
                computations.append(result)  # Append FMA result
            elif command[0] == 'C':
                hex_value = command[1]
                computations.append(hex_to_float(hex_value))  # Append converted hex float
            index += 1
        
        output_results.append(float_to_hex(computations[-1]))  # Append final result as hex
    
    return output_results

def main():
    input_data = read_input()  # Read input
    results = process_commands(input_data)  # Process commands and get results
    print("\n".join(results))  # Print results for all test cases

if __name__ == "__main__":
    main()
