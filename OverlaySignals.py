# This is code for overlaying of signals
# Install pydub, Audiosegment, os, numpy,matplotlib,wave and librosa

from pydub import AudioSegment
import os, wave, numpy
import matplotlib.pyplot as plt


def overlaysignals():
    # as per the driven input enter path for first audio file

    given1 = input("Please enter the path to the first file: \n")
    fn_wav = os.path.join('..', 'data', 'B', given1)

    # as per the driven input enter path for second audio file

    given2 = input("Please enter the path to second file: \n")
    fn_wav2 = os.path.join('..', 'data', 'B', given2)
    sound1 = AudioSegment.from_file(fn_wav)
    sound2 = AudioSegment.from_file(fn_wav2)

    # this will do overlaying of two audio files using combine function

    combined = sound1.overlay(sound2)

    # as per the driven output enter path to save your audio file

    out = input("Please provide a path to save the output file: \n")
    combined.export(out, format='wav')

    # Graphs
    # opening the first audio file and printing its graph plotting three graphs together on one page

    path_origin = given1
    raw = wave.open(path_origin)
    signal1 = raw.readframes(-1)
    signal1 = numpy.frombuffer(signal1, dtype="int16")
    f_rate1 = raw.getframerate()
    time1 = numpy.linspace(
        0,
        len(signal1) / f_rate1,
        num=len(signal1)
    )
    plt.subplot(3, 1, 1)
    plt.figure(1)
    plt.title("Input Sound Wave 1")
    plt.xlabel("Time")
    plt.plot(time1, signal1, color='lightcoral')

    # opening the second audio file and printing its graph plotting three graphs together on one page

    path_second = given2
    raw = wave.open(path_second)
    signal2 = raw.readframes(-1)
    signal2 = numpy.frombuffer(signal2, dtype="int16")
    f_rate2 = raw.getframerate()
    time2 = numpy.linspace(
        0,
        len(signal2) / f_rate2,
        num=len(signal2)
    )
    plt.subplot(3, 1, 2)
    plt.figure(1)
    plt.title("Input Sound Wave 2")
    plt.xlabel("Time")
    plt.plot(time2, signal2, color='lightcoral')

    # opening the saved output from the path driven by user and printing its graph plotting three graphs together on one page

    path_final = out
    raw = wave.open(path_final)
    signal3 = raw.readframes(-1)
    signal3 = numpy.frombuffer(signal3, dtype="int16")
    f_rate3 = raw.getframerate()
    time3 = numpy.linspace(
        0,
        len(signal3) / f_rate3,
        num=len(signal3)
    )
    plt.subplot(3, 1, 3)
    plt.figure(1)
    plt.title("Output Sound Wave")
    plt.xlabel("Time")
    plt.plot(time3, signal3, color='lightcoral')
    plt.show()

    # At the end we get the graphs of three audio files on one page with title


#overlaySignals()
