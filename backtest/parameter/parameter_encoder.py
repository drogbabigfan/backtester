from backtest.parameter.parameter_object import ParameterObject


class ParameterEncoderDecoder:
    def __init__(self, parameter_object: ParameterObject):
        self.parameter_object = parameter_object
        self.parameter_dict = parameter_object.get_parameter_dict()

    def encode(self, params):
        """
        주어진 파라미터 값을 인코딩합니다.
        :param params: 딕셔너리 형태의 파라미터 값
        :return: 인코딩된 파라미터 값 리스트
        """
        encoded = []
        for key, value in params.items():
            param_options = self.parameter_dict[key]
            if isinstance(param_options, dict):
                # 딕셔너리 형태의 파라미터일 경우
                for k, v in param_options.items():
                    if v == value:
                        encoded.append(k)
                        break
            else:
                # 리스트 형태의 파라미터일 경우
                encoded.append(param_options.index(value))
        return encoded

    def decode_to_index(self, encoded_params: list):
        """
        인코딩된 파라미터 값을 인덱스 값으로 디코딩합니다.
        :param encoded_params: list
        :return:dict
        """
        params = {}
        keys = list(self.parameter_dict.keys())
        for i, value in enumerate(encoded_params):
            key = keys[i]

            if key in self.parameter_dict:
                param_options = self.parameter_dict[key]
                int_value = int(value)

                if isinstance(param_options, dict):
                    if int_value not in param_options:
                        return self.error_case()
                    params[key] = int_value
                else:
                    if int_value < 0 or int_value >= len(param_options):
                        return self.error_case()
                    params[key] = int_value
            else:
                return self.error_case()

        return params


    def decode_to_value(self, encoded_params: list):
        """
        인코딩된 파라미터 값을 실제 파라미터 값으로 디코딩합니다.
        :param encoded_params: 인코딩된 파라미터 값 리스트
        :return: 딕셔너리 형태의 파라미터 값
        """

        if encoded_params[2] == 0:
            print(encoded_params)

        params = {}
        keys = list(self.parameter_dict.keys())
        for i, value in enumerate(encoded_params):
            key = keys[i]
            if key in self.parameter_dict:
                param_options = self.parameter_dict[key]
                int_value = int(value)  # numpy.float64를 int 타입으로 변환
                if isinstance(param_options, dict):
                    if int_value not in param_options:
                        return self.error_case()
                    params[key] = param_options.get(int_value, 0)
                else:
                    if int_value < 0 or int_value >= len(param_options):
                        return self.error_case()
                    params[key] = param_options[int_value]
            else:
                return self.error_case()
        return params


    def error_case(self):
        params = {}
        keys = list(self.parameter_dict.keys())
        for key in keys:
            params[key] = 0
        return params