#!/usr/bin/python3
def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes to expect for a valid UTF-8 character
    num_bytes = 0

    # Loop through each byte in the data set
    for byte in data:
        # Mask the byte to get the last 8 bits
        byte &= 0xFF

        """ If no bytes are expected, determine how many bytes
        this character requires"""
        if num_bytes == 0:
            if (byte >> 7) == 0b0:  # 1-byte character (ASCII)
                continue
            elif (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            else:  # Invalid byte
                return False
        else:
            # Check for continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If there are still bytes expected, return False
    return num_bytes == 0
