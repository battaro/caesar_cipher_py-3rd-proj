from logo_and_alphabet import logo, alphabet #importing the logo and list call alphabet  

#function have literally most thing important on this program
def caesar(plain_text, shift_amount, the_direction): #3 parameters used in this function
    #because the number of letters of alphabet is 26, we get the remainder 26 of shift_amount (lets say we wrote 60, 60 % 26 -> 8)
    #still right ? (52 which is '26 x 2', + 8 is 60) lets say we shift 'a' letter by 60 go to 8th place its 'i' letter and if we 
    #shift it by 8, same thing 'i' letter. same thing for every letter and number :)
    shift_amount %= 26 
    end_text = "" #variable used to store the text we want
    if the_direction == "decode": #if the user have an encrypted text already, he will write decode 
        shift_amount *= -1 #simply, instead of going right go left 
            
    for letter in plain_text: #letter is new variable will pass on each letter in plain_text 
        if letter not in alphabet: #if the letter not in the alphabet list (i mean here symbol,spaces,numbers)
            end_text += letter #just add it without control, just put it as it is on the right place
        else: #if the last condition not worked go here 
            pos = alphabet.index(letter) #new variable have the position of the letter on the alphabet list
            #put the new letter in the old variable but taking the position of the word plus the shift_amount
            end_text += alphabet[pos + shift_amount] 
    #print the encoded or decoded result and the end text        
    print(f"Here's the {the_direction}d result: {end_text}") 
       
print(logo) #print the logo of our program

isGameFinished = False #new boolean variable have 2 chance if its true the game will end else will game continue
while isGameFinished != True:#checked the variable and entered the loop

    #3 new variables we will use it like arguments for the 3 parameters on ceaser function
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    
    caesar(plain_text=text, shift_amount=shift, the_direction=direction) #call the function to start the encryption or decryption
    
    #when the program end, ask the user if he want to continue or no 
    answer = input("Type 'yes' if you want to continue. if you don't type 'no':\n").lower()#new variable 
    #if the answer is equal to no get out of the program else nothing will happen just stay normal 
    if answer == "no":
        print("Bye Bye")
        isGameFinished = True
        
#i programmed this cute program in 3 hours and just in 8 days of learning python
#u can use my code when u want and as u need not matter with me but
#Program Developed by Brimo Battaro :O
#i know i have so many grammatic mistakes in every repostory i share '_'
