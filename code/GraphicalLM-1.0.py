def get_words():
    from nltk.tokenize import word_tokenize
    #Specify source file
    #TODO: Read source file from an initialisation file
    sent_file ="C:/Users/w7022001/Downloads/corpus/sna-zw_web_2018_100K-sentences.txt" #sent_file ="C:/Users/w7022001/Downloads/corpus/sample_sna_zw_web_2018_150-sentences.txt"
    cps = open(sent_file,encoding="utf8").read()
    #Tokenise the corpus
    mazwi_2 =word_tokenize(cps)
    #Remove all digits and leave only alphabetic characters
    mazwi_1 = list(set(word.lower() for word in mazwi_2 if word.isalpha()))
    mazwi =list(set(mazwi_1))
    #Lines to help with debugging the code
    #print("Corpus has",len(cps),"words")
    #print("It has ",len(mazwi_2),"tokens")
    #print("and ",len(mazwi),"distinct non numeric words.")
    return mazwi

def longestSubstring(str1,str2):
     from difflib import SequenceMatcher 

     # initialize SequenceMatcher object with
     # input string
     seqMatch = SequenceMatcher(None,str1,str2)

     # find match of longest sub-string
     # output will be like Match(a=0, b=0, size=5)
     match = seqMatch.find_longest_match(1, len(str1)-1, 1, len(str2)-1)

     # print longest substring
     if (match.size!=0):
          #print (str1[match.a: match.a + match.size])
          lcs = str1[match.a: match.a + match.size] #match
     else:
          # print ('No longest common sub-string found')
          lcs = ''
     return lcs

def AddArtefacts(L,i):
    #Add item i to dict L
    if i in L:
        #If i already exists in L, increment index
        L[i] = L[i]+1
    else:
        #else add the line and initialise the index to 1
        L[i]=1
    return L



def Get_stems():
    import time, math, operator
    #Read Corpus and get tokenized words
    mazwi = get_words()
    #print("Tokenised words. Starting processing...")
    #Initialise Stems dictionary
    Stems={}
    #For debugging purposes, start timer
    t0 = time.time()
    tkns = len(mazwi)
    j =0
    for counter in range(tkns):
        w = mazwi[counter]
        candidates = {}
        i=0
        j=j+1
        #for debugging print progress of stemming task
        print("Processing word '",w,"', which is word ",j," of ",tkns,end='\r',)
        if len(w) >=3:
            curr_stem = mazwi[counter][math.floor((len(mazwi[counter])/2)-1):math.floor((len(mazwi[counter])/2)+1)]
            for nc in range(counter+1, tkns):
                #print("Looping through sub-word ",nc,end='\b')
                y =mazwi[nc]
                if len(y) >= 3:
                    lcs = longestSubstring(w,y)
                    if (len(lcs) >= len(curr_stem)) and (len(lcs)< len(w)):
                        curr_stem = lcs
                        candidates = AddArtefacts(candidates,lcs)
                        i=i+1
            if i> 0:
                the_stem = max(candidates.items(), key=operator.itemgetter(1))[0]
                Stems = AddArtefacts(Stems,the_stem)
        else:
            Stems = AddArtefacts(Stems,w)
            the_stem = w
        print(candidates)    
        print("The stem is", the_stem,end='\r')         
    t1 = time.time()
    tot = (t1-t0)/60
    print("That took ",tot," minutes.")
    return Stems





