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
                    <h1>Profissionais</h1>
                  </ion-list-header>
                  <div v-for="col of colaboradores" :key="col.id_usuario">
                    <ion-item>
                      <ion-avatar slot="start">
                        <ion-img
                          :src="
                            'http://192.168.8.7:5000/fotos?caminho=' + col.foto
                          "
                        ></ion-img>
                      </ion-avatar>
                      <ion-label>
                        <h3>{{ col.nm_usuario }}</h3>
                        <p>
                          <star-rating
                            :show-rating="true"
                            v-bind:star-size="12"
                            :rating="parseFloat(col.nota)"
                            :increment="0.01"
                          />
                        </p>
                        <p>Funcionário(a)</p>
                      </ion-label>
                      <div>
                        <ion-button
                          @click="
                            mostraServicosProf(col.id_usuario, col.nm_usuario)
                          "
                          id="btn_agendar"
                        >
                          <ion-icon
                            slot="icon-only"
                            name="calendar-clear"
                          ></ion-icon></ion-button
                        ><br />
                        <ion-button
                          @click="abreModalDetalheColaborador(col.id_usuario)"
                          color="medium"
                        >
                          <ion-icon
                            slot="icon-only"
                            name="information-circle"
                          ></ion-icon>
                        </ion-button>
                      </div>
                    </ion-item>
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
import Provider from "@/services/provider.js";
import { toastController } from "@ionic/core";
import ModalServicos from "./modal/ModalServicos";
import ModalDetalheCol from "./modal/ModalDetalheCol";
import StarRating from "vue-star-rating";

export default {
  components: {
    StarRating,
  },
  data() {
    return {
      id_cliente: "",
      colaboradores: [],
      nome: "",
      foto: "",
    };
  },
  methods: {
    async mostraServicosProf(id_colaborador, nm_colaborador) {
      console.log(id_colaborador);

      let modal = await this.$ionic.modalController.create({
        component: ModalServicos,
        componentProps: {
          propsData: {
            id_colaborador: id_colaborador,
            nm_colaborador: nm_colaborador,
          },
        },
      });
      modal.present();
    },
    async abreModalDetalheColaborador(id_colaborador) {
      // alert(id_cliente);
      let modal = await this.$ionic.modalController.create({
        component: ModalDetalheCol,
        componentProps: {
          propsData: {
            id_colaborador: id_colaborador,
          },
        },
      });
      modal.present();
    },
    listaColaboradores() {
      let dados = {
        tipo: "lista_colaboradores",
        nome: "",
        email: "",
        status: "",
        tp: "COL",
      };
      Provider.provider("usuarios", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            this.colaboradores = res.data.dados;
          } else {
            this.presentToast(res.data.msg);
          }
        })
        .catch((error) => {
          console.log("TIMEOUT " + error);
        });
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
    this.nome = dados.nm_usuario;
    this.foto = dados.foto;
    this.listaColaboradores();
  },
};
</script>

<style>
#page {
  --background: rgb(55, 52, 53);
}

#btn_agendar {
  --background: rgb(60, 187, 178);
  --background-activated: rgb(60, 187, 178);
  --background-hover: rgb(60, 187, 178);
}
</style>
