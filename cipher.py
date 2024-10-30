
def encrypted_value (value, shift = 3):
    char_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\{]{[/':;?/>.<,"

    encrypted_value = ""

    for character in value:

        #find current location
        original_index = char_set.find(character)

        shifted_index = (original_index + shift) % len(char_set)
        encrypted_value += char_set[shifted_index]
    
    return encrypted_value

def decrypted_value (value, shift = 3):
    char_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\{]{[/':;?/>.<,"

    decrypted_value = ""

    for character in value:

        #find current location
        original_index = char_set.find(character)

        shifted_index = (original_index - shift) % len(char_set)
        decrypted_value += char_set[shifted_index]
    
    return decrypted_value

#user_input = input("Input your password : ")

#encrypted_pass = encrypted_value(user_input)

#print("original text : " + user_input)
#print("encrypted : " + encrypted_pass)