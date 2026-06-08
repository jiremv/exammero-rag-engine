from app.shards.manejo.manejo_shard import ManejoShard

shard = ManejoShard()

print("========== PEATONES ==========")
print(
    shard.search(
        "peatones"
    )
)

print("========== VELOCIDAD ==========")
print(
    shard.search(
        "velocidad maxima"
    )
)

print("========== SEMAFORO ==========")
print(
    shard.search(
        "luz roja"
    )
)