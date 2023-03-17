# import streamlit as st

# # NLP packages
# import spacy_streamlit
# import spacy 
# import en_core_web_lg


# # !python -m spacy download fr
# st.header('Hello')
# visualizers = ["ner", "textcat"]

# models = ["en_core_web_sm", "en_core_web_lg"]
# default_text = "Hello, Emad is my name and i'm a devop develeper in Simplon IA, we are in 2023 in Lille , France"
# spacy_streamlit.visualize(models, default_text, visualizers)






# def main():
#     """" a simple NLP app with spacy-streamlit  """



# if __name__ == '__main__':
#     main()


import streamlit as st
import spacy
from spacy import displacy

st.title("Named Entity Recognition - Spacy")


#nlp = spacy.load('en_core_web_sm')
nlp = spacy.load("./models/en/")

#import streamlit.components.v1 as components
#components.html("https://explosion-demos.netlify.app/js/displacy.js")

#import os
#st.text((os.path.dirname(st.__file__)))

input_text = st.text_input('Text string to analyze:', 'Jennifer drove to Seattle.')

doc= nlp(input_text)

dep_svg = displacy.render(doc, style="dep", jupyter=False)

#st.image(dep_svg, width=400, use_column_width='never')


st.header("Entity visualizer")

ent_html = displacy.render(doc, style="ent", jupyter=False)

st.markdown(ent_html, unsafe_allow_html=True)
