

def batched(it, sz: int):
    """Generator for retrieving batches from an iterator."""

    start = 0
    while start + sz < len(it):
        yield it[start:start+sz]
        start += sz
    yield it[start:]
