# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start: end : step]
#            always starts at 0

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[-1])
print(credit_number[0:9:2])

# to get the last 4 digits of the credit_number 
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# to reverse the string 
credit_number = credit_number[::-1]
print(credit_number)