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
        """
        Adds new note to list.
        """
        self.notes.append(note)

    def entries(self):
        """
        Prints contents in notes to terminal. reversed index order except
        note content.
        """
        note_length = len(self.notes)
        
        if not note_length == 0:
            for idx, note in enumerate(self.notes):
                return f'{note_length - idx}: {note}'
        else:
            return 'Notebook empty.'

    def edit(self, key, note):
        """
        Edits the n newest note.
        """
        self.notes[-key] = note

    def delete(self, key):
        """
        Deletes notes from n index
        """
        if key >= 0:
            del self.notes[-key]
        else:
            print('Negative number not allowed!')

    def __list_to_dict(self):
        """
        Converts a list to a dictionary.
        """
        _dict = {}
        _dict.update({
            f'{idx}': f'{note}' for idx, note in enumerate(self.notes)
        })
        return _dict

    def export(self):
        """
        Returns notes as json format.
        """
        return json.dumps(self.__list_to_dict())

    def __del__(self):
        try:
            with open('guestbook.data', 'w', encoding='utf8') as fout:
                fout.writelines(f'{note}\n' for note in self.notes)

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
