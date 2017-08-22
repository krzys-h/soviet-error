import os
import sys
import string
import tempfile

import english_syllable

from melody import melodies

def sing(xml):
    filename = tempfile.mktemp()

    with open(filename, 'w') as f:
        f.write(xml)

    print('(tts \"%s\" \'singing)' % filename)


def calculate_syllabe_number_hotfices():
    syllabe_number_hotfices = {}
    with open('/usr/share/festival/dicts/cmu/cmudict-0.4.out') as cmudict:
        for line in cmudict:
            # XXX This sucks
            if len(line.split('"')) <= 1:
                continue

            word = line.split('"')[1]
            syllabe_number_hotfices[word] = line.count('((')
        
        
    syllabe_number_hotfices.update({
        'packages': 3,
    })
    return syllabe_number_hotfices


def synthesize(message, melody):
    syllabe_number_hotfices = calculate_syllabe_number_hotfices()

    char_whitelist = string.ascii_letters + ' '

    message = message.lower()

    result_lines = [
        '<?xml version="1.0"?>',
        '<!DOCTYPE SINGING PUBLIC "-//SINGING//DTD SINGING mark up//EN" ',
        '"Singing.v0_1.dtd"',
        '[]>',
        '<SINGING BPM="%s">' % melody.get_bpm(),
    ]

    def get_first_note():
        first_note = get_first_note.melody[0]
        get_first_note.melody = get_first_note.melody[1:]
        return first_note

    get_first_note.melody = melody.get_notes()

    for digit, digit_text in [
            ('0', 'zero'),
            ('1', 'one'),
            ('2', 'two'),
            ('3', 'three'),
            ('4', 'four'),
            ('5', 'five'),
            ('6', 'six'),
            ('7', 'seven'),
            ('8', 'eight'),
            ('9', 'nine'),
        ]:
        message = message.replace(
            digit,
            ' %s ' % digit_text,
        )

    message = ''.join([char if char in char_whitelist else ' ' for char in message])

    words = message.split(' ')

    words = [word for word in words if word != '']

    sys.stderr.write('%s\n' % ' '.join(words))

    for word in words:
        if word in syllabe_number_hotfices:
            num_syllabes = syllabe_number_hotfices[word]
        else:
            num_syllabes = english_syllable.count(word)
            
        if num_syllabes == 0:
            num_syllabes += 1

        notes = []
        beats = []
        for unused_i in range(num_syllabes):
            try:
                note, beat = get_first_note()
            except IndexError:
                raise Exception("End of melody at word: '%s'" % word)

            notes.append(note)
            beats.append(beat)

        result_lines.append(
            '<PITCH NOTE="%s"><DURATION BEATS="%s">%s</DURATION></PITCH>' % (
                ','.join(notes),
                ','.join([str(x) for x in beats]),
                word,
            )
        )

    result_lines.append('</SINGING>')

    sing('\n'.join(result_lines))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: %s melody text" % sys.argv[0])
        sys.exit(0)

    synthesize(sys.argv[2], melodies[sys.argv[1]])
