<template>
  <ion-page>
    <ion-header>
      <ion-toolbar id="page">
        <ion-title style="color: white">Horários</ion-title>
        <ion-buttons slot="primary">
          <ion-button @click="modalClose()" style="color: white">
            Sair
            <ion-icon style="color: white" slot="" name="close"></ion-icon>
          </ion-button>
        </ion-buttons>
      </ion-toolbar>
    </ion-header>
    <ion-content id="page">
      <ion-card style="background-color:white;">
        <ion-card-header>
          <ion-card-title class="ion-text-center"
            >Escolha um horário</ion-card-title
          >
        </ion-card-header>
        <ion-card-content>
          <ion-list id="form">
            <ion-item>
              <ion-label position="floating">Escolha uma data</ion-label>
              <IonInputVue v-model="data" type="date" />
              <ion-icon slot="end" name="calendar"></ion-icon>
            </ion-item>
          </ion-list>
          <ion-button @click="listaHorarios()" expand="block" id="btn_cad"
            >Mostrar horários</ion-button
          >
        </ion-card-content>
      </ion-card>
    </ion-content>
  </ion-page>
</template>

<script>
import { toastController } from "@ionic/core";
import Provider from "@/services/provider.js";
export default {
  props: ["id_servico", "id_col", "nm_col", "nm_ser"],
  data() {
    return {
      hor_banco: [],
      id_colab: this.id_col,
      nm_colab: this.nm_col,
      id_servi: this.id_servico,
      nm_servi: this.nm_ser,
      data: "",
    };
  },
  methods: {
    modalClose() {
      this.$ionic.modalController.dismiss();
    },
    listaHorarios() {
      let dados = {
        tipo: "list_hor",
        id_usuario: this.id_colab,
      };
      Provider.provider("horarios", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            this.hor_banco = res.data.dados;
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
  mounted() {},
};
</script>

<style>
#page {
  --background: rgb(55, 52, 53);
}

#btn_escolha {
  --background: rgb(60, 187, 178);
  --background-activated: rgb(60, 187, 178);
  --background-hover: rgb(60, 187, 178);
}

#form ion-input {
  font-family: "Poppins", sans-serif;
}

#form ion-label {
  font-family: "Poppins", sans-serif;
  font-weight: bold;
  color: rgb(55, 52, 53);
}

#btn_cad {
  --background: rgb(55, 52, 53);
  --background-activated: rgb(55, 52, 53);
  --background-hover: rgb(55, 52, 53);
}
</style>
