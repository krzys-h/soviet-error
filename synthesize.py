import os
import sys
import string
import tempfile

from melody import melodies
from xml_building import build_xml_file_content
from syllable_counter import get_number_of_syllables

def print_festival_singing_command(xml_file_content):
    filename = tempfile.mktemp()

    with open(filename, 'w') as f:
        f.write(xml_file_content)

    print('(tts \"%s\" \'singing)' % filename)


def synthesize(message, melody):
    char_whitelist = string.ascii_letters + ' '

    message = message.lower()

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

    pitches = []
    for word in words:
        num_syllabes = get_number_of_syllables(word)
        notes = []
        beats = []
        for unused_i in range(num_syllabes):
            try:
                note, beat = get_first_note()
            except IndexError:
                raise Exception("End of melody at word: '%s'" % word)

            notes.append(note)
            beats.append(beat)

        pitches.append((notes, beats, word))

    xml_file_content = build_xml_file_content(melody.get_bpm(), pitches)
    print_festival_singing_command(xml_file_content)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: %s melody text" % sys.argv[0])
        sys.exit(0)

    synthesize(sys.argv[2], melodies[sys.argv[1]])
