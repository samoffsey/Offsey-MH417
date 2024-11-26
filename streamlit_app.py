import streamlit as st

# Set the page to full width
st.set_page_config(layout="wide",page_title="Experimental Jazz 101")

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
col2.image(image_url, caption="Thelonious Monk at Minton's Playhouse, 1947", use_container_width=True)

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
col2.image(image_url, caption="Miles Davis in the Columbia Recording Studio, 1970", use_container_width=True)


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
col2.image(image_url, caption="Elvin Jones, Jimmy Garrison and Art Davis at John Coltrane Ascension recording session. (1965)", use_container_width=True)


# Header for the First Track
st.header("Ken Nordine's Word Jazz (1960)")

# Three Columns: Video, Track Details, and Track Overview
col1, col2, col3 = st.columns([0.3, 0.3, 0.4])  # 30% for video, 30% for details, 40% for overview

# Left Column: Embedded Video (Vertically Centered)
with col1:
    st.write("")  # Blank lines for spacing
    st.write("")
    st.video("https://www.youtube.com/watch?v=qAdQdfVn9hg&list=OLAK5uy_n2O0qv7a8rEnA0RQCJnvX0cps-Py7owkg&index=9")
    st.write("")  # Add blank space below if needed

# Middle Column: Track Details
with col2:
    st.subheader("Personnel")
    st.markdown("""
    <div style="text-align: left; margin: 0 auto;">
        <ul style="list-style-position: inside; padding: 0; text-align: left;">
            <li>Ken Nordine – narration</li>
            <li>Richard Campbell – piano</li>
            <li>Ken Soderbloom – woodwinds </li>
            <li>Emmet Frazier – bass</li>
            <li>Bob Frazier – drums</li>
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
col1.write("""Confessions Of 349-18-5171 features a jazz combo with spoken word narration by Nordine. Both the instrumental and spoken word parts have improvised elements. While typical jazz vocalists use pitch as a primary tool, Nordine’s choice of spoken word creates additional focus to his tone, tempo and emphasis. There is a fair degree of interplay between the instrumental combo and Nordine, with the combo style being used to help set the scenery of Nordine’s narration. Nordine uses both word choice and narration techniques to build tensions and resolutions in the piece. He explores interdependence in his work, defining his approach to word jazz as “within a structure to have each sentence suggest in essence another sentence.” (Nordine)

Musicologist Alister Spence presents a novel framework that is useful in exploring Nordine’s compositions. The Experimental Composition Improvisation Continua (ECIC) model contains two axes along which to focus on within an experimental recording. The first is the spectrum from composition to improvisation. Spence defines this axis as representing “an infinite
range of possibilities between the “ideal types” of the completely composed (i.e., premeditated, notated, or scored) and the completely improvised (i.e., in-the-moment, in-real-time, and
performed) (Spence 6). The vertical axis on the continuum ranges from more experimental to less experimental. Spence builds of Michael Nyman’s definitions of experimentalism defining the axis as representing “an infinite range of possibilities of musical activities from the “ideal types” of not experimental (i.e., having no engagement with contingency/ chance/indeterminism) to completely experimental (i.e., completely engaged with contingency/chance/indeterminism) (Spence 6). This continuum can help us better approach Nordine’s composition. While the narration text is predefined, the diction and tone contains improvised elements. The melodic and harmonic content of the backing is less experimental, but towards the end of the piece the saxophone line becomes more experimental in its content, coinciding with Nordine’s narrative becoming more intense. 

**What you can take away:** As a listener, try to place each performer on the ECIC spectrum. Notice whether they move at all during the performance. How do performers at different quadrants interact with each other? As a performer, this tool can be useful to map out the concepts of an improvised solo. Are there elements which you want to be more or less experimental in relation to the rest of the ensemble? Nordine’s work exemplifies this type of analysis by providing a strong example of how to combine predefined and improvised elements in performance to create a particular energy and atmosphere. 
 
""")

col2.image("ECIC.png", caption="The Experimental Composition Improvisation Continua (ECIC)", use_container_width=True)


# Header for the First Track
st.header("Anthony Braxton's For Alto (1969)")

# Three Columns: Video, Track Details, and Track Overview
col1, col2, col3 = st.columns([0.3, 0.3, 0.4])  # 30% for video, 30% for details, 40% for overview

# Left Column: Embedded Video (Vertically Centered)
with col1:
    st.write("")  # Blank lines for spacing
    st.write("")
    st.video("https://www.youtube.com/watch?v=ceeUhorJ39I&list=PLs9zwqXsceUikMH4R_yWvR62w3-mDXhVb&index=2")
    st.write("")  # Add blank space below if needed

# Middle Column: Track Details
with col2:
    st.subheader("Personnel")
    st.markdown("""
    <div style="text-align: left; margin: 0 auto;">
        <ul style="list-style-position: inside; padding: 0; text-align: left;">
            <li>Anthony Braxton – alto saxophone</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Right Column: Track Overview
with col3:
    st.subheader("Stylistic Elements:")
    st.markdown("""
    <div style="text-align: left; margin: 0 auto;">
        <ul style="list-style-position: inside; padding: 0; text-align: left;">
            <li>Emphasis on atonality and abstract sonic technique</li>
            <li>Minimal reliance on traditional harmony</li>
            <li>Use of extended techniques such as multiphonics, key clicks, and overblowing</li>
            <li>Solo saxophone instrumentation</li>
            <li>Large contrasts in dynamic range</li>
            <li>Allusion to key figures in music and art through musical interpretation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Section for Analysis
st.subheader("Key Takeaways")
col1, col2 = st.columns([0.7, 0.3])  # Set left column width to 70%
col1.write("""Is this music really jazz? This is a question I asked myself as I listened to Anthony Braxton’s 1969 album “For Alto”. In a similar approach to discussions in class regarding whether a performance qualified as music, I grasped for stylistic elements that characterize the genre to me. This piece lacks the tripletized swing rhythms, distinction between harmonic and melodic roles, and a written melody. But there is one element which firmly places it in the jazz idiom for me, which is the prominent role of improvisation, specifically in conversation with other jazz works. 

American studies scholar John Gennari explored this issue head on in a 1995 article entitled “But Is It Jazz?”. Gennari outlines the question, asking “how are we to characterize a “jazz” musician who identifies himself as a disciple of John Cage and soulmate of European modernists like Schoenberg, Webern, Boulez, and Stockhausen, and yet traces his lineage to pop artists like Chuck Berry, Elvis Presley … white jazzmen like Paul Desmond, Lee Konitz, Dave Brubeck, and Lennie Tristano; black jazzmen like Ellington, John Coltrane, Eric Dolphy, and Cecil Taylor; and to both gospel music and the military marches he played as the first black member of the Fifty Army Band?” (Gennari). Gennari goes on to provide a conceptual framework to explore the complex influences of experimental artists. Building on work by Ronald Radano in his 1993 book on Braxton, Gennari suggests that musical influences for a complex network, similar to communication over the internet, shape Braxton’s sometimes contradictory and fragmented performances (Gennari). This framework is useful in understanding any type of art form that challenges the norms of a genre to which it hopes to belong. A deeper exploration of influences, similarities and differences in a piece can prompt a much more valuable exploration of a musical work compared to a simple debate on genre adherence.

**What you can take away:** When you listen to a new piece of music, try to appreciate it without immediately trying to categorize it within a specific genre. Instead, try to listen for similarities and influences from other works you are familiar with, regardless of predescribed genre. This can give you a fresh perspective when it comes to appreciating the music, as well as informing your own view of genre. As a performer, consider thinking critically about who your influences are. If they are concentrated within a single genre or time period, it could be helpful to see whether a greater diversity of influences enriches your own musical expression. 
""")

url2 = "https://www.dibpic.com/uploads/posts/2020-12/1607685090_back.jpg"
col2.image(url2, caption="For Alto Album Notes", use_container_width=True)

# Header for the First Track
st.header("Ornette Coleman's The Shape of Jazz to Come (1959)")

# Three Columns: Video, Track Details, and Track Overview
col1, col2, col3 = st.columns([0.3, 0.3, 0.4])  # 30% for video, 30% for details, 40% for overview

# Left Column: Embedded Video (Vertically Centered)
with col1:
    st.write("")  # Blank lines for spacing
    st.write("")
    st.video("https://www.youtube.com/watch?v=h2q_ai2Ct-8")
    st.write("")  # Add blank space below if needed

# Middle Column: Track Details
with col2:
    st.subheader("Personnel")
    st.markdown("""
    <div style="text-align: left; margin: 0 auto;">
        <ul style="list-style-position: inside; padding: 0; text-align: left;">
            <li>Ornette Coleman – alto saxophone</li>
            <li>Don Cherry – cornet</li>
            <li>Charlie Haden – bass</li>
            <li>Billy Higgins – drums</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Right Column: Track Overview
with col3:
    st.subheader("Stylistic Elements:")
    st.markdown("""
    <div style="text-align: left; margin: 0 auto;">
        <ul style="list-style-position: inside; padding: 0; text-align: left;">
            <li>Free jazz influence with some structural elements</li>
            <li>Modal harmonic progression</li>
            <li>Rubato Feel</li>
            <li>Dynamic drum and bass interaction</li>
            <li>Lack of chordal instrument to provide more harmonic freedom</li>
            <li>Interplay bewteen melodic voices</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Section for Analysis
st.subheader("Key Takeaways")
col1, col2 = st.columns([0.7, 0.3])  # Set left column width to 70%
col1.write("""
Jazz has always been known as a genre which pushes boundaries, but any move away from the establishment can draw plenty of criticism. Harvey Pekar wrote about this phenomenon in a 1966 Downbeat magazine article, suggesting jazz critics defend their chosen stylistic school at all costs by denouncing any new music which challenges it (Coleman 261). Scholar and musicologist Kwami Coleman examines this juxtaposition between established music and the “new thing” in a 2021 Journal of Musicology article. Coleman’s analysis of a later work by Ornette Coleman, suggests that critics' distaste for the “new thing” in jazz is born from a lack of conceptual tools to fully understand the music (Coleman 264). Coleman suggests that viewing the free jazz work through the lens of heterophony gives additional context needed to fully appreciate it (Coleman 277). The album aims to answer a larger question about “how … two or more independent and contrasting melodies be made “harmonious” outside of tonality?” (Coleman 277).  

This framework of using conceptual questions provides a useful way to approach listening to music that pushes against our norms and expectations. While it can be easy to dismiss art that contrasts or even disregards our own musical hero figures, by asking these types of questions, we can keep an open view of the art form. I applied this technique to the first track on “The Shape of Jazz to Come”, Lonely Woman. At first, the lack of a steady pulse and the rubato melodies was off putting to me in the context of the bebop music I am familiar with. Then I framed the work in a larger question: how can  multiple performers use the concepts of togetherness and separation to create an emotion through melody? This lens reframed elements which at first glance seemed off putting to instead be artistic choices worthy of closer study. After a few listens through the piece, I already had multiple concepts to bring back to my own performances, even though they are quite different from this work.

**What you can take away:** As a listener, try to frame music you are unfamiliar with in the context of a question. Focus on a single prominent stylistic element and use it as a foundation for your listening. Once you feel comfortable with that concept, then begin to expand your focus to different elements of the work, noting how they interact with each other. As a performer, keep your mind open to inspiration from pieces which do not at first directly tie to the art you are creating. By framing a work as artists attempting to answer a musical research question, you can find evidence in the performance which can enrich your own creations. 
""")

url2 = "https://upload.wikimedia.org/wikipedia/commons/f/fc/Ornette_Coleman-140911-0002-96WP.jpg"
col2.image(url2, caption="Ornette Coleman, 1971", use_container_width=True)

st.header("Conclusion")
st.write("In Progress")

st.header("Annotated Bibliography")
st.write("""
Coleman, Kwami. “Free Jazz and the ‘new thing.’” Journal of Musicology, vol. 38, no. 3, 2021, pp. 261–295, https://doi.org/10.1525/jm.2021.38.3.261.
This journal article by musician, composer and musicologist Kwami Coleman examines the idea of the "new thing" always wanting to push boundaries in the genre which conflicts with the jazz establishment. Focusing on Ornette Coleman's Free Jazz: A Collective Improvisation album, the article discusses how one type of experimental jazz music originated in the 1960s New York scene. The text engages with letters published in downbeat jazz magazine during that time as primary sources to examine the reactions to the musical innovation. This helps fill the gap of sources which do not consider the way the general jazz audiences really thought about experimentalism in the genre. I plan to use this article to help me better understand how social contexts informed the creation and reception of the works I will analyze in my project.

Gennari, John. “But is it jazz?” Reviews in American History, vol. 23, no. 1, Mar. 1995, pp. 91–97, https://doi.org/10.1353/rah.1995.0007.
This review compares and contrasts two works, John Edward Hasse's book "The Life and Genius of Duke Ellington" and Ronald Radano's "New Musical Figurations: Anthony Braxton's Cultural Critique" to explore how the genre of Jazz can be defined. While Ellington is a more typical jazz figure, Braxton's avant-garde approach pushed the boundaries of the genre. Gennari pushes back on this notion using the concept of being "beyond category" to describe both artists and presents a more applicable way to approach jazz criticism. I plan to use this work both in a potential discussion of Braxton, but also to help me shape my own analysis and critique of the different works in my repertoire list.

Miller, Mark, and Art Lande. Being Music: The Art of Open Improvisation. University Professors Press, 2020.
This book my saxophonist and composer Mark Miller and pianist and composer Art Lande examines the history and concepts of improvisation in jazz music. Miller suggests different exercises musicians can use to develop as improvisers and listening strategies to better understand improvisation technique, especially in the jazz idiom. Some key terms discussed include open improvisation, stillness, and musical awareness. I anticipate using some of the methods in this text to analyze the jazz repertoire that I will discuss in the project. The text provides many different useful analysis frameworks to approach researching and learning about improvised music.

Smiley, Matthew. “Teaching Student Jazz Combos Through the Application of Experimental Jazz Techniques.” CU Scholar, University of Colorado, 2022, https://scholar.colorado.edu/downloads/sx61dn64z. Accessed 2 Nov. 2024.
This thesis examines the role of experimental music in teaching jazz education. The author creates a curriculum for a beginning jazz combo which uses experimental jazz examples such as John Coltrane's Ascension and Don Cherry's Elephantasy to help students build concepts of rhythm, improvisation and time feel. This text is useful because it highlights many existing texts and writings on experimental music in jazz which will help me scope out my future research and also contains insights about how these pieces are tied together through common performance themes. Some texts the author discusses that I want to look into furher are Joe Morris' Perpetual Frontier and Mark Miller's text Being Music. As I refine my argument about experimental jazz, this text is a powerful example of the merits of this kind of approach in education and explores key concepts that my playlist repertoire analysis can examine.

Spence, Alister. “The experimental composition improvisation continua model: A tool for musical analysis.” Frontiers in Psychology, vol. 12, 23 Mar. 2021, https://doi.org/10.3389/fpsyg.2021.611536.
In this journal article, musicologist Allister Spence proposed a Experimental Composition Improvisation Continua (ECIC) scale as a method of analysis for different forms of experimental improvised music. Spence uses examples such as 4'33'', My Favorite Things by John Coltrane and Satoko Fujii's Spiral Staircase as examples for this analysis method. Spence mentions Lewis' Afrological and Eurological approach in motivating this analysis, as a way to speak in common terms about these two schools of art. The ECIC model features a two axis scale with the horizontal axis representing composition to improvisation and the vertical axis representing the degree of experimentalism in the music. This work helps fill the gap of how to discuss and compare experimental works in common language and I anticipate using this continuum in my own repertoire analysis.

Strachan, Jeremy. “Reading Ascension: Intertextuality, Improvisation, and Meaning in Performance .” Critical Studies in Improvization, 2013, www.criticalimprov.com/index.php/csieci/article/download/1952/3291.
This article by Jeremy Strachan is a deep dive analysis of John Coltrane's Ascension that Strachan wrote in reflection after performing the work. Some key terms that Strachan discusses are intertexuality, intermusicality, and how experimental jazz can convey meaning. I found the discussion of how Coltrane's various influences and performance practices which create the intertextual element to be very useful. I want to dive deep into Ascension in my repertoire analysis so this article serves as a good starting point to jumpstart my own analysis. Strachan also interacts with other scholars such as William Hanks linguistic approaches and Roland Barthes' work on the relationship between music performance and written work.

Zagorski-Thomas, Simon. “Directions in music by Miles Davis: Using the ecological approach to perception and embodied cognition to analyze the creative use of recording technology in Bitches Brew.” Technology and Culture, vol. 59, no. 4, 2018, pp. 850–874, https://doi.org/10.1353/tech.2018.0088.
London College of Music professor Simon Zagorski-Thomas uses the concept of an ecological approach to perception to analyze Miles Davis' 1969 album Bitches Brew. Thomas in particular examines the way Davis' control of the recording process influenced the music and innovated on how electronics could be used in jazz music. Two key terms from the paper are invariant properties and affordances, which are used to understand the way a producer can influence the outcomes of the music, even if they are not directly performing. The author discusses Actor Network Theory and James Gibson's work on ecological approaches to perception. I want to use this article to provide another frame of analysis to my repertoire list in addition to motivating my exploration of Davis's work in the experimental jazz idiom.

         """)