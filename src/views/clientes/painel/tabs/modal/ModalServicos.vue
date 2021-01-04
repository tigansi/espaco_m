<template>
  <ion-page>
    <ion-header>
      <ion-toolbar id="page">
        <ion-title style="color: white">Serviços</ion-title>
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
            >Escolha um serviço</ion-card-title
          >
        </ion-card-header>
      </ion-card>

      <ion-card style="background-color:white;">
        <ion-card-content>
          <div v-if="tot_serv > 0">
            <div v-for="serv of servicos" :key="serv.id_servico">
              <ion-list>
                <ion-item>
                  <ion-grid>
                    <ion-row>
                      <ion-col size="7" size-md="9">
                        <ion-card-subtitle>{{
                          serv.nm_servico
                        }}</ion-card-subtitle>
                        <ion-card-subtitle
                          >R$ {{ serv.valor }}</ion-card-subtitle
                        >
                      </ion-col>
                      <ion-col size="5" size-md="3">
                        <ion-button
                          @click="
                            escolheServico(serv.id_servico, serv.nm_servico)
                          "
                          id="btn_escolha"
                          >Escolher</ion-button
                        >
                      </ion-col>
                    </ion-row>
                  </ion-grid>
                </ion-item>
              </ion-list>
            </div>
          </div>
          <div v-else>
            <ion-card-subtitle class="ion-text-center">
              Não há serviços disponíveis
            </ion-card-subtitle>
          </div>
        </ion-card-content>
      </ion-card>
    </ion-content>
  </ion-page>
</template>

<script>
import Provider from "@/services/provider.js";
import ModalHorarios from "./ModalHorarios";

export default {
  props: ["id_colaborador", "nm_colaborador"],
  data() {
    return {
      servicos: [],
      id_col: this.id_colaborador,
      nm_col: this.nm_colaborador,
      tot_serv: 0,
    };
  },
  methods: {
    modalClose() {
      this.$ionic.modalController.dismiss();
    },
    listaServicosProfissional() {
      let dados = {
        tipo: "lista_serv_prof",
        id_col: this.id_col,
      };
      Provider.provider("horarios", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            this.servicos = res.data.dados;
            this.tot_serv = this.servicos.length;
          } else {
            console.log(res.data.msg);
          }
        })
        .catch((error) => {
          console.log("TIMEOUT " + error);
        });
    },
    async escolheServico(id_servico, nm_servico) {
      let modal = await this.$ionic.modalController.create({
        component: ModalHorarios,
        componentProps: {
          propsData: {
            id_servico: id_servico,
            id_col: this.id_col,
            nm_col: this.nm_col,
            nm_ser: nm_servico,
          },
        },
      });
      modal.present();

      let res = await modal.onDidDismiss();
      if (res.data) {
        this.$ionic.modalController.dismiss();
      }
    },
  },
  mounted() {
    this.listaServicosProfissional();
  },
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
</style>
