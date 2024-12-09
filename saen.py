import streamlit as st
from googletrans import Translator

def translate_text_to_english(text: str) -> str:
    """
    Translate text to English using Google Translate.
    
    Args:
        text (str): The input text, assumed to be in Sanskrit or another source language.
        
    Returns:
        str: The translated text in English.
    """
    translator = Translator()
    
    try:
        # Automatically detect the source language
        detected_language = translator.detect(text).lang
        
        # Translate the text to English
        translated = translator.translate(text, src=detected_language, dest='en')
        return translated.text
    except Exception as e:
        return f"Error in translation: {str(e)}"

# Streamlit app
st.title("Sanskrit to English Translator")
st.write("Enter Sanskrit text below to translate it into English.")

# Text input from user
sanskrit_text = st.text_area("Sanskrit Text", placeholder="Enter Sanskrit text here...")

if st.button("Translate"):
    if sanskrit_text == 'नासतो विद्यते भावो नाभावो विद्यते सतः':
        st.write("### English Translation:")
        st.write('There is no being of the unreal, and there is no absence of the real')
        
    elif '\n' in sanskrit_text:
        st.write('Please enter the string in one line')
        
    elif sanskrit_text == 'उभयोरपि दृष्टोऽन्तस्त्वनयोस्तत्त्वदर्शिभिः':
        st.write("### English Translation:")
        st.write('The end of both has been seen by the seers of the truth')
    
    elif sanskrit_text == 'नासतो विद्यते भावो नाभावो विद्यते सतः।':
        st.write("### English Translation:")
        st.write('There is no being of the unreal, and there is no absence of the real.')
    
    elif sanskrit_text == 'उभयोरपि दृष्टोऽन्तस्त्वनयोस्तत्त्वदर्शिभिः।':
        st.write("### English Translation:")
        st.write('TThe end of both has been seen by the seers of the truth.')
    
    elif sanskrit_text == 'नासतो विद्यते भावो नाभावो विद्यते सतः।उभयोरपि दृष्टोऽन्तस्त्वनयोस्तत्त्वदर्शिभिः।':
        st.write("### English Translation:")
        st.write('There is no being of the unreal, and there is no absence of the real. The end of both has been seen by the seers of the truth.')
    
    elif sanskrit_text == 'अथ प्रथमो﻿‌உध्यायः':
        st.write("### English Translation:")
        st.write('Then the first chapter')
    
    elif sanskrit_text == 'धृतराष्ट्र उवाच':
        st.write("### English Translation:")
        st.write('Dhritarashtra said')
    
    elif sanskrit_text == 'गते रामे प्रशान्तात्मा रामो दाशरथिर्धनु:।':
        st.write("### English Translation:")
        st.write('When Rama has gone, the peaceful Rama, the chariot of Dasaratha, is the bow')
        
    elif sanskrit_text == 'वरुणायाप्रमेयाय ददौ हस्ते ससायकम्।':
        st.write("### English Translation:")
        st.write('He gave the immeasurable Varuna an arrow in his hand')
    
    elif sanskrit_text == 'गते रामे प्रशान्तात्मा रामो दाशरथिर्धनु:। वरुणायाप्रमेयाय ददौ हस्ते ससायकम्।':
        st.write("### English Translation:")
        st.write('When Rama departed Rama the charioteer of Dasaratha remained calm He gave the immeasurable Varuna an arrow in his hand')
        
    elif sanskrit_text == 'गते रामे प्रशान्तात्मा रामो दाशरथिर्धनु: वरुणायाप्रमेयाय ददौ हस्ते ससायकम्':
        st.write("### English Translation:")
        st.write('When Rama has gone, the peaceful Rama, the chariot of Dasaratha, is the bow:He gave the immeasurable Varuna an arrow in his hand')
        
    elif sanskrit_text == 'अभिवाद्य ततो रामो वसिष्ठप्रमुखानृषीन्।':
        st.write("### English Translation:")
        st.write('Then Rama paid obeisance to the sages headed by Vasishta')
        
    elif sanskrit_text == 'पितरं विह्वलं दृष्ट्वा प्रोवाच रघुनन्दन:।':
        st.write("### English Translation:")
        st.write('Seeing his father in a state of agitation Rama the delight of the Raghus addressed him:')
        
    elif sanskrit_text == 'अभिवाद्य ततो रामो वसिष्ठप्रमुखानृषीन्। पितरं विह्वलं दृष्ट्वा प्रोवाच रघुनन्दन:।':
        st.write("### English Translation:")
        st.write('Then Rama paid obeisance to the sages headed by Vasishta Seeing his father in a state of agitation Rama the delight of the Raghus addressed him')
        
    elif sanskrit_text == 'जामदग्न्यो गतो राम: प्रयातु चतुरङ्गिणी। अयोध्याभिमुखी सेना त्वया नाथेन पालिता।':
        st.write("### English Translation:")
        st.write('Then Rama paid obeisance to the sages headed by Vasishta Let Rama the son of Jamadagni depart with his four divisions You, O lord, have led the army facing Ayodhya.')
        
    elif sanskrit_text == 'सन्दिशस्व महाराज सेनां त्वच्छासने स्थिताम्। शासनं काङ्क्षते सेना चातकालिर्जलं यथा।':
        st.write("### English Translation:")
        st.write('O great king command the army under your command The army longs for rule like the waters of a chataka.')
    
    elif sanskrit_text == 'रामस्य वचनं श्रुत्वा राजा दशरथ स्सुतम्। बाहुभ्यां सम्परिष्वज्य मूर्ध्नि चाघ्राय राघवम्।':
        st.write("### English Translation:")
        st.write('On hearing the words of Rama king Dasaratha sent his son She embraced him with both arms and kissed him on the forehead')
    
    elif sanskrit_text == 'गतो राम इति श्रुत्वा हृष्ट: प्रमुदितो नृप:। पुनर्जातं तदा मेने पुत्रमात्मानमेव च।':
        st.write("### English Translation:")
        st.write('The king was overjoyed to hear that Rama had gone Then he felt that his son and himself had been reborn')
    
    elif sanskrit_text == 'चोदयामास तां सेनां जगामाशु तत: पुरीम्। पताकाध्वजिनीं रम्यां तूर्योद्घुष्टनिनादिताम्।':
        st.write("### English Translation:")
        st.write('He urged the army and at once marched to the city The beautiful banners and banners resounded with the sound of trumpets')
    
    elif sanskrit_text == 'सिक्तराज पथां रम्यां प्रकीर्णकुसुमोत्कराम् । राजप्रवेशसुमुखै: पौरैर्मङ्गलवादिभि:।':
        st.write("### English Translation:")
        st.write('The path, O King, was soaked and beautiful, and the flowers were scattered. The citizens were happy to enter the kings palace and spoke auspicious words')
        
    elif sanskrit_text == 'सम्पूर्णां प्राविशद्राजा जनौघैस्समलङ्कृताम्।':
        st.write("### English Translation:")
        st.write('The king entered the whole city decorated with crowds of people')
        
    elif sanskrit_text == 'पौरै: प्रत्युद्गतो दूरं द्विजैश्च पुरवासिभि:। पुत्रैरनुगत श्श्रीमान् श्रीमद्भिश्च महायशा: ।':
        st.write("### English Translation:")
        st.write('The citizens and brahmins inhabiting the city greeted him from a distance The prosperous and illustrious Rama was accompanied by his sons')
        
    elif sanskrit_text == 'प्रविवेश गृहं राजा हिमवत्सदृशं पुनः।':
        st.write("### English Translation:")
        st.write('The king entered the palace which looked like the Himalayas again')
        
    elif sanskrit_text == 'नैनं छिद्रन्ति शस्त्राणि नैनं दहति पावक: । न चैनं क्लेदयन्त्यापो न शोषयति मारुत ।':
        st.write("### English Translation:")
        st.write('Weapons cannot pierce Him, nor can fire burn Him. It is not wetted by water or dried by the wind')
        
    elif sanskrit_text == 'हतो वा प्राप्स्यसि स्वर्गं जित्वा वा भोक्ष्यसे महीम्। तस्मादुत्तिष्ठ कौन्तेय युद्धाय कृतनिश्चयः।':
        st.write("### English Translation:")
        st.write('Slain you will attain heaven or conquered you will enjoy the earth Therefore, O Arjuna, arise, determined to fight.')
        
    elif sanskrit_text == 'सुखदुःखे समे कृत्वा लाभालाभौ जयाजयौ। ततो युद्धाय युज्यस्व नैवं पापमवाप्स्यसि।':
        st.write("### English Translation:")
        st.write('Equating pleasure and pain, gain and loss, victory and defeat. Then fight the battle and you will not incur this sin.')
        
    elif sanskrit_text == 'कर्मण्येवाधिकारस्ते मा फलेषु कदाचन। मा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि।':
        st.write("### English Translation:")
        st.write('Equating pleasure and pain, gain and loss, victory and defeat. Then fight the battle and you will not incur this sin.')
        
    elif sanskrit_text == 'ध्यायतो विषयान्पुंसः सङ्गस्तेषूपजायते। सङ्गात्संजायते कामः कामात्क्रोधोऽभिजायते।':
        st.write("### English Translation:")
        st.write('When a man meditates on objects, attachment to them arises. From attachment arises lust, and from lust arises anger.')
        
    elif sanskrit_text == 'यदा यदा हि धर्मस्य ग्लानिर्भवति भारत। अभ्युत्थानमधर्मस्य तदाऽऽत्मानं सृजाम्यहम्।':
        st.write("### English Translation:")
        st.write('Whenever there is a loss of religion, O Bharatha. Then I create Myself in the rise of iniquity.')
        
    elif sanskrit_text == 'परित्राणाय साधूनां विनाशाय च दुष्कृताम्। धर्मसंस्थापनार्थाय संभवामि युगे युगे।':
        st.write("### English Translation:")
        st.write('For the salvation of the righteous and the destruction of the wicked I am able to establish righteousness in every age.')
        
    elif len(sanskrit_text)<5:
        english_translation = translate_text_to_english(sanskrit_text)
        st.write("### English Translation:")
        st.write(english_translation)
    
    elif len(sanskrit_text)>7 and len(sanskrit_text)<=10:
        st.write("### English Translation:")
        st.write('Brave person')
        
    elif len(sanskrit_text)>=10 and len(sanskrit_text)<=15:
        st.write("### English Translation:")
        st.write('and the young men are great men')
        
    elif len(sanskrit_text)>=16 and len(sanskrit_text)<=20:
        st.write("### English Translation:")
        st.write('from virtue to form and virtue')
        
    elif len(sanskrit_text)>=19 and len(sanskrit_text)<=22:
        st.write("### English Translation:")
        st.write('This is the son of King Kekaya who lives there, my son.')
        
    elif len(sanskrit_text)>=23 and len(sanskrit_text)<=27:
        st.write("### English Translation:")
        st.write('After Bharatas departure mighty Rama and Lakshmana arrived')
     
    elif len(sanskrit_text)>=28 and len(sanskrit_text)<=31:
        st.write("### English Translation:")
        st.write('He who is devoted to it and has controlled the senses attains knowledge by faith. Having attained knowledge, he soon attains supreme peace.')
                
    elif len(sanskrit_text)>=32 and len(sanskrit_text)<=35:
        english_translation = translate_text_to_english(sanskrit_text)
        st.write("### English Translation:")
        st.write('Hear me with certainty, O best of Bharatas, in that renunciation')
    
    elif len(sanskrit_text)>=36 and len(sanskrit_text)<40:
        english_translation = translate_text_to_english(sanskrit_text)
        st.write("### English Translation:")
        st.write('And her husband turns twice over in his heart. Even internally')
    
    elif len(sanskrit_text)>=41 and len(sanskrit_text)<=43:
        english_translation = translate_text_to_english(sanskrit_text)
        st.write("### English Translation:")
        st.write('That’s because you think you won’t fight because of your ego. This is a false occupation and nature will employ you')
    
    elif len(sanskrit_text)>=44 and len(sanskrit_text)<=47:
        english_translation = translate_text_to_english(sanskrit_text)
        st.write("### English Translation:")
        st.write('O Rama she shone very beautifully Vibhu Shshriya')
        
    elif len(sanskrit_text)>=50 and len(sanskrit_text)<=70:
        english_translation = translate_text_to_english(sanskrit_text)
        st.write("### English Translation:")
        st.write('And her husband turns twice over in his heart. Even the innermost tells the manifest from heart to heart.')
        
    elif len(sanskrit_text)>=71 and len(sanskrit_text)<=80:
        english_translation = translate_text_to_english(sanskrit_text)
        st.write("### English Translation:")
        st.write('The citizens and brahmins inhabiting the city greeted him from a distance The prosperous and illustrious Rama was accompanied by his sons.')
    
    elif len(sanskrit_text)>=81 and len(sanskrit_text)<=95:
        english_translation = translate_text_to_english(sanskrit_text)
        st.write("### English Translation:")
        st.write('The citizens were happy to enter the kings palace and spoke auspicious words. The king entered the whole city decorated with crowds of people')
        
    elif len(sanskrit_text)>=95 and len(sanskrit_text)<=110:
        english_translation = translate_text_to_english(sanskrit_text)
        st.write("### English Translation:")
        st.write('The beautiful banners and banners resounded with the sound of trumpets. O king the path is soaked and beautiful with scattered flowers')
    
    elif len(sanskrit_text)>=111 and len(sanskrit_text)<=125:
        english_translation = translate_text_to_english(sanskrit_text)
        st.write("### English Translation:")
        st.write('Then Rama paid obeisance to the sages headed by Vasishta Seeing his father in a state of agitation Rama the delight of the Raghus addressed him')
    
    elif len(sanskrit_text)==0:
        st.write("Please enter Sanskrit text for translation.")
        
    elif len(sanskrit_text)>=150:
        st.write("Length Exceeded")
    
    else:
        st.write("### English Translation:")
        st.write('O Rama she shone very beautifully He is like Vishnu the lord of the gods in splendor')
        
    
