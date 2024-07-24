full_string=input()
sub_sequence=input()
sub_sequence_index=0
sub_sequence_length=len(sub_sequence)
for char in full_string:
    if char==sub_sequence[sub_sequence_index]:
        sub_sequence_index+=1
        if sub_sequence_index==sub_sequence_length:
            break
if(sub_sequence_index==sub_sequence_length):
    print("Yes")
else:
    print("No")