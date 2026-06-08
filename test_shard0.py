from app.shards.manejo.manejo_shard import ManejoShard

shard = ManejoShard()

context = shard.search(
    "señal stop"
)

print(context)