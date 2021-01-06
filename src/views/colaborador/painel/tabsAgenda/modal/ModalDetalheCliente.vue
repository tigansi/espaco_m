<template>
  <ion-page>
    <ion-header>
      <ion-toolbar id="page">
        <ion-title style="color: white">Detalhes</ion-title>
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
          <center>
            <ion-avatar>
              <ion-img
                :src="'http://192.168.8.7:5000/fotos?caminho=' + foto"
              ></ion-img>
            </ion-avatar>
            <ion-label>
              <h2>{{ nm_cli }}</h2>
              <p>
                {{ nota }}
                <ion-icon name="star"></ion-icon>
              </p>
            </ion-label>
          </center>
          <ion-list id="form">
            <ion-item>
              <ion-label position="floating">E-mail</ion-label>
              <IonInputVue v-model="email" />
              <ion-icon slot="end" name="call"></ion-icon>
            </ion-item>
            <ion-item>
              <ion-label position="floating">Telefone</ion-label>
              <IonInputVue v-model="cel" />
              <ion-icon slot="end" name="mail"></ion-icon>
            </ion-item>
          </ion-list>
        </ion-card-content>
      </ion-card>
      <ion-card style="background-color:white">
        <ion-card-content v-if="tot_com > 0">
          <ion-list id="form">
            <div v-for="com of comentarios" :key="com.id_comentario">
              <ion-item>
                <ion-label position="floating">Cometário</ion-label>
                <IonTextareaVue v-bind:value="com.comentario"></IonTextareaVue>
                <ion-icon slot="end" name="chatbox"></ion-icon>
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

export default {
  components: {},
  props: ["id_cliente"],
  data() {
    return {
      id_cli: this.id_cliente,
      nm_cli: "",
      email: "",
      cel: "",
      foto: "",
      nota: 0,
      comentarios: [],
      tot_com: 0,
    };
  },
  methods: {
    modalClose() {
      this.$ionic.modalController.dismiss();
    },
    buscaDadosCliente() {
      let dados = {
        tipo: "info_user",
        tp: "COL",
        id: this.id_cli,
      };
      Provider.provider("usuarios", JSON.stringify(dados)).then((res) => {
        if (res.data.sucesso) {
          this.comentarios = res.data.comentarios;
          this.nm_cli = res.data.dados[0].nm_usuario;
          this.email = res.data.dados[0].email;
          this.cel = res.data.dados[0].celular;
          this.foto = res.data.dados[0].foto;
          this.nota = res.data.dados[0].nota;
          this.tot_com = this.comentarios.length;
        }
      });
    },
  },
  mounted() {
    this.buscaDadosCliente();
    console.log(this.nota);
  },
};
</script>

<style>
#page {
  --background: rgb(55, 52, 53);
}
</style>
