import sys
import json


class GuestBook:

    def __init__(self):
        self.notes = []

        try:
            with open('guestbook.data', 'r', encoding='utf8') as fin:
                line = fin.read()
                self.notes = line.splitlines()

        except FileNotFoundError:
            pass

    def new(self, note):
        self.notes.append(note)

    def entries(self):
        for idx, note in enumerate(self.notes):
            print(f'{idx}: {note}')

    def edit(self, key, note):
        """
        Edits the n newest note.
        """
        self.notes[-key] = note

    def delete(self, key):
        """
        Deletes notes from n
        """
        del self.notes[-key]
    
    def export(self):
        """
        Returns a dict
        """
        note_dict = {}
        for idx, note in enumerate(self.notes):
            note_dict.update({f'{idx}': f'{note}'})

        return note_dict

    def __del__(self):
        try:
            with open('guestbook.data', 'w', encoding='utf8') as fout:
                for note in self.notes:
                    fout.writelines(f'{note}\n')

        except FileNotFoundError:
            pass


def main(args):

    book = GuestBook()

    if len(args) == 1:
        sys.exit('No arguments where given..')

    elif len(args) >= 3:

        if args[1] == 'new':
            book.new(args[2])

        if args[1] == 'edit':
            book.edit(int(args[2]), args[3])
            
        if args[1] == 'delete':
            book.delete(int(args[2]))
    else:

        if args[1] == 'list':
            book.entries()
        
        if args[1] == 'export':
            print(book.export())
        

if __name__ == '__main__':
    main(sys.argv)
