import random
from hangman_word import word_list
from hangman_art import stage, logo

lives = 6

print(logo)

# Chọn ngẫu nhiên một từ từ danh sách word_list và chuyển nó thành chữ thường
chosen_word = random.choice(word_list)


placeholder = ""# Tạo chuỗi placeholder với số ký tự là dấu gạch dưới tương ứng với độ dài từ được chọn

word_length = len(chosen_word)
for place in range(word_length):
    placeholder += "_"
print("Word to guess:" + placeholder)  # In chuỗi placeholder để cho người chơi biết số ký tự cần đoán

# Biến game_over được sử dụng để kiểm soát vòng lặp (chơi cho đến khi đoán đúng từ)
game_over = False

# Danh sách lưu các chữ cái đã đoán đúng
correct_letter = []

# Vòng lặp chính của trò chơi, tiếp tục cho đến khi từ được đoán đúng
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    # Người chơi nhập một chữ cái
    guess = input("Guess a letter: ").lower()


    if guess in correct_letter:
        print(f"You have already guessed {guess}")

    # Chuỗi display sẽ lưu trạng thái hiện tại của từ (chứa các ký tự đoán đúng và các dấu gạch dưới)
    display = ""

    # Duyệt qua từng ký tự trong từ được chọn
    for letter in chosen_word:
        # Nếu chữ cái đoán đúng thì thêm nó vào display và lưu vào danh sách correct_letter
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        # Nếu chữ cái đã được đoán đúng trước đó, hiển thị nó
        elif letter in correct_letter:
            display += letter
        # Nếu chưa đoán đúng, tiếp tục hiển thị dấu gạch dưới
        else:
            display += "_"

    print("Word to guess:" + display)
    # In trạng thái hiện tại của từ được đoán
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stage[lives - 1])
        if lives == 0:
            game_over = True
            print("*********************You lost!*********************")
    # Nếu không còn dấu gạch dưới, người chơi đã đoán đúng từ và kết thúc trò chơi
    if "_" not in display:
        game_over = True  # Đặt game_over thành True để thoát khỏi vòng lặp
        print("*********************You win!*********************")  # Thông báo người chơi đã thắng


