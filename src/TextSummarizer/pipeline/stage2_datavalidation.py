from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_validation import DataValidation

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager().get_data_validation_config()
        data_validation=DataValidation(config=config)
        data_validation.validate_all_file_exist()
        