from scipy.io import wavfile  # scipy library to read wav files
import numpy as np
import matplotlib.pyplot as plt


def extract(input, output):
    fs, audiodata = wavfile.read(input)

    # Plot the audio signal in time
    plt.plot(audiodata)
    plt.title('Audio signal in time', size=16)

    # spectrum
    from scipy.fftpack import fft  # fourier transform
    n = len(audiodata)
    AudioFreq = fft(audiodata)
    AudioFreq = AudioFreq[0:int(np.ceil((n + 1) / 2.0))]  # Half of the spectrum
    MagFreq = np.abs(AudioFreq)  # Magnitude
    MagFreq = MagFreq / float(n)

    # Spectrogram
    from scipy import signal
    N = 64  # Number of point in the fft
    f, t, sxx = signal.spectrogram(audiodata, fs, window=signal.blackman(N), nfft=N)
    fig = plt.figure(frameon=False)
    plt.axis('off')
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.pcolormesh(t, f, 10 * np.log10(sxx))  # dB spectrogram

    plt.savefig(output, bbox_inches=0, transparent=True, pad_inches=0)
    # plt.show()
    plt.close()
