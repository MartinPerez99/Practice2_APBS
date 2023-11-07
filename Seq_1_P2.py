
text = 'abaaba$'
tally_text = "abba$aa"
def bwt_calculator(text):
    bwt = ''
    data = []
    length = len(text)

    for idx in range(length):
        row = text[idx:] + text[:idx]
        data.append(row)
    sorted_data = sorted(data)

    for i in sorted_data:
        bwt += i[length - 1]
    return bwt

#print(bwt_calculator('abaaba$'))


f_calculator = lambda text : ''.join(sorted(text))

#print(f_calculator(text))

def tally_calculator(bwt):
    import pandas as pd
    characters_of_interest = list(set(bwt.replace('$','')))

    dict_list = {caracter: [] for caracter in characters_of_interest}
    for i in range(1,len(bwt)+1):
        window = list(bwt[:i])
        for l in set(window):
            if l in characters_of_interest:
                dict_list[l].append(window.count(l))
    for caracter in characters_of_interest:
        while len(dict_list[caracter]) < len(bwt):
            dict_list[caracter].insert(0, 0)
    tally = pd.DataFrame(dict_list)
    tally = tally.rename(columns={key: key for key in tally.keys()})
    return tally

print(tally_calculator(tally_text))