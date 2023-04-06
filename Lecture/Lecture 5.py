
# cnts = fobj.read()
# print(f"First 20 characters in cnts: '{cnts[:20]}'")
# # Start with an empty string
# cnts_copy = ''
# # Iterate over each line of fobj for line in fobj:
#     # Add this line to the string `cnts_copy`
# cnts_copy += line # Print the result
# print(f"First 20 characters in cnts_copy: '{cnts_copy[:20]}'")
# # Close the file
# fobj.close()



# cnts = fobj.read()
# print(f"First 20 characters in cnts: '{cnts[:20]}'")
# # Start with an empty string
# cnts_copy = ''
# # Iterate over each line of fobj for line in fobj:
#     # Add this line to the string `cnts_copy`
# cnts_copy += line # Print the result
# print(f"First 20 characters in cnts_copy: '{cnts_copy[:20]}'")
# # Close the file
# fobj.close()



# cnts = ''
# print(f"First 20 characters in cnts: '{cnts[:20]}'")
# # Start with an empty string
# cnts_copy = ''
# # Iterate over each line of fobj for line in fobj:
#     # Add this line to the string `cnts_copy`
# cnts_copy += line # Print the result
# print(f"First 20 characters in cnts_copy: '{cnts_copy[:20]}'")
# # Close the file
# fobj.close()




# with open(SRCFILE, mode='r') as fobj:
# cnts = fobj.read()
# # Check if the object is closed inside the manager
# print(f'Is the fobj closed inside the manager? {fobj.closed}')


# def print_lines(pth):
# """ Function to print the lines of a file Parameters
# ----------
# pth : str
#         Location of the file
#     Notes
#     -----
#     Each line in the file will be printed as
#         line number: 'string with the line text'
#     """
# with open(pth) as fobj:
# for i, line in enumerate(fobj):
#             print(f"line {i}: {line}")
# with open(DSTFILE, mode='w') as fobj: fobj.write('This is a line')


# with open(DSTFILE, mode='w') as fobj:
# fobj.write('This is a line\n')
# fobj.write('This is a another line') print_lines(DSTFILE)

# def print_lines_rstrip(pth): with open(pth) as fobj:
# for i, line in enumerate(fobj):
# print(f"line {i}: '{line.rstrip()}'")
# with open(DSTFILE, mode='w') as fobj: fobj.write('This is a line\n') fobj.write('This is a another line')
# print_lines_rstrip(DSTFILE)

# def freqword(filepath):
# with open(filepath) as file:
#         # Count word frequency
# counts = dict() for line in file:
# words = line.split() for word in words:
# counts[word] = counts.get(word,0) + 1
#         # Find the most frequent word
# maxcount = None
# maxword = None
# for word,count in counts.items():
# if maxcount is None or count > maxcount: maxword = word
# maxcount = count # Return the result
# return(f"The most frequent word is: {maxword}, and the number of times appeared is: {maxcount}")
# ### Call the function
# freqword('iso.txt')
#
#
# import pandas as pd
# dates = [
#   '2020-01-02', '2020-01-03', '2020-01-06', '2020-01-07', '2020-01-08',
#   '2020-01-09', '2020-01-10', '2020-01-13', '2020-01-14', '2020-01-15',
#   ]
# prices = [
# 7.1600, 7.1900, 7.0000, 7.1000, 6.8600, 6.9500, 7.0000, 7.0200, 7.1100, 7.0400, ]
# ser = pd.Series(data=prices, index=dates) print(ser)