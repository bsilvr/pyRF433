
class Protocol:
    def __init__(self):
        self._transmit_data_format = "#<pulse_length>:<pulse_code>:<repeat>\0"
        self._pulse_length = 0
        self._repeat = 1
        self._pulse_0 = (0, 0)
        self._pulse_1 = (0, 0)

        self._bit_code = None
        self._pulse_code = None

    def generate_bit_code(self):
        raise NotImplementedError()

    @property
    def bit_code(self):
        return self._bit_code

    @property
    def pulse_code(self):
        return self._pulse_code

    @property
    def pulse_length(self):
        return self._pulse_length

    def get_transmit_data(self):
        if self._pulse_length == 0:
            raise ValueError(
                "The pulse_length was not overwritten in the child class")
        if self._pulse_code is None:
            raise ValueError("The bit_code was not generated")
        return self._transmit_data_format.replace(
                                    "<pulse_length>", str(self._pulse_length)
                                    ).replace(
                                    "<pulse_code>", str(self._pulse_code)
                                    ).replace(
                                    "<repeat>", str(self._repeat))

    def _send_0(self):
        return "1"

    def _send_1(self):
        return "0"

    def _send(self, bit):
        return self._send_0() if bit == "0" else self._send_1()

    def _transmit(self, bit):
        return self._transmit_0() if bit == "0" else self._transmit_1()

    def _transmit_0(self):
        return "1" * self._pulse_0[0] + "0" * self._pulse_0[1]

    def _transmit_1(self):
        return "1" * self._pulse_1[0] + "0" * self._pulse_1[1]

    def _convert_pulse_code(self):
        raise NotImplementedError()
