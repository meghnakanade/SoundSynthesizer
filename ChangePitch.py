# This is a code for changing the Pitch
# Install pydub, os, wave, numpy and matplotlib libraries

from pydub import AudioSegment
import os, wave, numpy
import matplotlib.pyplot as plt


def pitchChange():
    # Ask for path to the input file

    given = input("Please enter the path to your file: \n")
    fn_wav = os.path.join('..', 'data', 'B', given)
    sound = AudioSegment.from_file(fn_wav, format="wav")
    n = float(input("By what factor you want to change the pitch? \n"))

    octaves = n

    # changing the sample rate to change the pitch

    new_sampleRate = int(sound.frame_rate * (2.0 ** octaves))

    new_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sampleRate})

    out = input("Please enter a path to save the output file: \n")
    final = os.path.join('..', 'data', 'B', out)

    # save the new sound file

    new_sound.export(final, format="wav")

    # Plotting the graphs

    path_origin = given
    raw = wave.open(path_origin)
    signal1 = raw.readframes(-1)
    signal1 = numpy.frombuffer(signal1, dtype="int16")
    f_rate1 = raw.getframerate()
    time1 = numpy.linspace(
        0,
        len(signal1) / f_rate1,
        num=len(signal1)
    )
    plt.subplot(2, 1, 1)
    plt.figure(1)
    plt.title("Input Sound Wave")
    plt.xlabel("Time")
    plt.plot(time1, signal1, color='darkblue')

    path = out
    raw = wave.open(path)
    signal = raw.readframes(-1)
    signal = numpy.frombuffer(signal, dtype="int16")
    f_rate = raw.getframerate()
    time = numpy.linspace(
        0,
        len(signal) / f_rate,
        num=len(signal)
    )
    plt.subplot(2, 1, 2)
    plt.figure(1)
    plt.title("Output Sound Wave")
    plt.xlabel("Time")
    plt.plot(time, signal, color='darkblue')
    plt.show()
