import art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(text: str, shift: int, direction: str) -> str:
    shift %= 26
    
    if direction == "decode":
        shift *= -1
        
    result = []    
        
    for char in text:
        if char in alphabet:
            old_idx = alphabet.index(char)
            new_idx = (old_idx + shift) % 26
            result.append(alphabet[new_idx])
        else:
            result.append(char)
            
    return ''.join(result)


def main():
    while True:
        print(art.logo, "\n")

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").strip().lower()
        text = input("Type your message: ").strip().lower()
        shift = int(input("Type the shift number: "))

        message = caesar_cipher(text, shift, direction)
        print(f"Here is your '{direction}d' message: {message}")
        
        should_continue = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
        if should_continue != "yes":
            print("Goodbye!")
            break
        
        
main()