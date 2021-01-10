<template>
  <ion-page>
    <ion-content id="page">
      <ion-grid>
        <ion-row>
          <ion-col>
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
                      <p>{{ nome_adm }}</p>
                    </ion-label>
                  </ion-item>
                </ion-list>
              </ion-card-content>
            </ion-card>

            <ion-card style="background-color: white">
              <ion-card-content>
                <ion-list>
                  <ion-list-header>
                    <h1>Equipe</h1>
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
                        <h2>{{ col.nm_usuario }}</h2>
                        <p>Colaborador(a)</p>
                        <p>Avaliação:</p>
                      </ion-label>
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
import { toastController, alertController } from "@ionic/core";
import Provider from "@/services/provider.js";
export default {
  data() {
    return {
      form: {
        nome: "",
        celular: "",
        email: "",
        aniversario: "",
        senha: "",
        foto_user: "",
      },
      foto: "",
      nome_adm: "",
      colaboradores: [],
    };
  },
  methods: {
    async alertaSucesso(msg, tipo) {
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
    inicializa() {
      this.form.nome = "";
      this.form.celular = "";
      this.form.email = "";
      this.form.aniversario = "";
      this.form.senha = "";
      this.form.tipo_user = "";
    },
  },
  mounted() {
    var dados = JSON.parse(localStorage.getItem("isLogado"));
    this.nome_adm = dados.nm_usuario;
    this.foto = dados.foto;
    this.listaColaboradores();
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

.ion-toast {
  text-align: center;
}
</style>
