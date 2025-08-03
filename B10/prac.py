import string
# Đếm số lần từ xuất hiện trong 1 văn bản
def count_words(paragraph):
    # Thay đổi thành chữ in thường
    paragraph = paragraph.lower()

    # Loại dấu câu
    for char in string.punctuation:
        paragraph = paragraph.replace(char, "")
        
    # Tách từ
    words = paragraph.split()
    
    # Đếm tần suất
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1 # Cộng 1 lần đếm
        else:
            word_count[word] = 1 # Đếm 1 lần
            
    return word_count

p = "They rushed out the door, grabbing anything and everything they could think of they might need. There was no time to double-check to make sure they weren't leaving something important behind. Everything was thrown into the car and they sped off. Thirty minutes later they were safe and that was when it dawned on them that they had forgotten the most important thing of all."
result = count_words(paragraph=p)
# Hiển thị danh sahcs theo thứ tự chữ cái
max = 0
word_count_max = ""
for word, counter in sorted(result.items()):
    if counter > max:
        max = counter
        word_count_max = word
        
    print(f"{word}: {counter}")
print(f"Từ với số lần lặp cao nhất: {word_count_max}, lặp {max} lần")