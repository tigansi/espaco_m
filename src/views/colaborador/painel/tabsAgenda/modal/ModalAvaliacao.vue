<template>
  <ion-app>
    <ion-header>
      <ion-toolbar id="page">
        <ion-title style="color: white">Avaliação</ion-title>
        <ion-buttons slot="primary">
          <ion-button @click="modalClose()" style="color: white">
            Voltar
            <ion-icon style="color: white" slot="start" name="close"></ion-icon>
          </ion-button>
        </ion-buttons>
      </ion-toolbar>
    </ion-header>
    <ion-content id="page">
      <ion-card style="background-color:white">
        <ion-card-content>
          <ion-list id="form">
            <ion-list-header>
              <h1>Avaliação do cliente</h1>
            </ion-list-header>
            <ion-item>
              <star-rating v-bind:star-size="40" v-model="avaliacao" />
            </ion-item>
            <ion-item>
              <ion-label position="floating">Comentários</ion-label>
              <IonTextareaVue
                rows="5"
                cols="20"
                placeholder="Escreva algum comentário..."
              />
            </ion-item>
          </ion-list>
          <br />
          <ion-button
            @click="concluirComAvaliacao()"
            color="success"
            expand="block"
            >Avaliar o cliente</ion-button
          >
          <ion-button
            @click="concluirSemAvaliacao()"
            color="medium"
            expand="block"
            >Não quero avaliar</ion-button
          >
        </ion-card-content>
      </ion-card>
    </ion-content>
  </ion-app>
</template>

<script>
import StarRating from "vue-star-rating";
import { toastController } from "@ionic/core";
export default {
  components: {
    StarRating,
  },
  props: ["id_agenda"],
  data() {
    return {
      avaliacao: null,
      comentarios: "",
      id_agen: this.id_agenda,
    };
  },
  methods: {
    modalClose() {
      this.$ionic.modalController.dismiss();
    },
    concluirSemAvaliacao() {},
    concluirComAvaliacao() {
      console.log(this.avaliacao);
      if (this.avaliacao == 0 || this.avaliacao == null) {
        this.presentToast("A avaliação deve ser maior que zero");
      } else {
        //
      }
    },
    async presentToast(msg) {
      const toast = await toastController.create({
        message: msg,
        duration: 3000,
        color: "warning",
        position: "top",
        cssClass: "ion-toast",
      });
      toast.present();
    },
  },
};
</script>

<style>
#page {
  --background: rgb(55, 52, 53);
}

#form ion-textarea {
  font-family: "Poppins", sans-serif;
}

#form ion-label {
  font-family: "Poppins", sans-serif;
  font-weight: bold;
  color: rgb(55, 52, 53);
}
</style>
