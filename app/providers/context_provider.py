from app.shards.manejo.manejo_shard import (
    ManejoShard
)

class ContextProvider:

    def __init__(self):

        self.shard = ManejoShard()

    def search(
        self,
        tema: str
    ):

        resultados = self.shard.search(
            tema
        )

        fragmentos = resultados.split(
            "\n\n"
        )

        return fragmentos[0]

    def search_random(
        self
    ):

        return self.shard.search_random()