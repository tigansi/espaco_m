<template>
  <ion-page>
    <ion-content id="page">
      <ion-grid>
        <ion-row>
          <ion-col></ion-col>
          <ion-col size="12" size-sm>
            <div
              style="
                height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
              "
            >
              <ion-card style="--background: white">
                <ion-card-header>
                  <center>
                    <ion-img
                      id="img-logo"
                      :src="require('../../assets/logo/logo-dark.png')"
                    ></ion-img>
                    <p id="texto_info">
                      <strong>Bem vindo(a)</strong> Bem vindo(a) ao aplicativo
                      do
                      <strong>Espaço M</strong>
                    </p>
                  </center>
                </ion-card-header>
                <ion-card-content>
                  <form action="" method="post" id="form">
                    <ion-list>
                      <ion-item>
                        <ion-label position="floating">E-mail</ion-label>
                        <IonInputVue v-model="form.email" />
                        <ion-icon slot="end" name="mail"></ion-icon>
                      </ion-item>
                      <ion-item>
                        <ion-label position="floating">Senha</ion-label>
                        <IonInputVue v-model="form.senha" type="password" />
                        <ion-icon slot="end" name="lock-closed"></ion-icon>
                      </ion-item>
                    </ion-list>
                    <ion-button
                      @click="efetuaLogin"
                      id="btn_entrar"
                      expand="block"
                      >Entrar</ion-button
                    >
                  </form>
                  <br />
                  <center>
                    <p style="display: inline">Ainda não possui conta ?</p>
                    <a
                      @click="direcionaView('Cadastro')"
                      style="cursor: pointer"
                      >Clique aqui</a
                    >
                  </center>
                </ion-card-content>
              </ion-card>
            </div>
          </ion-col>
          <ion-col></ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script>
import { addIcons } from "ionicons";
import { mail, lockClosed } from "ionicons/icons";

import { toastController } from "@ionic/core";
import { loadingController } from "@ionic/core";
import Provider from "@/services/provider";

addIcons({
  "md-mail": mail,
  "ios-mail": mail,
  "md-lock-closed": lockClosed,
  "ios-lock-closed": lockClosed,
});
export default {
  data() {
    return {
      form: {
        email: "tiagoigansi17@gmail.com",
        senha: "123456",
      },
    };
  },
  methods: {
    direcionaView(view) {
      this.$router.push(view);
    },
    async efetuaLogin() {
      if (this.form.email == "") {
        this.presentToast("E-mail em branco");
      } else {
        if (this.form.senha == "") {
          this.presentToast("Senha em branco");
        } else {
          const loading = await loadingController.create({
            cssClass: "my-custom-class",
            message: "Um momento...",
          });
          loading.present();

          let dados = {
            tipo: "login",
            email: this.form.email,
            senha: this.form.senha,
          };

          Provider.provider("usuarios", JSON.stringify(dados))
            .then((res) => {
              if (res.data.dados) {
                localStorage.setItem(
                  "isLogado",
                  JSON.stringify(res.data.dados[0])
                );
                loading.dismiss();
                if (res.data.dados[0].tipo == "CLI") {
                  this.$router.push("HomePainelClientes/HomeClientes/Agendar");
                } else {
                  this.$router.push("/EscolhaPapel");
                }
              } else {
                loading.dismiss();
                this.presentToast(res.data.msg);
              }
            })
            .catch((error) => {
              loading.dismiss();
              this.presentToast(
                "danger",
                "Ocorreu um erro com o servidor. Contate o suporte"
              );
              console.log("TIMEOUT " + error);
            });
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

#img-logo {
  width: 210px;
}

#btn_entrar {
  --background: rgb(55, 52, 53);
  --background-activated: rgb(55, 52, 53);
  --background-hover: rgb(55, 52, 53);
}
</style>
