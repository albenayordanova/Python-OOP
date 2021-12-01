class Profile:
    us_min_l = 5
    us_max_l = 15
    pas_min_l = 8
    pas_min_upper = 1
    pas_min_digit = 1

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __validate_username(self, username):
        if self.us_min_l > len(username) or len(username) > self.us_max_l:
            raise ValueError('The username must be between 5 and 15 characters.')

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_username(value)
        self.__username = value

    def __validate_password(self, password):
        message = f"The password must be {self.pas_min_l} or more characters" \
                  f" with at least {self.pas_min_digit} digit and {self.pas_min_upper} uppercase letter."
        if len(password) < self.pas_min_l:
            raise ValueError(message)
        if not any([x for x in password if x.isdigit()]):
            raise ValueError(message)
        if not any([x for x in password if x.isupper()]):
            raise ValueError(message)

    @property
    def password(self):
        return ''.join('*' * len(self.__password))

    @password.setter
    def password(self, value):
        self.__validate_password(value)
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {self.password}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)