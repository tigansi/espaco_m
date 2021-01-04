<template>
  <ion-page>
    <ion-content id="page">
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
                      <p>{{ nome_col }}</p>
                      <p>Avaliação:</p>
                    </ion-label>
                  </ion-item>
                </ion-list>
              </ion-card-content>
            </ion-card>
            <ion-card style="background-color: white">
              <ion-card-content>
                <ion-list>
                  <ion-list-header>
                    <h1>Agenda do dia</h1>
                  </ion-list-header>
                  <div v-if="tot_agen_dia > 0">
                    <div v-for="age of agenda_dia" :key="age.id_agenda">
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
                          <h3>{{ age.nm_cliente }}</h3>
                          <p>{{ age.nm_servico }}</p>
                          <p>{{ age.data }}</p>
                        </ion-label>

                        <div v-if="age.is_andamento">
                          <ion-button
                            @click="paraServico(age.id_agenda)"
                            color="warning"
                            id="btn_play"
                            shape="round"
                          >
                            <ion-icon slot="icon-only" name="stop"></ion-icon>
                          </ion-button>
                          <ion-button
                            @click="
                              alertaConcluiServico(
                                age.id_agenda,
                                age.id_cliente
                              )
                            "
                            color="success"
                            id="btn_play"
                            shape="round"
                          >
                            <ion-icon
                              slot="icon-only"
                              name="check-mark-done-circle"
                            ></ion-icon>
                          </ion-button>
                        </div>
                        <div v-else>
                          <ion-button
                            @click="alertaIniciaServico(age.id_agenda)"
                            color="success"
                            id="btn_play"
                            shape="round"
                          >
                            <ion-icon slot="icon-only" name="play"></ion-icon>
                          </ion-button>
                        </div>
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
import Provider from "@/services/provider";
import { alertController } from "@ionic/core";
import ModalAvaliacao from "./modal/ModalAvaliacao";

export default {
  data() {
    return {
      nome_col: "",
      foto: "",
      id_usuario: "",
      agenda_dia: [],
      tot_agen_dia: 0,
      avaliacao_prof: null,
    };
  },
  methods: {
    async abreModalAvaliacao(id_agenda, id_cliente) {
      id_cliente;
      let modal = await this.$ionic.modalController.create({
        component: ModalAvaliacao,
        componentProps: {
          propsData: {
            id_agenda: id_agenda,
            id_cliente: id_cliente,
            id_usuario: this.id_usuario,
          },
        },
      });
      modal.present();
    },
    paraServico(id_agenda) {
      id_agenda;
      let dados = {
        tipo: "para_serv",
        id_agenda: id_agenda,
      };
      Provider.provider("agenda", JSON.stringify(dados)).then((res) => {
        if (res.data.sucesso) {
          this.listaAgendaProf();
        }
      });
    },
    async alertaIniciaServico(id_agenda) {
      const alert = await alertController.create({
        cssClass: "my-custom-class",
        header: "Atenção !",
        message: "Deseja dar inicío ao serviço ?",
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
              let dados = {
                tipo: "inicia_serv",
                id_agenda: id_agenda,
              };
              Provider.provider("agenda", JSON.stringify(dados)).then((res) => {
                if (res.data.sucesso) {
                  this.listaAgendaProf();
                }
              });
            },
          },
        ],
      });
      return alert.present();
    },
    async alertaConcluiServico(id_agenda, id_cliente) {
      const alert = await alertController.create({
        cssClass: "my-custom-class",
        header: "Atenção !",
        message: "Deseja concluir o serviço ?",
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
              let dados = {
                tipo: "conclui_serv",
                id_agenda: id_agenda,
              };
              Provider.provider("agenda", JSON.stringify(dados)).then((res) => {
                if (res.data.sucesso) {
                  /*this.alertaSucesso(
                    "Sucesso !!!",
                    "Serviço concluido com sucesso"
                  );*/
                  this.abreModalAvaliacao(id_agenda, id_cliente);
                  this.listaAgendaProf();
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
    listaAgendaProf() {
      let dados = {
        tipo: "list_agenda_prof",
        id_col: this.id_usuario,
      };
      Provider.provider("agenda", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            this.agenda_dia = res.data.dados;
            this.tot_agen_dia = this.agenda_dia.length;
          }
        })
        .catch((error) => {
          console.log("TIMEOUT " + error);
        });
    },
    buscaAvaliacao() {
      let dados = {
        tipo: "aval_prof",
        id_prof: this.id_usuario,
      };
      Provider.provider("avaliacao", JSON.stringify(dados)).then((res) => {
        if (res.data.sucesso) {
          this.avaliacao_prof = res.data.dados;
        }
      });
    },
  },
  mounted() {
    var dados = JSON.parse(localStorage.getItem("isLogado"));
    this.nome_col = dados.nm_usuario;
    this.foto = dados.foto;
    this.id_usuario = dados.id_usuario;
    this.listaAgendaProf();
  },
};
</script>

<style>
#page {
  --background: rgb(55, 52, 53);
}
</style>
