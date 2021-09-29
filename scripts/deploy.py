from brownie import accounts, config, SimpleStorage, network
import os


def deploy_simple_storage():
    account = getAccount()
    # account = accounts.load("metamask-account")
    # account = accounts.add(config["wallets"]["from_key"])
    print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)

    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    print("Transaction comited")

    stored_value = simple_storage.retrieve()
    print(stored_value)


def getAccount():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
