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
            <ion-card v-if="tot_aval_pend > 0" style="background-color:white">
              <ion-card-content>
                <ion-list id="form">
                  <ion-list-header>
                    <h1>Avaliações</h1>
                  </ion-list-header>
                  <div
                    v-for="(aval, index) in aval_pend"
                    :key="aval.id_avaliacao"
                  >
                    <div v-if="index == aval_pend.length - 1">
                      <ion-item>
                        <ion-label>
                          <h3>{{ aval.nm_avaliado }}</h3>
                          <p>Serviço: {{ aval.nm_servico }}</p>
                          <p>Valor: {{ aval.valor }} R$</p>
                          <p>Data: {{ aval.data }}</p>
                          <star-rating
                            v-bind:star-size="40"
                            v-model="avaliacao"
                          />
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
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script>
import { alertController, toastController } from "@ionic/core";
import Provider from "@/services/provider";
import StarRating from "vue-star-rating";
export default {
  components: {
    StarRating,
  },
  data() {
    return {
      nome: "",
      id_usuario: "",
      foto: "",
      agenda_cli: [],
      tot_age: 0,
      aval_pend: [],
      tot_aval_pend: 0,
      avaliacao: null,
      comentarios: "",
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
    verificaAvaliacaoPendente() {
      let dados = {
        tipo: "aval_pend",
        tp: "CLI_COL",
        id_avaliador: this.id_usuario,
      };
      Provider.provider("avaliacao", JSON.stringify(dados)).then((res) => {
        if (res.data.sucesso) {
          this.aval_pend = res.data.dados;
          this.tot_aval_pend = this.aval_pend.length;
        }
      });
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
            this.verificaAvaliacaoPendente();
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
    inicializa() {
      var dados = JSON.parse(localStorage.getItem("isLogado"));
      this.nome = dados.nm_usuario;
      this.foto = dados.foto;
      this.id_usuario = dados.id_usuario;
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
