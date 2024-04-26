s = "the sky is blue"
s_edit = s.split()
s_invert = ""
for c in range(len(s_edit) - 1, -1, -1):
    if c == (len(s_edit) - 1):
        s_invert += s_edit[c]
    else:
        s_invert += " " + s_edit[c]
    
#return s_invert
print(s_invert)