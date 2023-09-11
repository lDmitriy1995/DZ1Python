
#Задание 1

def is_palindrome(s): return s == s[::-1]

input_str = input("Введите строку: ")

if is_palindrome(input_str): print("Введенная строка является палиндромом.") 
else: print("Введенная строка не является палиндромом.")


#Задание 2

def main():
    text = input("Введите текст: ")
    reserved_words = input("Введите зарезервированные слова через пробел: ")
    words = reserved_words.split()

    modified_text = ""
    for word in text.split():
        if word.lower() in words:
            modified_text += word.upper() + " "
        else:
            modified_text += word + " "
    print("Измененный текст: " + modified_text.rstrip())


if __name__ == "__main__":
    main()

#Задание 3

text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin eget tortor vel lacinia eleifend. 
Aliquam ac dui sed diam fermentum ultricies. Mauris a ipsum quis nisl  pulvinar iaculis.
Phasellus tempor feugiat arcu, eu porttitor eros auctor a. Fusce sit amet finibus ex, vel euismod metus. Vivamus vitae odio ligula. 
Etiam nec dui eu tellus aliquet consequat. Integer viverra sagittis dolor at faucibus. 
Praesent venenatis neque sed dui vulputate, eu vehicula erat volutpat. Quisque consectetur, tellus eu suscipit gravida, ipsum felis lacinia nunc, et congue nisi risus vel velit.")

sentences = text.split('.')
print(f"Количество предложений: {len(sentences)}")
