import math

"""
program for calculating the frequencies of notes in an octave
given a reference note

formula:    f(n) = f0 * 2^(1/12 * n)
            n - semitone offset

input:      note name for the desired octave and octave number
            ex: C, 4
            reference note name and frequency
            ex: A4 = 440 Hz

desired_output: dictionary of names and frequencies
"""
# CONSTANTS:
NOTES = ("C","C#","D","D#","E","F","F#","G","G#","A","A#","B")

# generate the list of note names:

def note_name(index: int, octave: int) -> str:
    #return the note name with the octave
    return f"{NOTES[index]}{octave}"

def generate_octave(start_note: str, octave: int = 4, repeat_first_note: bool = False) -> None:
    #Generate note names for an octave starting from a given note

    start_index = NOTES.index(start_note)

    #conditional to choose whether or not to repeat the first note
    num_notes = 13 if repeat_first_note else 12

    list = []
    for i in range(num_notes):
        list.append(note_name((start_index + i) % 12, octave if (i+start_index)//12 == 0 else octave+1))
    return list

# Calculate the frequencies:

def note_distance(note1: str, note2: str) -> int:
    #For calculating note distance in semitones:
    oct1 = int(note1[-1])
    oct2 = int(note2[-1])

    name1 = note1[:-1]
    name2 = note2[:-1]

    dist = NOTES.index(name2) - NOTES.index(name1) + (oct2-oct1)*12
    return dist

def freq_formula(start_freq: float, semitone_offset: int) -> float:
    #Calculate frequency according to the formula

    note = start_freq * math.pow(2, 1/12 * semitone_offset)
    return round(note, 2)

def note_freq(note: str, ref_note: str = "A4", ref_freq:int = 440) -> float:
    # Use the formula to calculate any note frequency by name
    # Assume the standard reference note is A4 = 440 Hz
    offset = note_distance(ref_note, note)
    return freq_formula(ref_freq, offset)

def get_octave_frequencies(start_note: str, start_octave: int = 4, reference_note: str = "A4", reference_frequency: int = 440, repeat_first_note: bool = False) -> dict:
    # Now make the dictionary
    notes = generate_octave(start_note, start_octave, repeat_first_note)

    frequencies = []
    for i in range(len(notes)):
        freq = note_freq(notes[i], reference_note, reference_frequency)

        frequencies.append(freq)

    #dictionary comprehension example:
    note_data = {note : note_freq(note, reference_note, reference_frequency) for note in notes}
    return note_data

note_data = get_octave_frequencies("E", 4, repeat_first_note=True)
print(note_data)