from base import Melody


class WKNPMelody(Melody):
    @staticmethod
    def get_bpm():
        return 30

    @staticmethod
    def get_notes():
        return [
            ('D4', 0.3),
            ('B3', 0.3),
            ('B3', 0.3),
            ('C4', 0.3),
            ('A3', 0.3),
            ('A3', 0.3),
            ('G3', 0.3),
            ('B3', 0.3),
            ('D4', 0.3),
            ('D4', 0.3),
            ('B3', 0.3),
            ('B3', 0.3),
            ('C4', 0.3),
            ('A3', 0.3),
            ('A3', 0.3),
            ('G3', 0.3),
            ('B3', 0.3),
            ('G3', 0.3),
        ]
