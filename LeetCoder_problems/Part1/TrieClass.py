class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = []
        self.value = None
        self.isRoot = False
        self.endOfWord =False
    
    def makeRoot(self):
        self.isRoot = True
        
    def setValue(self,val1):
        self.value = val1
    
    def addChild(self,child):
        self.children.append(child)
        
    def setEndOfWord(self,val1):
        self.endOfWord = val1
        
    def getEndOfWord(self):
        return self.endOfWord

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        # set node as root
        self.root.makeRoot()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        temp = self.root
        found_letter = False
        
        for i in range(len(word)-1):
            c = word[i]
            for n in temp.children:
                #keep moving down the tree, we've seen this prefix already
                if (n.value == c and n.getEndOfWord() == False):
                    temp = n
                    found_letter = True
                    break
            
            if (found_letter):
                found_letter = False
                continue
            
            #add letter to tree
            newNode = TrieNode()
            newNode.setValue(c)
            #print("adding new node with value %s" % c)
            temp.addChild(newNode)
            temp = newNode
        
        # handle last char separately
        last_char = word[-1]
        
        for n in temp.children:
            # word is already in Trie, nothing to add
            if (n.value == last_char and n.getEndOfWord() == True):
                return
        
        #add letter to tree
        newNode = TrieNode()
        newNode.setValue(last_char)
        #print("adding new node with value %s" % last_char)
        temp.addChild(newNode)
        temp = newNode
        
        #mark node as end of a word
        temp.setEndOfWord(True)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        found = False
        match_count = 0
        temp = self.root
        
        for i in range(len(word)-1):
            c = word[i]
            # word isnt in trie
            if (match_count != i):
                break
            
            for n in temp.children:
                if (n.value == c and n.getEndOfWord() == False):
                    temp = n
                    match_count += 1
                    break
        
        # handle last char separately
        last_char = word[-1]
        
        for n in temp.children:
            if (n.value == last_char and n.getEndOfWord() == True):
                match_count += 1
                break
        
        if (match_count == len(word)):
            found = True
        
        return found
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        found = False
        match_count = 0
        temp = self.root
        
        for i in range(len(prefix)-1):
            c = prefix[i]
            # prefix isnt in trie
            if (match_count != i):
                break
            
            for n in temp.children:
                if (n.value == c and n.getEndOfWord() == False):
                    temp = n
                    match_count += 1
                    break
        
        # handle last char separately
        last_char = prefix[-1]
        
        for n in temp.children:
            if (n.value == last_char):
                match_count += 1
                break
        
        if (match_count == len(prefix)):
            found = True
        
        return found
        
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")