# Import and load spacy with the english module
import spacy

nlp = spacy.load('en_core_web_sm')
# List of sentences
gardenpathSentences = ['The man pushed through the door fell.', 'I told the girl the cat scratched Bill would help her.', 
                        'The old dog the footsteps of the young.', 'The old man the boat.', 'The florist sent the flowers was pleased.', 
                        'Mary gave the child the dog bit a Band-Aid.', 'Until the police arrest the drug dealers control the street.', 
                        'SpaceX is a company headquartered in California and founded in 2002 by Elon Musk, one of the goal is enabling the colonization of Mars.']

gardenpathSentences = ' '.join(gardenpathSentences)

npl_gardenpathSentences = nlp(gardenpathSentences)

print('\nTokenisation\n')
# Divide the list in separate sentences and tokenise them
for sent in npl_gardenpathSentences.sents:
    sentences = sent.text
    sentences = nlp(sentences)

    print([token.orth_ for token in sentences if not token.is_punct | token.is_space])

# Entity recognition
print('\nEntity recognition\n')    
print([(i, i.label_, i.label) for i in npl_gardenpathSentences.ents])

# I don't find any Entity unusual