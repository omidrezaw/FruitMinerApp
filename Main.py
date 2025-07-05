from requests import post
from time import sleep
import sys
from colorama import Fore
from os import system


def clear_console():
    system("cls" if sys.platform == "win32" else "clear")


def collect_gold(data, headers):
    retry_count = 0
    while retry_count < 3:
        try:
            return post("http://iran.fruitcraft.ir/cards/collectgold", data=data, headers=headers)
        except Exception as e:
            print(e)
            retry_count += 1
            sleep(0.5)
    return None


def deposit_to_bank(data, headers):
    retry_count = 0
    while retry_count < 3:
        try:
            return post("http://iran.fruitcraft.ir/player/deposittobank", data=data, headers=headers)
        except Exception as e:
            print(e)
            retry_count += 1
            sleep(0.5)
    return None


def start(maining_time, deposit_ask, headers):
    collect_data = "edata=Gk4KXVpRXRJDSEMTfmMXSA%3D%3D"
    deposit_data = "edata=Gk4KUEFQQERbUDpPAwkBAVRZRFQ4UB4aWwoEEA5GW05bAlUECgRTQ1JIBVQEUAVdFwhSQAAJCFsDF1BRBVoMBhFJ"

    done = 0
    lost = 0

    for i in range(400):
        try:
            collect_result = collect_gold(collect_data, headers)
            if collect_result is not None:
                if deposit_ask:
                    deposit_result = deposit_to_bank(deposit_data, headers)
                    if deposit_result is None:
                        lost += 1
                done += 1
        except Exception as e:
            print(e)
            lost += 1
        finally:
            sys.stdout.write(f"\r{Fore.LIGHTBLUE_EX}╔════════════════════════════════════════════╗\n"
                             f"║          {Fore.RESET}• Gold Mine Done: {Fore.GREEN}{done}{Fore.RESET}                  ║\n"
                             f"║          {Fore.RESET}• Gold Mine Lost: {Fore.RED}{lost}{Fore.RESET}                 ║\n"
                             f"║          {Fore.RESET}• Bank Deposit: {deposit_ask}               ║\n"
                             f"╚════════════════════════════════════════════╝")
            sys.stdout.flush()
        sleep(maining_time)


# ==== شروع برنامه ====

fruit_passport = input("Enter Your Fruit Passport: ").strip()
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; SM-A750F Build/QP1A.190711.020)',
    'Host': 'iran.fruitcraft.ir',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'cookie': f'FRUITPASSPORT={fruit_passport}'
}

clear_console()

try:
    power = int(input('How much is your mining power? >> '))
    capacity = int(input('How much is your mining capacity? >> '))
except ValueError:
    print("❗ لطفاً فقط عدد وارد کن.")
    sys.exit(1)

deposit_input = input('Do you want to deposit money in the bank? (Y or N) >> ').lower()
deposit_ask = deposit_input == "y"

maining_time = int(capacity / (power / 3600))

print("\n\n\n\n", f"{Fore.LIGHTBLUE_EX}╔════════════════════════════════════════════╗\n"
      f"║       {Fore.RESET}Mine time is: {Fore.CYAN}{maining_time}{Fore.RESET} sec        ║\n"
      f"╚════════════════════════════════════════════╝\n")

print(f"\n\n Maedan bot edited by: {Fore.RED}Cactus")

start(maining_time, deposit_ask, headers)