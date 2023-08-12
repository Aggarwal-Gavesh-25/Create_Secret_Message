# A python program to translate a message into secret code language.

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

st = input("Enter message: ")                                 # Inputting message from user

words = st.split(" ")                                       # Splitting every word in the string

coding = input("1 for Coding or 0 for Decoding\n")            #Asking whether code is to be coded or decoded

coding = True if (coding=="1") else False                   # Using short hand if else
print(coding)

if(coding): # For coding
  nwords = []                                               # Empty string to append new words
  for word in words:                                        # For every splitted word in the string
    if(len(word)>=3):
      r1 = "dsf"                                            # 3 random characters for start
      r2 = "jkr"                                            # 3 random characters for end
      stnew = r1+ word[1:] + word[0] + r2                   # Removing first character and appending it at the end & adding random chars at start and end
      nwords.append(stnew)                                  # Joining coded words to form secret message string
    else:
      nwords.append(word[::-1])                             # Reversing the string if else than 3 characters in the word
  
  print(" ".join(nwords))

else:   # For decoding
  nwords = []                                               # Empty string to append decoded words
  for word in words:
    if(len(word)>=3): 
      stnew = word[3:-3]                                    # Removed first 3 and last 3 characters
      stnew = stnew[-1] + stnew[:-1]                        # Placing last character at first                   
      nwords.append(stnew)                                  # Joining decoded words to form original message
    else:
      nwords.append(word[::-1])                             # Reversing the string if else than 3 characters in the word
  
  print(" ".join(nwords))
  