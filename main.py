import spectrumExtractor as se


def main():
    print('Bienvenido a Aplicaciones de la biometría de la voz.')
    se.extract('trn_079772.wav', 'test.png')
