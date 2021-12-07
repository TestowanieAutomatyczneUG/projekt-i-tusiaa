from hamcrest.core.base_matcher import BaseMatcher

def pesel(pesel: str):
    if not isinstance(pesel, str):
        return False
    if len(pesel) != 11 or not pesel.isdigit():
        return False

    wagi = [1, 3, 7, 9]
    value = 0
    months = list(range(81, 93)) + list(range(1, 13)) + list(range(21, 33))    

    for i in range(0, 10):
        value += int(pesel[i]) * wagi[i % 4]

    value = value % 10

    if value != 0:
        value = 10 - value

    if value != int(pesel[10]):
        return False

    if int(pesel[2:4]) not in months:
        return False

    if int(pesel[4:6]) not in range(1, 32):
        return False

    return True

class IsValidPesel(BaseMatcher):
    def _matches(self, item):
        return pesel(item)

    def describe_to(self, description):
        description.append_text("Invalid pesel!")