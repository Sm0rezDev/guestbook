import sys
import json


class GuestBook:

    def __init__(self):
        self.notes = {}

        try:
            with open('guestbook.data', 'r') as fin:
                self.notes = json.load(fin)

            self.notes = {int(k): v for k, v in self.notes.items()}

        except FileNotFoundError:
            pass

    def new(self, note):
        if not self.notes:
            self.notes[1] = note
        else:
            self.notes[max(self.notes.keys()) + 1] = note

    def entries(self):
        entries = ''

        for k, v in self.notes.items():
            if not v == '':
                entries += f'{k}: {v}\n'

        return entries

    def edit(self, key, note):
        self.notes[key] = note

    def delete(self, key):
        self.notes[key] = ''
    
    def export(self):
        return self.notes

    def __del__(self):
        with open('guestbook.data', 'w') as fout:
            json.dump(self.notes, fout)


def main(args):

    book = GuestBook()

    if len(args) == 1:
        sys.exit('No arguments where given..')

    elif len(args) >= 3:

        if args[1] == 'new':
            book.new(args[2])

        if args[1] == 'edit':
            book.edit(args[2], args[3])
            
        if args[1] == 'delete':
            try:
                book.delete(args[2])
            except Exception as e:
                print(f'Note {e} not found..')
    else:

        if args[1] == 'list':
            print(book.entries())
        
        if args[1] == 'export':
            print(book.export())
        

if __name__ == '__main__':
    main(sys.argv)
