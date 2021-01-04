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
      <ion-card style="background-color:white">
        <ion-card-header>
          <ion-card-title class="ion-text-center">Profissionais</ion-card-title>
        </ion-card-header>
        <ion-card-content>
          <ion-list>
            <div v-if="tot_col > 0">
              <div v-for="col of colaboradores" :key="col.id_col">
                <ion-item>
                  <ion-avatar slot="start">
                    <ion-img
                      :src="'http://192.168.8.7:5000/fotos?caminho=' + col.foto"
                    ></ion-img>
                  </ion-avatar>
                  <ion-label>
                    <h3>{{ col.nm_col }}</h3>
                    <p>Funcionário(a)</p>
                  </ion-label>

                  <ion-button
                    @click="escolheProf(col.id_col, col.nm_col)"
                    id="btn_agendar"
                    slot="end"
                    >Horários</ion-button
                  >
                </ion-item>
              </div>
            </div>
            <div v-else>
              <ion-card-subtitle class="ion-text-center">
                Não há profissionais disponíveis
              </ion-card-subtitle>
            </div>
          </ion-list>
        </ion-card-content>
      </ion-card>
    </ion-content>
  </ion-page>
</template>

<script>
import Provider from "@/services/provider";
import ModalHorarios from "./ModalHorarios";

export default {
  props: ["id_servico", "nm_servico"],
  data() {
    return {
      id_serv: this.id_servico,
      nm_serv: this.nm_servico,
      colaboradores: [],
      tot_col: 0,
    };
  },
  methods: {
    modalClose() {
      this.$ionic.modalController.dismiss();
    },
    listaProfissionaisServico() {
      let dados = {
        tipo: "lista_prof_serv",
        id_servico: this.id_serv,
      };
      Provider.provider("horarios", JSON.stringify(dados)).then((res) => {
        if (res.data.sucesso) {
          this.colaboradores = res.data.dados;
          this.tot_col = this.colaboradores.length;
        }
      });
    },
    async escolheProf(id_col, nm_col) {
      let modal = await this.$ionic.modalController.create({
        component: ModalHorarios,
        componentProps: {
          propsData: {
            id_servico: this.id_serv,
            id_col: id_col,
            nm_col: nm_col,
            nm_ser: this.nm_serv,
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
  created() {
    this.listaProfissionaisServico();
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
