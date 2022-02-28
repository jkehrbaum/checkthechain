from ctc import binary


def get_command_spec():
    return {
        'f': keccack_command,
        'help': 'compute keccak hash of data',
        'args': [
            {'name': 'data'},
            {'name': '--text', 'action': 'store_true'},
            {'name': '--hex', 'action': 'store_true'},
            {'name': '--raw', 'action': 'store_true'},
        ],
    }


def keccack_command(data, text, hex, raw):
    if text:
        hex = False
    elif hex:
        pass
    else:
        hex = data.startswith('0x')

    if hex:
        keccak = binary.keccak(data)
    else:
        keccak = binary.keccak_text(data)

    if raw:
        if not keccak.startswith('0x'):
            raise Exception('wrong format')
        keccak = keccak[2:]

    print(keccak)

