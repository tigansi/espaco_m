<template>
  <ion-page>
    <ion-content id="page">
      <ion-grid>
        <ion-row>
          <ion-col size="12">
            <ion-card style="background-color:white">
              <ion-card-header>
                <ion-grid>
                  <ion-row>
                    <ion-col size-md="9" size-sm="9">
                      <ion-card-subtitle>Bem vindo(a)</ion-card-subtitle>
                      <ion-card-title>{{ nome_col }} </ion-card-title>
                    </ion-col>
                    <ion-col>
                      <center>
                        <ion-avatar slot="end">
                          <ion-img
                            :src="
                              'http://192.168.8.7:5000/fotos?caminho=' + foto
                            "
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
                  <div v-for="age of agenda_dia" :key="age.id_agenda">
                    <ion-item>
                      <ion-avatar slot="start">
                        <ion-img
                          :src="
                            'http://192.168.8.7:5000/fotos?caminho=' + age.foto
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
                          @click="alertaConcluiServico(age.id_agenda)"
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
                </ion-list>
              </ion-card-content>
            </ion-card>

            <!--
            <ion-card style="background-color:white">
              <ion-card-content>
                <ion-list>
                  <ion-list-header>
                    <h1>Agenda geral</h1>
                  </ion-list-header>
                </ion-list>
              </ion-card-content>
            </ion-card>
            -->
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script>
import Provider from "@/services/provider";
import { alertController } from "@ionic/core";
export default {
  data() {
    return {
      nome_col: "",
      foto: "",
      id_usuario: "",
      agenda_dia: [],
    };
  },
  methods: {
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
    async alertaConcluiServico(id_agenda) {
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
                  this.alertaSucesso("Sucesso !!!", "Serviço concluido");
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
          }
        })
        .catch((error) => {
          console.log("TIMEOUT " + error);
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
