
def read(users:list[dict])-> None:
    for user in users[1:]:
        print(f'Twój znajomy {user['name']} opublikował: {user["posts"]} ')

def create_user(users:list[dict])->None:
    name: str = input('podaj imie użytkownika: ')
    surname: str = input('podaj nazwisko użytkownika: ')
    posts: str = int(input('podaj liczbę postów: '))
    user: dict = {'name': name, 'surname': surname, 'posts': posts}
    users.append(user)

def search_user(users: list[dict]) -> None:
    user_name: str = input('Kogo szukasz?: ')
    for user in users[1:]:
         if user['name'] == user_name:
              print(user)

def remove(users: list[dict]) -> None:
    user_name: str = input('Kogo szukasz?: ')
    for user in users[1:]:
         if user['name'] == user_name:
             users.remove(user)

def update(users: list[dict])-> None:
    user_name: str = input('Kogo szukasz?: ')
    for user in users[1:]:
        if user['name'] == user_name:
         new_user_name = input("Wprowazdz nowe imie: ")
         new_user_surname = input("Wprowazdz nowe nazwisko: ")
         new_user_posts = input("Wprowazdz nową liczbę postów: ")
         user["name"] = new_user_name
         user["surname"] = new_user_surname
         user["posts"] = new_user_posts
