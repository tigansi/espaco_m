<template>
  <ion-page>
    <ion-content id="page">
      <ion-card style="background-color:white">
        <ion-card-content>
          <ion-list>
            <ion-list-header>
              <h1>Profissionais</h1>
            </ion-list-header>
            <div v-for="col of colaboradores" :key="col.id_usuario">
              <ion-item>
                <ion-avatar slot="start">
                  <ion-img
                    :src="'http://192.168.8.7:5000/fotos?caminho=' + col.foto"
                  ></ion-img>
                </ion-avatar>
                <ion-label>
                  <h3>{{ col.nm_usuario }}</h3>
                  <p>Funcionário(a)</p>
                </ion-label>

                <ion-buttons>
                  <ion-button slot="end">Agendar</ion-button>
                </ion-buttons>
              </ion-item>
            </div>
          </ion-list>
        </ion-card-content>
      </ion-card>
    </ion-content>
  </ion-page>
</template>

<script>
import Provider from "@/services/provider.js";
import { toastController } from "@ionic/core";
export default {
  data() {
    return {
      colaboradores: [],
    };
  },
  methods: {
    listaColaboradores() {
      let dados = {
        tipo: "lista_colaboradores",
        nome: "",
        email: "",
        status: "",
        tp: "COL",
      };
      Provider.provider("usuarios", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            this.colaboradores = res.data.dados;
          } else {
            this.presentToast(res.data.msg);
          }
        })
        .catch((error) => {
          console.log("TIMEOUT " + error);
        });
    },
    async presentToast(msg) {
      const toast = await toastController.create({
        message: msg,
        duration: 2000,
        color: "warning",
        position: "top",
        cssClass: "ion-toast",
      });
      toast.present();
    },
  },
  mounted() {
    this.listaColaboradores();
  },
};
</script>

<style>
#page {
  --background: rgb(55, 52, 53);
}
</style>
