# coding: utf-8

# シーザー暗号解くためのスクリプト
MAPPING = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

TARGET_STRING = 'EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT.'

if __name__ == '__main__':
    taget_string = TARGET_STRING

    char_list = list(taget_string)
    print char_list

    add_index = 13
    index = 0
    count = len(MAPPING)
    new_char_list = [None] * 500
    print new_char_list

    for char in MAPPING:
        # index + add_index した文字列に変換する
        target_index = index + add_index
        if target_index >= count:
            target_index = target_index - count

        target_char = MAPPING[target_index]

        char_index = 0
        for change_char in char_list:
            is_upper = None
            if change_char.isupper():
                is_upper = 1
                change_char = change_char.lower()

            if change_char == char:
                if is_upper:
                    new_char_list[char_index] = target_char.upper()
                else:
                    new_char_list[char_index] = target_char
            char_index = char_index + 1

        index = index + 1

    puts_string = ''
    for char in new_char_list:
        if char is None:
            char = ' '
        puts_string = puts_string + char

    print puts_string
