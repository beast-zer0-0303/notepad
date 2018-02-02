# coding: utf-8
import hashlib
import crypt, getpass, pwd

PASSWORD_LIST = {
    '$6$Z4xEy/1KTCW.rz': '$6$Z4xEy/1KTCW.rz$Yxkc8XkscDusGWKan621H4eaPRjHc1bkXDjyFtcTtgxzlxvuPiE1rnqdQVO1lYgNOzg72FU95RQut93JF6Deo/',
    '$6$ffl1bXDBqKUiD': '$6$ffl1bXDBqKUiD$PoXP69PaxTTX.cgzYS6Tlj7UBvstr6JruGctoObFXCr4cYXjIbxBSMiQZiVkKvUxXUC23zP8PUyXjq6qEq63u1',
    '$6$ZsJXadT/rv': '$6$ZsJXadT/rv$T/2gVzYwMBaAsZnHIjnUSmTozIF/ebMvtHIJjikFehvB8pvy28DUIQYbTJLG6QAxhzJAKOROnZq0xV4hUGefM1',
    '$6$l0NHH5FF0H/U': '$6$l0NHH5FF0H/U$fPv3c5Cdls/UaZmglR4Qqh8vhpIBsmY1sEjHi486ZcDQ2Vx5GY0fcQYSorWj6l42jfI47w437n.NBm8NArFyT/',
    '$6$wAnAP/NMiLa/yE': '$6$wAnAP/NMiLa/yE$.gi4r3xYuPTg5z2S59z2EzFbqpmwZYy1tBSVA9/hqTFnWY0tHqXbwL.dFQwHzKTuzXV6WMgjEZlyzUPGzVtPb0',
    '$6$jTgFhKHk/': '$6$jTgFhKHk/$xQIdn7snYAAGvifxC02YLXcAKkiuPbJ3KBkH2Q8BZ12TL2aepaUJotgfKfNSPCXWebyCY/skOmOymok.KIm5D0',
    '$6$8LXZt/zPbLtIn1o': '$6$8LXZt/zPbLtIn1o$ynsZxueG88Kz0vDr3cyK.21cv4GWw9iaW9oYZcmZ9SY5UpMQS1wl2/dbXGyR8WzVBKKP/6k8VYvWuiNQ3We52/',
    '$6$jnA8m/S5aU0/': '$6$jnA8m/S5aU0/$PGrG8mDy.vs3W9xhG1qd56eOEainH9xntY48.duznt989TXMn6J.scOBqp4BWg3fHWxoFgBn26LYvcnqWGcoF1',
    '$6$ITB7n/qsP': '$6$ITB7n/qsP$fmrmItHX9B96PmhsxIX21vdYDvFHiIPnyzRFjWIbcd3y/DRHCm0lzyJEnWlQChdDAiFUFXtqwoTbEdREXQ99M.',
    '$6$LpgLJrjPV': '$6$LpgLJrjPV$6sa0KW08Q10S.C/BSUHlHaQZT5n8uIygZSsWP5drdmuhI7c17wWCK/GEzQS7g8EL//5bqdjo1C90smTDhLEcF1',
    '$6$0VSPwOzcL//6QR': '$6$0VSPwOzcL//6QR$RgtMpkfVPb5Cli7cjVE5jMgJlN10xY1R3jxRNrY0l/84R3.NvxP3I8XtkMkonU6DKhge0JGp54DZLQqUN9kL7/',
    '$6$zryub/lvSKj7Xl': '$6$zryub/lvSKj7Xl$eazV2fmcJa5M3qMovQqARGK59Qxtfv2zjUJvphKNnyUMVyBn.SjEFhRT/mAjz3QFroNbwmrYLtrpyxjH.q64n/',
    '$6$tAkM0dDUFe76d8K/': '$6$tAkM0dDUFe76d8K/$OnNGFEuIf1seMlLHb.8.y5/cpmBUcMbhLhOfFdd0E/DKASXPS4riB4uz2Fg3om9Atg.g7s.JFoKV0uuJ461KV/',
    '$6$0cCdE5Nfqu/HFS': '$6$0cCdE5Nfqu/HFS$PwnLdS.chtm6qGwf2Uuiko7V3fMwjcQ52M8hslvoReFQ9XOBXw603Ok20VJwWAwR6RNv6adn6a6kuRm5Y3.ge1',
    '$6$RgPs7j4eSa/v': '$6$RgPs7j4eSa/v$71CeLB9Z1Fafi6vi2ou5LzRz5xXWTzvZeZgelnm2przx.JQYp21p8h2BCyTYFd10MKD/cquPvn42vSzlJJJ8Q1',
    '$6$1uhGQ/5DwMp/': '$6$1uhGQ/5DwMp/$UjYTEVaChEzmUITvWpaZVvYYDLBULpI4IEyieClSsyC2NHwEnaDx6xwtUVpQPxEhi6R7OQhX68Oo5CfilYqDQ.',
    '$6$V/InSacMp8U': '$6$V/InSacMp8U$UpDgdL/GS/kdFmn1rO97YkLAeTgofu4fDVUGoV1PWnVFxUtVyx24ix5hJp53FkBuqdzmXgwGcb6MU5AWJWjaB1',
    '$6$d6mWSrE8vxDe': '$6$d6mWSrE8vxDe$UqTgKPfKxm0/Aboz8DeFNNiZsFBYyE6iGpqUzSX4UpWSDfXt1DERBtI29H2Gz5q.6ls3730naAo31wAacvs/L0',
    '$6$ulcKu/ddomcNGRJj': '$6$ulcKu/ddomcNGRJj$i8XB1D4YtLGbAHX0XHX88ObUWw8dQsrTqoliGAU//zGHNLmLeWd.4k5YHViNSy3rlGTQSRPtutlKnub8aRnzy0',
    '$6$cVnhE9CwfSIIA': '$6$cVnhE9CwfSIIA$wrn6p3cgfz.JOc6KVkieNCtc.FzkjUdcDDlivn0APnYv9/z4tt7hUpPft5T8kMmnx/hiF92vjnDxcauVyQySp.',
    '$6$2Pg2VxXg': '$6$2Pg2VxXg$K8AqsCMPAFiXSxNjETBWqEHQom9Q5dDIz9/nItxpQatrG9gvv9CRJP3kQzKLbRf13FxfOXpeEYIpOEK.2i1HP0',
}

def read_dictionaly(dictionaly_file):
    f = open(dictionaly_file)
    words = set(map(lambda x: x.replace('\n','').replace('\r',''), f.readlines()))
    f.close()
    return words

def dictionaly_attack(dictionaly, password, salt):
    # python2 系用
    for word in dictionaly:
        val = salt + word
        val = val.encode("ascii")
        if password == hashlib.sha512(val).hexdigest():
            print('OK')
            print(word)
            return

    print('dictionaly_attack NG')
    return

def dictionaly_attack2(dictionaly, password, salt):
    # python3 系用
    for word in dictionaly:
        if password == crypt.crypt(word, salt):
            # print('OK')
            print(word)
            return

    print('dictionaly_attack NG')
    return

if __name__ == '__main__':
    dictionaly = read_dictionaly('dictionaly.txt')
    for salt, password in PASSWORD_LIST.items():
        #print(salt)
        #print(password)
        #dictionaly_attack(dictionaly, password, salt)
        dictionaly_attack2(dictionaly, password, salt)
