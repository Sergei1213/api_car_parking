import requests

def main():
    r = requests.get('http://127.0.0.1:8000/data').json()

    print(r['cars'][1])


if __name__ == '__main__':
    main()
