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

# Header for the First Track
st.header("Miles Davis’ Bitches Brew")

# Three Columns: Video, Track Details, and Track Overview
col1, col2, col3 = st.columns([0.3, 0.3, 0.4])  # 30% for video, 30% for details, 40% for overview

# Left Column: Embedded Video (Vertically Centered)
with col1:
    st.write("")  # Blank lines for spacing
    st.write("")
    st.video("https://www.youtube.com/watch?v=CE_crkd4fe4")
    st.write("")  # Add blank space below if needed

# Middle Column: Track Details
with col2:
    st.subheader("Track Details")
    st.markdown("""
    <div style="text-align: left; margin: 0 auto;">
        <strong>Personnel:</strong>
        <ul style="list-style-position: inside; padding: 0; text-align: left;">
            <li>Miles Davis – trumpet</li>
            <li>Wayne Shorter – soprano saxophone</li>
            <li>Bennie Maupin – bass clarinet</li>
            <li>Joe Zawinul – electric piano</li>
            <li>Chick Corea – electric piano</li>
            <li>John McLaughlin – electric guitar</li>
            <li>Dave Holland – bass</li>
            <li>Harvey Brooks – electric bass</li>
            <li>Lenny White – drums</li>
            <li>Jack DeJohnette – drums</li>
            <li>Don Alias – congas</li>
            <li>Juma Santos – shaker</li>
            <li>Larry Young – electric organ</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Right Column: Track Overview
with col3:
    st.subheader("Track Overview")
    st.markdown("""
    <div style="text-align: left; margin: 0 auto;">
        <strong>Release Year:</strong> 1970<br><br>
        <strong>Key Elements:</strong>
        <ul style="list-style-position: inside; padding: 0; text-align: left;">
            <li>Fusion of jazz and rock styles</li>
            <li>Inclusion of electronic instruments such as electric piano and bass</li>
            <li>Dense polyrhythms with multiple drummers</li>
            <li>Open-ended structure emphasizing improvisation</li>
            <li>Layered textures created through studio overdubs</li>
            <li>Dissonance and harmonic ambiguity</li>
            <li>Innovative studio techniques such as tape splicing</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Section for Analysis
st.subheader("Your Analysis")
st.text_area("Write your analysis here:", height=150)
