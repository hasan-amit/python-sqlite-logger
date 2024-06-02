from app.app import App
from pathlib import Path


def main():
    App(path=f"{Path(__file__).resolve().parent}").start()


if __name__ == "__main__":
    main()