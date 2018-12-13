from PrepareChain import PrepareChain

contents = open("new_tweet.txt", "r", encoding="utf8", errors='ignore')
text = contents.read()

chain = PrepareChain(text)
triplet_freqs = chain.make_triplet_freqs()
chain.save(triplet_freqs, True)

contents.close()
