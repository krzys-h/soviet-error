def build_xml_file_content(bpm, pitches):
    result_lines = [
        '<?xml version="1.0"?>',
        '<!DOCTYPE SINGING PUBLIC "-//SINGING//DTD SINGING mark up//EN" ',
        '"Singing.v0_1.dtd"',
        '[]>',
        '<SINGING BPM="%s">' % bpm,
    ]

    for notes, beats, word in pitches:
        result_lines.append(
            '<PITCH NOTE="%s"><DURATION BEATS="%s">%s</DURATION></PITCH>' % (
                ','.join(notes),
                ','.join([str(x) for x in beats]),
                word,
            )
        )

    result_lines.append('</SINGING>')
    return '\n'.join(result_lines)
