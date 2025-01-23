def char_to_utf8(char):
    if len(char) != 1:
        raise ValueError("Input must be a single character")
    utf8_value = char.encode('utf-8')
    return utf8_value

def encrypt(utf8_value, shift):
    encrypted_text = ""
    for char in utf8_value:
        encrypted_text += chr((char + shift)%256)
    return encrypted_text

# Example usage
character = "Ȇ"
utf8_value = char_to_utf8(character)
e_text = encrypt(utf8_value, 4)
print(f"The UTF-8 value of '{character}' is {utf8_value}")
print(f"The encrypted value of '{character}' is {e_text}")