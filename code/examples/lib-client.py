from typing import Iterable, Any

def user_id(x: int) -> int:
    return x

class UserDB:
    def users(self):
        return [1, 2, 3]

    def user_ids(self) -> Iterable[int]:
        return map(user_id, self.users())


some_crazy_corner_case = False

def main() -> Any:
    user_ids = UserDB().user_ids()
    if (some_crazy_corner_case): user_ids.sort()
    return user_ids
