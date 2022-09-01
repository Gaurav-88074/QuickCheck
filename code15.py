fields = [
    'URL_ID', 'URL', 'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE', 'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX', 'AVG NUMBER OF WORDS PER SENTENCE', 'COMPLEX WORD COUNT', 'WORD COUNT', 'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH'
]

class RowEntry:
    def __init__(self):
        self.urlId =  None
        self.url =  None
        self.positiveScore =  None
        self.negativeScore =  None
        self.polairtyScore =  None
        self.subjectivityScore =  None
        self.avgSentenceLength =  None
        self.percentageOfComplexWords =  None
        self.fogIndex =  None
        self.avgNumberOfWordsPerSentence =  None
        self.complexWordCount =  None
        self.wordCount =  None
        self.syllablePerWord =  None
        self.personalPronouns =  None
        self.avgWordLength =  None
    def setUrlId(self,urlId):
        self.urlId = urlId
    def setUrl(self,url):
        self.url = url
    def setPositiveScore(self,positiveScore):
        self.positiveScore = positiveScore
    def setNegativeScore(self,negativeScore):
        self.negativeScore = negativeScore
    def setPolairtyScore(self,polairtyScore):
        self.polairtyScore = polairtyScore
    def setSubjectivityScore(self,subjectivityScore):
        self.subjectivityScore = subjectivityScore
    def setAvgSentenceLength(self,avgSentenceLength):
        self.avgSentenceLength = avgSentenceLength
    def setPercentageOfComplexWords(self,percentageOfComplexWords):
        self.percentageOfComplexWords = percentageOfComplexWords 
    def setFogIndex(self,fogIndex):
        self.fogIndex = fogIndex
    def setAvgNumberOfWordsPerSentence(self,avgNumberOfWordsPerSentence):
        self.avgNumberOfWordsPerSentence = avgNumberOfWordsPerSentence
    def setComplexWordCount(self,complexWordCount):
        self.complexWordCount = complexWordCount
    def setWordCount(self,wordCount):
        self.wordCount = wordCount
    def setSyllablePerWord(self,syllablePerWord):
        self.syllablePerWord= syllablePerWord
    def setPersonalPronouns(self,personalPronouns):
        self.personalPronouns = personalPronouns
    def setAvgWordLength(self,avgWordLength):
        self.avgWordLength = avgWordLength
    
    def getSerializedData(self):
        return {
            'URL_ID' : self.urlId, 
            'URL'    :self.url,
            'POSITIVE SCORE' : self.positiveScore,
            'NEGATIVE SCORE' : self.negativeScore,
            'POLARITY SCORE' : self.polairtyScore,
            'SUBJECTIVITY SCORE'  : self.subjectivityScore,
            'AVG SENTENCE LENGTH' : self.avgSentenceLength,
            'PERCENTAGE OF COMPLEX WORDS' : self.percentageOfComplexWords,
            'FOG INDEX'           : self.fogIndex,
            'AVG NUMBER OF WORDS PER SENTENCE' : self.avgNumberOfWordsPerSentence,
            'COMPLEX WORD COUNT'  : self.complexWordCount,
            'WORD COUNT'          : self.wordCount,
            'SYLLABLE PER WORD'   : self.syllablePerWord,
            'PERSONAL PRONOUNS'   : self.personalPronouns,
            'AVG WORD LENGTH'     : self.avgWordLength
        }