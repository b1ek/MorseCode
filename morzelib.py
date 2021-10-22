from enum import Enum as enum; 
import json, random, string
class MorseCode(enum):
    LONG = 1; 
    SHORT = 0; 
    PERIOD = 2; 
    L = LONG; 
    S = SHORT; 
    P = PERIOD; 
    SLONG = "-"; 
    SSHORT = "."; 
    SPERIOD = " "; 
    SL = SLONG; 
    SS = SSHORT; 
    SP = SPERIOD; 

    SOS = [S, S, S, L, L, L, S, S, S]; 
    def genEncoding(chars: str):
        L = MorseCode.L
        S = MorseCode.S

        _cb = list(chars); 
        random.shuffle(_cb); 
        chars = ''.join(_cb); 
        _buf = {}; 
        _buff = []; 
        _curlen = 2; 
        _noNuniquie = 0; 
        _l = len(chars)

        while 1:
            curr = random.choices([L, S], k=_curlen); 
            try: curchar = list(chars)[0]; 
            except Exception: break; 
            uniq = True; 
            for i in _buff:
                if curr.__eq__(i):
                    _noNuniquie += 1; 
                    uniq = False; 
            if uniq:
                _buf[curchar] = curr; 
                _buff.append(curr); 
                chars = chars.replace(curchar, ""); 
            if _noNuniquie > _curlen*4:
                _curlen += 1; 
        return _buf; 


    def toStr(input: list) -> str:
        out = []; 
        for i in input:
            if i == MorseCode.L.value:
                out.append(MorseCode.SL.value); 
            if i == MorseCode.S.value:
                out.append(MorseCode.SS.value); 
            if i == MorseCode.P.value:
                out.append(MorseCode.SP.value); 
        return ''.join(out); 

    def toInt(input: list)-> list[int]:
        out = []; 
        for i in input:
            if i == MorseCode.SL.value:
                out.append(MorseCode.L.value); 
            if i == MorseCode.SS.value:
                out.append(MorseCode.S.value); 
            if i == MorseCode.SP.value:
                out.append(MorseCode.P.value); 
        return out; 
    
    def fromStr(input: str):
        out = []; 
        for i in input:
            if i == MorseCode.SL.value:
                out.append(MorseCode.L); 
            else:
                out.append(MorseCode.S); 
        return out; 

    
    TRADITIONAL_EXTENDED = {
        "а": [S, L,],
        "б": [L, S, S, S,],
        "в": [S, L, L,],
        "г": [L, L, S,],
        "д": [L, S, S,],
        "е": [S,],
        "ж": [S, S, S, L,], # SSSL - Super Secure Shell :]
        "з": [L, L, S, S,],
        "и": [S, S,],
        "й": [S, L, L, L,],
        "к": [L, S, L,],
        "л": [S, L, S, S,],
        "м": [L, L,],
        "н": [L, S,],
        "о": [L, L, L,],
        "п": [S, L, L, S,],
        "р": [S, L, S,],
        "с": [S, L, S,],
        "т": [L,],
        "у": [S, S, L,], # SSL
        "ф": [S, S, L, S,],
        "х": [S, S, S, S,],
        "ц": [L, S, L, S,],
        "ч": [L, L, L, S,],
        "ш": [L, L, L, L,],
        "щ": [L, L, S, L,],
        "ъ": [L, L, S, L, L,],
        "ы": [L, S, L, L,],
        "ь": [L, S, S, L,],
        "э": [S, S, L, S, S,],
        "ю": [S, S, L, L,],
        "я": [S, L, S, L,],
        "err": [S, S, S, S, S, S, S, S,],
        "red": [S, S, S, S, S, S, S, S,],
        1: [S, L, L, L, L,], # don't use that
        2: [S, S, L, L, L,], # don't use that
        3: [S, S, S, L, L,], # don't use that
        4: [S, S, S, S, L,], # don't use that
        5: [S, S, S, S, S,], # don't use that
        6: [L, S, S, S, S,], # don't use that
        7: [L, L, S, S, S,], # don't use that
        8: [L, L, L, S, S,], # don't use that
        9: [L, L, L, L, S,], # don't use that
        0: [L, L, L, L, L,], # don't use that
        "1": [S, L, L, L, L,], # don't use that
        "2": [S, S, L, L, L,], # don't use that
        "3": [S, S, S, L, L,], # don't use that
        "4": [S, S, S, S, L,], # don't use that
        "5": [S, S, S, S, S,], # don't use that
        "6": [L, S, S, S, S,], # don't use that
        "7": [L, L, S, S, S,], # don't use that
        "8": [L, L, L, S, S,], # don't use that
        "9": [L, L, L, L, S,], # don't use that
        "0": [L, L, L, L, L,], # don't use that
        ".": [S, S, S, S, S,], # don't use that
        ",": [S, L, S, L, S, L,], # don't use that
        ":": [L, L, L, S, S, S,], # don't use that
        ";": [L, S, L, S, L,], # don't use that
        "(": [L, S, L, L, S, L,], # don't use that
        ")": [L, S, L, L, S, L,], # don't use that
        "\'": [S, L, L, L, L, S,], # don't use that
        "\"": [S, L, S, S, L, S,], # don't use that
        "—": [L, S, S, S, S, L,], # don't use that
        "/": [L, S, S, L, S,], # don't use that
        "?": [S, S, L, L, S, S,], # don't use that
        "!": [L, L, S, S, L, L,], # don't use that
        "-": [L, S, S, S, L,], # don't use that
        "@": [S, L, L, S, L, S,], # don't use that
        }; 
    CUSTOM = json.load(open("encoding.json", "tr", encoding="utf8")); 


def encodeMorse(string: str):
    out = []; 
    _encoding = MorseCode.CUSTOM.value; 
    for char in list(string):
        for el in _encoding[char]:
            out.append(el); 
        out.append(2)
    return out; 
def decodeMorse(input: list):
    _out = ""; 
    _encoding = MorseCode.CUSTOM.value; 
    _input = []
    _buf = []
    for i in input:
        if i == 2:
            _input.append(_buf.copy())
            _buf.clear()
        else:
            _buf.append(i)
    for i in _input:
        for key in _encoding:
            if _encoding[key] == i: _out = _out + key;
    return _out


if __name__ == "__main__":
    print("Morze lib v2.0"); 
    while 1:
        a = input("e for encode, d for decode: ").lower(); 
        if a == "e" or a == "d":
            break; 
    if a == "e":
        while 1:
            a = input("Text to encode: ").lower(); 
            c = input("You typed {0}.\nAre you sure? (y/any): ".format(a)).lower(); 
            if c == "y": break; 
        print(MorseCode.toStr(encodeMorse(a)))
    if a == "d": 
        print(".-- .-- . -.. .. - . - . -.- .-. - (traditional)")
        while 1:
            a = input("Text to decode: ").lower(); 
            c = input("You typed {0}.\nAre you sure? (y/any): ".format(a)).lower(); 
            if c == "y": break; 
        print(decodeMorse(MorseCode.toInt(a)))