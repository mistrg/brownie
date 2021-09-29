from brownie import SimpleStorage, accounts


def test_deploy():
    # arrange
    account = accounts[0]
    # act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # assert
    assert starting_value == expected


def test_updating_storage():
    # arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # act

    expected = 15
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)

    stored_value = simple_storage.retrieve()

    # assert
    assert stored_value == expected
