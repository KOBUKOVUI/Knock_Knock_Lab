#decrypted Ceaser 

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  
    return decrypted_text

def brute_force_caesar(ciphertext, reverse=False):
    for shift in range(1, 26):
        result = caesar_decrypt(ciphertext, shift)
        if reverse:
            result = result[::-1]  # Đảo ngược kết quả
        print(f"Shift {shift}: {result}")


ciphertext = "Khoor Zruog"  
brute_force_caesar(ciphertext, reverse=True)