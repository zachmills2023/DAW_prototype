def generate_chromatic():

    chromatic_scale = [16.3516] # This is the Hz value for C0

    # Find each consecutive semitone based on starting note C0 (16.35 Hz).
    for i in range(11):
        chromatic_scale.append(chromatic_scale[i] * 2 ** (1/12))
    
    # Find the octaves of each note in the scale.
    for i in range(96):
        chromatic_scale.append(chromatic_scale[i] * 2)

    return chromatic_scale

def display_chromatic():
    note_names = \
        [
        'C',
            'C♯/D♭',
        'D',
            'D♯/E♭',
        'E',
        'F',
            'F♯/G♭',
        'G',
            'G♯/A♭',
        'A',
            'A♯/B♭',
        'B'
        ]

    chromatic = generate_chromatic()

    octave_count = 0
    for i in range(len(chromatic)):
        if i % 12 == 0:
            octave_count = i / 12
        print(note_names[((i + 1) % 12) - 1] \
               + str(round(octave_count)) + '\t - \t' + str(round(chromatic[i], 2)))

def main():
    display_chromatic()

if __name__ == "__main__":
    main()
