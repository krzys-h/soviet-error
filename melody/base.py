class Melody(object):
    @classmethod
    def get_notes_iterator(cls):
        for note in cls.get_notes():
            yield note
