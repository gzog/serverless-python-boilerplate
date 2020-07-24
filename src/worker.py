from aws_lambda_powertools import Logger
import datetime

logger = Logger(service='worker')


@logger.inject_lambda_context
def run(event, context):
    current_time = datetime.datetime.now().time()
    name = context.function_name
    logger.info("Your worker function " + name + " ran at " + str(current_time))
