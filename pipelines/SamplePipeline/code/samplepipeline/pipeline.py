from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from samplepipeline.config.ConfigStore import *
from samplepipeline.udfs.UDFs import *
from prophecy.utils import *
from samplepipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Source_0 = Source_0(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/SamplePipeline")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/SamplePipeline")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
