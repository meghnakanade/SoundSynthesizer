# This is code for sampling of signals downsampling and upsampling
# Install pydub, Audiosegment, os, numpy,matplotlib,wave and librosa

import librosa, os
import soundfile as s
import wave, numpy, sys
import matplotlib.pyplot as plt


def resample():
    # as per the driven input enter path for  audio file

    given = input("Please enter the path to your file: \n")
    fn_wav = os.path.join('..', 'data', 'B', given)
    y, sr = librosa.load(fn_wav, sr=None)

    # Drive how much sampling frequency do user want here user is number of frequency

    print("How much sampling frequency do you want? (Please enter the value in Hz)")
    user = int(input())

    # Choosing a sampling method

    print("Please choose a sampling method. By default it is resampy’s high-quality mode (‘kaiser_best’).")
    print("""    1)Fourier Method
      2)Polyphase filtering
      3)Linear interpolation
      4)Last value
      5)Default""")

    # Using appropriate libraries and sampling them according to the user input

    choice = int(input())
    if user > sr:
        print("Your audio is being upsampled! ")
    elif user == sr:
        print("OOPS you already have the audio you need!")
    else:
        print("Your audio is being downsampled! ")
    if choice == 1:
        changed = librosa.resample(y, sr, user, res_type='scipy')
    elif choice == 2:
        changed = librosa.resample(y, sr, user, res_type='polyphase')
    elif choice == 3:
        changed = librosa.resample(y, sr, user, res_type='linear')
    elif choice == 4:
        changed = librosa.resample(y, sr, user, res_type='zero_order_hold')
    elif choice == 5:
        changed = librosa.resample(y, sr, user)
    else:
        print("Invalid choice")
        sys.exit()

    # Enter a path to save the output audio file

    final = input("Resampling Done! Please enter a path to save the file: \n")
    s.write(final, changed, user)

    # Plotting the graph

    # Setting the figure size

    plt.figure(figsize=(10, 6))

    # opening the first audio file and printing its graph plotting two graphs together on one page

    path_origin = given
    raw = wave.open(path_origin)
    signal1 = raw.readframes(-1)
    signal1 = numpy.frombuffer(signal1, dtype="int16")
    f_rate1 = raw.getframerate()

    time1 = numpy.linspace(
        0,  # start
        len(signal1) / f_rate1,
        num=len(signal1)
    )

    plt.subplot(2, 1, 1)
    plt.figure(1)
    plt.title("Input Sound Wave")
    plt.xlabel("Time")
    plt.plot(time1, signal1, color='darkmagenta')

    # ----------------------------------------------
    # opening the final output audio file and printing its graph plotting two graphs together on one page

    path = final
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
    plt.plot(time, signal, color='darkmagenta')
    plt.show()
