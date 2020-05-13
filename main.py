import warnings
import predictor


def main():
    print('Bienvenido a Aplicaciones de la biometría de la voz.')
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    predictor.analyze('Data/S4/spk_000935/trn_059924.wav')


if __name__ == "__main__":
    main()
