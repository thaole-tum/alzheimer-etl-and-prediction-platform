import kagglehub


if __name__ == "__main__":
    path = kagglehub.dataset_download("rabieelkharoua/alzheimers-disease-dataset")
    print(f"Path to dataset files: {path}")
