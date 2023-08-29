import logging
import time

def main():
    for i in range(10):
        logging.info("Hello world!")
        print("Hello world!")
        time.sleep(1)

if __name__ == '__main__':
    main()