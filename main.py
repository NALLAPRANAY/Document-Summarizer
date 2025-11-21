from TextSummarizer.pipeline.stage1_dataingestion import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger
try:
    logger.info("Intiating data ingestion inti artifacts")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info("Data ingestion completed into artifacts")
except Exception as e:
    logger.exception(e)
    raise e