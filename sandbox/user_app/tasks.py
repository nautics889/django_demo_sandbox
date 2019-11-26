from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def foobar():
    logger.info('Foobar')
    print('\n\nfoobar\n\n', flush=True)
    return
