from app.shards.manejo.manejo_shard import ManejoShard

shard = ManejoShard()

for tema in [
    "PARE",
    "PEATONES",
    "SEMAFORO",
    "VELOCIDAD",
    "ADELANTAR"
]:
    print("\n================")
    print(tema)
    print("================")

    print(
        shard.search(tema)
    )