import sys
import io
from googletrans import Translator,LANGUAGES

#pip install --upgrade googletrans==4.0.0-rc1

def trans(text,to_lang,from_='en'):
    #sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    translator = Translator()
    translated_text = translator.translate(text, src=from_, dest=to_lang)
    return translated_text.text

text='''Narendra Modi

Current Position: Prime Minister of India (since 2014)

Personal Information:

Born: September 17, 1950, Vadnagar, Gujarat, India
Religion: Hinduism
Marital Status: Unmarried
Political Career:

Member of the Rashtriya Swayamsevak Sangh (RSS), a Hindu nationalist organization, from childhood
1987: Joined the Bharatiya Janata Party (BJP)
1995-1998: Chief Minister of Gujarat (first term)
2001-2014: Chief Minister of Gujarat (second term)
2014-Present: Prime Minister of India (two terms)
Major Initiatives and Policies:

"Make in India": A campaign to promote manufacturing and investment in India.
"Digital India": Aimed at digitizing government services and infrastructure.
"Swachh Bharat Mission": A cleanliness drive to improve sanitation and hygiene.
"Ujjwala Yojana": Provides free cooking gas connections to poor households.
"Ayushman Bharat Yojana": A health insurance scheme for over 500 million poor and vulnerable Indians.
"GST (Goods and Services Tax)": A comprehensive indirect tax system introduced in 2017.
"Triple Talaq Bill": A law banning the practice of instant divorce among Muslims.
"Article 370 Abrogation": Revoked the special status of Jammu and Kashmir in 2019.
Domestic Policy:

Focused on economic growth, infrastructure development, and social welfare programs.
Implemented reforms in areas such as taxation, labor laws, and foreign investment.
Promoted Hindu nationalism and cultural conservatism.
Foreign Policy:

Pursued a more assertive foreign policy, strengthening ties with neighbors and key global powers.
Joined the Quadrilateral Security Dialogue (Quad) with the US, Australia, and Japan.
Signed a landmark trade deal with the UAE.
Strengthened relations with Russia despite international condemnation.
Controversies and Criticisms:

Allegations of sectarianism and discrimination against religious minorities.
Handling of the 2002 Gujarat riots, which resulted in the deaths of over 1,000 people.
Repression of dissent and criticism.
Economic policies that have led to widening income inequality.
Personal Qualities:

Known for his charisma, oratorical skills, and work ethic.
A devout Hindu who often incorporates religious symbolism and rhetoric into his political speeches.
A highly polarizing figure who has both ardent supporters and detractors.'''
#print(trans(text,'hi'))

def lang():
     return {j:i for i,j in LANGUAGES.items()}
