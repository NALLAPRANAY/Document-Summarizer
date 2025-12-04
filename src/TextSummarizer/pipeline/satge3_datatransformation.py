from TextSummarizer.logging import logger
from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_transformation import DataTransformation
class DataTransformationPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager().get_data_transformation_config()
        data_transformation=DataTransformation(config=config)
        data_transformation.convert()
