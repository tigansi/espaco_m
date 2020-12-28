<template>
  <ion-page>
    <ion-content id="page">
      <ion-card style="background-color:white;">
        <ion-card-header>
          <ion-grid>
            <ion-row>
              <ion-col size-md="9" size-sm>
                <ion-card-subtitle>Bem vindo(a)</ion-card-subtitle>
                <ion-card-title>{{ nome }} </ion-card-title>
              </ion-col>
              <ion-col>
                <center>
                  <ion-avatar>
                    <ion-img
                      :src="'http://192.168.8.7:5000/fotos?caminho=' + foto"
                    ></ion-img>
                  </ion-avatar>
                </center>
              </ion-col>
            </ion-row>
          </ion-grid>
        </ion-card-header>
      </ion-card>
      <ion-card style="background-color:white">
        <ion-card-content>
          <ion-list>
            <ion-list-header>
              <h1>Agenda do dia</h1>
            </ion-list-header>
            <div v-for="age of agenda_cli" :key="age.id_agenda">
              <ion-item>
                <ion-avatar slot="start">
                  <ion-img
                    :src="'http://192.168.8.7:5000/fotos?caminho=' + age.foto"
                  ></ion-img>
                </ion-avatar>
                <ion-label>
                  <h3>{{ age.nm_usuario }}</h3>
                  <p>{{ age.nm_servico }}</p>
                  <p>{{ age.data }}</p>
                </ion-label>
              </ion-item>
            </div>
          </ion-list>
        </ion-card-content>
      </ion-card>
    </ion-content>
  </ion-page>
</template>

<script>
import Provider from "@/services/provider";
export default {
  data() {
    return {
      nome: "",
      id_usuario: "",
      foto: "",
      agenda_cli: [],
    };
  },
  methods: {
    listaAgendaCliente() {
      let dados = {
        tipo: "list_agenda_cli",
        id_usuario: this.id_usuario,
      };
      Provider.provider("agenda", JSON.stringify(dados)).then((res) => {
        if (res.data.sucesso) {
          this.agenda_cli = res.data.dados;
        }
      });
    },
    inicializa() {
      var dados = JSON.parse(localStorage.getItem("isLogado"));
      this.nome = dados.nm_usuario;
      this.foto = dados.foto;
      this.id_usuario = dados.id_usuario;
    },
  },
  mounted() {
    this.inicializa();
    this.listaAgendaCliente();
  },
};
</script>

<style>
#page {
  --background: rgb(55, 52, 53);
}
</style>
