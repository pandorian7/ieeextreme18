import math

bin_str = dict()
vals = dict()

def binary_mantissa_to_fraction(mantissa):
    # Initial value for integer part of binary '1.'
    fraction_value = 1.0
    
    # Convert binary fraction part after '1.'
    for i, bit in enumerate(mantissa, start=1):
        if bit == '1':
            fraction_value += 1 / (2 ** i)
    
    return fraction_value


def fraction_to_binary_mantissa(fraction, precision=23):
    """
    Convert a decimal fraction to a binary mantissa string.
    
    Args:
        fraction (float): The fractional decimal number to convert.
        precision (int): Number of binary places to calculate (default 10).
    
    Returns:
        str: Binary representation of the fraction part as a mantissa.
    """
    binary_mantissa = []
    for _ in range(precision):
        fraction *= 2
        bit = int(fraction)  # Extract the integer part (0 or 1)
        binary_mantissa.append(str(bit))
        fraction -= bit  # Remove the integer part, keeping only the fraction
    
        if fraction == 0:
            break  # Stop if fraction becomes zero
    
    return ''.join(binary_mantissa)


def get_bin(val):
    sign = "0" if val>0 else "1"
    if val <0:
        val *= -1
    expo_val = int(math.log2(val))
    expo = format(expo_val+127, "08b")
    val /= 2**expo_val
    val -= 1
    mantissa = fraction_to_binary_mantissa(val).rjust(23,"0")
    return format(int(sign+expo+mantissa, base=2), "08x")


def get_decimal(val):
    decimal_val = int(val, base=16)
    bin_val = format(decimal_val, '032b')
    bin_str[val] = bin_val
    
    sign = bin_val[0]
    expo = bin_val[1:9]
    mantissa = bin_val[9:]
    # print(sign, expo, mantissa)
# 
    sign_val = 1 if sign=="0" else -1

    ret = sign_val*binary_mantissa_to_fraction(mantissa) * 2**(int(expo, 2)-127)
    vals[val] = ret
    return ret

def hex_to_binary(hex_str):
    """Convert a hexadecimal string to a binary string."""
    # Convert hex to int, then to binary, removing the '0b' prefix
    return bin(int(hex_str, 16))[2:]

def binary_to_hex(bin_str):
    """Convert a binary string to a hexadecimal string."""
    # Convert binary to int, then to hex, removing the '0x' prefix
    return hex(int(bin_str, 2))[2:].upper()  # Return uppercase hex

def nand_hex_strings(hex_str1, hex_str2):
    """Calculate the NAND of two hexadecimal string values of the same length."""
    # Convert hex strings to binary
    bin_str1 = hex_to_binary(hex_str1)
    bin_str2 = hex_to_binary(hex_str2)

    # Perform the NAND operation
    result = []
    for b1, b2 in zip(bin_str1.zfill(len(hex_str1) * 4), bin_str2.zfill(len(hex_str2) * 4)):
        # Convert characters to integers, perform NAND, and append result
        nand_bit = '1' if not (b1 == '1' and b2 == '1') else '0'
        result.append(nand_bit)

    # Convert the result binary string back to hex
    result_bin_str = ''.join(result)

    # Convert the binary result to hexadecimal and return
    return binary_to_hex(result_bin_str)

# Example usage
 # Expected output: Hex representation of the NAND result


def testcase():
    C = [input()] 
    L = int(input())
    get_decimal(C[-1])
    if (L):
        raise Exception('UHH')
    Q = int(input())
    for _ in range(Q):
        comm, *args = input().split()
        if comm == "C":
            C.append(args[0])
            get_decimal(C[-1])
        if comm == "F":
            i, j, k = map(int, args)
            vi = get_decimal(C[i])
            vj = get_decimal(C[j])
            vk = get_decimal(C[k])
            C.append(get_bin(vi*vj+vk))
            get_decimal(C[-1])
        if comm == "N":
            i, j = map(int, args)
            C.append(nand_hex_strings(C[i], C[j]))



    print(C[-1].lower())
    
T = int(input())

for _ in range(T):
    testcase()

# print(nand_hex_strings("BF800000", "40800000"))

# print(get_decimal("40800000"))

