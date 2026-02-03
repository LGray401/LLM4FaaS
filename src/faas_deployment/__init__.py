"""FaaS deployment module."""
from .prepare_functions import FunctionPreparer
from .deploy_and_execute import TinyFaaSManager

__all__ = ['FunctionPreparer', 'TinyFaaSManager']
