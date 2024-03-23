import os

if __name__ == '__main__':
    known_bad_commit = 'c1a4be04b972b6c17db242fc37752ad517c29402'
    known_good_commit = 'e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c'

    os.system(f'git bisect start {known_bad_commit} {known_good_commit}')

    python_39_path = 'C:\\Users\\marbe\\AppData\\Local\\Programs\\Python\\Python39-32\\python.exe'
    target = '.\\manage.py'

    command = f'{python_39_path} {target} test'

    os.system(f'git bisect run {command}')
