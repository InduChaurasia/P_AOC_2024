import re
from utilities import read_file,Year

def get_input():
    register=[]
    programe=[]
    for line in read_file(Year.y2024,'day17.txt'):
        if line:
            numbers = re.findall(r'\d+', line)
            numbers = list(map(int, numbers))
            if line.startswith('Register'):
                register.extend(numbers)
            else:
                programe.extend(numbers)
    return register,programe

def combo_val(val,register):

    if val<=3:
        return val
    elif val==4:
        return register[0]
    elif val==5:
        return register[1]
    elif val==6:
        return register[2]
    elif val==7:
        raise RuntimeError(f'invalid value {val}')

def execute_instruction(register,programe):
    output = []
    index=0
    while index<len(programe)-1:
        instruction=programe[index]
        operand=programe[index+1]
        if instruction==0:
            register[0]=register[0]>>combo_val(operand,register)
        elif instruction==1:
            register[1]=register[1] ^ operand
        elif instruction==2:
            register[1]=combo_val(operand,register)%8
        elif instruction==3:
            if register[0]!=0:
                index=operand
                continue
        elif instruction==4:
            register[1]=register[1] ^ register[2]
        elif instruction==5:
            val = combo_val(operand,register)%8
            output.append(val)
        elif instruction==6:
            register[1]=register[0]>>combo_val(operand,register)
        elif instruction==7:
            register[2]=register[0]>>combo_val(operand,register)
        index+=2
    return output

def main():
    register,programe = get_input()
    print(execute_instruction(register,programe))
if __name__=='__main__':
    main()
