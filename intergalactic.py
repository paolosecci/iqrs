def roman_to_int(r_str):
    if not r_str:
        return 0
    rom_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    rom_len = len(r_str)
    sum_out = rom_dic[r_str[-1]]
    for i in range(rom_len-1, 0, -1):
        here = rom_dic[r_str[i]]
        prev = rom_dic[r_str[i-1]]
        if prev >= here:
            sum_out += prev
        else:
            sum_out -= prev
    return sum_out

path_to_input_txt = input("enter path to text file: ")

#intergalactic unit value calculator
defs = []
queries = []
with open(path_to_input_txt, 'r') as file:
    str_in = file.read()
list_in = str_in.split("\n")
for s in list_in:
    if "?" in s:
        queries.append(s)
    else:
        defs.append(s)
for i in range(len(defs)):
    this_def = defs[i]
    if not "is" in this_def:
        if defs[i] != defs[-1]:
            defs[i+1] = defs[i] + " " + defs[i+1]
            defs[i] = "404"
for i in range(len(defs)):
    this_def = defs[i]
    if not "is" in this_def:
        defs[i] = "404"
while("404" in defs) : 
    defs.remove("404")
numeral_defs = []
credits_defs = []
for s in defs:
    if "Credits" in s:
        credits_defs.append(s)
    else:
        numeral_defs.append(s)
num_dict = {}
for n_def in numeral_defs:
    x = n_def.split()
    num_dict.update({x[0]: x[2]})
cred_dict = {}
for c_def in credits_defs:
    x = c_def.split()
    first_half = []
    second_half = []
    reached_is = False
    for w in x:
        if w == "is":
            reached_is = True
        elif reached_is:
            second_half.append(w)
        else:
            first_half.append(w)
    x_key = first_half[-1]
    first_half = first_half[:-1]
    roman_num = ""
    for i in range(len(first_half)):
        roman_num += num_dict[first_half[i]]
    x_val = int(second_half[0]) / roman_to_int(roman_num)
    cred_dict.update({x_key: x_val})
print(cred_dict)
#query response system
q_res = []
for q in queries:
    q_ign = []
    reached_is = False
    super_is = False
    for w in q.split():
        if w == "is":
            if reached_is:
                super_is = True
            else:
                reached_is = True
        elif reached_is:
            q_ign.append(w)
    if not reached_is:
        q_re = "I have no idea what you are talking about"
    elif super_is:
        q_re = "I have no idea what you are talking about"
    else:
        q_ign.remove("?")
        q_object = ""
        for word in q_ign:
            q_object += word + " "
        if q_ign[-1] in cred_dict.keys():
            multiplier = cred_dict[q_ign[-1]]
            del q_ign[-1]
            should_write_credits = True
        else:
            multiplier = 1
            should_write_credits = False
        #convert ign to rn
        q_rn = ""
        for x in q_ign:
            q_rn += num_dict[x]
        answer = multiplier * roman_to_int(q_rn)
        if should_write_credits:
            q_re = q_object + "is " + str(int(answer)) + " Credits"
        else:
            q_re = q_object + "is " + str(int(answer))
    q_res.append(q_re)
out_string = ""
for qr in q_res:
    out_string += qr + "\n"
print("\n")
print(out_string)
with open("output.txt", "w") as out_file:
    out_file.write(out_string)