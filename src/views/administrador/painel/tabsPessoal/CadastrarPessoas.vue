<template>
  <ion-app>
    <ion-content id="page">
      <ion-grid>
        <ion-row>
          <ion-col>
            <ion-card style="background-color:white">
              <ion-card-header>
                <ion-grid>
                  <ion-row>
                    <ion-col size="8" size-sm>
                      <ion-card-subtitle>Bem vindo(a)</ion-card-subtitle>
                      <ion-card-title>{{ nome_adm }} </ion-card-title>
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
          </ion-col>
          <ion-col>
            <ion-card style="background-color:white">
              <ion-card-content>
                <div id="form">
                  <ion-list>
                    <ion-list-header>
                      <h1>Novo colaborador</h1>
                    </ion-list-header>
                    <ion-item>
                      <ion-label position="floating">Nome</ion-label>
                      <IonInputVue v-model="form.nome" />
                      <ion-icon slot="end" name="person"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <input
                        type="hidden"
                        v-mask="'(##) ####-#####'"
                        v-model="form.celular"
                      />
                      <ion-label position="floating">Celular</ion-label>
                      <IonInputVue type="tel" v-model="form.celular" />
                      <ion-icon slot="end" name="call"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <ion-label position="floating">E-mail</ion-label>
                      <IonInputVue v-model="form.email" type="email" />
                      <ion-icon slot="end" name="mail"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <ion-label position="stacked">Aniversário</ion-label>
                      <IonInputVue
                        v-model="form.aniversario"
                        placeholder="Coloque sua data de nascimento"
                        type="date"
                      />
                      <ion-icon slot="end" name="calendar"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <ion-label position="floating">Senha</ion-label>
                      <IonInputVue v-model="form.senha" type="password" />
                      <ion-icon slot="end" name="lock-closed"></ion-icon>
                    </ion-item>

                    <ion-item>
                      <ion-label position="floating">Tipo de usuário</ion-label>
                      <ion-icon slot="end" name="people"></ion-icon>
                      <IonSelectVue v-model="form.tipo_user">
                        <ion-select-option value="CLI"
                          >Cliente</ion-select-option
                        >
                        <ion-select-option value="COL"
                          >Colaborador</ion-select-option
                        >
                        <ion-select-option value="ADM"
                          >Administrador</ion-select-option
                        >
                      </IonSelectVue>
                    </ion-item>
                  </ion-list>

                  <br />

                  <ion-button @click="efetuaCadastro" size="block" id="btn_cad"
                    >Cadastrar</ion-button
                  >
                </div>
              </ion-card-content>
            </ion-card>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-app>
</template>

<script>
import {
  toastController,
  loadingController,
  alertController,
} from "@ionic/core";
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
    };
  },
  methods: {
    async efetuaCadastro() {
      if (this.form.nome == "") {
        this.presentToast("Campo nome está em branco");
      } else {
        if (this.form.celular == "") {
          this.presentToast("Campo celular está em branco");
        } else {
          if (this.form.email == "") {
            this.presentToast("Campo e-mail está em branco");
          } else {
            if (this.form.aniversario == "") {
              this.presentToast("Campo aniversário está em branco");
            } else {
              if (this.form.senha == "" || this.form.senha.length < 6) {
                this.presentToast(
                  "Campo senha está em branco ou é muito pequena"
                );
              } else {
                if (this.form.tipo_user == "") {
                  this.presentToast("Campo tipo de usuário está em branco");
                } else {
                  let dados = {
                    tipo: "cad_usuario",
                    nome: this.form.nome,
                    celular: this.form.celular,
                    email: this.form.email,
                    aniversario: this.form.aniversario,
                    senha: this.form.senha,
                    tp: this.form.tipo_user,
                  };

                  const loading = await loadingController.create({
                    cssClass: "my-custom-class",
                    message: "Um momento...",
                  });
                  loading.present();

                  Provider.provider("usuarios", JSON.stringify(dados))
                    .then((res) => {
                      if (res.data.sucesso) {
                        this.inicializa();
                        loading.dismiss();
                        this.alertaSucesso(res.data.msg, "Sucesso");
                      } else {
                        loading.dismiss();
                        this.alertaSucesso(res.data.msg, "Problemas !!!");
                      }
                    })
                    .catch((error) => {
                      loading.dismiss();
                      console.log("TIMEOUT " + error);
                    });
                }
              }
            }
          }
        }
      }
    },
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
