from TextSummarizer.logging import logger
from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.model_training import ModelTrainer

class ModelTrainerPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager().get_model_trainer_config()
        model_trainer=ModelTrainer(config)
        model_trainer.train()
