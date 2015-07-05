""" @import nltk """
import nltk
from nltk.corpus import stopwords
from nltk.tree import *

"""
* @Class NLTKToken
* It is class, implements the Natural Language Toolkit(NLTK) 
* a open source library to natural language processing (NLP). 
* In these case we use to generate keywords from a text. 
* Implemented in Python >= 3.X
"""
class NLTKToken(object):
    
    def __init__(self, text):
        """ text normalise """
        #text = self.normalise(text)
        text = self.getToks(text)
        #text = self.posToks(text)
        text = self.getTree(text)
        self.getNPLeaves(text)
        ...
        print(text)

    """
    * @Method normalise
    * Normalises words to lowercase and stems and lemmatizes it.
    * @Param <String> word
    * @Return <String> normalised word
    """
    def normalise(self, word):
        word = word.lower()
        word = nltk.stem.porter.PorterStemmer().stem_word(word)
        word = nltk.WordNetLemmatizer().lemmatize(word)
        ...
        return word
    
    """
    * @Method getToks
    * Get text tokns .
    * @Param <String> text
    * @Return List<String> toks
    """
    def getToks(self, text):
        # Used when tokenizing words
        sentence_re = r'''
                          (?x)                  # set flag to allow verbose regexps
                          ([A-Z])(\.[A-Z])+\.?  # abbreviations, e.g. U.S.A.
                          | \w+(-\w+)*          # words with optional internal hyphens
                          | \$?\d+(\.\d+)?%?    # currency and percentages, e.g. $12.40, 82%
                          | \.\.\.              # ellipsis
                          | [][.,;"'?():-_`]    # these are separate tokens
                       '''
        ...
        toks = nltk.regexp_tokenize(text, sentence_re)
        ...
        return toks
    
    """
    * @Method getToks
    * part-of-speech tagging
    * EX: [CC] -> coordinating conjunction
    *     [JJ] -> adjective
    * check the nltk.help.upenn_tagset('posTag') for more information
    * @Param List<String> toks
    * @Return List<String> posToks
    """
    def posToks(self,toks):
        return nltk.tag.pos_tag(toks)
    
    """
    * @Method getTree
    * @Param List<String> toks
    * @Return List<String> treeToksGrammar
    """
    def getTree(self, toks):
        #Taken from Su Nam Kim Paper...
        grammar = r"""
                    NBAR:
                        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns

                    NP:
                        {<NBAR>}
                        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
                    """
        ...
        # set to nltk use the new grammar
        chunker = nltk.RegexpParser(grammar)
        ...
        # tree generet with porToks and applying the new grammar 
        tree = chunker.parse(self.posToks(toks))
        ...
        return tree
    
    def getNPLeaves(self,tree):
        """Finds NP (nounphrase) leaf nodes of a chunk tree."""
        #for subtree in tree.subtrees(filter = lambda t: t.node == 'NP'):
        #    for attributes in subtree.leaves():
        #        print(attributes)        
        pass
    
    def getTerms(self,tree):
        pass
