
import logging
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler, AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

sb = SkillBuilder()

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speak_output = "Bem-vindo ao Monitoramento GoodWe! Você pode perguntar sobre status, consumo ou geração."
        return handler_input.response_builder.speak(speak_output).ask("O que você gostaria de saber?").response

class GetStatusIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("GetStatusIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "O status atual é: operacional."
        return handler_input.response_builder.speak(speak_output).response

class GetConsumoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("GetConsumoIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "O consumo atual é de 2.5 quilowatt-hora."
        return handler_input.response_builder.speak(speak_output).response

class GetGeracaoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("GetGeracaoIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "A geração atual é de 4.3 quilowatt-hora."
        return handler_input.response_builder.speak(speak_output).response

class FallbackIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Desculpe, não entendi. Você pode perguntar sobre status, consumo ou geração."
        return handler_input.response_builder.speak(speak_output).ask("Pode repetir?").response

class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.response

class GlobalExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        logger.error(exception, exc_info=True)
        speak_output = "Ocorreu um erro inesperado. Tente novamente mais tarde."
        return handler_input.response_builder.speak(speak_output).ask(speak_output).response

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(GetStatusIntentHandler())
sb.add_request_handler(GetConsumoIntentHandler())
sb.add_request_handler(GetGeracaoIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_exception_handler(GlobalExceptionHandler())

lambda_handler = sb.lambda_handler()