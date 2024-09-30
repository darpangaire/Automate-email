import re


def check_email(email):
    # Find the index of '@'
    local_idx = email.find('@')

    # Ensure there is an '@' symbol in the email
    if local_idx == -1:
        print("Invalid email: No '@' symbol found.")
        return

    # Split into local part and domain part
    localPart = email[:local_idx]
    domainParts = email[local_idx + 1:]

    # Checking the overall length of the email
    if len(email) > 254:
        print('Invalid email: Email length exceeds 254 characters.')
        return

    # Validate the local part and domain part
    if check_localParts(localPart) and domain_checkParts(domainParts):
        print('Valid email')
    else:
        print('Invalid email')


def check_localParts(localPart):
    # Check local part length
    if len(localPart) > 64:
        return False

    # Local part should not start or end with '.'
    if localPart[0] == '.' or localPart[-1] == '.':
        return False

    # Local part should not contain consecutive dots
    if '..' in localPart:
        return False

    # Local part should contain at least one alphanumeric character
    if not any(char.isalnum() for char in localPart):
        return False

    # Local part should only contain valid characters
    if not re.match(r'^[\w.!#$%&\'*+/=?^_`{|}~-]+$', localPart):
        return False

    return True


def domain_checkParts(domainParts):
    # List of valid top-level domains (TLDs)
    domainEnds = ['.org', '.net', '.tech', '.io', '.in', '.com', '.edu']

    # Find the index of the first dot
    idx = domainParts.find('.')

    # Ensure the domain has a valid format
    if idx == -1:
        return False

    # Split domain into the name and TLD
    domainName = domainParts[:idx]
    domainTLD = domainParts[idx:]

    # Domain name should not start or end with '-'
    if domainName.startswith('-') or domainName.endswith('-'):
        return False

    # Domain name should contain at least one alphanumeric character
    if not any(char.isalnum() for char in domainName):
        return False

    # Check if the TLD is in the allowed list
    if domainTLD not in domainEnds:
        return False

    # Check if there are any spaces in the domain part
    if domainParts.isspace():
        return False

    # Check length of the domain part
    if len(domainParts) > 255:
        return False

    return True


# Test the email validation
check_email('darpangaire11@gmail.com')
