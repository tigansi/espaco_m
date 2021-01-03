<template>
  <ion-page>
    <ion-content id="page">
      <ion-grid>
        <ion-row>
          <ion-col size="12">
            <ion-card style="background-color:white;">
              <ion-card-header>
                <ion-grid>
                  <ion-row>
                    <ion-col size-md="9" size-sm>
                      <ion-card-subtitle>Bem vindo(a)</ion-card-subtitle>
                      <ion-card-title>{{ nome }} </ion-card-title>
                    </ion-col>
                    <ion-col>
                      <center>
                        <ion-avatar>
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
                    <h1>Serviços</h1>
                  </ion-list-header>
                  <div v-for="serv of servicos" :key="serv.id_servico">
                    <ion-item>
                      <ion-label>
                        <h3>{{ serv.nm_servico }}</h3>
                        <p>Valor: {{ serv.valor }} R$</p>
                        <p>Duração: {{ serv.duracao }} minutos</p>
                      </ion-label>
                      <ion-button
                        @click="abreModalProf(serv.id_servico, serv.nm_servico)"
                        id="btn_agendar"
                        shape="round"
                        >Agendar</ion-button
                      >
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
import Provider from "@/services/provider";
import ModalProfissionais from "./modal/ModalProfissionais";

export default {
  data() {
    return {
      nome: "",
      id_usuario: "",
      foto: "",
      servicos: [],
    };
  },
  methods: {
    listaServicos() {
      let dados = {
        tipo: "list_serv",
      };
      Provider.provider("servicos", JSON.stringify(dados)).then((res) => {
        if (res.data.sucesso) {
          this.servicos = res.data.dados;
        }
      });
    },
    async abreModalProf(id_servico, nm_servico) {
      console.log(id_servico);
      let modal = await this.$ionic.modalController.create({
        component: ModalProfissionais,
        componentProps: {
          propsData: {
            id_servico: id_servico,
            nm_servico: nm_servico,
          },
        },
      });
      modal.present();
    },
  },
  mounted() {
    var dados = JSON.parse(localStorage.getItem("isLogado"));
    this.nome = dados.nm_usuario;
    this.foto = dados.foto;
    this.id_usuario = dados.id_usuario;
    this.listaServicos();
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
