from dataclasses import dataclass

""""Basic generator class"""


@dataclass
class NewUser:
    first_name: str = None
    last_name: str = None
    email: str = None
    password: str = None
    password_confirm: str = None
