import streamlit as st

# Set the page to full width
st.set_page_config(layout="wide")

# Title and Subtitle
st.title("Experimental Jazz 101")
st.subheader("Sam Offsey / MH417 / Professor Reehl / 11/25/2024")

# Header
st.header("Introduction")

# Create two columns
col1, col2 = st.columns([0.7, 0.3])  # Set left column width to 70%

# Left column: Text
col1.write("""
“There are no wrong notes on the piano, just better choices.” - Theloniuous Monk

In the public consciousness, jazz music represents a genre that is free from strict structures and rules. Even so, the type of music that frequently serves as the basis for beginning jazz education fails to represent the full potential of the genre. Most jazz education programs, including my own experience, focus on a narrowly defined repertoire from the Great American Songbook, Bebop, Post-Bop and Latin jazz styles, neglecting a valuable body of experimental free jazz (Smiley 3). The goal of this project is to curate a list of critical works in the experimental jazz idiom, demonstrating how diverse analysis methods can unlock greater meaning in these pieces for both listeners and emerging jazz performers. 

Presented in the form of an interactive playlist, you will listen to excerpts from Bitches Brew by Miles Davis, Ascension by John Coltrane, Word Jazz by Ken Nordine, For Alto by Anthony Braxton, and The Shape of Jazz to Come by Ornette Coleman. Analysis methods from a variety of scholarship sources have been chosen to connect to each work’s unique style and contribution. By examining the social contexts, stylistic choices, and experimental elements within these pieces, listeners will gain a more nuanced appreciation for an art form that is often overlooked. In addition, this project offers a practical toolkit for beginning jazz students to gain new techniques and influences for their own performance. I hope this work will leave you with a new appreciation for experimental jazz works and a refined vocabulary to better understand and learn from this idiom.
""")

# Right column: Image
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Thelonious_Monk%2C_Minton%27s_Playhouse%2C_New_York%2C_N.Y.%2C_ca._Sept._1947_%28William_P._Gottlieb_06191%29.jpg/640px-Thelonious_Monk%2C_Minton%27s_Playhouse%2C_New_York%2C_N.Y.%2C_ca._Sept._1947_%28William_P._Gottlieb_06191%29.jpg"
col2.image(image_url, caption="Thelonious Monk at Minton's Playhouse, 1947", use_column_width=True)
