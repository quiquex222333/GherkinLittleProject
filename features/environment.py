"""Environment module for behave"""
from behave import fixture
from behave.model_core import Status
from main.core.request_manager import RequestsManager
from main.utils.logger_utils import LoggerUtils


def before_all(context):
    """Before_all
    """
    context.logger = LoggerUtils.config_logger('basic_logger')
    context.logger.info('Set primary user credentials')
    context.rm = RequestsManager.get_instance()
    context.id_dictionary = {}


def after_all(context):
    """After all
    """


def before_feature(context, feature):
    """Before feature hook
    """
    context.logger.info(f"=============Started {feature.name}")


def after_feature(context, feature):
    """after feature hook
    """


def before_scenario(context, scenario):
    """Before scenario hook
    """
    context.logger.info(f"=============Started {scenario.name}")


def after_scenario(context, scenario):
    """After scenario hook if the scenario is failed take a screenshot
    """
    context.logger.info(scenario.name)
    context.logger.info(' '.join(scenario.tags))
    if scenario.status == Status.failed:
        context.logger.error(f"============ Failed scenario {scenario.name}")
    else:
        context.logger.info(f"============ Scenario passed {scenario.name}")
    context.logger.info(f"============Finished {scenario.name}\n\n\n")
