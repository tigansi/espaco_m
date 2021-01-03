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
      <ion-card style="background-color: white">
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
                v-model="comentarios"
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
import { toastController, alertController } from "@ionic/core";
import Provider from "@/services/provider";
export default {
  components: {
    StarRating,
  },
  props: ["id_cliente", "id_agenda", "id_usuario"],
  data() {
    return {
      avaliacao: null,
      comentarios: "",
      id_cli: this.id_cliente,
      id_agen: this.id_agenda,
      id_user: this.id_usuario,
    };
  },
  methods: {
    modalClose() {
      this.$ionic.modalController.dismiss();
    },
    concluirSemAvaliacao() {
      this.presentToast("Avaliação não efetuada");
      this.modalClose();
    },
    concluirComAvaliacao() {
      console.log(this.id_agen);
      if (this.avaliacao == 0 || this.avaliacao == null) {
        this.presentToast("A avaliação deve ser maior que zero");
      } else {
        let dados = {
          tipo: "cad_aval",
          id_agenda: this.id_agen,
          id_avaliador: this.id_user,
          id_avaliado: this.id_cli,
          comentarios: this.comentarios,
          avaliacao: this.avaliacao,
          tp: "COL_CLI",
        };
        Provider.provider("avaliacao", JSON.stringify(dados)).then((res) => {
          if (res.data.sucesso) {
            this.alertaSucesso("Sucesso !!!", res.data.msg);
            this.modalClose();
          }
        });
      }
    },
    async alertaSucesso(tipo, msg) {
      const alert = await alertController.create({
        cssClass: "my-custom-class",
        header: tipo,
        message: msg,
        buttons: ["OK"],
      });

      await alert.present();
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
