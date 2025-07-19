class Tnode:
    def __init__(self):
        self.isendword = False
        self.storetrie = {}


class Trie:
    def __init__(self):
        self.root = Tnode()

    def insertele(self, key):
        element = self.root
        for a in key:
            if not element.storetrie.get(a):
                element.storetrie[a] = Tnode()
            element = element.storetrie[a]
        element.isendword = True

    def buildtrie(self, grp):
        for key, values in grp.items():
            for word in values:
                self.insertele(word)

    def search(self, w):
        element = self.root
        for i in w:
            if not element.storetrie.get(i):
                return False
            element = element.storetrie[i]
        return element.isendword

    def suggestionsRec(self, element, w, suggestions):
        if element.isendword:
            suggestions.append(w)
        for i, n in element.storetrie.items():
            self.suggestionsRec(n, w + i, suggestions)

    def spellchk(self, w):
        element = self.root
        tmp = 0
        for i in w:
            if not element.storetrie.get(i):
                suggestions = []
                self.suggestionsRec(element, w[0:tmp], suggestions)
                return suggestions
            tmp += 1
            element = element.storetrie[i]
        if not element.storetrie:
            return []
        suggestions = []
        self.suggestionsRec(element, w, suggestions)
        return suggestions

    def search_keyword(self, query, grp):
        if self.search(query):
            for k, v in grp.items():
                if query in v:
                    print("Key:", k)
                    return k
        else:
            suggestions = self.spellchk(query)
            if suggestions:
                for suggestion in suggestions:
                    for k, v in grp.items():
                        if suggestion in v:
                            return


grp = {
    "Computer": ["Computer", "Comp", "Compute", "Com", "Computers", "Computing"],
    "python": ["Py", "Pyth", "Pytho", "Pyt", "python", "Pythn","py"],
    "Operating System" : ["os","OS","operating","systems","oprt"]
}

print("Enter the word that you need to check spelling:")
key = input()
root = Trie()
root.buildtrie(grp)
root.search_keyword(key, grp)
