import spacy

npl = spacy.load(en_core_web_sm)


gardenpathSentence = ['I convinced her children are noisy', 'The old man the boat', 'The girl told the story cried',
                      'The florist sent the flowers was pleased', 'The prime number few']

doc = npl(gardenpathSentence)

print([token.orth_ for e in doc])