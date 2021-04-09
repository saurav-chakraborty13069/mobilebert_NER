import preprocess
from bert import Ner


model = Ner("bert_base_cased_2")

def predict(input):


    for text in input:
        text_cleaned = preprocess.clean_data(text['address'])
        print(text_cleaned)
        out = model.predict(text_cleaned)
        print(out)
        # print(type(mobilebert_uncased))
        # return jsonify({"result":mobilebert_uncased})
        words = {}
        a1 = []
        a2 = []
        a3 = []
        s = []
        c = []
        ps = []

        for item in out:

            tag = item['tag'].split('-')
            word = item['word']

            if len(tag) == 2:
                if tag[1] == 'A1':
                    # print(word)
                    a1.append(word)
                    # words['A1'] = a1.append(word)
                elif tag[1] == 'A2':
                    a2.append(word)
                    # words['A2'] = a2.append(word)
                elif tag[1] == 'A3':
                    a3.append(word)
                    # words['A3'] = a3.append(word)
                elif tag[1] == 'C':
                    c.append(word)
                    # words['C'] = c.append(word)
                elif tag[1] == 'S':
                    s.append(word)
                    # words['S'] = s.append(word)
                elif tag[1] == 'PC':
                    ps.append(word)
                # words['PS'] = ps.append(word)

        words['A1'] = " ".join(a1  )  # address1
        words['A2'] = " ".join(a2)
        words['A3'] = " ".join(a3)
        words['C'] = " ".join(c)
        words['S'] = " ".join(s)
        words['PS'] = " ".join(ps)
        print(words)
        return words

def main():
    input = [{"refno": 712713495,
      "address": "3 Landmark House , Somerset , Wirral Park Road , Glastonbury , Somerset , , Ba6 9Fr",
      "country": "UK"}]
    predict(input)


if __name__=='__main__':
    main()