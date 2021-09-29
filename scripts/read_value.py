from brownie import SimpleStorage, accounts, config


def read_contract():
    print(SimpleStorage[-1])  # latest deployement


def main():
    read_contract()
