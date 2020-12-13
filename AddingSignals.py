# This is code for adding of signals
# Install pydub, Audiosegment, os, numpy,matplotlib,wave and librosa

from pydub import AudioSegment
import os, numpy
import matplotlib.pyplot as plt
import wave


def addSignals():
   # as per the driven input enter path for first audio file

   given = input("Please enter the path to your file: \n")
   fn_wav = os.path.join('..', 'data', 'B', given)
   soundFile = AudioSegment.from_file(fn_wav)
   sound = [soundFile]

   # Enter a number for how many signals user wants to add

   n = int(input("How many sound files you wish to add to the original one?"))

   # as per the driven input enter path for  audio files to add them to first file

   print("Please enter the complete path to the file in the order you wish to add them:")
   for i in range(0, n):
      s = input()
      fs = os.path.join('..', 'data', 'B', s)
      soundF = AudioSegment.from_file(fs)
      sound.append(soundF)
      temp = s
   combined_file = sound[0]

   # Combing them using for loop

   for i in range(1, len(sound)):
      combined_file += sound[i]

   # as per the driven output enter path to save file

   out = input("Where do you want to store the output? (path)")
   combined_file.export(out, format='wav')
   print("Process complete! ")

   # plotting graphs
   # opening the first audio file and printing its graph plotting three graphs together on one page

   path1 = given
   raw = wave.open(path1)
   signal1 = raw.readframes(-1)
   signal1 = numpy.frombuffer(signal1, dtype="int16")
   f_rate1 = raw.getframerate()
   time = numpy.linspace(
      0,  # start
      len(signal1) / f_rate1,
      num=len(signal1)
   )
   plt.subplot(3, 1, 1)
   plt.figure(1)
   plt.title("Input Sound Wave 1")
   plt.xlabel("Time")
   plt.plot(time, signal1, color='firebrick')

   # -----------------------------------------------------
   # opening the second audio file and printing its graph plotting three graphs together on one page

   path2 = temp
   raw2 = wave.open(path2)
   signal2 = raw2.readframes(-1)
   signal2 = numpy.frombuffer(signal2, dtype="int16")
   f_rate2 = raw2.getframerate()
   time2 = numpy.linspace(
      0,
      (len(signal2) / f_rate2),
      num=len(signal2)
   )
   plt.subplot(3, 1, 2)
   plt.figure(1)
   plt.title("Input Sound Wave 2")
   plt.xlabel("Time")
   plt.plot(time2, signal2, color='firebrick')

   # ------------------------------------------------------
   # opening the output audio file and printing its graph plotting three graphs together on one page

   path3 = out
   raw3 = wave.open(path3)
   signal3 = raw3.readframes(-1)
   signal3 = numpy.frombuffer(signal3, dtype="int16")
   f_rate3 = raw3.getframerate()
   time3 = numpy.linspace(
      0,  # start
      len(signal3) / f_rate3,
      num=len(signal3)
   )
   plt.subplot(3, 1, 3)
   plt.figure(1)
   plt.title("Output Sound Wave")
   plt.xlabel("Time")
   plt.plot(time3, signal3, color='firebrick')
   plt.show()
