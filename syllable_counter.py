import english_syllable

def load_festival_CMU_dict(path='/usr/share/festival/dicts/cmu/cmudict-0.4.out'):
    cmu_dict = {}
    with open(path) as cmu_dict_file:
        for line in cmu_dict_file:
            # XXX This sucks
            if len(line.split('"')) <= 1:
                continue

            word = line.split('"')[1]
            cmu_dict[word] = line.count('((')
    return cmu_dict


def get_number_of_syllables(word):
    if not hasattr(get_number_of_syllables, 'CMU_dict_cache'):
        get_number_of_syllables.CMU_dict_cache = load_festival_CMU_dict()

    if word in get_number_of_syllables.CMU_dict_cache:
        num_syllables = get_number_of_syllables.CMU_dict_cache[word]
    else:
        num_syllables = english_syllable.count(word)

    if num_syllables == 0:
        num_syllables += 1

    return num_syllables

