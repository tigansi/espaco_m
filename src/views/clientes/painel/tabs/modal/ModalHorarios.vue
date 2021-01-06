<template>
  <ion-page>
    <ion-header>
      <ion-toolbar id="page">
        <ion-title style="color: white">Horários</ion-title>
        <ion-buttons slot="primary">
          <ion-button @click="modalClose()" style="color: white">
            Voltar
            <ion-icon style="color: white" slot="start" name="close"></ion-icon>
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
              <IonInputVue
                v-model="data"
                type="date"
                placeholder="dd/mm/aaaa"
              />
              <ion-icon slot="end" name="calendar"></ion-icon>
            </ion-item>
          </ion-list>
          <ion-button @click="buscaHorarios()" expand="block" id="btn_cad"
            >Mostrar horários</ion-button
          >
        </ion-card-content>
      </ion-card>
      <ion-card style="background-color:white">
        <ion-card-header>
          <ion-card-title class="ion-text-center"
            >Lista de horários</ion-card-title
          >
        </ion-card-header>
        <ion-card-content>
          <ion-grid>
            <ion-row>
              <div v-for="hor of hor_banco" :key="hor.id_horario">
                <ion-col>
                  <ion-button
                    @click="alertaConfirmaHorario(hor.id_horario, hor.data)"
                    style="width:73.213px; height:36px"
                    id="btn_hor"
                    >{{ hor.data }}</ion-button
                  >
                </ion-col>
              </div>
            </ion-row>
          </ion-grid>
        </ion-card-content>
      </ion-card>
    </ion-content>
  </ion-page>
</template>

<script>
import { toastController, alertController } from "@ionic/core";
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
    buscaHorarios() {
      let dados = {
        tipo: "list_hor_serv_prof",
        id_usuario: this.id_colab,
        id_servico: this.id_servico,
        dia: this.data,
        id_cliente: "",
      };
      Provider.provider("horarios", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            console.log(res.data.dados);
            this.hor_banco = res.data.dados;
          } else {
            this.presentToast(res.data.msg);
          }
        })
        .catch((error) => {
          console.log("TIMEOUT " + error);
        });
    },
    async alertaConfirmaHorario(id_hor, hor) {
      var servicos = "Serviço: " + this.nm_ser;
      var horarios = "Horario: " + hor;
      var profissi = "Profissional: " + this.nm_colab;

      var msg = profissi + "<br>" + horarios + "<br>" + servicos;

      const alert = await alertController.create({
        cssClass: "my-custom-class",
        header: "Atenção !",
        subHeader: "Deseja confirmar ?",
        message: msg,
        buttons: [
          {
            text: "Cancelar",
            role: "cancel",
            cssClass: "secondary",
            handler: (blah) => {
              console.log("Confirm Cancel:", blah);
            },
          },
          {
            text: "Confirmar",
            handler: () => {
              console.log("Confirm Okay");
              let dados = {
                tipo: "agenda_hor",
                id_hor: id_hor,
                id_cli: this.id_cliente,
              };
              Provider.provider("agenda", JSON.stringify(dados)).then((res) => {
                if (res.data.sucesso) {
                  this.alertaSucesso("Sucesso", res.data.msg);
                  this.$ionic.modalController.dismiss(true);
                }
              });
            },
          },
        ],
      });
      return alert.present();
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
        duration: 2000,
        color: "warning",
        position: "top",
        cssClass: "ion-toast",
      });
      toast.present();
    },
  },
  mounted() {
    var dados = JSON.parse(localStorage.getItem("isLogado"));
    this.id_cliente = dados.id_usuario;
  },
};
</script>

<style>
#page {
  --background: rgb(55, 52, 53);
}

#btn_escolha,
#btn_hor {
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
