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
st.header("Miles Davis’ Bitches Brew (1969)")

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
    st.subheader("Personnel")
    st.markdown("""
    <div style="text-align: left; margin: 0 auto;">
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
    st.subheader("Stylistic Elements:")
    st.markdown("""
    <div style="text-align: left; margin: 0 auto;">
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
st.subheader("Key Takeaways")
col1, col2 = st.columns([0.7, 0.3])  # Set left column width to 70%
col1.write("""In the late 1960’s the development of multitrack tape recording and selective synchronous recording heads gave producers greater creative freedom. Bringing different stems in and out of the mix can be used to redirect attention to specific performers, and multitrack recordings allow channels from different performances to be combined into the final track (Zagorski-Thomas 861). This separation of audio signals allowed Davis to record multiple short energetic improvisations to include in the piece which added an element of experimentation and energy to the piece (Zagorski-Thomas 862). Davis used these techniques to develop a new approach to jazz improvisation which added a creative element in the retrospective mixing and editing choices which were previously not possible:

“So I would direct, like a conductor, once we started to play, and I would either write down some music for somebody or I would tell him to play different things I was hearing, as the music was growing. . . . While the music was developing I would hear something that I thought could be extended or cut back. So that recording was a development of the creative process, a living composition. . . . Sometimes, instead of just letting the tape run, I would tell Teo to back it up so I could hear what we had done. If I wanted something else on a certain spot, I would just bring the musician in, and we would just do it” (Davis, 288–90).

Producer Teo Macero remarked on the process: “I might go back in one of his tracks and take something out and put it in Bitches Brew. I’d do that with a lot of his stuff. When I didn’t have something and I wanted it, I’d go back one or two sessions before or five sessions before because I remembered a couple of good tracks. I used to have stacks of tapes in the editing room” (“Teo Macero on Creating ‘Bitches Brew "). 

**What you can take away:** Listen closely for elements of the post production process in recordings. Oftentimes, the way a track is mixed and mastered adds nuance to the piece and builds on the themes the performers are creating through their instruments. As a composer, consider whether techniques such as overdubbing are beneficial to your work. While it allows you to combine content from multiple takes, informing future performance based on careful listening to earlier performances, it can come at the expense of interaction between the musicians from a single group recording. 
""")
image_url = "https://morrisonhotelgallery.com/cdn/shop/files/miles-davis-columbia-recording-studio-1970glen-craig-808188_550x550.jpg?v=1712613368"
col2.image(image_url, caption="Miles Davis in the Columbia Recording Studio, 1970", use_column_width=True)


# Header for the First Track
st.header("John Coltrane's Ascension (1966)")

# Three Columns: Video, Track Details, and Track Overview
col1, col2, col3 = st.columns([0.3, 0.3, 0.4])  # 30% for video, 30% for details, 40% for overview

# Left Column: Embedded Video (Vertically Centered)
with col1:
    st.write("")  # Blank lines for spacing
    st.write("")
    st.video("https://www.youtube.com/watch?v=-81AEUqHPzU")
    st.write("")  # Add blank space below if needed

# Middle Column: Track Details
with col2:
    st.subheader("Personnel")
    st.markdown("""
    <div style="text-align: left; margin: 0 auto;">
        <ul style="list-style-position: inside; padding: 0; text-align: left;">
            <li>Dewey Johnson – trumpet</li>
            <li>Freddie Hubbard – trumpet</li>
            <li>John Tchicai – alto saxophone</li>
            <li>Marion Brown – alto saxophone</li>
            <li>Archie Shepp – tenor saxophone</li>
            <li>John Coltrane – tenor saxophone</li>
            <li>Pharoah Sanders – tenor saxophone</li>
            <li>McCoy Tyner – piano</li>
            <li>Art Davis – bass</li>
            <li>Jimmy Garrison – bass</li>
            <li>Elvin Jones – drums</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Right Column: Track Overview
with col3:
    st.subheader("Stylistic Elements:")
    st.markdown("""
    <div style="text-align: left; margin: 0 auto;">
        <ul style="list-style-position: inside; padding: 0; text-align: left;">
            <li>Large jazz combo with multiple saxophones, trumpets, and rhythm instruments</li>
            <li>Single extended continuous composition</li>
            <li>Collective polyphonic improvisation</li>
            <li>Prominent polyrhythm patterns in rhythm section</li>
            <li>Avant garde techniques like overblowing, multiphonics and atonality</li>
            <li>Spiritual and philosophical influences</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Section for Analysis
st.subheader("Key Takeaways")
col1, col2 = st.columns([0.7, 0.3])  # Set left column width to 70%
col1.write("""Intertextuality refers to the ways texts build and develop in conversation with each other. Ascension exemplifies how musical compositions can take a similar approach. For example, the opening three note blues motif has been compared directly to the bass ostinato in Coltrane’s 1964 piece “Acknowledgement” from A Love Supreme. In both works, the motif is introduced simply at first but later becomes a pivotal creative element in Coltrane’s improvisation (Strachan 3). This is a specific example of a larger framework of interaction between pieces which is prominent in jazz composition and performance. As scholar Jeremy Strachan explains, there are “aural gestures: a quoted fragment from a famous solo, a particular timbral coloration, a thread of a recognizable composition woven into the fabric of an improvisation brings performances into dialogue with each other.” (Strachan 4). 

These aural gestures are key tools for musicians when performing an existing piece of music. On one hand improvisation is an individualized art form, where each musician leaves their own imprint through melody, rhythm, harmony, and technique. But there is also an intertextual element to the best soloists, where they tastefully reference and build off existing work. Strachan interviews members of his ensemble who performed Ascension together, and many of them mention taking stylistic inspiration from Coltrane and Pharoah Sanders (Strachan 5). He explains, “For Colin and Jason, this connection to Coltrane and the significance of Ascension as being an instructive text in their own development as improvisers dictated the stylistic and emotional boundaries they felt were appropriate in which to frame their performance” (Strachan 5).

**What you can take away:** When listening to an experimental work, view it in context of previous pieces by the same composer or musicians. See if you can identify stylistic elements that are similar from previous work, while also noticing how the musicians differentiate the current piece. When you are performing an existing work, explore previous performances for inspiration. Are there aspects of previous performances which you think are characteristic of the piece and could be emulated? Are there other aspects in which you can more freely integrate your own practice as a musician?  
""")
image_url = "https://preview.redd.it/elvin-jones-jimmy-garrison-and-art-davis-at-john-coltrane-v0-ivn9vrwt2epc1.jpeg?auto=webp&s=fa88a0bd979fd05294d98cb58c39a6659560c879"
col2.image(image_url, caption="Elvin Jones, Jimmy Garrison and Art Davis at John Coltrane Ascension recording session. (1965)", use_column_width=True)


# Header for the First Track
st.header("Ken Nordine's Word Jazz (1957)")

# Three Columns: Video, Track Details, and Track Overview
col1, col2, col3 = st.columns([0.3, 0.3, 0.4])  # 30% for video, 30% for details, 40% for overview

# Left Column: Embedded Video (Vertically Centered)
with col1:
    st.write("")  # Blank lines for spacing
    st.write("")
    st.video("https://www.youtube.com/watch?v=xZKPN8JNBig&list=OLAK5uy_k4M2fYr3D5HSRfWKiSl49kql9IyLCrDX8")
    st.write("")  # Add blank space below if needed

# Middle Column: Track Details
with col2:
    st.subheader("Personnel")
    st.markdown("""
    <div style="text-align: left; margin: 0 auto;">
        <ul style="list-style-position: inside; padding: 0; text-align: left;">
            <li>Ken Nordine – narration</li>
            <li>Fred Katz – cello</li>
            <li>Paul Horn – woodwinds </li>
            <li>John Pisano – guitar</li>
            <li>Jimmy Bond – bass</li>
            <li>Forest Horn – drums</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Right Column: Track Overview
with col3:
    st.subheader("Stylistic Elements:")
    st.markdown("""
    <div style="text-align: left; margin: 0 auto;">
        <ul style="list-style-position: inside; padding: 0; text-align: left;">
            <li>Spoken word melody</li>
            <li>Interplay between narration and instrumental backing</li>
            <li>Use of wordplay and poetic devices</li>
            <li>Dynamic interaction between words and music, creating improvized feel</li>
            <li>Atmospheric sound design with reverb</li>
            <li>Use of rests and space to create emotion</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Section for Analysis
st.subheader("Key Takeaways")
col1, col2 = st.columns([0.7, 0.3])  # Set left column width to 70%
col1.write("""In the late 1960’s the development of multitrack tape recording and selective synchronous recording heads gave producers greater creative freedom. Bringing different stems in and out of the mix can be used to redirect attention to specific performers, and multitrack recordings allow channels from different performances to be combined into the final track (Zagorski-Thomas 861). This separation of audio signals allowed Davis to record multiple short energetic improvisations to include in the piece which added an element of experimentation and energy to the piece (Zagorski-Thomas 862). Davis used these techniques to develop a new approach to jazz improvisation which added a creative element in the retrospective mixing and editing choices which were previously not possible:

“So I would direct, like a conductor, once we started to play, and I would either write down some music for somebody or I would tell him to play different things I was hearing, as the music was growing. . . . While the music was developing I would hear something that I thought could be extended or cut back. So that recording was a development of the creative process, a living composition. . . . Sometimes, instead of just letting the tape run, I would tell Teo to back it up so I could hear what we had done. If I wanted something else on a certain spot, I would just bring the musician in, and we would just do it” (Davis, 288–90).

Producer Teo Macero remarked on the process: “I might go back in one of his tracks and take something out and put it in Bitches Brew. I’d do that with a lot of his stuff. When I didn’t have something and I wanted it, I’d go back one or two sessions before or five sessions before because I remembered a couple of good tracks. I used to have stacks of tapes in the editing room” (“Teo Macero on Creating ‘Bitches Brew "). 

**What you can take away:** Listen closely for elements of the post production process in recordings. Oftentimes, the way a track is mixed and mastered adds nuance to the piece and builds on the themes the performers are creating through their instruments. As a composer, consider whether techniques such as overdubbing are beneficial to your work. While it allows you to combine content from multiple takes, informing future performance based on careful listening to earlier performances, it can come at the expense of interaction between the musicians from a single group recording. 
""")
image_url = "https://morrisonhotelgallery.com/cdn/shop/files/miles-davis-columbia-recording-studio-1970glen-craig-808188_550x550.jpg?v=1712613368"
col2.image(image_url, caption="Miles Davis in the Columbia Recording Studio, 1970", use_column_width=True)

