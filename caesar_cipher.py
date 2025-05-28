alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def encode_or_decode(direction, text, shift):
    ans = ""
    if direction == "decode":
        shift *= -1
    for i in text:
        if i in alphabet:
            ans += alphabet[((alphabet.index(i) + shift) % 26)]
        else:
            ans += i
    print(f"Here is the {direction}d result: {ans}")


while 1:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    encode_or_decode(direction, text, shift)
    x = input("Type 'yes' if you want to go again, otherwise type 'no'.").lower
    if x == "no":
        break
