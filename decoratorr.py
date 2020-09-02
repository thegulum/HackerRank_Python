def layout(_func):
    def local_func():
        dinamik_hisse = _func
        txt = f"Header / {dinamik_hisse} / Footer"
        return txt
    return local_func


@layout
def home():
    return "Ana sehifeye aid olan hisse"
print(home())
