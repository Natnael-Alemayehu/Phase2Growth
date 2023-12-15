def read_expired_account_ids(file_path="account/accountid_expired.txt"):
    # Import libraries
    import os

    # Create the directory if it doesn't exist
    os.makedirs("account", exist_ok=True)

    # Open the file in read mode
    #   with open(file_path, "r") as f:
    with open(os.path.join("account", "accountid_expired.txt"), "r") as f:
        # Read all lines of the file
        lines = f.readlines()

    # Strip any trailing whitespace from each line
    lines = [line.rstrip() for line in lines]

    # Convert each line to an integer (assuming IDs are integers)
    expired_ids = [int(line) for line in lines]

    return expired_ids

# Example usage
expired_ids = read_expired_account_ids()
# print(f"Expired account IDs: {expired_ids}")

def read_all_account_ids(file_path="account/all_accountid.txt"):
    
    # Import libraries
    import os

    # Create the directory if it doesn't exist
    os.makedirs("account", exist_ok=True)

    # Open the file in read mode
    #   with open(file_path, "r") as f:
    with open(os.path.join("account", "all_accountid.txt"), "r") as f:
        # Read all lines of the file
        lines = f.readlines()

    # Strip any trailing whitespace from each line
    lines = [line.rstrip() for line in lines]

    # Convert each line to an integer (assuming IDs are integers)
    all_ids = [int(line) for line in lines]

    return all_ids

def read_active_account_ids(file_path="account/active_account.txt"):
    
    # Import libraries
    import os

    # Create the directory if it doesn't exist
    os.makedirs("account", exist_ok=True)

    # Open the file in read mode
    #   with open(file_path, "r") as f:
    with open(os.path.join("account", "active_account.txt"), "r") as f:
        # Read all lines of the file
        lines = f.readlines()

    # Strip any trailing whitespace from each line
    lines = [line.rstrip() for line in lines]

    # Convert each line to an integer (assuming IDs are integers)
    active_ids = [int(line) for line in lines]

    return active_ids
