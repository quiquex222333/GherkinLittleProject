from behave import step
from assertpy import assert_that
from main.utils.constants import HttpMethods
from main.utils.request_utils import RequestUtils as ru
from main.core.file_reader import FileReader

@step(u'A "{http_method}" request to "{endpoint}"')
def step_retrieve_numbers_dt(context, http_method, endpoint):
    """Sample step to retrieve numbers
    :param context: Global context from behave
    :type context: obj
    :param http_method: HTTP method
    :type http_method: string
    :param endpoint: Application's endpoint method
    :type endpoint: obj
    """
    context.http_method = http_method
    context.endpoint = endpoint

@step(u"The request is sent")
def step_impl_send(context):
    """Sends request
    :param context: Global context from behave
    :type context: obj
    """
    context.status_code, context.json_response = context.rm.do_request(context.http_method,
                                                                       context.endpoint)

@step(u'The status code should be {status_code:d}')
def step_impl_status(context, status_code):
    """Compare status code

    :param context: Global context from behave
    :type context: obj
    :param status_code: status code retrieved
    :type status_code: int
    """
    assert_that(context.status_code).is_equal_to(status_code)

@step(u'The schema is validated with "{schema}"')
def step_impl_validate_schema(context, schema):
    """Validate body response schema

    :param context: Global context from behave
    :type context: obj
    :param schema: name schema file
    :type schema: String
    """
    json_schema = FileReader.read_schema(schema)
    assert_that(ru.validate_body_schema(context.json_response, json_schema),
                f"The response should contains {json_schema}").is_true()
