<template>
  <ion-page>
    <ion-header>
      <ion-toolbar id="page" style="color:white">
        <ion-title>Cadastro</ion-title>
        <ion-buttons slot="start">
          <ion-back-button> </ion-back-button>
        </ion-buttons>
      </ion-toolbar>
    </ion-header>
    <ion-content id="page">
      <ion-grid>
        <ion-row>
          <ion-col></ion-col>
          <ion-col size="12" size-sm>
            <ion-card style="background-color:white">
              <ion-card-content>
                <form method="post" id="form">
                  <ion-list>
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
                      <ion-label position="floating"
                        >Digite novamente a senha</ion-label
                      >
                      <IonInputVue v-model="form.senha2" type="password" />
                      <ion-icon slot="end" name="lock-closed"></ion-icon>
                    </ion-item>
                  </ion-list>

                  <br />

                  <ion-button @click="efetuaCadastro" size="block" id="btn_cad"
                    >Cadastrar</ion-button
                  >
                </form>
              </ion-card-content>
            </ion-card>
          </ion-col>
          <ion-col></ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script>
import { addIcons } from "ionicons";
import {
  arrowBackCircleOutline,
  call,
  mail,
  person,
  lockClosed,
  calendar,
} from "ionicons/icons";
import { toastController } from "@ionic/core";
import { loadingController } from "@ionic/core";
import { alertController } from "@ionic/core";
import Provider from "@/services/provider";

addIcons({
  "md-arrow-back-circle-outline": arrowBackCircleOutline,
  "ios-arrow-back-circle-outline": arrowBackCircleOutline,
  "md-call": call,
  "ios-call": call,
  "md-mail": mail,
  "ios-mail": call,
  "md-person": person,
  "ios-person": person,
  "md-lock-closed": lockClosed,
  "ios-lock-closed": lockClosed,
  "md-calendar": calendar,
  "ios-calendar": calendar,
});
export default {
  data() {
    return {
      form: {
        nome: "",
        celular: "",
        email: "",
        aniversario: "",
        senha: "",
        senha2: "",
      },
    };
  },
  methods: {
    async efetuaCadastro() {
      if (this.form.nome == "") {
        this.presentToast("Campo nome está em branco", "warning");
      } else {
        if (this.form.celular == "") {
          this.presentToast("Campo celular está em branco", "warning");
        } else {
          if (this.form.email == "") {
            this.presentToast("Campo email está em branco", "warning");
          } else {
            if (this.form.aniversario == "") {
              this.presentToast("Campo aniversário está em branco", "warning");
            } else {
              if (this.form.senha == "" || this.form.senha.length < 6) {
                this.presentToast(
                  "Campo senha está em branco ou é muito curta",
                  "warning"
                );
              } else {
                if (this.form.senha2 == "") {
                  this.presentToast("Campo senha está em branco", "warning");
                } else {
                  if (this.form.senha != this.form.senha2) {
                    this.presentToast("As senhas não são iguais", "warning");
                  } else {
                    const loading = await loadingController.create({
                      cssClass: "my-custom-class",
                      message: "Um momento...",
                    });
                    loading.present();

                    let dados = {
                      tipo: "cad_usuario",
                      nome: this.form.nome,
                      celular: this.form.celular,
                      email: this.form.email,
                      aniversario: this.form.aniversario,
                      senha: this.form.senha,
                    };

                    Provider.provider("usuarios", JSON.stringify(dados))
                      .then((res) => {
                        if (res.data.sucesso) {
                          this.inicializa();
                          loading.dismiss();
                          //this.presentToast(res.data.msg);
                          this.alertaSucesso(res.data.msg, "Sucesso");
                        } else {
                          loading.dismiss();
                          this.alertaSucesso(res.data.msg, "Problemas !!!");
                          console.log(res.data.msg);
                        }
                      })
                      .catch((error) => {
                        loading.dismiss();
                        this.alertaSucesso(
                          "Ocorreu um erro com o servidor. Contate o suporte",
                          "Erro !!!"
                        );
                        console.log("TIMEOUT " + error);
                      });
                  }
                }
              }
            }
          }
        }
      }
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
    async alertaSucesso(msg, tipo) {
      const alert = await alertController.create({
        cssClass: "my-custom-class",
        header: tipo,
        message: msg,
        buttons: ["OK"],
      });

      await alert.present();
    },
    inicializa() {
      this.form.nome = "";
      this.form.celular = "";
      this.form.email = "";
      this.form.aniversario = "";
      this.form.senha = "";
      this.form.senha2 = "";
    },
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
