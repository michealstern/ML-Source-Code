# st = input("Enter message :")
# coding = True
# if (coding):
#     if(len(st)>=3):
#         r1 = "dsf"
#         r2 = "jkr"
#         st = r1 + st[1:] + st[0] + r2
#         print(st)
# else:
#     pass

st = input("Enter message : ")
words = st.split(" ")
coding = input("1 for coding 0 for decoding : ")
coding = True if (coding=="1") else False
if (coding):  #CODING
    nwords = []  # store strings.
    for word in words:
     if(len(word)>=3):  # if the word contain less than 3 characters.(hello world)
        r1 = "dsf"
        r2 = "jkr"
        stnew = r1 + word[1:] + word[0] + r2  # remove the first letter and append it at the end.(elloh orldw)
        nwords.append(stnew)  # Now append the 3 random characters at the starting and the end. (dsfellohjkr dsforldwjkr)
     else:  # simple revers the string.(i am st)
         nwords.append(word[::-1]) # (i ma ts)
    print(" ".join(nwords))
    
else:    # DECODING: 
    nwords = []  # Stor strings.
    for word in words:
     if(len(word)>=3):  # if the word contain less than 3 characters revers it.(dsfellojkr dsforldwjkr)
        stnew = word[3:-3]  #  Remove 3 random character from start and end.(elloh orldw)
        stnew = stnew[-1] + stnew[:-1] # Remove the last latter.(ello orld)
        nwords.append(stnew)  # append it to the beginning. (hello world)
     else:
         nwords.append(word[::-1])
    print(" ".join(nwords))