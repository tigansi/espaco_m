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
                    <ion-col size="8" size-sm size-md="9">
                      <ion-card-subtitle>Bem vindo(a)</ion-card-subtitle>
                      <ion-card-title>{{ nome_adm }} </ion-card-title>
                    </ion-col>
                    <ion-col size="4" size-sm size-md="3">
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
          </ion-col>
          <ion-col>
            <ion-card style="background-color:white">
              <ion-card-content>
                <div id="form">
                  <ion-list>
                    <ion-list-header>
                      <h1>Listar colaboradores</h1>
                    </ion-list-header>
                    <ion-item>
                      <ion-label position="floating">Nome</ion-label>
                      <IonInputVue v-model="form.nome" />
                      <ion-icon slot="end" name="person"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <ion-label position="floating">E-mail</ion-label>
                      <IonInputVue v-model="form.email" />
                      <ion-icon slot="end" name="mail"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <ion-label position="floating">Status</ion-label>
                      <IonSelectVue v-model="form.status">
                        <ion-select-option value="0"
                          >Demitido</ion-select-option
                        >
                        <ion-select-option value="1"
                          >Em atividade</ion-select-option
                        >
                      </IonSelectVue>
                      <ion-icon slot="end" name="checkmark-done"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <ion-label position="floating">Tipo de usuário</ion-label>
                      <IonSelectVue v-model="form.tp">
                        <ion-select-option value="CLI"
                          >Cliente</ion-select-option
                        >
                        <ion-select-option value="COL"
                          >Funcionário</ion-select-option
                        >
                        <ion-select-option value="ADM"
                          >Administrador</ion-select-option
                        >
                      </IonSelectVue>
                      <ion-icon slot="end" name="people"></ion-icon>
                    </ion-item>
                  </ion-list>
                  <br />

                  <ion-button
                    @click="efetuaPesquisa"
                    expand="block"
                    id="btn_cad"
                    >Pesquisar</ion-button
                  >
                </div>
              </ion-card-content>
            </ion-card>
          </ion-col>

          <ion-col size-md="6" size="12" size-sm>
            <div v-for="col of colaboradores" :key="col.id_usuario">
              <ion-card style="background-color:white">
                <ion-card-content>
                  <ion-grid>
                    <ion-row>
                      <ion-col>
                        <ion-card-subtitle>{{ col.tipo }}</ion-card-subtitle>
                        <ion-card-subtitle>{{
                          col.nm_usuario
                        }}</ion-card-subtitle>
                        <ion-card-subtitle>{{ col.email }}</ion-card-subtitle>
                      </ion-col>
                      <ion-col size="3">
                        <center>
                          <ion-avatar>
                            <ion-img
                              :src="
                                'http://192.168.8.7:5000/fotos?caminho=' +
                                  col.foto
                              "
                            ></ion-img>
                          </ion-avatar>

                          <div v-if="form.status == '1'">
                            <ion-button
                              @click="efetuaDemissao(col.id_usuario, col.tipo)"
                              color="danger"
                              size="small"
                            >
                              <ion-icon
                                slot="icon-only"
                                name="person-remove"
                              ></ion-icon>
                            </ion-button>
                          </div>
                          <div v-else-if="form.status =='0'">
                            <ion-button color="success" size="small">
                              <ion-icon
                                slot="icon-only"
                                name="person-add"
                              ></ion-icon>
                            </ion-button>
                          </div>
                        </center>
                      </ion-col>
                    </ion-row>
                  </ion-grid>
                </ion-card-content>
              </ion-card>
            </div>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  loadingController,
  toastController,
  alertController,
} from "@ionic/core";
import Provider from "@/services/provider.js";
export default {
  data() {
    return {
      form: {
        nome: "",
        email: "",
        status: "",
        tp: "",
      },
      nome_adm: "",
      foto: "",
      total: "",
      colaboradores: [],
    };
  },
  methods: {
    async efetuaDemissao(id, tipo) {
      this.confirmaDemissao(id, tipo);
    },

    async efetuaPesquisa() {
      let dados = {
        tipo: "lista_colaboradores",
        nome: this.form.nome,
        email: this.form.email,
        status: this.form.status,
        tp: this.form.tp,
      };

      const loading = await loadingController.create({
        cssClass: "my-custom-class",
        message: "Um momento...",
      });
      loading.present();

      Provider.provider("usuarios", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            this.colaboradores = res.data.dados;
            this.total = res.data.total;
            loading.dismiss();

            console.log(this.colaboradores);
            this.presentToast(res.data.msg);
          } else {
            loading.dismiss();
            this.presentToast(res.data.msg);
          }
        })
        .catch((error) => {
          loading.dismiss();
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
    async confirmaDemissao(id, tipo) {
      const alert = await alertController.create({
        cssClass: "my-custom-class",
        header: "Atenção !!!",
        message: "<strong>Deseja confirmar a demissão ?</strong>",
        buttons: [
          {
            text: "Não",
            role: "cancel",
            cssClass: "secondary",
            handler: (blah) => {
              console.log("Confirm Cancel:", blah);
            },
          },
          {
            text: "Sim",
            handler: () => {
              console.log("Confirm Okay");
              let dados = {
                tipo: "desliga_user",
                id: id,
                tp: tipo,
              };
              Provider.provider("usuarios", JSON.stringify(dados))
                .then((res) => {
                  if (res.data.sucesso) {
                    this.presentToast(res.data.msg);
                    this.efetuaPesquisa();
                  } else {
                    this.presentToast(res.data.msg);
                  }
                })
                .catch((error) => {
                  console.log("TIMEOUT " + error);
                });
            },
          },
        ],
      });
      return alert.present();
    },
  },
  mounted() {
    var dados = JSON.parse(localStorage.getItem("isLogado"));
    this.nome_adm = dados.nm_usuario;
    this.foto = dados.foto;
  },
};
</script>

<style>
#page {
  --background: rgb(55, 52, 53);
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
