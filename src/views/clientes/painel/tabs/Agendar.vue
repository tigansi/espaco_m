<template>
  <ion-page>
    <ion-content id="page">
      <ion-refresher mode="md" slot="fixed" @ionRefresh="doRefresh($event)">
        <ion-refresher-content
          pulling-icon="chevron-down-circle-outline"
          refreshing-text="Atualizando..."
        ></ion-refresher-content>
      </ion-refresher>
      <ion-grid>
        <ion-row>
          <ion-col size="12">
            <ion-card style="background-color: white">
              <ion-card-content>
                <ion-list>
                  <ion-item>
                    <ion-avatar slot="start">
                      <ion-img
                        :src="'http://192.168.8.7:5000/fotos?caminho=' + foto"
                      ></ion-img>
                    </ion-avatar>
                    <ion-label>
                      <h2>Bem vindo(a)</h2>
                      <p>{{ nome }}</p>
                      <p>Cliente</p>
                    </ion-label>
                  </ion-item>
                </ion-list>
              </ion-card-content>
            </ion-card>
            <ion-card style="background-color:white">
              <ion-card-content>
                <ion-list>
                  <ion-list-header>
                    <h1>Agendamentos</h1>
                  </ion-list-header>
                  <div v-if="tot_age > 0">
                    <div v-for="age of agenda_cli" :key="age.id_agenda">
                      <ion-item>
                        <ion-avatar slot="start">
                          <ion-img
                            :src="
                              'http://192.168.8.7:5000/fotos?caminho=' +
                                age.foto
                            "
                          ></ion-img>
                        </ion-avatar>
                        <ion-label>
                          <h3>{{ age.nm_usuario }}</h3>
                          <p>{{ age.nm_servico }}</p>
                          <p>{{ age.data }}</p>
                        </ion-label>
                        <ion-button
                          @click="
                            alertaConfirmaDesistencia(
                              age.id_agenda,
                              age.id_horario
                            )
                          "
                          color="warning"
                          shape="round"
                          >Desistir</ion-button
                        >
                      </ion-item>
                    </div>
                  </div>
                  <div v-else>
                    <br />
                    <ion-card-subtitle class="ion-text-center"
                      >Não há agendamentos</ion-card-subtitle
                    >
                  </div>
                </ion-list>
              </ion-card-content>
            </ion-card>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script>
import { alertController, toastController } from "@ionic/core";
import Provider from "@/services/provider";
import ModalAvalPend from "./modal/ModalAvalPend";

export default {
  data() {
    return {
      nome: "",
      id_usuario: "",
      foto: "",
      agenda_cli: [],
      tot_age: 0,
    };
  },
  methods: {
    async alertaConfirmaDesistencia(id_agenda, id_horario) {
      const alert = await alertController.create({
        cssClass: "my-custom-class",
        header: "Atenção !",
        message: "Deseja desistir do horário ?",
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
                tipo: "desiste_agenda",
                id_horario: id_horario,
                id_agenda: id_agenda,
                id_cli: this.id_cliente,
              };
              Provider.provider("agenda", JSON.stringify(dados)).then((res) => {
                if (res.data.sucesso) {
                  this.agenda_cli = [];
                  this.listaAgendaCliente();
                  this.alertaSucesso("Sucesso !!!", res.data.msg);
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
    listaAgendaCliente() {
      let dados = {
        tipo: "list_agenda_cli",
        id_usuario: this.id_usuario,
      };
      Provider.provider("agenda", JSON.stringify(dados)).then((res) => {
        if (res.data.sucesso) {
          this.agenda_cli = res.data.dados;
          this.tot_age = this.agenda_cli.length;
        }
      });
    },
    async verificaAvaliacaoPendente() {
      let dados = {
        tipo: "aval_pend",
        tp: "CLI_COL",
        id_avaliador: this.id_usuario,
      };
      Provider.provider("avaliacao", JSON.stringify(dados)).then((res) => {
        if (res.data.sucesso) {
          this.abreModalAvalPend(res.data.dados);
        } else {
          console.log(res.data.msg);
        }
      });
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
    async abreModalAvalPend(aval_pend) {
      let modal = await this.$ionic.modalController.create({
        component: ModalAvalPend,
        componentProps: {
          propsData: {
            aval: aval_pend,
          },
        },
      });
      modal.present();
    },
    inicializa() {
      var dados = JSON.parse(localStorage.getItem("isLogado"));
      this.nome = dados.nm_usuario;
      this.foto = dados.foto;
      this.id_usuario = dados.id_usuario;
    },
    doRefresh(event) {
      this.inicializa();
      this.listaAgendaCliente();
      this.verificaAvaliacaoPendente();

      setTimeout(() => {
        console.log("Async operation has ended");
        event.target.complete();
      }, 2000);
    },
  },
  mounted() {
    this.inicializa();
    this.listaAgendaCliente();
    this.verificaAvaliacaoPendente();
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

ion-toast {
  text-align: center;
}
</style>
