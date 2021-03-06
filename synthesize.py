import sys
import tempfile

from melody import melodies
from xml_building import build_xml_file_content
from syllable_counter import get_number_of_syllables
from filters import filter_digits_to_text, filter_remove_nonletters


def print_festival_singing_command(xml_file_content):
    filename = tempfile.mktemp()

    with open(filename, 'w') as f:
        f.write(xml_file_content)

    print('(tts \"%s\" \'singing)' % filename)


def synthesize(message, melody):
    message = message.lower()
    message = filter_digits_to_text(message)
    message = filter_remove_nonletters(message)

    words = message.split(' ')

    words = [word for word in words if word != '']

    notes_iterator = melody.get_notes_iterator()
    pitches = []
    for word in words:
        num_syllabes = get_number_of_syllables(word)
        notes = []
        beats = []
        for unused_i in range(num_syllabes):
            try:
                note, beat = next(notes_iterator)
            except StopIteration:
                notes_iterator = melody.get_notes_iterator()
                note, beat = next(notes_iterator)

            notes.append(note)
            beats.append(beat)

        pitches.append((notes, beats, word))

    xml_file_content = build_xml_file_content(melody.get_bpm(), pitches)
    print_festival_singing_command(xml_file_content)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s melody" % sys.argv[0])
        print("Text is read from stdin")
        sys.exit(0)

    synthesize(sys.stdin.read(), melodies[sys.argv[1]])
