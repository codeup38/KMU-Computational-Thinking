
def load_dictionary(filename):
    # (랜덤 공백)숫자(랜덤 공백)영단어(랜덤 공백)뜻(랜덤 공백)
    words = {}
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        for line in lines :
            line = line.strip()
            
            if line is None :
                continue
            
            part = line.split(maxsplit=1)
            
            if len(part) < 2 :
                continue
            
            word, meaning = part[1].split(maxsplit=1)
            words[word] = meaning.strip('"')
        
    return words
            


def main():
    dictionary = load_dictionary('vocabulary.txt')

    while True :
        user_input = input('단어를 입력하세요. 중단을 원하면 quit를 입력하세요.\n')

        if user_input.lower()== 'quit' :
            break

        if user_input in dictionary :
            print(f'{user_input}: {dictionary[user_input]}\n')
        else :
            print(f"{user_input}은(는) 사전에 없습니다.")


if __name__ == "__main__":
    main()