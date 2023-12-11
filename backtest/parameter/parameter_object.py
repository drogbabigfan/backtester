import abc
class ParameterObject(abc.ABC):
    @abc.abstractmethod
    def get_parameter_dict(self):
        pass