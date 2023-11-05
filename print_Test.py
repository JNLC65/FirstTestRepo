import timeit

# f-string formatting
f_string_time = timeit.timeit("f'number: {12345}'", number=1000000)

# str.format() method
format_time = timeit.timeit("'number: {}'.format(12345)", number=1000000)

print(f"f-string time: {f_string_time} microseconds")
print(f"str.format() time: {format_time} microseconds")
print(f"Difference: {format_time - f_string_time} microseconds")