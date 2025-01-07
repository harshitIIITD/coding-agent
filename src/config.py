class Config:
    def __init__(self):
        self.model_name = "Qwen"
        self.model_path = None
        self.output_dir = "fine_tuned_model"
        self.epochs = 3
        self.batch_size = 8
        self.max_length = 100
        self.train_data_path = "data/train_data.json"
        self.test_data_path = "data/test_data.json"

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dict(self):
        return {
            "model_name": self.model_name,
            "model_path": self.model_path,
            "output_dir": self.output_dir,
            "epochs": self.epochs,
            "batch_size": self.batch_size,
            "max_length": self.max_length,
            "train_data_path": self.train_data_path,
            "test_data_path": self.test_data_path,
        }

    def from_dict(self, config_dict):
        for key, value in config_dict.items():
            if hasattr(self, key):
                setattr(self, key, value)
