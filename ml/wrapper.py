from recbole.quick_start import load_data_and_model

MODEL_FILE = 'RecVAE-May-26-2023_19-17-17.pth'


def run():
    try:
        config, model, dataset, train_data, valid_data, test_data = load_data_and_model(
            model_file=MODEL_FILE, 
        )
        return 'ok'
    except Exception as e:
        raise e
