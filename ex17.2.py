class Kangaroo:
    def _init_(self, pouch_contents=None):
        if pouch_contents is None:
            self.pouch_contents = []
        else:
            self.pouch_contents = pouch_contents

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

    def _str_(self):
        contents = [str(item) for item in self.pouch_contents]
        return f'Kangaroo with pouch contents: {contents}'

if __name__ == '_main_':
    kanga = Kangaroo()
    roo = Kangaroo()
    kanga.put_in_pouch(roo)

    print(kanga)
    print(roo)