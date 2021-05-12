i = 0
tokens = "22.35"
val = 0
while (i < len(tokens) and (tokens[i].isdigit() or tokens[i] == ".")):
    #print(tokens[i])
    if tokens[i] == ".":
        i += 1
        k = i
        y = 1
        while (k < len(tokens) and tokens[i].isdigit()):
            y = y * 10
            val = val + (float(tokens[k]) * (1/y))
            k += 1
            print(val)
        i = k
    else:  
        val = (val * 10) + int(tokens[i])
        print(val)
        i += 1

print(i)
        


			