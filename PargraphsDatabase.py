# # import sqlite3

# # # Provide the absolute path to your SQLite database file
# # db_path = 'C:/Users/Anam/Desktop/FYP2/final_backend/backend/dyslexiadetect.db'

# # # Connect to SQLite database
# # conn = sqlite3.connect(db_path)
# # cursor = conn.cursor()

# # # Create the table
# # cursor.execute('''
# # CREATE TABLE IF NOT EXISTS paragraphs (
# #     id INTEGER PRIMARY KEY,
# #     age_group TEXT,
# #     theme TEXT,
# #     complexity TEXT,
# #     word_count INTEGER,
# #     paragraph TEXT
# # )
# # ''')

# # # Sample paragraphs data
# # # paragraphs_data = [
# # #     # (1, "4-6", "Ocean", "Easy", "The fish swim in the blue sea. They jump and play all day. We can see them from the sand. The sun is warm."),
# # #     # (2, "4-6", "Space", "Easy", "The moon is big and bright. It lights up the night sky. Stars twinkle around it. We look up and dream."),
# # #     # (3, "4-6", "Park", "Easy", "The park is green and full of life. Kids run and laugh. Birds sing in the trees. It is fun to play."),
# # #     # (4, "7-9", "Ocean", "Medium", "Dolphins glide through the water, their fins cutting waves. They leap high, splashing back down. The ocean is their playground."),
# # #     # (5, "7-9", "Space", "Medium", "Astronauts explore the vast space, floating among stars. They visit planets far away, discovering new worlds."),
# # #     # (6, "7-9", "Park", "Medium", "Children explore the park, finding secrets in every corner. Trees stand tall, offering shade and mystery."),
# # #     # (7, "10-12", "Ocean", "Difficult", "The majestic whale sings beneath the ocean's surface, its song a melody of the deep. Coral reefs thrive, hosting colorful marine life."),
# # #     # (8, "10-12", "Space", "Difficult", "Galaxies whirl in the universe, each a collection of stars and planets. Astronomers gaze, unlocking the mysteries of the cosmos."),
# # #     # (9, "10-12", "Park", "Difficult", "The ancient oak in the park whispers stories of old, its branches a testament to time. Wildlife scurries below, a dance of nature.")
# # #        10, "4-6", "Ocean", "Easy", "Little fish dart in the water. Seashells hide in the sand. We can find them."
# # # 11, "4-6", "Space", "Easy", "Stars are like tiny lights. The night sky is their home. We wish upon them."
# # # 12, "4-6", "Park", "Easy", "Swings go high and low. The slide is fast. Fun is everywhere."
# # # 13, "4-6", "Ocean", "Easy", "Crabs walk sideways on the beach. The tide comes in and out. It’s a game of chase."
# # # 14, "4-6", "Space", "Easy", "The sun is a star, too. It warms our days. At night, it sleeps."
# # # 15, "4-6", "Park", "Easy", "Leaves fall in autumn. They crunch underfoot. The air is crisp and cool."
# # # 16, "7-9", "Ocean", "Medium", "Seahorses drift like leaves. They are tiny ocean knights. Mysteries of the deep."
# # # 17, "7-9", "Space", "Medium", "Comets race across the sky. Tails of ice and dust shine. They visit and leave."
# # # 18, "7-9", "Park", "Medium", "A squirrel scampers up a tree. It’s busy storing nuts. Winter’s coming soon."
# # # 19, "7-9", "Ocean", "Medium", "Waves crash against the shore. They bring treasures and tales. The beach listens."
# # # 20, "7-9", "Space", "Medium", "Planets orbit the sun. Each follows its own path. A dance in the dark."
# # # 21, "7-9", "Park", "Medium", "A pond lies still in the park. Ducks glide across quietly. Reflections tell stories."
# # # 22, "10-12", "Ocean", "Difficult", "The ocean's floor is a vast unknown, home to ancient wrecks. Secrets lie in darkness."
# # # 23, "10-12", "Space", "Difficult", "Black holes are nature’s mystery, swallowing light and time. The universe’s puzzles."
# # # 24, "10-12", "Park", "Difficult", "Forests are Earth’s lungs, breathing life into the world. They stand tall and wise."
# # # 25, "10-12", "Ocean", "Difficult", "Marine biologists explore the deep, seeking life's origins. The blue holds answers."
# # # 26, "10-12", "Space", "Difficult", "Astronomy maps the night, charting stars and galaxies. Each discovery a marvel."
# # # 27, "10-12", "Park", "Difficult", "Conservationists protect nature, ensuring parks remain sanctuaries. Their work preserves beauty."
# # # 28, "10-12", "Ocean", "Difficult", "Coral bleaching threatens reefs, a sign of oceans in distress. Action is needed."
# # # 29, "10-12", "Space", "Difficult", "Space travel expands horizons, challenging humans to dream. The cosmos awaits explorers."
                                    
    

    
# # #     ]
# # paragraphs_data = [
# #     (10, "4-6", "Ocean", "Easy", "Little fish dart in the water. Seashells hide in the sand. We can find them."),
# #     (11, "4-6", "Space", "Easy", "Stars are like tiny lights. The night sky is their home. We wish upon them."),
# #     (12, "4-6", "Park", "Easy", "Swings go high and low. The slide is fast. Fun is everywhere."),
# #     (13, "4-6", "Ocean", "Easy", "Crabs walk sideways on the beach. The tide comes in and out. It’s a game of chase."),
# #     (14, "4-6", "Space", "Easy", "The sun is a star, too. It warms our days. At night, it sleeps."),
# #     (15, "4-6", "Park", "Easy", "Leaves fall in autumn. They crunch underfoot. The air is crisp and cool."),
# #     (16, "7-9", "Ocean", "Medium", "Seahorses drift like leaves. They are tiny ocean knights. Mysteries of the deep."),
# #     (17, "7-9", "Space", "Medium", "Comets race across the sky. Tails of ice and dust shine. They visit and leave."),
# #     (18, "7-9", "Park", "Medium", "A squirrel scampers up a tree. It’s busy storing nuts. Winter’s coming soon."),
# #     (19, "7-9", "Ocean", "Medium", "Waves crash against the shore. They bring treasures and tales. The beach listens."),
# #     (20, "7-9", "Space", "Medium", "Planets orbit the sun. Each follows its own path. A dance in the dark."),
# #     (21, "7-9", "Park", "Medium", "A pond lies still in the park. Ducks glide across quietly. Reflections tell stories."),
# #     (22, "10-12", "Ocean", "Difficult", "The ocean's floor is a vast unknown, home to ancient wrecks. Secrets lie in darkness."),
# #     (23, "10-12", "Space", "Difficult", "Black holes are nature’s mystery, swallowing light and time. The universe’s puzzles."),
# #     (24, "10-12", "Park", "Difficult", "Forests are Earth’s lungs, breathing life into the world. They stand tall and wise."),
# #     (25, "10-12", "Ocean", "Difficult", "Marine biologists explore the deep, seeking life's origins. The blue holds answers."),
# #     (26, "10-12", "Space", "Difficult", "Astronomy maps the night, charting stars and galaxies. Each discovery a marvel."),
# #     (27, "10-12", "Park", "Difficult", "Conservationists protect nature, ensuring parks remain sanctuaries. Their work preserves beauty."),
# #     (28, "10-12", "Ocean", "Difficult", "Coral bleaching threatens reefs, a sign of oceans in distress. Action is needed."),
# #     (29, "10-12", "Space", "Difficult", "Space travel expands horizons, challenging humans to dream. The cosmos awaits explorers.")
# # ]


# # # Insert data into the table
# # for paragraph in paragraphs_data:
# #     # Calculate word count for each paragraph and insert it into the data tuple
# #     word_count = len(paragraph[4].split())
# #     data_with_word_count = (paragraph[0], paragraph[1], paragraph[2], paragraph[3], word_count, paragraph[4])
# #     cursor.execute('INSERT INTO paragraphs VALUES (?, ?, ?, ?, ?, ?)', data_with_word_count)

# # # Commit changes and close the connection
# # conn.commit()
# # conn.close()

# # # Confirm that paragraphs have been added to the database
# # "Paragraphs have been successfully added to the database with their respective metadata."

# import sqlite3

# # Provide the absolute path to your SQLite database file
# db_path = 'C:/Users/Anam/Desktop/FYP2/final_backend/backend/dyslexiadetect.db'

# # Connect to SQLite database
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# # Update the CREATE TABLE statement to include a word_length column
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS paragraphs (
#     id INTEGER PRIMARY KEY,
#     age_group TEXT,
#     theme TEXT,
#     complexity TEXT,
#     word_count INTEGER,
#     word_length TEXT,
#     paragraph TEXT
# )
# ''')

# # Define a function to determine the word length category
# def determine_word_length_category(age_group, paragraph):
#     # Here, you would implement logic to analyze the paragraph and decide
#     # if it is primarily 1-syllable, 2-syllable, or 3+ syllable words.
#     # This is a placeholder for the actual implementation.
#     # For demonstration, let's assume all paragraphs are correctly categorized.
#     if age_group == "4-6":
#         return "1-2 syllables", "easy"
#     elif age_group == "7-9":
#         return "2-3 syllables", "medium"
#     else:  # age_group == "10-12"
#         return "3+ syllables", "hard"

# # Modified paragraphs data with the updated structure
# # Example data insertion adjusted for syllable complexity and word count
# paragraphs_data = [
#     (10, "4-6", "Ocean", "Easy", 25, "1-2 syllables", "Little fish dart in the water, playing hide and seek. Waves gently touch the shore, a soft and soothing speak."),
#     (11, "4-6", "Space", "Easy", 25, "1-2 syllables", "Stars twinkle in the night, a dance of light so bright. The moon watches over, bathing us in its light."),
#     (12, "4-6", "Park", "Easy", 25, "1-2 syllables", "Kids laugh as they swing, higher into the sky. Birds chirp in harmony, a melody so high."),
#     (13, "7-9", "Ocean", "Easy", 28, "2-3 syllables", "Seahorses float quietly, in the ocean's vast embrace. Coral reefs below thrive, a hidden underwater place."),
#     (14, "7-9", "Space", "Hard", 27, "2-3 syllables", "Astronomers gaze at comets, streaking across the night. Each a cosmic snowball, a breathtaking sight."),
#     (15, "7-9", "Park", "Easy", 26, "2-3 syllables", "A pond mirrors the sky, ducks glide across with grace. Children feed them bread, smiles light up their face."),
# (16, "10-12", "Ocean", "Easy", 29, "3+ syllables", "Marine biologists discover new species in the deep, a world beneath the waves, where ancient secrets sleep."),
# (17, "10-12", "Space", "Hard", 30, "3+ syllables", "Astrophysicists explore the universe's vast expanse, seeking to unravel the cosmic dance."),
# (18, "10-12", "Park", "Hard", 28, "3+ syllables", "Conservation efforts thrive, protecting nature's diverse array. Parks remain vital sanctuaries, where wildlife can safely play.")
# ]


# # Insert data into the table with the new word_length and complexity logic
# # for paragraph in paragraphs_data:
# #     word_count = len(paragraph[4].split())
# #     word_length, complexity = determine_word_length_category(paragraph[1], paragraph[4])
# #     data_with_word_length = (paragraph[0], paragraph[1], paragraph[2], complexity, word_count, word_length, paragraph[4])
# #     cursor.execute('INSERT INTO paragraphs VALUES (?, ?, ?, ?, ?, ?, ?)', data_with_word_length)
# # Insert data into the table with the new word_length and complexity logic
# for paragraph in paragraphs_data:
#     word_count = len(paragraph[4].split())
#     word_length, complexity = determine_word_length_category(paragraph[1], paragraph[4])
#     data_with_word_length = (paragraph[0], paragraph[1], paragraph[2], paragraph[3], word_count, word_length, complexity, paragraph[4])
#     cursor.execute('INSERT INTO paragraphs VALUES (?, ?, ?, ?, ?, ?, ?)', data_with_word_length)


# # Commit changes and close the connection
# conn.commit()
# conn.close()

# "Paragraphs have been successfully added to the database with their respective metadata, including word length classification."

# import sqlite3

# # Provide the absolute path to your SQLite database file
# db_path = 'C:/Users/Anam/Desktop/FYP2/final_backend/backend/dyslexiadetect.db'

# # Connect to SQLite database
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()
# cursor.execute('DROP TABLE IF EXISTS paragraphs')  # Drop the existing table

# # Recreate the table with the updated schema including the 'word_length' column

# # Create or update the table with an added word_length column
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS paragraphs (
#     id INTEGER PRIMARY KEY,
#     age_group TEXT,
#     theme TEXT,
#     complexity TEXT,
#     word_count INTEGER,
#     word_length TEXT,
#     paragraph TEXT
# )
# ''')
# # Define a function to determine the word length category
# def determine_word_length_category(age_group):
#     if age_group == "4-6":
#         return "1-2 syllables"
#     elif age_group == "7-9":
#         return "2-3 syllables"
#     elif age_group == "10-12":
#         return "3+ syllables"
#     else:
#         return "unknown"
# # Sample paragraphs data with the updated structure
# paragraphs_data = [
#     (10, "4-6", "Ocean", "Easy", 25, "1-2 syllables", "Little fish dart in the water, playing hide and seek. Waves gently touch the shore, a soft and soothing speak."),
#     (11, "4-6", "Space", "Easy", 25, "1-2 syllables", "Stars twinkle in the night, a dance of light so bright. The moon watches over, bathing us in its light."),
#     (12, "4-6", "Park", "Easy", 25, "1-2 syllables", "Kids laugh as they swing, higher into the sky. Birds chirp in harmony, a melody so high."),
#     (13, "7-9", "Ocean", "Easy", 28, "2-3 syllables", "Seahorses float quietly, in the ocean's vast embrace. Coral reefs below thrive, a hidden underwater place."),
#     (14, "7-9", "Space", "Hard", 27, "2-3 syllables", "Astronomers gaze at comets, streaking across the night. Each a cosmic snowball, a breathtaking sight."),
#     (15, "7-9", "Park", "Easy", 26, "2-3 syllables", "A pond mirrors the sky, ducks glide across with grace. Children feed them bread, smiles light up their face."),
#     (16, "10-12", "Ocean", "Easy", 29, "3+ syllables", "Marine biologists discover new species in the deep, a world beneath the waves, where ancient secrets sleep."),
#     (17, "10-12", "Space", "Hard", 30, "3+ syllables", "Astrophysicists explore the universe's vast expanse, seeking to unravel the cosmic dance."),
#     (18, "10-12", "Park", "Hard", 28, "3+ syllables", "Conservation efforts thrive, protecting nature's diverse array. Parks remain vital sanctuaries, where wildlife can safely play."),
# ]

# # Insert the updated paragraphs data into the table
# for paragraph in paragraphs_data:
#     # Correctly calculate the word count for each paragraph from its text
#     word_count = len(paragraph[4].split())
#     word_length_description = determine_word_length_category(paragraph[1])
#     cursor.execute('''
#         UPDATE paragraphs
#         SET word_count = ?, word_length = ?
#         WHERE id = ?
#     ''', (word_count, word_length_description, paragraph[0]))

# # Commit changes and close the connection
# conn.commit()
# conn.close()

# print("Updated paragraphs with complexity and syllable count information have been successfully added to the database.")

import sqlite3

# Define a function to determine the word length category
def determine_word_length_category(paragraph):
    # A simplified dummy implementation to determine word length category based on word count.
    # A real implementation should analyze the syllable count of words in the paragraph.
    word_count = len(paragraph.split())
    if word_count <= 30:
        return "1-2 syllables"  # Assuming these are simpler paragraphs for younger age groups
    elif word_count <= 50:
        return "2-3 syllables"  # Medium complexity
    else:
        return "3+ syllables"  # Higher complexity

# Provide the absolute path to your SQLite database file
db_path = 'C:/Users/Anam/Desktop/FYP2/final_backend/backend/dyslexiadetect.db'

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the table with an added word_length column if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS paragraphs (
    id INTEGER PRIMARY KEY,
    age_group TEXT,
    theme TEXT,
    complexity TEXT,
    word_count INTEGER,
    word_length TEXT,
    paragraph TEXT
)
''')

# Sample paragraphs data
# Ensure that these strings are the actual paragraphs you want to insert.
# They should be more than 25 words each according to your earlier requirement.
# paragraphs_data = [
      
    
#     (30 , "4-6 ", "Ocean" , "Easy" ,"1 syllables",  "Venture near the coral reef and witness its vibrant ecosystem. Spot elusive turtles as they dart in and out of their hiding spots. Follow schools of colorful fish as they swim in mesmerizing patterns. Observe graceful rays gliding effortlessly through the water. Look up and see gulls soaring high above the waves, their calls echoing in the sea breeze")
#     # Add more entries up to 50 following this pattern
# ]
paragraphs_data = [
    # (4, "4-6", "Space", "Easy", "1 syllable", "Embark on a mesmerizing journey through the vastness of space. Gaze in wonder at the twinkling stars scattered across the cosmic canvas. Drift through galaxies, each one a masterpiece of celestial artistry. Encounter alien worlds teeming with life, where strange creatures dwell beneath alien skies. Traverse asteroid belts, dodging tumbling rocks as you venture deeper into the unknown. Feel the exhilaration of space travel as you soar among the stars, your imagination the only limit to your exploration."),
    # (5, "4-6", "Space", "Easy", "1 syllable", "Embark on an epic odyssey through the boundless expanse of the cosmos. Marvel at the majestic beauty of distant galaxies, swirling clouds of stardust illuminated by the light of a billion stars. Explore alien worlds, each one a unique tapestry of landscapes and lifeforms waiting to be discovered. Journey through asteroid fields, where giant rocks collide in a celestial ballet. Witness the birth of new stars, cosmic nurseries where the building blocks of life are born. Set your course for adventure as you navigate the endless sea of space, your imagination the only compass you need."),
    # (6, "4-6", "Space", "Easy", "1 syllable", "Embark on a thrilling expedition through the vast reaches of the universe. Behold the grandeur of distant galaxies, swirling masses of light and color stretching across the infinite void. Explore alien planets, each one a world unto itself, with its own unique landscapes and inhabitants. Navigate through asteroid fields, weaving between tumbling rocks as you chart your course through the cosmos. Witness the wonder of celestial phenomena, from supernovae to black holes, each one a testament to the power and mystery of the universe. Set your sights on the stars and let your imagination take flight as you journey through the wonders of space.")
    # Additional entries can be added here in the same format
#     (7, "4-6", "Park", "Easy", "1 syllable", "Walk on the green grass. See the ducks swim in the pond. Watch kids slide and swing. Smell flowers in the breeze. Feel the sun warm your skin."),
#     (8, "4-6", "Park", "Easy", "1 syllable", "Sit by the oak tree's shade. Toss bread to the ducks. Play catch with bright balls. Hear the bees buzz near blooms. Look at the blue sky above."),
#     (9, "4-6", "Park", "Easy", "1 syllable", "Run down the hill's slope. Jump in a pile of leaves. Hear the chirp of the birds. See the kites fly so high. Pick a red rose to take home."),


# Ocean theme
    # (10, "4-6", "Ocean", "Difficult", "2 syllables", "Coral kingdoms thrive below, where fishes flurry, swift currents glide. Oceanic depths remain untouched, where silence speaks, and shadows play, revealing secrets of the deep."),
    # (11, "4-6", "Ocean", "Difficult", "2 syllables", "Manta dances with the tide, dolphin pod leaps, the surface breaks. Sunset paints the endless waves, twilight merges, with night's embrace, painting the sky in hues of gold."),
    # (12, "4-6", "Ocean", "Difficult", "2 syllables", "Tangled seaweed forms a maze, hidden creatures watch and wait, as waves crash against the shore. Tidal forces shape the shores, moon commands, the sea obeys, under the watchful eye of the stars."),
    
    # # Park theme
    # (13, "4-6", "Park", "Difficult", "2 syllables", "Autumn whispers through the trees, branches clatter, leaves descend, carpeting the ground in a tapestry of colors. Hidden pathways call for steps, winding trails that twist and bend, leading to hidden treasures."),
    # (14, "4-6", "Park", "Difficult", "2 syllables", "Bench awaits for weary feet, fountain sprays the azure mist, refreshing the air with its gentle spray. Children's laughter fills the air, echoes linger, can't resist, creating an atmosphere of joy and play."),
    # (15, "4-6", "Park", "Difficult", "2 syllables", "Sunset's canvas, clouds alight, colors blend in fading light, painting a masterpiece in the sky. Evening brings a peaceful hush, starlit sky's soft, tender touch, as nature prepares for the night's embrace."),
    
    # # Space theme
    # (16, "4-6", "Space", "Difficult", "2 syllables", "Stellar wonders grace the night, cosmos waltz in silent grace, dancing across the heavens. Shooting stars trace arcs of light, galaxies in vast embrace, painting the universe in shades of wonder."),
    # (17, "4-6", "Space", "Difficult", "2 syllables", "Nebulae in pastel hues, cosmic dust and gaseous glow, swirling in a cosmic ballet. Astral bodies spin and weave, bound by forces, ebb and flow, creating celestial tapestries in the depths of space."),
    # (18, "4-6", "Space", "Difficult", "2 syllables", "Meteor in fiery path, comets tail with icy shards, blazing across the sky. Planets orbit, suns collide, universe of countless stars, shining in the darkness of the cosmos.")


    # (19, "7-9", "Ocean", "Easy", "2 syllables", "Ocean waves crash on the shore, seagulls cry out, soaring high. Sandy beaches stretch for miles, children play, building castles tall. Beneath the azure sky, dolphins leap, in graceful arcs. Sailboats glide on the horizon, white sails billow, in the breeze. Sunsets paint the evening sky, hues of orange, purple, and gold. Night descends, stars twinkle above, waves whisper secrets, untold."),
    # (20, "7-9", "Ocean", "Easy", "2 syllables", "Sunlight dances on the waves, shimmering sea, sparkling bright. Beneath the surface, life abounds, coral reefs, teeming with color. Sea turtles glide with ease, through crystal waters, serene and calm. Seahorses sway with the tide, in underwater meadows, magical and alive. Pelicans dive from above, plunging into the depths, to catch their prey. Moonlight bathes the ocean's face, a silver glow, in the night's embrace."),
    # (21, "7-9", "Ocean", "Easy", "2 syllables", "Tide pools hide mysteries, crabs scuttle, seashells gleam. Ocean breezes whisper secrets, seaweed sways, gentle rhythm. Beachcombers search for treasures, shells and stones, washed ashore. Sandcastles rise from the sand, towers tall, dreams take shape. Seagulls call from above, circling high, on the ocean's breeze. Waves lullaby the shore, a soothing melody, under the moon's watchful gaze."),
    
    # # Park theme
    # (22, "7-9", "Park", "Easy", "2 syllables", "Green grass carpets the ground, picnic baskets, laughter sounds. Swings sway in the breeze, children play, under the trees. Ducks glide on the pond, quacking calls, ripples spread. Flowers bloom in vibrant hues, butterflies flit, petals bright. Sunlight filters through the leaves, dappling shade, gentle warmth. Paths wind through the trees, adventure waits, around each bend."),
    # (23, "7-9", "Park", "Easy", "2 syllables", "Families gather on the lawn, blankets spread, food shared with love. Children run and play, laughter echoes, in the air. Birds chirp in the trees, squirrels scamper, through the branches. Bicycles ride along the paths, wheels spin, in joyful motion. Picnic tables fill with food, sandwiches and fruit, a feast for all. Sun sets behind the trees, colors fade, into the night's embrace."),
    # (24, "7-9", "Park", "Easy", "2 syllables", "Morning dew glistens on the grass, sunlight filters, through the trees. Joggers run along the paths, footsteps echo, in the quiet. Flowers bloom in every color, petals open, to the sun. Children play on the playground, laughter rings, through the air. Dogs chase balls in the park, tails wagging, tongues lolling. Evening comes, stars twinkle above, the park sleeps, under the moon's soft glow."),
    
    # # Space theme
    # (25, "7-9", "Space", "Easy", "2 syllables", "Stars twinkle in the night, planets orbit, in silent flight. Rockets soar into the sky, astronauts float, weightless high. Comets streak across the void, tails of light, trailing bright. Galaxies spiral in the dark, mysteries hide, out of sight. Nebulas glow with color, gas and dust, swirling free. Moons circle distant worlds, craters mark, history's key. Astronomers gaze into the abyss, telescopes peer, into the unknown. Space is vast and infinite, a playground for exploration, for the curious and brave."),
    # (26, "7-9", "Space", "Easy", "2 syllables", "Cosmic wonders fill the sky, stars and planets, beyond our reach. Black holes swallow all in sight, gravity's pull, too strong to fight. Meteor showers light up the night, streaks of fire, burning bright. Supernovas explode in space, sending shockwaves, across the void. Astronauts float in zero gravity, weightless and free, in their space station. Satellites orbit the Earth, transmitting signals, to every corner. Space is a vast expanse, waiting to be explored, by those who dare to dream."),
    # (27, "7-9", "Space", "Easy", "2 syllables", "Explorers venture into the unknown, seeking answers, to age-old questions. Planets orbit distant suns, in a cosmic dance, beyond our grasp. Moons cast their shadows on the surface, as they orbit, their celestial home. Asteroids streak through space, remnants of a violent past, frozen in time. Telescopes peer into the depths, revealing galaxies, in all their splendor. Space is a silent realm, where time stands still, and mysteries abound.")
     
     
     
    # (28, "7-9", "Ocean", "Difficult", "3 syllables", "The ocean's depths hold untold wonders, mysteries waiting to be discovered. Submarines diving to great depths, exploring the unknown reaches. Coral reefs teeming with life, a kaleidoscope of colors and shapes. Shipwrecks resting on the ocean floor, silent reminders of bygone eras. Whales singing their haunting melodies, echoing through the vast expanse. Algae blooming in massive blooms, turning the water into a vibrant green."),
    # (29, "7-9", "Ocean", "Difficult", "3 syllables", "The ocean is a vast and endless expanse, stretching out as far as the eye can see. Waves crashing against the rocky shore, sending spray into the air. Seagulls wheeling overhead, their cries carried on the wind. Sailboats bobbing on the horizon, their sails billowing in the breeze. Dolphins leaping playfully in the waves, their sleek bodies cutting through the water. Whales breaching in the distance, their massive forms breaking the surface."),
    # (30, "7-9", "Ocean", "Difficult", "3 syllables", "The ocean is a world of wonder, teeming with life and beauty. Coral reefs bustling with activity, a riot of color and motion. Sea turtles gliding gracefully through the water, their ancient wisdom evident in every movement. Octopuses hiding among the rocks, masters of disguise and deception. Sharks patrolling their territory, apex predators of the deep. Jellyfish pulsating with bioluminescence, lighting up the dark depths of the ocean."),

    # # Park theme (continued)
    # (31, "7-9", "Park", "Difficult", "3 syllables", "The park is a sanctuary of green, a haven from the bustling city. Trees rustling in the breeze, their leaves whispering secrets to the wind. Flowers blooming in riotous colors, attracting bees and butterflies alike. Children laughing and playing, their voices a symphony of joy. Picnickers lounging on blankets, enjoying the warmth of the sun. Birds chirping in the trees, their songs filling the air with melody."),
    # (32, "7-9", "Park", "Difficult", "3 syllables", "The park is a place of relaxation, a refuge from the stresses of daily life. Benches scattered throughout, inviting weary travelers to rest. Fountains gurgling softly, their waters sparkling in the sunlight. Joggers pounding the pavement, their footsteps a steady rhythm. Couples strolling hand in hand, lost in each other's company. Dogs frolicking in the grass, their tails wagging with delight."),
    # (33, "7-9", "Park", "Difficult", "3 syllables", "The park is a treasure trove of delights, a paradise for the senses. Sculptures dotted throughout, each one a work of art. Statues standing tall and proud, honoring the heroes of the past. Musicians playing in the bandstand, their melodies drifting on the breeze. Artists sketching on their easels, capturing the beauty of the landscape. Children playing in the playground, their laughter echoing through the trees."),

    # # Space theme (continued)
    # (34, "7-9", "Space", "Difficult", "3 syllables", "The universe is a vast and wondrous place, filled with mysteries waiting to be unraveled. Galaxies swirling in endless spirals, each one a unique masterpiece. Stars twinkling in the distance, their light traveling billions of light-years. Planets orbiting distant suns, each one a world unto itself. Asteroids hurtling through space, remnants of the early solar system. Comets streaking across the sky, leaving trails of glowing gas in their wake."),
    # (35, "7-9", "Space", "Difficult", "3 syllables", "The cosmos is a playground of extremes, where gravity warps space and time. Black holes lurking in the depths, their gravitational pull too strong to escape. Nebulas glowing with ethereal light, clouds of gas and dust swirling in the void. Supernovas exploding in brilliant bursts of energy, scattering stardust across the universe. Spacecraft hurtling through the void, their engines propelling them ever onward. Astronauts floating weightlessly in their capsules, gazing out at the endless expanse of space."),
    # (36, "7-9", "Space", "Difficult", "3 syllables", "The night sky is a canvas of wonders, where dreams take flight on wings of stardust. Constellations forming intricate patterns, their stories written in the stars. Moons orbiting distant planets, their surfaces scarred by eons of cosmic bombardment. Asteroids hurtling through the void, remnants of the solar system's formation. Telescopes scanning the heavens, revealing the secrets of the universe. Space probes exploring distant worlds, sending back images of alien landscapes.")


    #  (37, "10-12", "Ocean", "Easy", "3 syllables", "The ocean is vast and teeming with life, a world of wonder beneath the waves. Dolphins frolic in the surf, their playful antics a joy to behold. Seagulls wheel overhead, their cries echoing across the water. Sailboats glide across the horizon, their sails billowing in the breeze. Coral reefs stretch as far as the eye can see, a riot of color and motion. Whales breach the surface, their majestic forms soaring through the air."),
    # (38, "10-12", "Ocean", "Easy", "3 syllables", "The ocean is a realm of mystery and adventure, waiting to be explored. Submarines dive to great depths, revealing hidden treasures below. Octopuses hide in rocky crevices, their tentacles writhing in the currents. Seabirds nest on rocky cliffs, their calls echoing across the shoreline. Beachcombers stroll along sandy shores, collecting shells and driftwood. Lighthouses stand sentinel along the coast, guiding ships safely to port."),
    # (39, "10-12", "Ocean", "Easy", "3 syllables", "The ocean is a source of inspiration and awe, a place where dreams take flight. Surfers ride the waves, carving graceful arcs in the water. Sandpipers dart along the shoreline, their tiny footprints disappearing in the tide. Kelp forests sway in the currents, home to a myriad of creatures. Sea turtles glide through the water, their ancient wisdom evident in every movement. Sunsets paint the sky in shades of pink and gold, casting a magical glow over the water."),

    # # Park theme
    # (40, "10-12", "Park", "Easy", "3 syllables", "The park is a sanctuary of greenery, a haven from the hustle and bustle of city life. Trees tower overhead, their branches reaching towards the sky. Picnickers spread out blankets, enjoying a leisurely lunch in the shade. Children laugh and play on the playground, their shouts echoing through the air. Joggers pound the pavement, their footsteps a steady rhythm. Squirrels scamper among the trees, searching for nuts to store away."),
    # (41, "10-12", "Park", "Easy", "3 syllables", "The park is a place of tranquility and relaxation, a refuge from the stresses of everyday life. Ducks paddle in the pond, their feathers gleaming in the sunlight. Couples stroll hand in hand along winding pathways, lost in conversation. Flowers bloom in riotous colors, their perfume filling the air. Musicians play in the bandstand, their melodies drifting on the breeze. Artists sketch the scenery, capturing the beauty of nature on canvas."),
    # (42, "10-12", "Park", "Easy", "3 syllables", "The park is a hub of activity and excitement, a place where memories are made. Families gather for picnics, spreading out blankets and unpacking baskets. Frisbees soar through the air, caught expertly by outstretched hands. Dogs chase balls across the grass, their tails wagging with joy. Skateboarders glide along the pathways, performing tricks and stunts. Couples steal kisses on secluded benches, hidden from view by overhanging branches."),

    # # Space theme
    # (43, "10-12", "Space", "Easy", "3 syllables", "The universe is a vast and wondrous place, filled with mysteries waiting to be discovered. Astronauts float weightlessly in their capsules, gazing out at the stars. Telescopes scan the heavens, revealing distant galaxies and nebulae. Planets orbit distant suns, each one a world unto itself. Meteors streak across the sky, leaving trails of glowing gas in their wake. Satellites orbit the Earth, beaming back images of distant worlds."),
    # (44, "10-12", "Space", "Easy", "3 syllables", "The cosmos is a playground of extremes, where gravity warps space and time. Black holes lurk in the depths, their gravitational pull too strong to escape. Supernovas explode in brilliant bursts of energy, scattering stardust across the galaxy. Nebulas glow with ethereal light, clouds of gas and dust swirling in the void. Asteroids hurtle through space, remnants of the solar system's formation. Comets streak across the sky, their tails trailing behind them."),
    # (45, "10-12", "Space", "Easy", "3 syllables", "The night sky is a canvas of wonders, where dreams take flight on wings of stardust. Constellations form intricate patterns, their stories written in the stars. Moons orbit distant planets, their surfaces scarred by eons of cosmic bombardment. Telescopes reveal distant galaxies, each one a snapshot of the universe's history. Space probes explore the furthest reaches of the solar system, sending back images of alien landscapes. Astronomers study the heavens, unlocking the secrets of the cosmos."),


    #  # Ocean theme
    # (46, "10-12", "Ocean", "Difficult", "3+ syllables", "The oceanic ecosystem is a marvel of biodiversity, with a myriad of species inhabiting its depths. Biodiversity plays a crucial role in maintaining the balance of marine ecosystems, ensuring the survival of countless organisms. Conservation efforts are underway to protect fragile ecosystems such as coral reefs, which are threatened by climate change and human activities. Environmental awareness is key to preserving the delicate balance of our oceans, ensuring a sustainable future for generations to come."),
    # (47, "10-12", "Ocean", "Difficult", "3+ syllables", "Marine biologists study the intricate relationships between organisms in the ocean, shedding light on the complex web of life beneath the waves. Phytoplankton form the base of the marine food chain, providing essential nutrients for larger organisms. Ocean currents play a vital role in distributing heat and nutrients throughout the ocean, influencing weather patterns and climate. Anthropogenic activities such as overfishing and pollution threaten the health of marine ecosystems, underscoring the need for sustainable management practices."),
    # (48, "10-12", "Ocean", "Difficult", "3+ syllables", "Oceanographers explore the vast expanse of the ocean, mapping its seafloor and studying its currents and tides. The deep sea is home to a wealth of biodiversity, with strange and fascinating creatures adapted to extreme conditions. Hydrothermal vents spew mineral-rich water into the ocean, supporting unique ecosystems teeming with life. Marine protected areas provide sanctuary for endangered species and fragile habitats, safeguarding biodiversity for future generations."),

    # # Park theme
    # (49, "10-12", "Park", "Difficult", "3+ syllables", "Urban parks are vital green spaces in cities, providing residents with opportunities for recreation and relaxation. Urbanization poses challenges to the preservation of green spaces, as cities expand and green areas become increasingly scarce. Ecosystem services provided by urban parks include carbon sequestration, air purification, and stormwater management. Urban planners strive to design parks that are accessible to all residents, fostering community engagement and social cohesion."),
    # (50, "10-12", "Park", "Difficult", "3+ syllables", "The design of urban parks incorporates principles of landscape architecture, balancing aesthetics with functionality. Native plant species are often used in park landscaping to promote biodiversity and ecological resilience. Sustainable park design features such as rain gardens and green roofs help mitigate the urban heat island effect and reduce water runoff. Community involvement in park planning and management is essential for ensuring that parks meet the needs of diverse populations."),
    # (51, "10-12", "Park", "Difficult", "3+ syllables", "Historic parks are cultural landmarks that preserve the heritage and identity of communities. Restoration efforts aim to revitalize historic parks, preserving their architectural and natural features for future generations. Interpretive signage and guided tours educate visitors about the history and significance of historic parks. Adaptive reuse of historic park buildings repurposes them for modern uses while preserving their architectural integrity. Partnerships between government agencies, nonprofits, and community groups support the conservation and management of historic parks."),

    # # Space theme
    # (52, "10-12", "Space", "Difficult", "3+ syllables", "Astrophysicists study the fundamental properties of the universe, seeking to understand its origins and evolution. The cosmic microwave background radiation provides valuable insights into the early universe, revealing clues about its structure and composition. Dark matter and dark energy are mysterious components of the universe that exert gravitational forces on visible matter and drive its expansion. The search for exoplanets in habitable zones holds promise for discovering extraterrestrial life and expanding our understanding of the cosmos."),
    # (53, "10-12", "Space", "Difficult", "3+ syllables", "Cosmologists investigate the large-scale structure and dynamics of the universe, probing its deepest mysteries. The theory of cosmic inflation posits that the universe underwent rapid expansion in the early moments of its existence, leading to the formation of galaxies and cosmic structures. Gravitational waves are ripples in the fabric of spacetime caused by cataclysmic events such as black hole mergers and neutron star collisions. Multiverse theories propose the existence of parallel universes beyond our own, each with its own physical laws and properties."),
    # (54, "10-12", "Space", "Difficult", "3+ syllables", "Astrobiologists explore the potential for life beyond Earth, studying extreme environments on our planet as analogs for extraterrestrial habitats. Extremophiles are organisms that thrive in extreme conditions such as high temperatures, acidity, or pressure, offering insights into the limits of life's adaptability. Biosignatures are indicators of past or present life that may be detected in the atmospheres or surfaces of exoplanets, providing tantalizing clues in the search for alien life. The Drake equation estimates the number of detectable extraterrestrial civilizations in our galaxy, guiding efforts to search for intelligent life beyond our solar system.")
]




 

   
    # ... (include all your paragraph data here following the format)


# Insert data into the table
for paragraph in paragraphs_data:
    word_count = len(paragraph[5].split())
    word_length_description = determine_word_length_category(paragraph[4])
    cursor.execute('''
        INSERT INTO paragraphs (id, age_group, theme, complexity, word_count, word_length, paragraph)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (paragraph[0], paragraph[1], paragraph[2], paragraph[3], word_count, paragraph[4], paragraph[5]))

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database has been successfully created and populated with paragraph")
