import hashlib
import time


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password: str):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password: str):
        return self.hash_password(password) == self.password

    def __str__(self):
        return f'User({self.nickname}, {self.age})'


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Video:{self.title}, {self.duration}sec, Adult: {self.adult_mode}"


class UrTube:
    def __init__(self):
        self.users: [User] = []
        self.videos: [Video] = []
        self.current_user: [User] = None

    def log_in(self, login: str, password: str):
        for user in self.users:
            if user.nickname == login and user.check_password(password):
                self.current_user = user
                print(f"Добро пожаловать, {login}!")
                return
        print(f"Пользователь {login} не существует или пароль неверен.")

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *video_objs: Video):
        for video in video_objs:
            if all(video.title != v.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_input: str) :
        search_input_lower = search_input.lower()
        return [video.title for video in self.videos if search_input_lower in video.title.lower()]

    def watch_video(self, title: str):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((v for v in self.videos if v.title == title), None)

        if video is None:
            print("Видео не найдено")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Начинается воспроизведение: {video.title}")
        for second in range(1, video.duration + 1):
            print(second, end=" ", flush=True)
            time.sleep(1)

        video.time_now = 0
        print("\nКонец видео")



if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')



