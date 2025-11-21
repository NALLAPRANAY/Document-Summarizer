from TextSummarizer.pipeline.stage1_dataingestion import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger
from TextSummarizer.pipeline.stage2_datavalidation import DataValidationTrainingPipeline
try:
    logger.info("Intiating data ingestion inti artifacts")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info("Data ingestion completed into artifacts")
    logger.info("Intiate Data validation")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
except Exception as e:
    logger.exception(e)
    raise e