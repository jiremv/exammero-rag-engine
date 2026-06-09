# test_count.py

from app.shards.manejo.manejo_shard import (
    ManejoShard
)

shard = ManejoShard()

data = shard.collection.get()

print(
    "DOCUMENTOS:",
    len(
        data["documents"]
    )
)