<template>
  <ion-page>
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
              <h1>Avaliações</h1>
            </ion-list-header>
            <div v-for="(aval, index) in aval_pend" :key="aval.id_avaliacao">
              <div v-if="index == aval_pend.length - 1">
                <ion-item>
                  <ion-label>
                    <h3>{{ aval.nm_avaliado }}</h3>
                    <p>Serviço: {{ aval.nm_servico }}</p>
                    <p>Valor: {{ aval.valor }} R$</p>
                    <p>Data: {{ aval.data }}</p>
                    <star-rating v-bind:star-size="40" v-model="avaliacao" />
                  </ion-label>
                </ion-item>

                <ion-item>
                  <ion-label position="floating">Comentários</ion-label>
                  <IonTextareaVue
                    v-model="comentarios"
                    rows="3"
                    cols="20"
                    placeholder="Escreva algum comentário..."
                  />
                </ion-item>
                <br />
                <ion-button
                  @click="
                    realizaAvaliacao(
                      aval.id_agenda,
                      aval.id_cliente,
                      aval.id_avaliacao
                    )
                  "
                  color="success"
                  expand="block"
                  >Avaliar profissional</ion-button
                >
              </div>
            </div>
          </ion-list>
        </ion-card-content>
      </ion-card>
    </ion-content>
  </ion-page>
</template>

<script>
import StarRating from "vue-star-rating";
import { alertController, toastController } from "@ionic/core";
import Provider from "@/services/provider";

export default {
  components: {
    StarRating,
  },
  props: ["aval"],
  data() {
    return {
      aval_pend: [],
      tot_aval_pend: 0,
      avaliacao: null,
      comentarios: "",
    };
  },
  methods: {
    modalClose() {
      this.$ionic.modalController.dismiss();
    },
    realizaAvaliacao(id_agenda, id_avaliado, id_avaliacao) {
      //alert(id_avaliacao);
      if (this.avaliacao == 0 || this.avaliacao == null) {
        this.presentToast("A avaliação deve ser maior que zero");
      } else {
        let dados = {
          tipo: "cad_aval",
          id_avaliacao: id_avaliacao,
          id_agenda: id_agenda,
          id_avaliador: this.id_usuario,
          id_avaliado: id_avaliado,
          comentarios: this.comentarios,
          avaliacao: this.avaliacao,
          tp: "CLI_COL",
        };
        Provider.provider("avaliacao", JSON.stringify(dados)).then((res) => {
          if (res.data.sucesso) {
            this.alertaSucesso("Sucesso !!!", res.data.msg);
            this.aval_pend = [];
            this.avaliacao = 0;
            this.modalClose();
            //this.verificaAvaliacaoPendente();
          }
        });
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
    async alertaSucesso(tipo, msg) {
      const alert = await alertController.create({
        cssClass: "my-custom-class",
        header: tipo,
        message: msg,
        buttons: ["OK"],
      });

      await alert.present();
    },
  },
  mounted() {
    this.aval_pend = this.aval;
  },
};
</script>

<style>
#page {
  --background: rgb(55, 52, 53);
}

#form ion-input {
  font-family: "Poppins", sans-serif;
}

#form ion-label {
  font-family: "Poppins", sans-serif;
  font-weight: bold;
  color: rgb(55, 52, 53);
}
</style>
