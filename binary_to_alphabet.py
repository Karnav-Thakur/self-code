# binary to alphabet

# seperate multiple alphabets by a small 'b' like -> 100b100 will print DD

def binary_to_alphabet(bi:str):
    bi_split = bi.split("b")
    

    alphabets = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}
    
    clean = [i.strip()[::-1] for i in bi_split]
    
    check = [number for elem in clean for number in elem if int(number) != 0 if int(number) != 1]
    
    if check == []:
        check = False

    if not check:
        pass

    
    else:
        print("Give me a binary number")
        return
    word = ""
    for bi_list in clean:    
        som = 0
        for index,i in enumerate(bi_list):
            power = 2 ** index
            som += int(i)*power
        word += alphabets[som]
        
    return word

print(binary_to_alphabet("1011b0001b10010b1110b0001b10110"))


