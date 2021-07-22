import zlib

from collections import defaultdict
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import EnglishStemmer
import nltk
from nltk.stem.porter import *

stemmer = EnglishStemmer()


class token:
    def __init__(self, val, start, end, id):
        self.val = val
        self.offset_end = end
        self.offset_start = start
        self.id = id


class gram:
    def __init__(self, val, start, end):
        self.hashVal = zlib.crc32(bytes(val, "utf8"))
        self.start = start
        self.end = end


class document:
    def __init__(self, name, text):
        self.name = name
        self.tokens = plag.preprocess(text)
        self.grams = plag.offset_to_gram(self.tokens)
        self.checksumMap = plag.generateHashMap(self.grams)


class matchrange:
    def __init__(self, susp_start, susp_end, src_start, src_end):
        self.susp_start = susp_start
        self.susp_end = susp_end
        self.src_start = src_start
        self.src_end = src_end
        self.tokensclaimed = src_end - src_start


class plag:

    def preprocess(self, str):
        # # Stemming
        # nltk_stemedList = []
        # for word in nltk_tokenList:
        #     nltk_stemedList.append(p_stemmer.stem(word))
        #
        # # Lemmatization
        # wordnet_lemmatizer = WordNetLemmatizer()
        # nltk_lemmaList = []
        # for word in nltk_stemedList:
        #     nltk_lemmaList.append(wordnet_lemmatizer.lemmatize(word))
        #
        # print("Stemming + Lemmatization")
        # print(nltk_lemmaList)
        # # Filter stopword
        # filtered_sentence = []
        # nltk_stop_words = set(stopwords.words("english"))
        # for w in nltk_lemmaList:
        #     if w not in nltk_stop_words:
        #         filtered_sentence.append(w)
        # # Removing Punctuation
        # punctuations = ":,;"
        # for word in filtered_sentence:
        #     if word in punctuations:
        #         filtered_sentence.remove(word)
        # print(" ")
        # print("Remove stopword & Punctuation")
        # print(filtered_sentence)
        # str=" ".join(filtered_sentence)
        # print(str)
        # l=re.split(r'@|\.|\?|\!', str)
        # print(l)

        offset_data = []
        id = 0
        n = len(str)
        curr = ""
        j = 0
        s = ""
        for i in range(n):
            s = str[i]
            if not re.search(r'[\s\.]', s):
                if re.search(r"[\w\-]", s):
                    curr += s
            else:
                if j != i and len(curr) != 0:
                    offset_data.append(token(stemmer.stem(curr.lower()), j, i, id))
                    id += 1
                curr = ""
                j = i + 1
        for i in offset_data:
            print(i.val, i.offset_start, i.offset_end)
        return offset_data

    def offset_to_gram(self, off_data, grams):
        data = []
        n = len(off_data)
        s = [""]
        for i in range(grams - 1):
            s.append(off_data[i].val)
        for i in range(grams - 1, n):
            low = off_data[i - grams + 1].id
            high = off_data[i].id + 1
            s = s[1:] + [off_data[i].val]
            data.append(gram(" ".join(s), low, high), )
        return data

    def generateHashMap(self, grams):
        checksumMap = defaultdict(lambda: [])
        for i in grams:
            checksumMap[i.hashVal].append(i)
        return checksumMap


x = open("ex.txt", encoding='utf8')
y = x.read()
print("bgf")
a = plag()
a.preprocess(y)


def getMatches(grams: list[gram],
               src_doc: document):
    offset_map = defaultdict(lambda: [])
    matches = []
    for _gram in grams:
        if not src_doc.checksumMap[_gram.hashVal]:
            continue

        for z in src_doc.checksumMap[_gram.hashVal]:
            offset = _gram.start - z.start

            if offset in offset_map and offset_map[offset][-1].self.susp_end + 1 == _gram.end:
                offset_map[offset][-1].self.susp_end = _gram.end
                offset_map[offset][-1].self.src_end = z.end
            else:
                offset_map[offset].append(matchrange(_gram.start, _gram.end, z.start, z.end))

    for offset in offset_map:
        for values in offset_map[offset]:
            for value in values:
                value.tokensclaimed = value.susp_end - value.susp_start
                matches.append(value)
    return matches


def detectruns(src_len, susp_len, confidence, matches):
    if src_len > susp_len:
        sub_len = susp_len
    else:
        sub_len = src_len

    target_tokens = int(sub_len * (confidence))

    hits = [False for i in range(susp_len)]

    for match in matches:
        for i in range(match.susp_start, match.susp_end):
            hits[i] = True

    total_matches = 0
    for i in range(sub_len):
        if hits[i]:
            total_matches += 1

    out = []
    if total_matches >= target_tokens:
        out.append(0)

    for i in range(1,susp_len):
        if hits[i-1]:
            total_matches-=1
        end = i+sub_len-1

        if end < susp_len and hits[end]:
            total_matches+=1

        if total_matches>=target_tokens:
            out.append(i)

    if len(out)==0:
        return []

    # final_out = [i for i in range ]
