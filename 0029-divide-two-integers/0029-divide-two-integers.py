class Solution:
    def divide(self, dividend, divisor):
        # Handle edge case for overflow (when dividend is -2^31 and divisor is -1)
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine the sign of the result
        sign = -1 if (dividend < 0) != (divisor < 0) else 1
        
        # Work with positive values for easier manipulation
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Initialize the result (quotient)
        quotient = 0
        
        # Perform the division using subtraction and bit shifts
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):  # Double the divisor
                temp <<= 1
                multiple <<= 1
            # Subtract the largest possible chunk
            dividend -= temp
            quotient += multiple
        
        # Apply the sign
        quotient *= sign
        
        # Ensure the result is within the 32-bit integer range
        return max(min(quotient, 2**31 - 1), -2**31)