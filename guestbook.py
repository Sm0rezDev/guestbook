import sys
import json


class GuestBook:

    def __init__(self):
        self.notes = {}

        try:
            with open('guestbook.data', 'r') as fin:
                self.notes = json.load(fin)

        except FileNotFoundError:
            pass

    def new(self, note):
        count = len(self.notes)
        self.notes[count] = note
    
    def entries(self):
        entries = ''

        for k, v in self.notes.items():
            entries += f'{k}: {v}\n'
        
        return entries

    def edit(self, key, note):
        self.notes[key] = note

    def delete(self, key):
        self.notes.pop(key)

    def __del__(self):
        with open('guestbook.data', 'w') as fout:
            json.dump(self.notes, fout)
